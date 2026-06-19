"""Enforce the dev/validation and observable/scoring separations as RUNNABLE
guards, not comments (founding rule; cmte SWE MAJOR-3).

1. Importing the order-only estimator must NOT pull in nachocausal.scoring
   (which reveals r). 2. The estimator source must not reference the embedding
   or the scoring subpackage. 3. Guard-v must actually RAISE when O is made to
   depend on labels — proving it is not decoration.
"""

import importlib
import sys

import numpy as np

from nachocausal import estimator, generator


def test_estimator_import_does_not_pull_in_scoring():
    for mod in list(sys.modules):
        if mod.startswith("nachocausal.scoring"):
            del sys.modules[mod]
    importlib.reload(estimator)
    assert not any(m.startswith("nachocausal.scoring") for m in sys.modules), \
        "importing the estimator must not import the scoring subpackage"


def test_estimator_source_is_coordinate_free():
    # Check the executable source with the module/function docstrings stripped
    # (the docstrings legitimately *mention* scoring/coordinates in prose; the
    # import-leak test above covers the real no-scoring-import guarantee).
    import ast
    import inspect

    tree = ast.parse(inspect.getsource(estimator))
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef,
                             ast.Module)) and ast.get_docstring(node):
            node.body = node.body[1:]  # drop the docstring expr
    code_src = ast.unparse(tree)
    for forbidden in ("embedding", "Coordinates", "[:, 1]", "scoring"):
        assert forbidden not in code_src, f"estimator code references {forbidden!r}"


def test_guard_v_can_fail():
    # A genuine order-only O is invariant under relabelling: verify_order_only
    # returns without raising. Then we corrupt the recomputation to depend on a
    # label and confirm the guard RAISES — i.e. it is a guardrail that can fail.
    emb, _, _ = generator.numpy_sprinkle(seed=20240617, intensity=420.0)
    C = generator.past_matrix_fast(emb, "BH")
    estimator.verify_order_only(C, seed=1)  # must not raise on real order-only O

    import pytest
    orig = estimator.estimate_O

    def label_dependent(pm):
        O, mn, L = orig(pm)
        if mn:
            O[mn[0]] = O[mn[0]] + 1  # contaminate with an index-dependent value
        return O, mn, L

    estimator.estimate_O = label_dependent
    try:
        with pytest.raises(ValueError):
            estimator.verify_order_only(C, seed=1)
    finally:
        estimator.estimate_O = orig
