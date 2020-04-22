from collections import Counter
from player import *
import random

def initGame(playerdata, player, spy):
    playerid = []
    for each in range(player):
        playerid.append('innocent')
        x = random.sample(range(player), spy)
    for each in x:
        playerid[each] = 'spy'

    for each in playerid:
        playerdata.addPlayer(each)

def startGame(playerdata):
    stillplaying = True
    winner = ''
    for playerId in range(playerdata.playerCount):
        if playerdata.isSpy(playerId):
            print('player #' + str(playerId) + ' is a spy')
        else:
            print('player #' + str(playerId) + "'s word is: " + playerdata.playerWord)
        #Network

    while stillplaying:
        for playerId in playerdata.getAlivePlayers():
            input('player #' + str(playerId) + " says: ")
            #network
        
        guess = vote(playerdata)
        stats = gameStats(playerdata)
        if guess is not False and guess == playerdata.playerWord:
            stillplaying = False
            winner = 'spy'
        else:
            stillplaying = stats['stillplaying']
            winner = stats['winner']
    
    print('game over! the winner is ' + winner)

def vote(playerdata):
    resultList = []
    for playerId in range(playerdata.playerCount):
        resultList.append(input('player #' + str(playerId) + ' voted: '))

    result = Counter(resultList).most_common(1)[0][0]
    playerdata.kill(result)
    if playerdata.playerList[str(result)]['Role'] == 'spy':
        guess = input('player #' + result + ' died and he is a spy, but he can still guess the word: ')
        return guess
    else:
        print('player #' + result + ' died and he is a innocent, so sad.')
        return False
    

def gameStats(playerdata):
    winner = ''
    isSpyAlive = False
    isInnocentAlive = False
    stillplaying = True
    alives = playerdata.getAlivePlayers()

    for id in alives:
        if playerdata.playerList[str(id)]['Role'] == 'innocent':
            isInnocentAlive = True
        else:
            isSpyAlive = True

    if isInnocentAlive is False and isSpyAlive is True:
        winner = 'spy'
        stillplaying = False
    elif isInnocentAlive is True and isSpyAlive is False:
        winner = 'innocent'
        stillplaying = False
    elif len(alives) <= 2 and isSpyAlive is True:
        winner = 'spy'
        stillplaying = False
    return {'stillplaying':stillplaying,'winner':winner}