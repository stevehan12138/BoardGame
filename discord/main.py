from discord.ext.commands import Bot
import discord
import random
import linecache

word = linecache.getline(r'words.txt', random.randrange(1, 9)).replace('\n', '').replace('\r', '')
player = 0
playerdiscord = [] #[[player, dm, role, alive, vote] ...]
lobbyfull = False
TOKEN = 'NzAyNjgwNDg0OTU3NjUxMDE3.XqGv9w.mF4-92buTe6zmaJmkk2tUPVaZlY'
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
    await ctx.send('Vote recorded(' + str(votecount) + '/5')
    for each in range(player):
        if playerdiscord[each][0] == member:
            playerdiscord[each][4]+=1

client.run(TOKEN)

