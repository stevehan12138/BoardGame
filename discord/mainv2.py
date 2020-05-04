import discord
import random
from discord.ext.commands import Bot
from player import PlayerData
from config import tkn

BOT_PREFIX = ("?", "!")
client = Bot(command_prefix=BOT_PREFIX)
p = PlayerData()
players = 5
spies = 1
lobbyfull = False
channel = None
started = False

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
    global channel
    if await p.addPlayer('innocent',ctx.message.author) is True:
        await ctx.send('You are ready, '  + ctx.message.author.mention + ' (' + str(p.playerCount) + '/5)')
        channel = ctx
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
    global started
    if lobbyfull is True and started is False:
        started = True
        await ctx.send('Game started. Check your DM to see your role. Then you guys can talk, try ask each other what their word is. After that, type !vote @SOMEONE to vote someone')
        await ctx.send('Spies can type !guess WORD in their DM to the bot and guess the word if they think that they got the right word.')
        global p
        x = random.sample(range(players), spies)
        for each in x:
            p.playerList[each]['Role'] = 'spy'
        for each in range(players):
            if p.playerList[each]['Role'] == 'spy':
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
    if voter is not False and victim is not False:
        if p.playerList[voter]['isAlive'] is True and p.playerList[victim]['isAlive'] is True and p.playerList[voter]['Voted'] is not True:
            p.votecount+=1
            p.playerList[voter]['Voted'] = True
            p.playerList[victim]['Vote']+=1
            await ctx.send('Vote recorded(' + str(p.votecount) + '/' + str(len(p.getAlivePlayers())) + ')')
            if p.votecount == len(p.getAlivePlayers()):
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
                    await ctx.send('Game over! ' + winner + ' are the winners!')
                    await ctx.send('The word is ' + p.playerWord + ' for innocents.')

        else:
            await ctx.send("You can't vote because you voted a dead person or you are dead, or you voted too many times.")
    else:
        await ctx.send("You are not playing or you voted someone that is not playing.")

@client.command(name='guess',
                description="vote",
                pass_context=True)
async def guess(ctx, word):
    global p
    global channel
    id = p.findPlayer(ctx.message.author)
    if id is not False:
        if isinstance(ctx.channel, discord.DMChannel) and p.playerList[id]['Role'] == 'spy':
            if word.lower() == p.playerWord:
                await channel.send('Gameover! ' + ctx.message.author.mention + ' is the spy and he got the word.')
            else:
                p.playerList[p.findPlayer(ctx.message.author)]['isAlive'] = False
                await channel.send(ctx.message.author.mention + ' is a spy and he was trying to guess the word, but it was wrong. Now he is dead, yee.')
        else:
            await ctx.send("You can't do that in a public channel, or you aren't a spy")
    else:
        await ctx.send("You aren't playing stop it get some help")

client.run(tkn)