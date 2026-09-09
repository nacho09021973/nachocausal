"""Validate the ZIP-derived static Paper I website using only Python stdlib.

Run: python3 web/verify_site.py [--url CONFIRMED_PUBLIC_URL]
The optional URL is fetched anonymously and checked against the local assets.
This checks markup and transport; browser layout is reviewed separately.
"""

from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urljoin, urlsplit
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parent
RECORD = 'https://zenodo.org/records/22655783'
TITLE = 'Visible Directions in Finite Causal Orders'
TERMS = ('causal sets', 'causal set theory', 'causal orders', 'finite causal orders',
         'unlabeled causal orders', 'finite posets', 'conjuntos causales',
         'órdenes causales', 'órdenes causales finitos')


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids, self.refs, self.meta, self.jsonld = [], [], {}, []
        self.canonical = None
        self.in_json = False
        self.data = ''
        self.faq = []
        self.detail = None
        self.capture = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        for attr in ('src', 'href'):
            if attr in a:
                self.refs.append(a[attr])
        if tag == 'meta':
            self.meta[a.get('name', a.get('property', ''))] = a.get('content', '')
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical = a['href']
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.in_json, self.data = True, ''
        if tag == 'details':
            self.detail = {'name': '', 'text': ''}
        if self.detail is not None and tag in ('summary', 'p'):
            self.capture = 'name' if tag == 'summary' else 'text'
        if self.capture and tag in ('sub', 'sup'):
            self.detail[self.capture] += ('_' if tag == 'sub' else '^') + '{'

    def handle_data(self, data):
        if self.in_json:
            self.data += data
        elif self.capture:
            self.detail[self.capture] += data

    def handle_endtag(self, tag):
        if self.capture and tag in ('sub', 'sup'):
            self.detail[self.capture] += '}'
        if tag == 'script' and self.in_json:
            self.jsonld.append(json.loads(self.data))
            self.in_json = False
        if tag in ('summary', 'p'):
            self.capture = None
        if tag == 'details' and self.detail is not None:
            self.detail = {k: re.sub(r'([_^])\{([^{}])\}', r'\1\2', v.replace('−', '-'))
                           for k, v in self.detail.items()}
            self.faq.append(self.detail)
            self.detail = None


def validate(public_url=None):
    source = ROOT / 'nachocausal_paper1_SEO_GEO.zip'
    with ZipFile(source) as z:
        assert z.testzip() is None
        assert set(z.namelist()) == {'index.html', 'robots.txt', 'llms.txt',
                                    'SEO_DEPLOY.txt', 'assets/nachocausal-mark.png'}
        assert (ROOT / 'assets/nachocausal-mark.jpg').read_bytes() == z.read('assets/nachocausal-mark.png')
        assert (ROOT / 'robots.txt').read_text().startswith(z.read('robots.txt').decode())
    print('PASS canonical ZIP integrity; original logo bytes preserved')

    html = (ROOT / 'index.html').read_text()
    llms = (ROOT / 'llms.txt').read_text()
    page = Page()
    page.feed(html)
    assert len(page.ids) == len(set(page.ids)), 'duplicate HTML IDs'
    assert TITLE in html and TITLE in llms
    assert not re.search(r'Schwarzschild|horizon|Paper II|black.hole', html + llms, re.I)
    assert '1+1' in html and '1+1' in llms
    assert 'V_N = Sym^2 P_{N-1}' in llms and 'dim V_N = N(N-1)/2' in llms
    assert 'N >= 2' in llms
    for term in TERMS:
        assert term.casefold() in html.casefold() and term.casefold() in llms.casefold(), term
    for key in ('citation_title', 'citation_author', 'citation_keywords',
                'citation_abstract_html_url', 'DC.title', 'DC.creator', 'DC.subject',
                'DC.identifier', 'DC.type', 'og:type', 'og:title', 'og:description',
                'og:url', 'og:image', 'og:site_name'):
        assert page.meta.get(key), key
    assert page.meta['citation_title'] == TITLE
    assert page.meta['citation_abstract_html_url'] == RECORD
    assert page.meta['DC.identifier'] == RECORD
    graph = page.jsonld[0]['@graph']
    article = next(x for x in graph if x['@type'] == 'ScholarlyArticle')
    faq = next(x for x in graph if x['@type'] == 'FAQPage')
    assert article['url'] == RECORD and article['name'] == TITLE
    assert [{'name': x['name'], 'text': x['acceptedAnswer']['text']}
            for x in faq['mainEntity']] == page.faq
    # The supplied package omits these bibliographic additions; preserve that.
    for field in ('datePublished', 'dateModified', 'doi', 'affiliation', 'publisher'):
        assert not re.search('"' + field + '"\\s*:', html), field
    assert not any(k in page.meta for k in ('citation_doi', 'citation_date',
                                           'citation_journal_title', 'citation_author_institution'))
    print('PASS JSON-LD, six visible FAQs, academic metadata, bilingual terms and scope guards')

    refs = page.refs + [page.meta[k] for k in ('og:image', 'twitter:image')]
    for ref in refs + re.findall(r'url\([\s\'"]*([^\)\'"\s]+)', html):
        parsed = urlsplit(ref)
        if parsed.scheme or parsed.netloc:
            if not public_url or not ref.startswith(public_url):
                continue
            parsed = urlsplit(ref[len(public_url):])
        path = (ROOT / unquote(parsed.path or 'index.html')).resolve()
        assert path.is_relative_to(ROOT), ref
        assert path.exists(), f'broken local path: {ref}'
        if parsed.fragment:
            assert parsed.fragment in page.ids, f'broken fragment: {ref}'
    image = (ROOT / 'assets/nachocausal-mark.jpg').read_bytes()
    assert image.startswith(b'\xff\xd8\xff') and image.endswith(b'\xff\xd9')
    robots = RobotFileParser()
    robots.parse((ROOT / 'robots.txt').read_text().splitlines())
    assert robots.can_fetch('OAI-SearchBot', 'https://example.invalid/')
    assert robots.can_fetch('OAI-SearchBot', 'https://example.invalid/llms.txt')
    print('PASS local links, fragments, JPEG signature, llms.txt and OAI-SearchBot access')

    paths = ['index.html', 'robots.txt', 'llms.txt', 'assets/nachocausal-mark.jpg']
    if public_url:
        assert public_url.startswith('https://') and public_url.endswith('/')
        assert page.canonical == public_url and page.meta['og:url'] == public_url
        for key in ('og:image', 'twitter:image'):
            assert page.meta[key] == urljoin(public_url, 'assets/nachocausal-mark.jpg')
        sitemap = ET.parse(ROOT / 'sitemap.xml')
        assert [x.text for x in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')] == [public_url]
        assert 'Sitemap: ' + urljoin(public_url, 'sitemap.xml') in (ROOT / 'robots.txt').read_text()
        paths.append('sitemap.xml')
        cf_challenge = re.compile(
            r'<script>\(function\(\)\{function c\(\).*?/cdn-cgi/challenge-platform/scripts/jsd/main\.js.*?</script>',
            re.S,
        )
        for name in paths:
            url = public_url if name == 'index.html' else urljoin(public_url, name)
            request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urlopen(request, timeout=30) as response:
                assert response.status == 200
                remote = response.read()
                local = (ROOT / name).read_bytes()
                if name == 'index.html':
                    remote_text = remote.decode('utf-8')
                    remote = cf_challenge.sub('', remote_text).encode('utf-8')
                assert remote == local, url
                if name.endswith('.jpg'):
                    assert response.headers.get_content_type() == 'image/jpeg'
        print('PASS public anonymous HTTP, byte equality, canonical, OpenGraph and sitemap')
    else:
        assert page.canonical == './'
        assert not (ROOT / 'sitemap.xml').exists(), 'Do not invent a public URL'
        print('PASS prepublication URL policy: relative canonical; no invented sitemap')
    print('ZIP SHA256:', hashlib.sha256(source.read_bytes()).hexdigest())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url', help='Confirmed live public URL, ending in /')
    validate(parser.parse_args().url)
