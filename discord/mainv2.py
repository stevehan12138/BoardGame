import discord
import random
from discord.ext.commands import Bot
from player import PlayerData
from config import tkn

BOT_PREFIX = ("?", "!")
client = Bot(command_prefix=BOT_PREFIX)
p = PlayerData()
players = 4
spies = 1
lobbyfull = False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(name='ready',
                description="ready",
                pass_context=True)
async def ready(ctx):
    global p
    global players
    global lobbyfull
    if await p.addPlayer('innocent',ctx.message.author) is True:
        await ctx.send('You are ready, '  + ctx.message.author.mention + ' (' + str(p.playerCount) + '/4)')
    else:
        await ctx.send("You ready too much you know stop it get some help")
    if p.playerCount == players:
        await ctx.send('Everyone is ready, type !startgame to start the game.')
        lobbyfull = True

@client.command(name='startgame',
                description="Start the game",
                pass_context=True)
async def startgame(ctx):
    global lobbyfull
    global spies
    if lobbyfull is True:
        await ctx.send('Game started. Check your DM to see your role. Then you guys can talk, try ask each other what their word is. After that, type !vote @SOMEONE to vote someone')
        global p
        x = random.sample(range(players), spies)
        for each in x:
            p.playerList[each]['Role'] = 'spy'
        for each in range(player):
            if p.playerList[each][2] == 'spy':
                await p.playerList[each]['DM'].send('You are a spy.')
            else:
                await p.playerList[each]['DM'].send('You are a innocent with the word ' + p.playerWord + '.')

@client.command(name='vote',
                description="vote",
                pass_context=True)
async def vote(ctx, player: discord.Member):
    global p
    global players
    voter = p.findPlayer(ctx.message.author)
    victim = p.findPlayer(player)
    if p.playerList[voter]['isAlive'] is True and p.playerList[victim]['isAlive'] is True and p.playerList[voter]['Voted'] is not True:
        p.votecount+=1
        p.playerList[voter]['Voted'] = True
        p.playerList[victim]['Vote']+=1
        await ctx.send('Vote recorded(' + str(p.votecount) + '/4)')
        if p.votecount == players:
            await ctx.send('Everyone voted, calculating the result...')
            result = []
            for each in range(players):
                result.append(p.playerList[each]['Vote'])
            finalresult = result.index(max(result))
            p.kill(finalresult)
            if p.playerList[finalresult]['Role'] == 'spy':
                await ctx.send(p.playerList[finalresult]['Player'].mention + ' is dead and he is a spy, goodjob.')
            else:
                await ctx.send(p.playerList[finalresult]['Player'].mention + ' is dead and he is a innocent, so sad.')
            p.resetVoting()

            winner = p.gameStats()
            if winner is not False:
                await ctx.send('Game over! ' + winner + 'are the winners!')

    else:
        await ctx.send("You can't vote because you voted a dead person or you are dead, or you voted too many times.")

client.run(tkn)