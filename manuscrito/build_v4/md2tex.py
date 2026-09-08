#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
PIPELINE_PROVENANCE=RECONSTRUCTED_BY_GOLDEN_REPLAY

Markdown -> LaTeX converter reconstructed by forensic replay against the
golden PDF (manuscrito_v4_es.pdf @ 7ba3c04). This is NOT the original
pipeline; it is a reconstruction whose output is scored against the golden.

Structural decisions and the golden evidence behind each:
  * article 11pt, geometry margin=1in   -> body box x in [72,540], letter 612x792
  * lmodern + T1 fontenc, no fontspec   -> pdffonts: LMRoman* Type 1, subset
  * title \LARGE\bfseries centered      -> LMRoman12-Bold, ink height 15.12 ~ 17.28pt
                                           (lmbx12 is the largest LM bold face)
  * author + email \large, two lines    -> ink height 10.56 ~ 12pt, baselines 13.95pt apart
  * abstract = stock article abstract    -> x in [99.3,512.7] = 72+2.5em .. 540-2.5em,
    with \abstractname renamed             first line indented 1.5em, \small
  * sections \Large\bfseries             -> ink height 12.60 ~ 14.4pt
  * bibliography \small, hanging indent  -> ink height 8.80 ~ 10pt, label x0=68.0,
                                           continuation x0=87.9
  * DOIs/URLs via \nolinkurl             -> "_" prints literally, no /Link or /URI
                                           annotations anywhere, no monospace font
  * NO babel                             -> reproduces the historical build, which had
                                           no Spanish hyphenation patterns available
"""
import re, sys, io

# ---------------------------------------------------------------- inline

MATHSPAN = re.compile(r'\$[^$]*\$')

def _protect(s):
    """Replace inline math by placeholders so markup regexes cannot enter math."""
    store = []
    def sub(m):
        store.append(m.group(0))
        return '\x00%d\x00' % (len(store) - 1)
    return MATHSPAN.sub(sub, s), store

def _restore(s, store):
    return re.sub(r'\x00(\d+)\x00', lambda m: store[int(m.group(1))], s)

def inline(s):
    s, store = _protect(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', s)
    s = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'\\emph{\1}', s)
    return _restore(s, store)

# DOI / URL handling: the golden drops the sentence-final period after a DOI or
# URL and typesets it verbatim in roman (\nolinkurl + \urlstyle{rm}).
DOI = re.compile(r'\bdoi:\s*(10\.\S+?)\.?(?=\s*$|\s)')
URL = re.compile(r'\bURL\s+(https?://\S+?)\.?(?=\s*$|\s)')

def urls(s):
    # The golden sets DOIs as ORDINARY roman text, not through url.sty: a
    # url.sty DOI comes out 2.8-5.0pt wider than the golden's on every entry
    # whose last line ends in one, it never breaks at "/" or ":" (which plain
    # text cannot do either), and it does break at the internal hyphens (which
    # plain text does).  Only the one bare URL goes through \nolinkurl, which
    # is what lets it break after "https://www.".  Both drop the sentence-final
    # period, and the single "_" is escaped rather than made verbatim.
    s = URL.sub(lambda m: r'\nolinkurl{%s}' % m.group(1), s)
    # The golden separates "doi:" from the number by a thin space (measured ink
    # gap 1.67pt against 3.32pt for a word space), and keeps the ordinary extra
    # space after other colons such as "(10):", so this is a local thin space
    # rather than \frenchspacing.
    s = DOI.sub(lambda m: r'doi:\,' + m.group(1).replace('_', r'\_'), s)
    return s


# ---------------------------------------------------------------- displays

TAGLINE = re.compile(r'(?m)^\s*(\\tag\{[^}]*\})\s*$')

def split_qquad(c):
    r"""Split at \qquad separators that sit at brace depth 0 and outside any
    \begin{...}...\end{...}, so \qquad inside \text{}, pmatrix or aligned is
    never a split point."""
    parts, buf, depth, env, i, n = [], [], 0, 0, 0, len(c)
    while i < n:
        if c.startswith('\\begin{', i):
            env += 1
        elif c.startswith('\\end{', i):
            env -= 1
        elif c.startswith('\\qquad', i) and depth == 0 and env == 0:
            parts.append(''.join(buf)); buf = []
            i += 6
            continue
        ch = c[i]
        if ch == '{': depth += 1
        elif ch == '}': depth -= 1
        elif ch == '\\' and i + 1 < n:
            buf.append(c[i:i+2]); i += 2; continue
        buf.append(ch); i += 1
    parts.append(''.join(buf))
    return [x.strip() for x in parts]

BOXED = re.compile(r'^\\boxed\{(.*)\}$', re.S)

def display_body(c):
    """Wrap a display's content so LaTeX can pack it into rows if it is too
    wide.  Returns the content unchanged when there is nothing to split."""
    inner, wrap = c, None
    m = BOXED.match(c.strip())
    if m and m.group(1).count('{') == m.group(1).count('}'):
        # The \boxed padding (\;...\;) stays OUTSIDE the packed rows: both rows
        # of (6.5) are ink-centred on 306.0 in the golden, which they could not
        # be if one row carried a leading \; and the other a trailing one.
        t = m.group(1).strip()
        lead = tail = ''
        if t.startswith('\\;'):
            lead, t = '\\;', t[2:]
        if t.endswith('\\;'):
            tail, t = '\\;', t[:-2]
        inner = t
        wrap = '\\boxed{' + lead + '%s' + tail + '}'
    parts = split_qquad(inner)
    if len(parts) < 2:
        return c
    packed = r'\autodisplay{%s}' % ''.join(r'\dpart{%s}' % x for x in parts)
    return wrap % packed if wrap else packed

# ---------------------------------------------------------------- blocks

HEADING = re.compile(r'^(#{1,6})\s+(.*)$')
SECNUM  = re.compile(r'^(\d+)\.\s+(.*)$')

ITALIC_ONLY = re.compile(r'^\*(?!\*)(.+)\*$')
THM_KINDS = {'Teorema': 'teorema', 'Corolario': 'corolario', 'Lema': 'lema',
             'Proposici\u00f3n': 'proposicion', 'Definici\u00f3n': 'definicion',
             'Observaci\u00f3n': 'observacion',
             'Theorem': 'teorema', 'Corollary': 'corolario', 'Lemma': 'lema',
             'Proposition': 'proposicion', 'Definition': 'definicion',
             'Remark': 'observacion'}
THM_HEAD = re.compile(
    r'^\*\*(Teorema|Corolario|Lema|Proposici\u00f3n|Definici\u00f3n|Observaci\u00f3n|'
    r'Theorem|Corollary|Lemma|Proposition|Definition|Remark)'
    r'\s+(\d+)\s*(?:\(([^)]*)\))?\.\*\*\s*(.*)$')
PROOF_HEAD = re.compile(r'^\*(Demostraci\u00f3n|Proof)\.\*')

def theorem_spans(lines):
    # Returns (thm_heads, thm_italic, thm_close, proof_open, proof_close).
    #
    # A theorem body in this markdown runs from its "**Kind n (note).**" head
    # paragraph through every display-math block and every fully-italic
    # paragraph that follows it, and stops at the first plain paragraph or
    # heading.  The golden confirms it: there is no \topsep between a theorem
    # head and the display beneath it (26.12pt on page 5, i.e. \abovedisplayskip
    # alone), so the display sits inside the environment.
    #
    # Proofs run from "*Demostracion.*" to the paragraph carrying the closing
    # $\square$.  The golden embeds no msam10, so amssymb's \square was never
    # typeset there; the QED box it does draw is amsthm's rule-built \openbox.
    heads, italic, close, opens, closes = {}, set(), set(), set(), set()
    n = len(lines)

    def skip_blank(k):
        while k < n and not lines[k].strip():
            k += 1
        return k

    def block_end(k):
        """index just past the block starting at k (k must be non-blank)."""
        if lines[k].strip() == '$$':
            k += 1
            while k < n and lines[k].strip() != '$$':
                k += 1
            return k + 1
        return k + 1

    for j, l in enumerate(lines):
        st = l.strip()
        m = THM_HEAD.match(st)
        if m:
            heads[j] = (m.group(1), int(m.group(2)), m.group(3), m.group(4))
            last, k = j, skip_blank(j + 1)
            while k < n:
                sk = lines[k].strip()
                if sk == '$$':
                    last = k
                    k = skip_blank(block_end(k))
                    continue
                if ITALIC_ONLY.match(sk) and not THM_HEAD.match(sk) \
                   and not PROOF_HEAD.match(sk):
                    italic.add(k)
                    last = k
                    k = skip_blank(k + 1)
                    continue
                break
            close.add(last)
        elif PROOF_HEAD.match(st):
            k = j
            while k < n:
                sk = lines[k].strip()
                if k > j and (sk.startswith('## ') or PROOF_HEAD.match(sk)):
                    k = j
                    break
                if r'\square' in sk:
                    break
                k += 1
            opens.add(j)
            closes.add(min(k, n - 1))
    return heads, italic, close, opens, closes

def closing_italics(lines):
    """Line numbers of the italic-only paragraphs that sit, contiguously, just
    before the unnumbered references heading: the dedication and the epigraph."""
    ref = None
    for j, l in enumerate(lines):
        m = HEADING.match(l.strip())
        if m and len(m.group(1)) == 2 and not SECNUM.match(m.group(2).strip()) \
           and not m.group(2).strip().lower().startswith('resumen'):
            ref = j
    if ref is None:
        return {}
    found, j = [], ref - 1
    while j >= 0:
        st = lines[j].strip()
        if not st:
            j -= 1
            continue
        if ITALIC_ONLY.match(st):
            found.append(j); j -= 1
            continue
        break
    found.reverse()
    roles = {}
    if len(found) >= 2:
        roles[found[0]] = 'dedication'
        for k in found[1:]:
            roles[k] = 'epigraph'
    elif len(found) == 1:
        roles[found[0]] = 'dedication'
    return roles

def convert(md):
    lines = md.replace('\r\n', '\n').split('\n')
    closing = closing_italics(lines)
    thm_heads, thm_italic, thm_close, proof_open, proof_close = theorem_spans(lines)
    open_env = []
    i, n = 0, len(lines)
    out = []
    meta = {'title': '', 'author': '', 'email': ''}
    in_abstract = False
    seen_section = False

    def flush_para(buf):
        if not buf:
            return
        txt = ' '.join(x.strip() for x in buf).strip()
        if txt:
            out.append(inline(txt))
            out.append('')

    para = []
    while i < n:
        line = lines[i]
        st = line.strip()

        # ---- blank
        if not st:
            flush_para(para); para = []
            i += 1
            continue

        # ---- display math
        if st == '$$':
            flush_para(para); para = []
            start = i
            body, i = [], i + 1
            while i < n and lines[i].strip() != '$$':
                body.append(lines[i]); i += 1
            i += 1
            b = '\n'.join(body).strip('\n')
            tag = TAGLINE.search(b)
            if tag:
                b = display_body(TAGLINE.sub('', b).strip()) + '\n' + tag.group(1)
            else:
                b = display_body(b.strip())
            if r'\tag{' in b:
                out.append(r'\begin{equation*}'); out.append(b)
                out.append(r'\end{equation*}'); out.append('')
            else:
                out.append(r'\['); out.append(b); out.append(r'\]'); out.append('')
            if start in thm_close and open_env:
                out.append(r'\end{%s}' % open_env.pop()); out.append('')
            continue

        # ---- heading
        m = HEADING.match(st)
        if m:
            flush_para(para); para = []
            level, text = len(m.group(1)), m.group(2).strip()
            if level == 1:
                meta['title'] = inline(text)
                i += 1
                continue
            # level 2
            if in_abstract:
                out.append(r'\end{abstract}'); out.append('')
                in_abstract = False
            sm = SECNUM.match(text)
            if sm:
                out.append(r'\section{%s}' % inline(sm.group(2)))
                seen_section = True
            elif not seen_section and text.lower().startswith(('resumen', 'abstract')):
                meta['abstractname'] = text
                out.append(r'\begin{abstract}')
                in_abstract = True
            else:
                out.append(r'\section*{%s}' % inline(text))
                meta.setdefault('starred', []).append(text)
            out.append('')
            i += 1
            continue

        # ---- table
        if st.startswith('|'):
            flush_para(para); para = []
            rows, i = [], i
            while i < n and lines[i].strip().startswith('|'):
                rows.append(lines[i].strip()); i += 1
            out.extend(table(rows))
            continue

        # ---- bullet list (bibliography)
        if st.startswith('- '):
            flush_para(para); para = []
            items = []
            while i < n and lines[i].strip().startswith('- '):
                items.append(lines[i].strip()[2:].strip()); i += 1
            out.append(r'\begin{bibliolist}')
            for it in items:
                # The golden's "[Key]" is a rigid list label, not inline text:
                # the label-to-text ink gap is a constant 3.98pt across entries
                # whose lines are stretched by different amounts.
                m = re.match(r'^\*\*(\[[^\]]*\])\*\*\s*(.*)$', it)
                if m:
                    out.append(r'\item[\textbf{%s}] %s'
                               % (inline(m.group(1)), urls(inline(m.group(2)))))
                else:
                    out.append(r'\item %s' % urls(inline(it)))
            out.append(r'\end{bibliolist}'); out.append('')
            continue

        # ---- front matter (before any heading other than title)
        if meta['title'] and not out and not in_abstract:
            if st.startswith(('Autor de correspondencia:', 'Corresponding author:')):
                meta['email'] = st.split(':', 1)[1].strip()
                i += 1
                continue
            if not meta['author']:
                meta['author'] = inline(st)
                i += 1
                continue

        if i in thm_italic and open_env:
            flush_para(para); para = []
            im = ITALIC_ONLY.match(st)
            out.append(inline(im.group(1)))
            out.append('')
            if i in thm_close:
                out.append(r'\end{%s}' % open_env.pop()); out.append('')
            i += 1
            continue

        if i in thm_heads:
            flush_para(para); para = []
            kind, num, note, body = thm_heads[i]
            meta['thmcount'] = meta.get('thmcount', 0) + 1
            if meta['thmcount'] != num:
                sys.stderr.write(
                    'WARNING: %s %d is the %dth theorem-like block; the shared '
                    'amsthm counter will not reproduce the source number\n'
                    % (kind, num, meta['thmcount']))
            b = body.strip()
            im = ITALIC_ONLY.match(b)
            if im:            # amsthm plain already italicises the statement
                b = im.group(1)
            env = THM_KINDS[kind]
            out.append(r'\begin{%s}%s' % (env, '[%s]' % inline(note) if note else ''))
            out.append(inline(b))
            if i in thm_close:
                out.append(r'\end{%s}' % env)
            else:
                open_env.append(env)
            out.append('')
            i += 1
            continue

        if i in proof_open or i in proof_close:
            flush_para(para); para = []
            if i in proof_open:
                out.append(r'\begin{proofblock}')
            txt = PROOF_HEAD.sub('', st).lstrip() if i in proof_open else st
            if i in proof_close:
                txt = txt.replace('$\\square$', '').rstrip()
            out.append(inline(txt))
            if i in proof_close:
                out.append(r'\end{proofblock}')
            out.append('')
            i += 1
            continue

        if i in closing:
            flush_para(para); para = []
            body = ITALIC_ONLY.match(st).group(1)
            cmd = r'\dedicationline' if closing[i] == 'dedication' else r'\epigraphline'
            out.append('%s{%s}' % (cmd, inline(body)))
            out.append('')
            i += 1
            continue

        para.append(st)
        i += 1

    flush_para(para)
    if in_abstract:
        out.append(r'\end{abstract}')
    return meta, out

def cells(row):
    r = row.strip()
    if r.startswith('|'): r = r[1:]
    if r.endswith('|'):   r = r[:-1]
    return [c.strip() for c in r.split('|')]

def table(rows):
    hdr = cells(rows[0])
    body = [cells(r) for r in rows[2:]] if len(rows) > 2 else []
    k = len(hdr)
    # The golden sets the one table in \small (row ink height 9.40 against
    # 10.30 for 11pt body text, 11.95pt row pitch) and lets the paragraph that
    # follows run on unindented, i.e. no blank line after \end{center}.
    # Column alignment: the golden centres the narrow first column (its data
    # cells sit 2.0pt right of the header's left edge, exactly a centring
    # offset) and left-aligns the wide one.  Rule: a column whose every cell is
    # a single short token is centred, otherwise left.
    cols = [[hdr[j]] + [(r + [''] * k)[j] for r in body] for j in range(k)]
    spec = '@{}' + ''.join(
        'c' if all(len(c.strip('$ ')) <= 3 for c in col) else 'l'
        for col in cols) + '@{}'
    o = [r'\begin{center}', r'\small', r'\begin{tabular}{%s}' % spec, r'\toprule']
    o.append(' & '.join(inline(c) for c in hdr) + r' \\')
    o.append(r'\midrule')
    for r in body:
        r = (r + [''] * k)[:k]
        o.append(' & '.join(inline(c) for c in r) + r' \\')
    o += [r'\bottomrule', r'\end{tabular}', r'\end{center}']
    return o

# ---------------------------------------------------------------- preamble

PREAMBLE = r"""%% PIPELINE_PROVENANCE=RECONSTRUCTED_BY_GOLDEN_REPLAY
\documentclass[11pt]{article}

%% ------------------------------------------------------------------
%% HYPHENATION: reproduce the historical build, which had no Spanish
%% hyphenation patterns available. babel is deliberately NOT loaded, so
%% nothing can select \l@spanish, and automatic syllabic hyphenation is
%% switched off outright: the golden PDF contains zero pattern-generated
%% hyphen breaks (its single hyphenated line break is the explicit hyphen
%% in "real-analitica", which \exhyphenpenalty still allows).
%% This makes the build independent of texlive-lang-spanish being installed;
%% no package is uninstalled to achieve it.
%% ------------------------------------------------------------------
\language=255              % a language slot with no patterns loaded
\hyphenpenalty=10000       % never take a pattern-generated break
\exhyphenpenalty=50        % ... but keep explicit-hyphen breaks (LaTeX default)
\lefthyphenmin=62          % TeX refuses to hyphenate when these exceed 63
\righthyphenmin=62

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{textcomp}
\usepackage{newunicodechar}
%% LuaTeX feeds UTF-8 straight to the 8-bit T1 font, so codepoints outside the
%% Latin-1-aligned part of T1 must be mapped explicitly or they render as the
%% wrong glyph silently (U+00A7 -> gbreve, U+00BF -> sterling) or vanish.
%% The Latin-1-aligned accented letters (aeioun with acute/tilde/diaeresis)
%% already hit the correct T1 slots and are deliberately left untouched.
\newunicodechar{§}{\textsection}
\newunicodechar{¿}{\textquestiondown}
\newunicodechar{–}{\textendash}
\newunicodechar{—}{\textemdash}
\newunicodechar{č}{\v{c}}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{mathrsfs}
\usepackage[letterpaper,margin=1in]{geometry}
\usepackage{hyperref}
\hypersetup{hidelinks,pdfborder={0 0 0}}
\usepackage{url}
%% The golden breaks DOIs at their internal hyphens ("10.1016/0012-" /
%% "365X(94)90370-0", "10.1007/978-3-642-" / "02441-2_28"), which url.sty does
%% not allow out of the box; without this the whole DOI is forced onto its own
%% line and the enclosing entry re-breaks.
%% The golden also never breaks a URL at ":" or "/" -- it breaks the long
%% ism.ac.jp URL after "https://www." -- so url.sty's "big break" class, which
%% would otherwise win over the period, is emptied.
\makeatletter
\def\UrlBreaks{\do\.\do\-}
\def\UrlBigBreaks{}
\def\UrlNoBreaks{\do\(\do\[\do\{\do\<\do\:\do\/}
\makeatother
\urlstyle{rm}

%% amsthm environments (Spanish names). The golden markdown hard-codes its own
%% theorem numbering in the prose, so the manuscript body does not instantiate
%% these counters; they are declared for pipeline completeness only.
%% Real amsthm environments on one shared counter.  The golden's theorem heads
%% show amsthm's plain style exactly: "Teorema 1" bold, the parenthetical note
%% medium *upright* (\thm@notefont), the closing period bold again, the head
%% unindented (\thm@indent = \noindent), and the statement italic.  The numbers
%% the golden markdown carries in its prose (1,2,3,4,5,6 across Teorema and
%% Corolario) are exactly one shared counter, and the converter checks that.
\theoremstyle{plain}
\newtheorem{teorema}{__THEOREMNAME__}
\newtheorem{corolario}[teorema]{__COROLLARYNAME__}
\newtheorem{lema}[teorema]{__LEMMANAME__}
\newtheorem{proposicion}[teorema]{__PROPOSITIONNAME__}
\newtheorem{definicion}[teorema]{__DEFINITIONNAME__}
\newtheorem{observacion}[teorema]{__REMARKNAME__}
\renewcommand{\proofname}{__PROOFNAME__}

%% Spanish fixed names without babel
\renewcommand{\abstractname}{__ABSTRACTNAME__}
\renewcommand{\refname}{__REFNAME__}

%% Hanging-indent reference list, calibrated to the golden: the first line of
%% each entry starts 4pt LEFT of the text margin (ink x0 = 68.0) and the
%% continuation lines sit at x0 = 88.0, \small, 12pt baselines, ~2.1pt between
%% entries.  leftmargin 16pt with itemindent -20pt reproduces both edges.
%% The golden's reference list is spaced like LaTeX's own thebibliography:
%% every inter-word gap on an entry line is uniform (~3.40pt on a justified
%% line, including the gap after "Bombelli." and after "2000."), i.e. the
%% extra space after "." is switched off (as thebibliography does), and the
%% entries are set
%% \sloppy.  The body text keeps normal sentence spacing (7.44pt after "2/9."
%% on page 12), so this is local to the list, exactly as thebibliography does it.
\newenvironment{bibliolist}%
  {\small\sloppy\sfcode`\.=1000\relax
   \begin{list}{}{%
     \setlength{\topsep}{0pt}%
     \setlength{\partopsep}{0pt}%
     \setlength{\parsep}{0pt}%
     \setlength{\itemsep}{__ITEMSEP__}%
     \setlength{\leftmargin}{__LEFTMARGIN__}%
     \setlength{\itemindent}{__ITEMINDENT__}%
     \setlength{\labelwidth}{0pt}%
     \setlength{\labelsep}{__LABELSEP__}%
     \setlength{\listparindent}{0pt}%
     \renewcommand{\makelabel}[1]{##1}}}%
  {\end{list}}

%% Centred dedication / epigraph blocks
%% Golden page 17: last body line 88.99, "For Karim." 133.65, epigraph lines
%% 159.39 and 172.94 (one plain \baselineskip apart), "Referencias" 212.92.
%% The epigraph is centred on a measure narrower than the text block: its first
%% line is 363.8pt wide and breaks before "what", so the measure lies between
%% 363.8pt and 392.9pt.  \centering rather than the center environment, so the
%% skips below are the whole of the vertical spacing and are calibrated directly.
\newcommand{\dedicationline}[1]{%
  \par\vspace{__DEDSKIP__}{\centering\emph{#1}\par}}
\newcommand{\epigraphline}[1]{%
  \par\vspace{__EPISKIP__}%
  {\centering\parbox{__EPIWIDTH__}{\centering\emph{#1}}\par}%
  \vspace{__EPIAFTER__}}

%% The golden avoids overfull lines that unhyphenated Spanish text would
%% otherwise force; \emergencystretch supplies the extra pass that lets TeX
%% find those breaks. It only affects paragraphs the normal passes fail on,
%% so every other line break is untouched.
\tolerance=__TOLERANCE__
\emergencystretch=__EMSTRETCH__

%% ------------------------------------------------------------------
%% Over-wide displays.  Two displays in this manuscript, (5.10) and (6.5),
%% are wider than \linewidth as a single row; the golden sets each of them as
%% a centred two-row \begin{gathered} carrying one \tag, split at a \qquad
%% (inside the \boxed frame, for (6.5)).  The split is width-driven, not
%% source-driven: (6.5) has four top-level \qquad separators and the golden
%% breaks only at the third, i.e. greedy line filling.
%%
%% \autodisplay reproduces that at typesetting time.  It measures each
%% candidate row and only emits a \begin{gathered} when more than one row is
%% actually needed, so every display that already fits comes out byte-for-byte
%% as it would without this wrapper.
%% ------------------------------------------------------------------
\usepackage{booktabs}
\usepackage{etoolbox}
\makeatletter
\newcommand*\ag@rowm{}
\newcommand*\ag@bodym{}
\newcount\ag@rows
\newbox\ag@box
%% Width a packed row must fit into.  Not the bare \linewidth: the golden keeps
%% (6.5) to two rows even though its first three parts plus the \text{...} part
%% would still measure under \linewidth, so the usable width is \linewidth less
%% the room a right-hand \tag and the \boxed frame need.
\newdimen\ag@slack \ag@slack=__DISPSLACK__
\newdimen\ag@max
\newif\ifag@rowempty
\newcommand{\ag@flush}{%
  \ifag@rowempty\else
    \ifnum\ag@rows>0 \appto\ag@bodym{\\}\fi
    \expandafter\appto\expandafter\ag@bodym\expandafter{\ag@rowm}%
    \advance\ag@rows by 1
    \renewcommand*\ag@rowm{}\ag@rowemptytrue
  \fi}
\newcommand{\dpart}[1]{%
  \ifag@rowempty
    \appto\ag@rowm{#1}\ag@rowemptyfalse
  \else
    \setbox\ag@box\hbox{$\displaystyle\ag@rowm\qquad #1$}%
    \ag@max=\linewidth \advance\ag@max by -\ag@slack
    \ifdim\wd\ag@box>\ag@max
      \ag@flush\appto\ag@rowm{#1}\ag@rowemptyfalse
    \else
      \appto\ag@rowm{\qquad #1}%
    \fi
  \fi}
\newcommand{\autodisplay}[1]{%
  \renewcommand*\ag@rowm{}\renewcommand*\ag@bodym{}%
  \ag@rows=0 \ag@rowemptytrue
  #1%
  \ag@flush
  \ifnum\ag@rows>1
    \begin{gathered}\ag@bodym\end{gathered}%
  \else
    \ag@bodym
  \fi}
\makeatother

%% Theorem / corollary / proof blocks.  The golden markdown hard-codes its own
%% theorem numbering and its own bold head + italic statement, so these wrappers
%% supply only what amsthm would otherwise contribute: \topsep above and below,
%% no paragraph indent on the head line, and (for proofs) amsthm's rule-drawn
%% QED box placed by \pushQED/\popQED.  Measured in the golden: head lines sit
%% at x0=72.0 (unindented) with ~8.4-9.0pt of extra lead, inner paragraphs stay
%% indented at x0=88.9, and a proof whose QED will not fit on the last line
%% spends a whole extra line on it (the 35.4pt gap on page 7).
%% All six QED boxes in the golden sit on a line of their own, flush right,
%% one \baselineskip below the last text line -- amsthm's own \qed (penalty
%% 9999) would keep them on that line instead, so the break is forced here.
\newcommand{\qedownline}{%
  \unskip\nobreak\hfil\penalty-10000\hbox{}\nobreak\hfill\qedsymbol}
%% The golden separates the italic "Demostracion." head from the body by a
%% rigid 5.5pt (= \labelsep), not by an interword space -- measured 5.46pt of
%% ink gap on page 5 against 4.85pt for a stretchable sentence space -- and
%% sets the head flush at the margin (x0 = 72.0), not at \parindent.
\makeatletter
\newenvironment{proofblock}%
  {\par\addvspace{\topsep}%
   \noindent{\itshape\proofname\@addpunct{.}}\hskip\labelsep\ignorespaces}%
  {\qedownline\par\addvspace{\topsep}}
\makeatother

\pagestyle{plain}
\setcounter{secnumdepth}{3}

\begin{document}

%% Title block. Not \maketitle: the golden sets the title \LARGE *bold*
%% (LMRoman12-Bold scaled to 17.28pt -- lmbx12 is the largest LM bold face,
%% which is why no LMRoman17 appears in the golden's font list) and gives the
%% author and the correspondence address as two \large lines with no date.
%% The three skips are calibrated against the golden's measured ink tops:
%% title 114.92, author 148.77, email 162.72, \abstractname 204.58.
\vspace*{__TOPSKIP__}
\begin{center}
  {\LARGE\bfseries __TITLE__ \par}
  \vspace{__TITLESKIP__}
  {\large __AUTHOR__\\ __EMAIL__ \par}
\end{center}
\vspace{__PRESKIP__}

"""

DEFAULTS = dict(
    ITEMSEP='2.153pt', LEFTMARGIN='16pt', ITEMINDENT='-16pt', LABELSEP='4pt',
    DEDSKIP='31.22pt', EPISKIP='17.29pt', EPIAFTER='12.97pt', EPIWIDTH='0.8\\textwidth',
    TITLESKIP='16.45pt', TOLERANCE='9999', EMSTRETCH='2em', DISPSLACK='40pt', PRESKIP='4.59pt', TOPSKIP='9.90pt',
)

def build(md, overrides=None):
    meta, body = convert(md)
    p = dict(DEFAULTS)
    if overrides: p.update(overrides)
    abstract = meta.get('abstractname', 'Resumen')
    english = abstract.lower().startswith('abstract')
    names = {
        'THEOREMNAME': 'Theorem' if english else 'Teorema',
        'COROLLARYNAME': 'Corollary' if english else 'Corolario',
        'LEMMANAME': 'Lemma' if english else 'Lema',
        'PROPOSITIONNAME': 'Proposition' if english else "Proposici\\'on",
        'DEFINITIONNAME': 'Definition' if english else "Definici\\'on",
        'REMARKNAME': 'Remark' if english else "Observaci\\'on",
        'PROOFNAME': 'Proof' if english else "Demostraci\\'on",
        'REFNAME': 'References' if english else 'Referencias',
    }
    pre = PREAMBLE
    pre = pre.replace('__TITLE__', meta['title'])
    pre = pre.replace('__AUTHOR__', meta['author'])
    pre = pre.replace('__EMAIL__', meta['email'])
    pre = pre.replace('__ABSTRACTNAME__', abstract)
    for k, v in names.items():
        pre = pre.replace('__%s__' % k, v)
    for k, v in p.items():
        pre = pre.replace('__%s__' % k, v)
    return pre + '\n'.join(body) + '\n\n\\end{document}\n'

if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    md = io.open(src, encoding='utf-8').read()
    io.open(dst, 'w', encoding='utf-8').write(build(md))
    sys.stderr.write('wrote %s\n' % dst)
