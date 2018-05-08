from highscores import loadFile
from menu import Menu


# game starts
if __name__ == "__main__":
    SCORES = loadFile()
    Menu(SCORES)
    exit()
