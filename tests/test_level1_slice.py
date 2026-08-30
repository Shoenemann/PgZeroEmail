from zeroemail.game import ZeroEmailGame


def test_level_one_tracks_search_and_undo_flow():
    game = ZeroEmailGame()
    game.start_level("level-1")

    assert game.level.id == "level-1"
    assert game.level.name == "First Dispatch"

    found = game.search("Luce di San Vito")
    assert found is True
    assert "t-1" in game.current_matches

    game.open_thread("t-1")
    assert game.active_thread_id == "t-1"

    game.record_mistake()
    game.undo()
    assert game.active_thread_id is None

    assert game.is_level_complete() is False

    game.search("Sofia")
    game.open_thread("t-2")
    game.complete_objective()
    assert game.is_level_complete() is True
