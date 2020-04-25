from discord.ext.commands import Bot
import discord
import random
import linecache
import sys
sys.path.append(r'./')
from config import tkn

word = linecache.getline(r'words.txt', random.randrange(1, 9)).replace('\n', '').replace('\r', '')
player = 0
playerdiscord = [] #[[player, dm, role, alive, vote] ...]
lobbyfull = False
TOKEN = tkn
BOT_PREFIX = ("?", "!")
client = Bot(command_prefix=BOT_PREFIX)
votecount = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(name='startgame',
                description="Start the game",
                pass_context=True)
async def startgame(ctx):
    global lobbyfull
    if lobbyfull is True:
        await ctx.send('Game started. Check your DM to see your role. Then you guys can talk, try ask each other what their word is. After that, type !vote @SOMEONE to vote someone')
        global playerdiscord
        global player
        global word
        x = random.sample(range(player), 2)
        for each in x:
            playerdiscord[each][2] = 'spy'
        for each in range(player):
            if playerdiscord[each][2] == 'spy':
                await playerdiscord[each][1].send('You are a spy.')
            else:
                await playerdiscord[each][1].send('You are a innocent with the word ' + word + '.')
            

    else:
        await ctx.send('We need more players to start the game.')

@client.command(name='ready',
                description="Get ready for the game",
                pass_context=True)
async def ready(ctx):
    global player
    if player >= 6:
        global lobbyfull
        lobbyfull = True
        await ctx.send('Everyone is ready, type !startgame to start the game.')
    else:
        await ctx.send('You are ready, '  + ctx.message.author.mention + ' (' + str(player) + '/5)')
        dm = await ctx.message.author.create_dm()
        global playerdiscord
        playerdiscord.append([ctx.message.author, dm, 'Innocent', True, 0])
        player+=1

@client.command(name='vote',
                description="test",
                pass_context=True)
async def vote(ctx, member: discord.Member):
    global votecount
    global playerdiscord
    global player
    if votecount >= 6:
        highest = 0
        victim = 0
        for each in range(player):
            if playerdiscord[each][4] > highest:
                highest = playerdiscord[each][4]
                victim = each
        playerdiscord[victim][3] = False
        if playerdiscord[victim][2] == 'innocent':
            await ctx.send('Vote is done, ' + playerdiscord[victim][0].mention + ' is dead and his/her role is innocent. So sad.')
        else:
            await ctx.send('Vote is done, ' + playerdiscord[victim][0].mention + ' is dead and his/her role is spy, yee.')
        votecount = 0
        for each in range(player):
            playerdiscord[each][4] = 0
        
        winner = ''
        isSpyAlive = False
        isInnocentAlive = False
        alives = []

        for each in range(player):
            if playerdiscord[each][2] == 'innocent' and playerdiscord[each][3] == True:
                isInnocentAlive = True
            else:
                isSpyAlive = True
            if playerdiscord[each][3] == True:
                alives.append(1)

        if isInnocentAlive is False and isSpyAlive is True:
            winner = 'spy'
            await ctx.send('Gameover! The winners are the spies.')
        elif isInnocentAlive is True and isSpyAlive is False:
            winner = 'innocent'
            await ctx.send('Gameover! The winners are the innocents.')
        elif len(alives) <= 2 and isSpyAlive is True:
            winner = 'spy'
            await ctx.send('Gameover! The winners are the spies.')

        if winner != '':
            for each in range(player):
                await ctx.send(playerdiscord[each][0].mention + "'s role is " + playerdiscord[each][2])

    else:
        for each in range(player):
            if playerdiscord[each][3] == True and playerdiscord[each][0] == ctx.message.author:
                await ctx.send('Vote recorded(' + str(votecount) + '/5)')
                for each in range(player):
                    if playerdiscord[each][0] == member:
                        playerdiscord[each][4]+=1
                votecount+=1
                break
            else:
                print('burh')

client.run(TOKEN)

