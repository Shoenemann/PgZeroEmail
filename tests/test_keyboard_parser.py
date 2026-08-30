import time

from zeroemail.keyboard import KeyboardParser


def test_parser_handles_single_and_multi_key_shortcuts():
    parser = KeyboardParser(timeout_seconds=0.25)

    assert parser.feed("?") == "help"
    assert parser.feed("/") == "search"

    parser.feed("g")
    parser.feed("i")
    assert parser.current_sequence() == ["g", "i"]
    assert parser.get_result() == "gi"

    parser.feed("*")
    parser.feed("a")
    assert parser.get_result() == "*a"

    parser.feed("[")
    assert parser.get_result() == "["

    parser.feed("{")
    assert parser.get_result() == "{"


def test_parser_handles_shifted_actions_and_timeouts():
    parser = KeyboardParser(timeout_seconds=0.05)

    parser.feed("I", shifted=True)
    assert parser.get_result() == "Shift + i"

    parser.feed("g")
    time.sleep(0.07)
    assert parser.get_result() is None
    assert parser.current_sequence() == []


def test_parser_rejects_incomplete_sequences():
    parser = KeyboardParser(timeout_seconds=0.25)
    parser.feed("g")
    assert parser.get_result() is None
    assert parser.current_sequence() == ["g"]

    parser.reset()
    assert parser.current_sequence() == []
