import random
import linecache 

players = int(input('number of players: '))
spies = int(input('number of spies: '))
innocents = players - spies
word = linecache.getline(r'words.txt', random.randrange(1, 9)).replace('\n', '').replace('\r', '')
winner = ''

def main():
    counter = 0
    stillplaying = True
    playerid = setid(players,spies)
    playeralive = playerid
    for each in playerid:
        counter+=1
        if each == 'innocent':
            print('player #' + str(counter) +' is a innocent with the word '+ word)
        else:
            print('player #' + str(counter) +' is a spy')

    while stillplaying:
        counter = 0
        for each in playeralive:
            counter+=1
            print(playeralive)
            if each == 'dead':
                continue
            input('player #' + str(counter) +' says: ')
        
        result = vote(playeralive)
        playeralive[result[0]['victim']] = 'dead'
        templist = playeralive.copy()
        templist.remove('dead')

        if 'spy' not in playeralive:
            stillplaying = False
            winner = 'innocent'

        if 'innocent' not in playeralive:
            stillplaying = False
            winner = 'spies'
        elif len(templist) <= 2 and 'spy' in playeralive:
            stillplaying = False
            winner = 'spies'


        if result[0]['guess'] == 'correct':
            stillplaying = False
            winner = 'spies'
    print('Gameover! the winners are ' + winner)


def setid(players, spies):
    playerid = []
    for each in range(players):
        playerid.append('innocent')

    x = random.sample(range(players), spies)
    for each in x:
        playerid[each] = 'spy'
    return playerid

def vote(playerid):
    result = [{'victim':'','guess':''},[]]
    counter = 0

    for each in playerid:
        result[1].append(0)
    
    for each in playerid:
        counter+=1
        if each == 'dead':
            continue
        result[1][int(input('Player #' + str(counter) + ' voted: ')) - 1] += 1

    result[0]['victim'] = result[1].index(max(result[1]))
    id = str(result[0]['victim'] + 1)

    if playerid[result[0]['victim']] == 'spy':
        if input('player #' + id + ' died and he is a spy, he is making his final guesses ') == word:
            result[0]['guess'] = 'correct'
        else:
            result[0]['guess'] = 'wrong'
    else:
        print('player #' + id + ' died and he is a innocent, so sad')
    return result

main()

            