from zeroemail.shortcuts import SHORTCUTS, SOURCE_SHORTCUTS, validate_registry


def test_registry_has_all_source_commands():
    missing = validate_registry(SOURCE_SHORTCUTS)
    assert not missing, f"Missing or duplicate source commands: {missing}"
    assert len({shortcut.id for shortcut in SHORTCUTS}) == len(SHORTCUTS)


def test_registry_lookups_work():
    by_notation = {shortcut.notation: shortcut for shortcut in SHORTCUTS}
    assert by_notation["?"]
    assert by_notation["/"]
    assert by_notation["gi"].category == "navigation"
    assert by_notation["e"].category == "thread_actions"
    assert by_notation["x"].category == "selection"
