import linecache
import random

class Boardgame:
    '''
                PlayerList
                    |
        -   -   -   -   -   -   -
        |   |   |   |   |   |   |
        1   2   3  ...
        |
        -   -
        |   |
   isAlive Role
    '''

    def __init__(self):
        self.playerId = 0
        self.playerCount = 0
        self.playerList = {}
        self.playerWord = linecache.getline(r'words.txt', random.randrange(1, 9)).replace('\n', '').replace('\r', '')

    def addPlayer(self,role):
        id = str(self.playerId)
        self.playerList[id] = {}
        self.playerList[id]['Role'] = role
        self.playerList[id]['isAlive'] = True
        self.playerId += 1
        self.playerCount += 1
        return id

    def isAlive(self,id):
        if self.playerList[id]['isAlive'] is True:
            return True
        else:
            return False

    def isSpy(self, id):
        if self.playerList[str(id)]['Role'] == 'spy':
            return True
        else:
            return False

    def kill(self,id):
        self.playerList[id]['isAlive'] = False

    def getAlivePlayers(self):
        alivePlayers = []
        for id in range(self.playerCount):
            if self.playerList[str(id)]['isAlive'] is True:
                alivePlayers.append(id)
        return alivePlayers

    def displayList(self):
        print(self.playerList)

    