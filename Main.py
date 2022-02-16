import asyncio
import os
import random
from perlin_noise import PerlinNoise
from math import floor, ceil
from numpy import place, sign, square
import time
import re
import discord
from discord.ext import commands
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '!',case_insensitive=True, intents = intents)
client.remove_command('help')

task = {}

global save
save = eval(open("save.txt","r",encoding="utf8").read())

def write():
    File = open("save.txt","w",encoding="utf8")
    File.write(str(save))
    File.close()

tools = {'hands' : {'outputs' : ['stick', 'rock', 'dirt', ], 'amount' : 1}}
items = {}
recipes = {
    'thatch' : {
        'recipe' : {
            'tuft of grass' : 3,
        },
        'requires' : '(True)',
        'intel':0
    },
    'rope' : {
        'recipe' : {
            'mud clump' : 1,
            'thatch' : 2,
        },
        'requires' : 'has(id, "thatch")',
        'intel':3
    },
    'bundle of sticks' : {
        'recipe' : {
            'rope' : 1,
            'stick' : 10
        },
        'requires' : 'has(id, "rope")',
        'intel':5
    },
    'crude wooden wall' : {
        'recipe' : {
            'bundle of sticks' : 1,
            'mud clump' : 5
        },
        'requires' : 'has(id, "bundle of sticks")',
        'intel':15
    },
    'crude axe' : {
        'recipe' : {
            'rope' : 2,
            'stick' : 2,
            'mud clump' : 1,
            'rock' : 3
        },
        'requires' : 'has(id, "rope") and has(id, "rock")',
        'intel':10,
        'durability': 10
    },
    'crude pickaxe' : {
        'recipe' : {
            'rope' : 2,
            'stick' : 1,
            'mud clump' : 1,
            'rock' : 4
        },
        'requires' : 'has(id, "rope") and has(id, "rock")',
        'intel':10,
        'durability': 10
    },
    'crude fishing pole' : {
        'recipe' : {
            'rope' : 3,
            'stick' : 2,
            'mud clump' : 1,
            'rock' : 1
        },
        'requires' : 'has(id, "rope") and has(id, "rock")',
        'intel':10,
        'durability': 10
    },
    
}

#functions

def user_check(id):
    defaults = {
            'stats' : {
                'alive' : True,
                'intelligence' : 0,
                'int level' : 0,
                'online' : 0
            },
            'settings' : {
                
            },
            'inv' : {},
            'recipes' : []
    } 
    try:
        save['users'][id]
        for i in defaults:
            if i not in save['users'][id]:
                save['users'][id][i] = defaults[i]
    except:
        random.seed()
        pos = [random.randint(0,500)-250, random.randint(0,500)-250]
        x,y = ( -(list(pos)[1]) , (list(pos)[0]) )
        square = fetch_square(id, x, y)
        while square['biome'] != 'temperate' or square['square'] != 'grass' :
            pos = [random.randint(0,500)-250, random.randint(0,500)-250]
            x,y = ( -(list(pos)[1]) , (list(pos)[0]) )
            square = fetch_square(id, x, y)
        
        save['users'][id] = {
            'stats' : {
                'alive' : True,
                'intelligence' : 0,
                'int level' : 0,
                'online' : 0
            },
            'settings' : {
                
            },
            'pos' : pos,
            'inv' : {},
            'recipes' : []
    } 

def fetch_square(id = 0, x = 0, y = 0, zoom = 1000):
    noise = PerlinNoise(octaves=5, seed=543)
    biomenoise = PerlinNoise(octaves=1, seed=558)
    
    elevation_scale = '🟪🟪🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟨🟫🟫🟫🟫🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬜⬜'
    squares ={
        '🟪' : 'deep ocean',
        '🟦' : 'ocean',
        '🟨' : 'sand',
        '🟫' : 'dirt',
        '🟩' : 'grass',
        '⬛' : 'stone',
        '⬜' : 'snow',
        '🟧' : 'mud'
    }
    biomes = {      
    'desert':{'🟫' : '🟨', '🟩' : '🟨', '🟦' : '🟨', '🟪':'🟦'},
    'rocky' : {'🟫' : '⬛', '🟩' : '⬛', '⬜' : '⬛', '🟦' : '🟨'},
    'grasslands':{'🟫' : '🟩'},
    'temperate' : {},
    'forest' : {'🟩' : '🟫', '🟨' : '🟧'},
    'swamp' : {'🟫' : '🟧', '🟩' : '🟫','🟨' : '🟦', '🟪' : '🟦'},
    'snow' : {'🟩':'⬜', '⬛':'⬜', '🟫':'⬛'}
    }
    
    has = []
    minerals = []
    
    pos =[(x)/zoom,(y)/zoom]
    elevation=noise(pos)
    biome = biomenoise(pos)
    random.seed(str(pos))
    a2=elevation+0.5
    biome=biome+0.5
    a2*=len(elevation_scale)
    biome*=len(list(biomes.keys()))
    vis = elevation_scale[max(0, min(floor(a2), len(elevation_scale)-1))]
    biome = (list(biomes.keys()))[max(0, min(floor(biome), len(list(biomes.keys()))-1))]
    
    square = squares[vis]
    
    temp = 101-round((elevation+0.5)*101,2)
    
    wheatnoise = PerlinNoise(octaves=15, seed=558)
    
    if vis in biomes[biome]:
        vis = biomes[biome][vis]
        sqaure = squares[vis]
    
    if str(pos) in save['terrrain']['overide']:changed = save['terrrain']['overide'][str(pos)]#Need to make a copy so it doesn't directly change the overide dict, but when tried python seems to break down and not accept that
    #pre item gen overide does not work because of that
    
    #Top is least important and bottom is most important (aka which is shown on top)
    #To do:
    # -Make a better layering sytem for this mess
    # -Make a more unified system
    # -More organization
    # -Better overide system
    
    placements = []
    
    #item gen go here?
    if biome == 'rocky':#many rocks :)
        for i in range(max(random.randint(-1,5), 0)):
            if i == 0:continue
            has.append('rock')
    if square in ['grass', 'dirt', 'mud']:
        for i in range(max(random.randint(-1 if biome == 'forest' else -4,2), 0)):#more trees=more sticks
            if i == 0:continue
            has.append('stick')
    if square in ['mud', 'dirt']:
        if random.randint(0,100) == 0:
            has.append('mushroom')
        if random.randint(0,3) == 0:
            has.append('mud clump')
    if biome == 'swamp' and square in ['mud', 'dirt']:
        if random.randint(0,5) == 0:
            for i in range(random.randint(1,3)):has.append('herb')
    if square == 'grass':
        if random.randint(0, max(round(a2-(21 if biome == 'grasslands' else 15)), 0)) == 0:    
            has.append('tuft of grass')
        for i in range(max(random.randint(-2,3), 0)):#Move rock code somewhere else?
            if i == 0:continue
            has.append('rock')
        if random.randint(0,5) == 0:
            for i in range(random.randint(1,4)):has.append('mud clump')
    if not biome in ['desert', 'rocky', 'snow'] and square in ['mud', 'sand'] and wheatnoise(pos) >= 0.3:
        has.append('wheat plant')
    if square in ['dirt', 'grass']:
        if random.randint(0, max(round(a2-(20 if biome == 'forest' else 19)), 0)) == 0:    
            placements.append('oak tree')
        for i in range(max(random.randint(-1,4), 0)):
            if i == 0:continue
            has.append('rock')
    if biome == 'desert' and square == 'sand':
        if random.randint(0, max(round(a2-(18)), 2)) == 0:    
            placements.append('cactus')
        for i in range(max(random.randint(-5,2), 0)):
            if i == 0:continue
            has.append('rock')
    if square in ['snow', 'stone']:
        if random.randint(0, max(round(a2-34)+10,1)) == round(a2-41) and biome != 'rocky':
            placements.append('pine tree')
        elif random.randint(0,10 if biome == 'rocky' else 15) == 0:
            placements.append('boulder')
    
    if square == 'stone':
        mineral_chances = {
            'rock' : 4,
            'stone' : 10,
            'raw iron' : 30,
            'raw copper' : 40,
            'coal' : 50,
            'raw gold' : 60
        }
        for i in mineral_chances:
            if random.randint(0, mineral_chances[i]) == 0:
                for _ in range (random.randint(1,2)):minerals.append(i)
    
    #post item gen overide pre extra visuals
    if str(pos) in save['terrrain']['overide']:
        #Tried using exec, but python does not allow it :O
        if 'vis' in changed:vis=changed['vis']
        if 'square' in changed:square=changed['square']
        if 'has' in changed:has=changed['has']
        if 'temp' in changed:temp=changed['temp']
        if 'player' in changed:player=changed['player']
        if 'biome' in changed:biome=changed['biome']
        if 'elevation' in changed:elevation=changed['elevation']
        if 'minerals' in changed:minerals=changed['minerals']
        if 'placements' in changed:placements=changed['placements']
    
    #vis
    if 'mushroom' in has:vis = '🍄'
    if 'herb' in has:vis = '🌿'
    if 'tuft of grass' in has:vis = '🌱'
    if 'wheat plant' in has:vis = '🌾' 
    if 'oak tree' in placements:vis = '🌳'
    if 'cactus' in placements:vis = '🌵' 
    if 'pine tree' in placements:vis = '🎄' if random.randint(0,500) == 0 else '🌲'
    if 'boulder' in placements:vis = '🪨'#ROCK, THIS IS ROCK
    
    if 'crude wooden wall' in placements:vis='🌰'
    
    player = False
    for i in save['users']:#scuff
        x,y = ( -(list(save['users'][i]['pos'])[1]) , (list(save['users'][i]['pos'])[0]) )
        if i == client.user.id or i == id:continue
        if str(f'[{x/1000}, {y/1000}]') == str(pos):player = True
    
    #complete overide
    if str(pos) in save['terrrain']['overide']:
        #Tried using exec, but python does not allow it :O
        if 'vis' in changed:vis=changed['vis']
        if 'square' in changed:square=changed['square']
        if 'has' in changed:has=changed['has']
        if 'temp' in changed:temp=changed['temp']
        if 'player' in changed:player=changed['player']
        if 'biome' in changed:biome=changed['biome']
        if 'elevation' in changed:elevation=changed['elevation']
        if 'minerals' in changed:minerals=changed['minerals']
        if 'placements' in changed:placements=changed['placements']
    
    return {
        'vis' : vis,
        'square' : square,
        'has' : has,
        'temp' : temp,
        'player' : player,
        'biome' : biome,
        'elevation' : elevation,
        'minerals' : minerals,
        'placements' : placements
    }    

def has(id, item):
    return item in save['users'][id]['inv']

@client.event
async def on_ready():
    me = client.get_user(666999744572293170)
    await me.send('ONLINE')
    print('Boot up complete')

#commands

@client.command()
async def surroundings(ctx):
    
    taskid = int(task[ctx.channel.id])
    
    #Need to not make terrible
    
    async def fetch_area(id, player = False):
        x,y = ( -(list(save['users'][id]['pos'])[1]+3) , (list(save['users'][id]['pos'])[0]-3) )
        player_square = fetch_square(id, x-3, y+3)
        temp = player_square["temp"]
        
        temp_emoji = '🧊🥶😬😕🙂😐😞🥵🔥'#Innefficent
        temp_scale = ['Extremely Cold', 'Very Cold', 'Cold', 'Chilly', 'Mild', 'Warm', 'Hot', 'Very Hot', 'Extremely Hot']
        
        a=[]
        for i in range(7):
            b=[]
            for j in range(7):
                square =  fetch_square(id, x+i, y+j)
                if (square['player'] or (i == 3 and j == 3)) and player:b.append('🙂')#Maybe add emotions depending on how hungery?
                else:b.append(square['vis'])
            a.append(''.join(b))
        return f'It feels {temp_scale[floor((temp+5)/110*9)]} {temp_emoji[floor((temp+5)/110*9)]}\n'+f'cords: {y+3}, {-x-3}\n'+f'biome: {player_square["biome"]}\n'+'\n'.join(a)
    

    msg = await ctx.reply(await fetch_area(ctx.author.id))
    
    for _ in range(60):
        for _ in range(25):
            time.sleep(0.01)
            if task[ctx.channel.id] != taskid:return
        await msg.edit(await fetch_area(ctx.author.id, True))
        for _ in range(75):
            time.sleep(0.01)
            if task[ctx.channel.id] != taskid:return
        await msg.edit(await fetch_area(ctx.author.id))

@client.command()
async def walk(ctx, direction = random.choice(['up', 'down', 'left', 'right']), amount = 1):
    id = ctx.author.id
    x,y = ( -(list(save['users'][id]['pos'])[1]) , (list(save['users'][id]['pos'])[0]) )
    
    ups=['up', 'north']
    downs=['down', 'south']
    lefts=['left', 'east']
    rights=['right', 'west']
    
    #I don't even fucking know at this point
    for i in range(min(abs(amount), 10)):  
        last = (x,y)
        if direction in lefts:y-=sign(amount)
        if direction in rights:y+=sign(amount)
        if direction in ups:x-=sign(amount)
        if direction in downs:x+=sign(amount)
        if fetch_square(id, x,y)['vis'] == '🟦' or fetch_square(id, x,y)['vis'] == '🟪':
            x, y = last
            if has(id, 'boat'):pass
            await ctx.reply('You have seem to hit water, you can\'t swim what do you do?')#Can't swim dipshit
            break
            
    
    save['users'][id]['pos'] = [y,-x]#WHYYYYYY
    await surroundings(ctx)
    
@client.command()
async def look(ctx):
    id = ctx.author.id
    x,y = ( -(list(save['users'][id]['pos'])[1]) , (list(save['users'][id]['pos'])[0]) )
    items = list(fetch_square(id, x, y)['has'] + fetch_square(id, x, y)['placements'])
    #Hell Below
    
    readable = ''
    if items == []:
        readable = 'that you are standing on '+fetch_square(id, x, y)['square']
    elif len(set(items)) == 1:#Should make function, will I? Whoooo knows
        readable = f'{items.count(items[0]) if items.count(items[0])>1 else "a"} {items[0]}{"s" if items.count(items[0])>1 else ""}'#Need to change whether it's a or an based on vowel first letter
    elif len(set(items)) == 2:
        readable = f'{items.count(items[0]) if items.count(items[0])>1 else "a"} {items[0]}{"s" if items.count(items[0])>1 else ""} '
        readable += 'and '
        readable += f'{items.count(items[1]) if items.count(items[1])>1 else "a"} {items[1]}{"s" if items.count(items[1])>1 else ""} '
    else:
        for i in range(len(set(items)) - 2):
            readable += f'{items.count(items[i]) if items.count(items[i])>1 else "a"} {items[i]}{"s" if items.count(items[i])>1 else ""}, '
        readable += f'{items.count(items[len(set(items)) - 2]) if items.count(items[len(set(items)) - 2])>1 else "a"} {items[len(set(items)) - 2]}{"s" if items.count(items[len(set(items)) - 2])>1 else ""}, '
        readable += 'and '
        readable += f'{items.count(items[len(set(items)) - 1]) if items.count(items[len(set(items)) - 1])>1 else "a"} {items[len(set(items)) - 1]}{"s" if items.count(items[len(set(items)) - 1])>1 else ""} '
    await ctx.reply(f'You see {readable}')

@client.command()
async def pickup(ctx):
    id = ctx.author.id
    x,y = ( -(list(save['users'][id]['pos'])[1]) , (list(save['users'][id]['pos'])[0]) )
    items = list(fetch_square(id, x, y)['has'])
    random.seed()#Gotta do this cus fetch square uses random.seed in the function
    if items == []:
        await ctx.reply('You see nothing to pickup')
        return
    item =  random.choice(items)
    if item in save['users'][id]['inv']:save['users'][id]['inv'][item]['amount'] += 1
    else:save['users'][id]['inv'][item] = {'amount':1}
    items.remove(item)
    if not str(f'[{x/1000}, {y/1000}]') in save['terrrain']['overide']: save['terrrain']['overide'][str(f'[{x/1000}, {y/1000}]')] = {}
    save['terrrain']['overide'][str(f'[{x/1000}, {y/1000}]')]['has'] = list(items)
    save['users'][id]['stats']['int level'] += 1
    await ctx.reply(f'You picked up a {item}')

@client.command()
async def inv(ctx, *, txt = 'all'):
    id = ctx.author.id   
    reg1 = 0
    inv = []
    pageinv=[]
    if txt != 'all':
        try: 
            embed=discord.Embed(title=txt, description=f'{txt}({ save["users"][id]["inv"][txt.lower()]})')
            embed.set_author(name=" ")
            embed.set_footer(text=" ")             
            await ctx.reply(embed = embed)
            return
        except:
            if ctx.message.mentions != []:
                id = ctx.message.mentions[0].id
                try:save["users"][id]
                except:
                    await ctx.reply('That person does not have a pocket')
                    return
            else:
                await ctx.reply("You don't have any of that item")
                return
    for i in sorted(sorted(list(save["users"][id]['inv'].keys())),key=lambda item:save["users"][id]['inv'][item]['amount'], reverse = True):             
        if save["users"][id]['inv'][i]['amount'] > 0: 
            inv.append(f'__**{i}**({ save["users"][id]["inv"][i]["amount"]})__')
            reg1 += 1
        if reg1 == 30:
            pageinv.append('\n'.join(inv))
            inv = []
            reg1 = 0
    if reg1 != 30:
        pageinv.append('\n'.join(inv))            
    embed=discord.Embed(title="Inventory(Page 1)", description=pageinv[0])
    if id == ctx.author.id:embed.set_footer(text=ctx.author)
    else:embed.set_footer(text=ctx.message.mentions[0])
    msg = await ctx.reply(embed=embed)
    num=1
    await msg.add_reaction("◀")
    await msg.add_reaction("▶")
    await msg.add_reaction("⏹")
    while True:
        def check(reaction, user):
            return user==ctx.message.author and str(reaction.emoji) in ["▶","◀","⏹"]
        try: reaction, user = await client.wait_for("reaction_add", timeout=300, check = check)
        except asyncio.TimeoutError: break
        else:
            if not user == client.user:
                try: await msg.remove_reaction(emoji=reaction.emoji, member=user)
                except: pass
                if str(reaction.emoji) == "▶": 
                    if num < len(pageinv): num += 1
                elif str(reaction.emoji) == "◀":
                    if num > 1: num -= 1
                elif str(reaction.emoji) == "⏹": break
            embed=discord.Embed(title=f"Inventory(Page {num})", description=pageinv[num - 1])
            if id == ctx.author.id:embed.set_footer(text=ctx.author)
            else:embed.set_footer(text=ctx.message.mentions[0])
            await msg.edit(content = '', embed = embed)
    await msg.remove_reaction(emoji= "▶", member = client.user)      
    await msg.remove_reaction(emoji= "◀", member = client.user)
    await msg.remove_reaction(emoji= "⏹", member = client.user)          

@client.command()
async def think(ctx):
    id = ctx.author.id  
    possible = []
    for i in recipes:
        if eval(recipes[i]['requires']) and i not in save['users'][id]['recipes']:
            possible.append(i)
    random.shuffle(possible)
    if possible == []:
        await ctx.reply('You have nothing to think about')
        return
    for i in possible:
        if random.randint(0, max(recipes[i]['intel']-save['users'][id]['stats']['intelligence'], 0)) == 0:
            unlocked = list(save['users'][id]['recipes'])
            unlocked.append(i)
            save['users'][id]['recipes'] = unlocked
            await ctx.reply(f'You thought of a way to craft {i} \nRecipe:'+ '\n' + "\n".join( (x.capitalize() + ': ' + str(recipes[i]['recipe'][x])) for x in recipes[i]['recipe']))
            break
    else:
        await ctx.reply('You were on the verge of thinking of something but failed to!\nKeep trying!')

@client.command()
async def craft(ctx, *, item = ''):
    id = ctx.author.id
    unlocked = list(save['users'][id]['recipes'])
    recipe = item.lower().strip()
    x,y = ( -(list(save['users'][id]['pos'])[1]) , (list(save['users'][id]['pos'])[0]) )
    items = list(fetch_square(id, x, y)['has'])
    placements = list(fetch_square(id, x, y)['placements'])
    if recipe == '':
        await ctx.reply('You need to specify what you would like to craft')
        return
    if recipe not in recipes or recipe not in unlocked:
        await ctx.reply('You don\'t know that recipe')
        return
    if 'station' in recipes[recipe]:
        if not recipes[recipe]['station'] in placements:
            await ctx.reply(f'You need to be on a {recipes[recipe]["station"]}')
            return
    for i in recipes[recipe]['recipe']:
        if i not in save['users'][id]['inv']:
            await ctx.reply(f'You don\'t have enough {i}')
            break
        if save['users'][id]['inv'][i]['amount'] < recipes[recipe]['recipe'][i]:
            await ctx.reply(f'You don\'t have enough {i}')
            break
    else:
        for i in recipes[recipe]['recipe']:
            save['users'][id]['inv'][i]['amount'] -= recipes[recipe]['recipe'][i]
        if recipe in save['users'][id]['inv']:save['users'][id]['inv'][recipe]['amount'] += 1
        else:save['users'][id]['inv'][recipe] = {'amount' : 1}
        if 'durability' in recipes[recipe]:
            if 'durability' in save['users'][id]['inv'][recipe]:save['users'][id]['inv'][recipe]['durability'] += recipes[recipe]['durability']
            else:save['users'][id]['inv'][recipe]['durability'] = recipes[recipe]['durability']
        save['users'][id]['stats']['int level'] += 1
        await ctx.reply(f'You crafted {recipe}')

@client.command()
async def use(ctx, *, tool = ''):
    id = ctx.author.id
    x,y = ( -(list(save['users'][id]['pos'])[1]) , (list(save['users'][id]['pos'])[0]) )
    items = list(fetch_square(id, x, y)['has'])
    placements = list(fetch_square(id, x, y)['placements'])
    minerals= list(fetch_square(id, x, y)['minerals'])
    
    if tool == '':
        await ctx.reply('You need to specify which tool to use')
        return
    if tool not in save['users'][id]['inv']:
        await ctx.reply('You don\'t have that tool')
        return
    if save['users'][id]['inv'][tool]['durability'] <= 0 or save['users'][id]['inv'][tool]['amount']<=0:
        await ctx.reply('You don\'t have that tool')
        return
    if tool in ['crude axe']:
        if 'oak tree' in placements:#Must find better way to do this
            placements.remove('oak tree')
            if 'oak log' in save['users'][id]['inv']:save['users'][id]['inv']['oak log']['amount'] += 1
            else:save['users'][id]['inv']['oak log'] = {'amount' : 1}
            await ctx.reply('You chopped down the oak tree and got an oak log')
        elif 'pine tree' in placements:
            placements.remove('pine tree')
            if 'pine log' in save['users'][id]['inv']:save['users'][id]['inv']['pine log']['amount'] += 1
            else:save['users'][id]['inv']['pine log'] = {'amount' : 1}
            await ctx.reply('You chopped down the pine tree and got an pine log')
        else:
            await ctx.reply('You must be standing on a tree to use this')
            return
    if tool in ['crude pickaxe']:
        if minerals == []:
            await ctx.reply('There is nothing to mine here')
            return
        else:
            mineral = random.choice(minerals)
            if mineral in save['users'][id]['inv']:save['users'][id]['inv'][mineral]['amount'] += 1
            else:save['users'][id]['inv'][mineral] = {'amount' : 1}
            minerals.remove(mineral)
            await ctx.send(f'You mined and got {mineral}')
    if tool in ['crude fishing pole']:
        for i in range(3):
            for j in range(3):
                if fetch_square(id, (x-1)+i, (y-1)+j)['square'] in ['ocean', 'deep ocean']:break
            else:continue#Best not to think about it
            break
        else:
            await ctx.send('You need to be next to water to use this')
            return
        fish = 'fish'
        await ctx.send(f'You got a {fish}')
        if fish in save['users'][id]['inv']:save['users'][id]['inv'][fish]['amount'] += 1
        else:save['users'][id]['inv'][fish] = {'amount' : 1}
            
        
    
    save['users'][id]['inv'][tool]['durability'] -= 1
    
    if ceil(save['users'][id]['inv'][tool]['durability'] / recipes[tool]['durability']) < save['users'][id]['inv'][tool]['amount']:#Not reliable if a tool doesn't have a recipe, will do for now
        save['users'][id]['inv'][tool]['amount'] -= 1
        await ctx.reply(f'Your {tool} broke')
    
    
    if not str(f'[{x/1000}, {y/1000}]') in save['terrrain']['overide']: save['terrrain']['overide'][str(f'[{x/1000}, {y/1000}]')] = {}
    save['terrrain']['overide'][str(f'[{x/1000}, {y/1000}]')]['minerals'] = list(minerals)
    save['terrrain']['overide'][str(f'[{x/1000}, {y/1000}]')]['placements'] = list(placements)
    save['terrrain']['overide'][str(f'[{x/1000}, {y/1000}]')]['has'] = list(items)

@client.command()
async def recipe(ctx, *, recipe = ''):
    id = ctx.author.id
    unlocked = list(save['users'][id]['recipes'])
    recipe = recipe.lower().strip()
    if recipe == '':
        await ctx.reply('You need to specify what recipe you would like to see')
        return
    if recipe not in recipes or recipe not in unlocked:
        await ctx.reply('You don\'t know that recipe')
        return
    await ctx.reply("\n".join( (x.capitalize() + ': ' + str(recipes[recipe]['recipe'][x])) for x in recipes[recipe]['recipe']))

@client.command()
async def place(ctx, *, placement = ''):
    id = ctx.author.id
    x,y = ( -(list(save['users'][id]['pos'])[1]) , (list(save['users'][id]['pos'])[0]) )
    placements = list(fetch_square(id, x, y)['placements'])
    if placement == '':
        await ctx.reply('You need to specify which tool to use')
        return
    if placement not in save['users'][id]['inv']:
        await ctx.reply('You don\'t have that')
        return
    if save['users'][id]['inv'][placement]['amount']<=0:
        await ctx.reply('You don\'t have that')
        return
    if placements:
        await ctx.reply(f'You can\'t place that there, there is a {placements[0]} already there')
        return
    placements.append(placement)
    save['users'][id]['inv'][placement]['amount']-=1
    
    if not str(f'[{x/1000}, {y/1000}]') in save['terrrain']['overide']: save['terrrain']['overide'][str(f'[{x/1000}, {y/1000}]')] = {}
    save['terrrain']['overide'][str(f'[{x/1000}, {y/1000}]')]['placements'] = list(placements)
#other

@client.event
async def on_message(txt):
    user_check(txt.author.id)
    if txt.author.id != 807757190316163104:#dis da bot id    
        if not txt.guild:
            await txt.reply('Hey! Outside is currently in beta and to make sure all bugs are squished and found playing outside in the dms is not allowed. Sorry! When the bot goes out of beta this will be allowed!\n if you are somehow playing this bot without being in the official outside server here is the invite link! https://discord.gg/CqdY897Qxm')
            return
        elif str(txt.guild) != 'Outside':print('-------------',txt.guild )
        if txt.channel.id in task:task[txt.channel.id] += 1
        else:task[txt.channel.id] = 1
    await client.process_commands(txt)
    for i in client.commands:
        if txt.content.lower() == f'!{i.name}':
            save['users'][txt.author.id]['stats']['online'] = round(time.time())
    if save['users'][txt.author.id]['stats']['intelligence']+1 <= floor(save['users'][txt.author.id]['stats']['int level'] ** 0.55):
        save['users'][txt.author.id]['stats']['intelligence'] = floor(save['users'][txt.author.id]['stats']['int level'] ** 0.55)
        await txt.reply('Your intelligence increased')
    if txt.author.id == 302050872383242240:
        if str(txt.embeds[0].color) == '#24b7b7':
            if 'Bump done! :thumbsup:' in txt.embeds[0].description:
                user_id = int(re.findall(r'(?<=<@)(.*?)(?=>)', txt.embeds[0].description)[0])
                await txt.reply(f'Thank you <@{user_id}> for bumping the server!')
                user =  discord.utils.get(client.get_all_members(), id=user_id)
                role = discord.utils.get(client.get_guild(807722851045998653).roles, id=942835439558066196) 
                await  user.add_roles(role)
        print(str(txt.embeds[0].color), txt.embeds[0].description)
    write()
    for i in save['users']:
        try:    
            user =  discord.utils.get(client.get_all_members(), id=i)
            role = discord.utils.get(client.get_guild(807722851045998653).roles, id=942616316018327552)
            if round(time.time()) - save['users'][i]['stats']['online'] < 300:
                await user.add_roles(role)#This method is... eh
            elif role in user.roles:
                await user.remove_roles(role)
        except:pass
     
    
@client.command()
@commands.has_role("Has touched grass")
async def map(ctx, x=0, y=0, zoom = 1000, size =10):
    
    a=[]
    for i in range(size):
        b=[]
        for j in range(size):
            square = fetch_square(id, ((-y) + size//2)+i, x-size//2+j, zoom)
            b.append(square['vis'] if not square['player'] else '🙂')
        a.append(''.join(b))
    await ctx.reply('\n'.join(a))

@client.command()
async def help(ctx, x=0, y=0, zoom = 1000, size =10):
    await ctx.reply(r'''***Commands***
-**surroundings**-
 • Shows the area around you and your current temperature
-**walk**-
 • Will randomly walk you one square either up, down, left or right 
 • You can specify which direction and distance to go by doin !walk <direction> <distance>
 • Max distance is 10
-**pickup**-
 • Will pickup a random item that's in the square you're in
-**inv**-
 • Let's you see your items
-**look**-
 • Tells you all the current items in the square you're in
-**think**-
 • Has a chance to unlock new recipes
 • some recipes require items to be crafted before they can be unlocked
 • The higher intelligence you have the more likely you are to unlock a new recipe.
-**craft**-
 • Crafts the specified item if you have enough resources in your inv
-**recipe**-
 • Shows the recipe of a specified item

*Command prefix is* ``!``''')

@client.command()
async def temp(ctx):
    await pickup(ctx)
    await look(ctx)


if __name__ == '__main__':client.run(open("bottoken.txt","r").read())#allow for importing without running the bot