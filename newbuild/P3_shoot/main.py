from highscores import loadFile
from menu import Menu


if __name__ == "__main__":
    SCORES = loadFile()
    Menu(SCORES)
    exit()
