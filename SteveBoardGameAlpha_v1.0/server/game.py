from server import Server
from collections import Counter
from player import *
import random

s = Server('', 42069, 1024)

def main():
    playerdata = Boardgame()
    waitingRoom(6)
    initGame(playerdata, 6, 2)
    startGame(playerdata)


def waitingRoom(players):
    while True:
        s.newClient()
        for each in range(s.clientId):
            s.sendData(each, 'print', ('Player #%s has joined(%s/5).' % (s.clientId - 1, s.clientId - 1)))
        print('Player #%s has joined(%s/5).' % (s.clientId - 1, s.clientId - 1))
        if s.clientId == players:
            break
    print('All player joined. The game is starting now.')

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
            print('You are player #' + str(playerId) + ' and you are a spy')
            s.sendData(playerId,'print','You are player #' + str(playerId) + ' and you are a spy')
        else:
            print('You are player #' + str(playerId) + " and you are a innocent with the word: " + playerdata.playerWord)
            s.sendData(playerId,'print','You are player #' + str(playerId) + " and you are a innocent with the word: " + playerdata.playerWord)

    while stillplaying:
        for playerId in playerdata.getAlivePlayers():
            s.sendData(playerId, 'input', 'Describe your word:')
            response = s.receiveData(playerId)
            for player in range(playerdata.playerCount):
                s.sendData(player, 'print', 'player #' + str(playerId) + " says: " + response)
        
        guess = vote(playerdata)
        stats = gameStats(playerdata)
        if guess is not False and guess == playerdata.playerWord:
            for player in range(playerdata.playerCount):
                s.sendData(player, 'print', 'Spy got the right word!')
            stillplaying = False
            winner = 'spy'
        else:
            stillplaying = stats['stillplaying']
            winner = stats['winner']
    
    for playerId in range(playerdata.playerCount):
        s.sendData(playerId, 'gameover', 'game over! the winner is ' + winner)
    print('game over! the winner is ' + winner)

def vote(playerdata):
    resultList = []
    for playerId in range(playerdata.playerCount):
        s.sendData(playerId, 'input', 'Vote someone you think is bad: ')
        resultList.append(s.receiveData(playerId))

    result = Counter(resultList).most_common(1)[0][0]
    playerdata.kill(result)
    if playerdata.playerList[str(result)]['Role'] == 'spy':
        for playerId in range(playerdata.playerCount):
            s.sendData(playerId, 'print', 'player #' + result + ' died and he is a spy, but he can still guess the word: ')
        s.sendData(result, 'input', '')
        return s.receiveData(result)
    else:
        print('player #' + result + ' died and he is a innocent, so sad.')
        for playerId in range(playerdata.playerCount):
            s.sendData(playerId, 'print', 'player #' + result + ' died and he is a innocent, so sad.')
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

main()