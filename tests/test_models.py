from zeroemail.models import Folder, Level, Message, Objective, Progress, Thread


def test_minimal_level_fixture_builds():
    msg = Message(
        id="m-1",
        subject="Luce di San Vito",
        sender="sofia@example.com",
        body="The dossier is in the archive.",
        folder="inbox",
    )

    thread = Thread(id="t-1", messages=[msg], folder="inbox")
    folder = Folder(id="inbox", name="Inbox", threads=[thread])
    objective = Objective(id="o-1", description="Find the clue thread")
    level = Level(
        id="level-1",
        name="First Dispatch",
        folder="inbox",
        threads=[thread],
        objectives=[objective],
        shortcuts=["?", "/", "z", "o", "u"],
    )
    progress = Progress(current_level="level-1", learned_shortcuts=["?", "/", "z"])

    assert msg.subject == "Luce di San Vito"
    assert folder.threads[0].id == "t-1"
    assert level.objectives[0].description == "Find the clue thread"
    assert progress.current_level == "level-1"
