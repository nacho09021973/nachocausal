import ast
import importlib
import inspect
import sys

import numpy as np

from nachocausal import c1_selector as c1_selector_module
from nachocausal.c1_selector import (
    c1_selector,
    c1_status,
    cover_relations,
    down_closure,
    maximal_elements,
    relational_interface,
)
from nachocausal.selection_guard import verify_selection_order_only


def test_c1_selector_import_does_not_pull_in_scoring():
    for mod in list(sys.modules):
        if mod.startswith("nachocausal.scoring"):
            del sys.modules[mod]
    importlib.reload(c1_selector_module)
    assert not any(m.startswith("nachocausal.scoring") for m in sys.modules)


def test_c1_selector_source_is_coordinate_free():
    tree = ast.parse(inspect.getsource(c1_selector_module))
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef,
                             ast.Module)) and ast.get_docstring(node):
            node.body = node.body[1:]
    code_src = ast.unparse(tree)
    for forbidden in ("embedding", "Coordinates", "[:, 1]", "scoring"):
        assert forbidden not in code_src, f"C1 selector references {forbidden!r}"


def chain_poset(n):
    C = np.zeros((n, n), dtype=bool)
    for y in range(n):
        for x in range(y):
            C[y, x] = True
    return C


def diamond_poset():
    C = np.zeros((4, 4), dtype=bool)
    C[1, 0] = True
    C[2, 0] = True
    C[3, 1] = True
    C[3, 2] = True
    C[3, 0] = True
    return C


def two_component_poset():
    C = np.zeros((4, 4), dtype=bool)
    C[1, 0] = True
    C[3, 2] = True
    return C


def assert_max_reference_trivializes(C):
    selection = c1_selector(C)
    reference = maximal_elements(C)
    assert selection["R"] == reference
    assert down_closure(C, reference) == frozenset(range(C.shape[0]))
    assert selection["interface"] == frozenset()
    assert c1_status(selection) == "NO_INTERFACE"


def test_max_reference_trivializes_hand_built_finite_posets():
    for C in (chain_poset(1), chain_poset(5), diamond_poset(), two_component_poset()):
        assert_max_reference_trivializes(C)


def test_c1_selector_selection_guard_on_synthetic_posets():
    for C in (chain_poset(5), diamond_poset(), two_component_poset()):
        verify_selection_order_only(C, c1_selector, seed=17)


def v_poset():
    """Lean witness poset (Horizon.lean `VPoset`): a < b, a < c, b || c."""
    C = np.zeros((3, 3), dtype=bool)
    C[1, 0] = True  # a < b
    C[2, 0] = True  # a < c
    return C


def test_corrected_orientation_nonempty_on_lean_witness():
    # Executable counterpart of `VPoset.relationalHorizon_nonempty_witness`:
    # with reference R = {b} (a strict subset of the maximal elements),
    # the infalling interface contains exactly the cover link (a, c).
    C = v_poset()
    interface = relational_interface(C, frozenset({1}))
    assert interface == frozenset({(0, 2)})


def test_old_orientation_is_empty_for_every_reference():
    # Executable counterpart of `relationalHorizonOld_eq_empty`: cover pairs
    # from B_R into A_R do not exist for any reference on these posets.
    for C in (chain_poset(5), diamond_poset(), two_component_poset(), v_poset()):
        n = C.shape[0]
        covers = cover_relations(C)
        for bits in range(1 << n):
            reference = frozenset(i for i in range(n) if bits & (1 << i))
            accessible = down_closure(C, reference)
            black_region = frozenset(i for i in range(n) if i not in accessible)
            old_orientation = frozenset(
                (x, y) for x, y in covers if x in black_region and y in accessible
            )
            assert old_orientation == frozenset()
