import pygame
import os
from main import *
from menu import *
from global_inst import *



#loads the high scores saved from pickle file
def loadFile():
    #loads the scores using pickle
    with open("highscores.txt", "r") as f:
        scores = f.read().splitlines()

    scorefile = []
    for f in scores:
        # print(f)
        scorefile.append(int(f))
    return scorefile


#adds score to high score list if in top 10 scores
def addScore(newscore, highscores):
    highscores.append(newscore)

    #sort descending
    highscores.sort(reverse=True)

    #removes the lowest score that was present
    while(len(highscores) > 10):
        highscores.pop()


def saveScores (scored):
    f = open("highscores.txt", "w")
    for s in scored:
        f.write("%i\n" % s)
    f.close()
