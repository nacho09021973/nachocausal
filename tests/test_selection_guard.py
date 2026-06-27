import ast
import importlib
import inspect
import sys

import pytest

from nachocausal import generator
from nachocausal import selection_guard
from nachocausal.selection_guard import verify_selection_order_only


def test_selection_guard_import_does_not_pull_in_scoring():
    for mod in list(sys.modules):
        if mod.startswith("nachocausal.scoring"):
            del sys.modules[mod]
    importlib.reload(selection_guard)
    assert not any(m.startswith("nachocausal.scoring") for m in sys.modules)


def test_selection_guard_source_is_coordinate_free():
    tree = ast.parse(inspect.getsource(selection_guard))
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef,
                             ast.Module)) and ast.get_docstring(node):
            node.body = node.body[1:]
    code_src = ast.unparse(tree)
    for forbidden in ("embedding", "Coordinates", "[:, 1]", "scoring"):
        assert forbidden not in code_src, f"selection guard references {forbidden!r}"


def minimal_elements_selector(past_matrix):
    has_past = past_matrix.any(axis=1)
    return {"R": {int(i) for i, value in enumerate(has_past) if not value}}


def label_zero_selector(_past_matrix):
    return {"R": {0}}


def test_selection_guard_accepts_relabel_conjugate_selection():
    emb, _, _ = generator.numpy_sprinkle(seed=20240618, intensity=420.0)
    C = generator.past_matrix_fast(emb, "BH")
    verify_selection_order_only(C, minimal_elements_selector, seed=1)


def test_selection_guard_can_fail_on_label_dependent_selection():
    emb, _, _ = generator.numpy_sprinkle(seed=20240618, intensity=420.0)
    C = generator.past_matrix_fast(emb, "BH")
    with pytest.raises(ValueError):
        verify_selection_order_only(C, label_zero_selector, seed=1)
