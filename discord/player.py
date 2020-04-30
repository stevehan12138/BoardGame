import linecache
import random
import discord
from discord.ext.commands import Bot

class PlayerData:
    '''
                PlayerList
                    |
        -   -   -   -   -   -   -
        |   |   |   |   |   |   |
        |   ...
        |
        -    -   -   -   -     -
        |    |   |   |   |     |
   isAlive Role Vote DM Player Voted
    '''

    def __init__(self):
        self.playerCount = 0
        self.playerList = []
        self.playerWord = linecache.getline(r'words.txt', random.randrange(1, 9)).replace('\n', '').replace('\r', '')
        self.votecount = 0

    async def addPlayer(self, role, player: discord.Member):
        if self.findPlayer(player) is False:
            self.playerList.append({})
            self.playerList[self.playerCount]['Role'] = role
            self.playerList[self.playerCount]['isAlive'] = True
            self.playerList[self.playerCount]['Vote'] = 0
            self.playerList[self.playerCount]['Player'] = player
            self.playerList[self.playerCount]['DM'] = await player.create_dm()
            self.playerList[self.playerCount]['Voted'] = False
            self.playerCount += 1
            return True
        else:
            return False

    def isAlive(self, player: discord.Member):
        id = self.findPlayer(player)
        if self.playerList[id]['isAlive'] is True:
            return True
        else:
            return False

    def isSpy(self, player: discord.Member):
        id = self.findPlayer(player)
        if self.playerList[str(id)]['Role'] == 'spy':
            return True
        else:
            return False

    def kill(self,id):
        self.playerList[id]['isAlive'] = False

    def getAlivePlayers(self):
        alivePlayers = []
        for id in range(self.playerCount):
            if self.playerList[id]['isAlive'] is True:
                alivePlayers.append(id)
        return alivePlayers

    def findPlayer(self, player: discord.Member):
        id = False
        for each in range(self.playerCount):
            if self.playerList[each]['Player'] == player:
                id = each
            else:
                pass
        return id

    def gameStats(self):
        winner = False
        alives = self.getAlivePlayers()
        isInnocentAlive = False
        isSpyAlive = False
        for each in alives:
            if self.playerList[each]['Role'] == 'innocent':
                isInnocentAlive = True
            else:
                isSpyAlive = True

        if isInnocentAlive is False and isSpyAlive is True:
            winner = 'spies'
        elif isInnocentAlive is True and isSpyAlive is False:
            winner = 'innocents'
        elif len(alives) <= 2 and isSpyAlive is True:
            winner = 'spies'
        
        return winner

    def resetVoting(self):
        self.votecount = 0
        for each in range(self.playerCount):
            self.playerList[each]['Vote'] = 0
            self.playerList[each]['Voted'] = False
        return True