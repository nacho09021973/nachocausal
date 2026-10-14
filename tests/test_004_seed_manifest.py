"""C1/C2 checks with mocked draws and synthetic IDs; no virgin causet is generated."""

import json
import subprocess

import pytest

from nachocausal2p1 import seed_manifest as manifest, thresholds

SHA = "0123456789abcdef0123456789abcdef01234567"
SEEDS = list(range(8_000_000, 8_000_020))  # synthetic IDs, not a draw


@pytest.fixture
def frozen(monkeypatch, tmp_path):
    monkeypatch.setattr(thresholds, "STATUS", "FROZEN")
    monkeypatch.setattr(manifest, "MANIFEST_PATH", tmp_path / "manifest.json")
    monkeypatch.setattr(manifest, "_draw", lambda sha: list(SEEDS))
    calls = []

    def git(*args):
        calls.append(args)
        if args[0] == "log":
            return SHA + "\n"
        if args[0] == "show":
            return manifest.MANIFEST_PATH.read_text()
        return ""

    monkeypatch.setattr(manifest, "_git", git)
    return calls


def doc():
    return {"freeze_commit": SHA, "draw_seed": 0x01234567, "seeds": list(SEEDS)}


def test_c2_creates_manifest_once_and_checks_instrument(frozen):
    path = manifest.create_manifest(SHA)
    assert json.loads(path.read_text()) == doc()
    assert ("diff", "--exit-code", SHA, "--", *manifest.SEALED_PATHS) in frozen
    assert manifest.load_manifest() == doc()
    with pytest.raises(FileExistsError):
        manifest.create_manifest(SHA)


def test_candidate_never_draws_or_loads_manifest(monkeypatch):
    def forbidden(*args):
        raise AssertionError("no draw or manifest read before freeze")

    monkeypatch.setattr(thresholds, "STATUS", "CANDIDATE_NOT_FROZEN")
    monkeypatch.setattr(manifest, "_draw", forbidden)
    monkeypatch.setattr(manifest, "load_manifest", forbidden)
    assert thresholds.validation_seeds() == ()
    with pytest.raises(RuntimeError, match="FROZEN"):
        manifest.create_manifest(SHA)


@pytest.mark.parametrize("change", [
    {"freeze_commit": SHA[:8]}, {"freeze_commit": "f" * 40}, {"draw_seed": 5},
    {"seeds": []}, {"seeds": list(reversed(SEEDS))},
    {"seeds": SEEDS[:-1] + [SEEDS[0]]}, {"seeds": SEEDS[:-1] + [7_000_100]},
    {"seeds": SEEDS[:-1] + [8_000_050]}, {"seeds": [str(s) for s in SEEDS]},
    {"extra": True},
])
def test_manifest_refuses_wrong_c1_draw_or_band(frozen, change):
    bad = doc()
    bad.update(change)
    with pytest.raises((ValueError, RuntimeError)):
        manifest.check_manifest(bad)


def test_drift_and_dirty_tree_stop_before_draw(frozen, monkeypatch):
    original = manifest._git

    def forbidden_draw(*args):
        raise AssertionError("draw must not be reached")

    monkeypatch.setattr(manifest, "_draw", forbidden_draw)

    def drift(*args):
        if args[0] == "diff":
            raise RuntimeError("instrument drift")
        return original(*args)

    monkeypatch.setattr(manifest, "_git", drift)
    with pytest.raises(RuntimeError, match="instrument drift"):
        manifest.create_manifest(SHA)
    monkeypatch.setattr(manifest, "_git", lambda *a: " M tests/x.py\n" if a[0] == "status" else original(*a))
    with pytest.raises(RuntimeError, match="clean tree"):
        manifest.create_manifest(SHA)
    assert not manifest.MANIFEST_PATH.exists()


def test_uncommitted_manifest_is_refused(frozen, monkeypatch):
    manifest.MANIFEST_PATH.write_text(json.dumps(doc()))
    original = manifest._git
    monkeypatch.setattr(manifest, "_git", lambda *a: "{}\n" if a[0] == "show" else original(*a))
    with pytest.raises(RuntimeError, match="committed HEAD"):
        manifest.load_manifest()


def test_frozen_without_manifest_cannot_admit_virgin_seed(frozen):
    from nachocausal2p1 import validate

    with pytest.raises(FileNotFoundError):
        validate.check_seed(SEEDS[0])


def test_recipe_uses_frozen_rng_seed_band_and_ensemble(monkeypatch):
    calls = []

    class FakeRng:
        def choice(self, band, *, size, replace):
            calls.append((int(band[0]), int(band[-1]), len(band), size, replace))
            return list(reversed(SEEDS))

    def rng(seed):
        calls.append(seed)
        return FakeRng()

    monkeypatch.setattr(manifest.np.random, "default_rng", rng)
    assert manifest._draw(SHA) == SEEDS
    assert calls == [0x01234567, (8_000_000, 8_999_999, 1_000_000, 20, False)]


def test_actual_git_c1_c2_binding_and_drift(monkeypatch, tmp_path):
    """Real Git metadata, synthetic document/instrument/draw; no actual C1 or C2 in this repo."""
    def git(*args):
        return subprocess.run(["git", "-C", str(tmp_path), "-c", "core.hooksPath=/dev/null", *args],
                              check=True, capture_output=True, text=True).stdout.strip()

    git("init", "-q")
    git("config", "user.name", "Manifest test")
    git("config", "user.email", "manifest-test@example.invalid")
    (tmp_path / "docs").mkdir()
    (tmp_path / "nachocausal2p1").mkdir()
    frozen_doc = tmp_path / manifest.FROZEN_DOC
    instrument = tmp_path / "nachocausal2p1/thresholds.py"
    frozen_doc.write_text("synthetic frozen document\n")
    instrument.write_text("synthetic immutable instrument\n")
    git("add", manifest.FROZEN_DOC, "nachocausal2p1/thresholds.py")
    git("commit", "-qm", "Synthetic C1")
    sha = git("rev-parse", "HEAD")
    monkeypatch.setattr(manifest, "ROOT", tmp_path)
    monkeypatch.setattr(manifest, "MANIFEST_PATH", tmp_path / manifest.MANIFEST_REL)
    monkeypatch.setattr(thresholds, "STATUS", "FROZEN")
    monkeypatch.setattr(manifest, "_draw", lambda _: list(SEEDS))
    manifest.create_manifest(sha)
    with pytest.raises(RuntimeError, match="provenance check failed"):
        manifest.load_manifest()  # not yet committed
    git("add", manifest.MANIFEST_REL)
    git("commit", "-qm", "Synthetic C2")
    assert git("rev-parse", "HEAD") != sha
    assert manifest.load_manifest()["freeze_commit"] == sha
    instrument.write_text("drift\n")
    with pytest.raises(RuntimeError, match="provenance check failed"):
        manifest._check_freeze(sha)
    with pytest.raises(RuntimeError, match="clean tree"):
        manifest.load_manifest()
