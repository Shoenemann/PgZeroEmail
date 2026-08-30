from zeroemail.inbox import InboxState


def test_inbox_state_tracks_mutations_and_undo():
    state = InboxState()
    state.add_thread("t-1", "inbox")
    state.add_thread("t-2", "starred")
    state.star("t-1")
    state.mark_read("t-1")
    state.select("t-1")

    assert "t-1" in state.starred
    assert "t-1" in state.read
    assert "t-1" in state.selected

    undo = state.undo()
    assert undo is not None
    assert undo["action"] == "select"

    state.clear_selection()
    assert state.selected == []

    state.archive("t-2")
    assert state.history[-1]["action"] == "archive"
