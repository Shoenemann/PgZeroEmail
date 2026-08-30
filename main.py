import pgzrun

from zeroemail.game import ZeroEmailGame


game = ZeroEmailGame()


def draw():
    game.draw()


def update():
    game.update()


def on_key_down(key):
    game.handle_key(key)


pgzrun.go()
