_BW='You need the ``managerelations`` permission to do that'
_BV='You must specify what stance you would like to take'
_BU='You are not in a nation!, you can found one with !found'
_BT='You are not in a nation with that person'
_BS='You need the ``giveperms`` permission to do that'
_BR='inviteonly'
_BQ="You don't know that recipe"
_BP='You do not have a pocket'
_BO='south'
_BN='north'
_BM='Nation'
_BL='Health'
_BK='has(id, "thatch fabric")'
_BJ='raw iron'
_BI='has(id, "thatch")'
_BH='bread'
_BG='cooked frog leg'
_BF='crude wooden hammer'
_BE='crude wooden knife'
_BD='crude wooden spear'
_BC='crude wooden fishing pole'
_BB='crude wooden pickaxe'
_BA='crude wooden axe'
_B9='crude hammer'
_B8='crude knife'
_B7='crude spear'
_B6='crude fishing pole'
_B5='crude pickaxe'
_B4='crude axe'
_B3='bundle of sticks'
_B2='save.txt'
_B1='master'
_B0='"Automatic File Updates"'
_A_='commit'
_Az='Main.py'
_Ay='war'
_Ax='allies'
_Aw='delclaims'
_Av='makeclaims'
_Au='defaultpermissions'
_At='That person does not have a pocket'
_As='animals'
_Ar='frog'
_Aq='bunny'
_Ap='fish'
_Ao='ram'
_An='cow'
_Am='chicken'
_Al='boulder'
_Ak='temperate'
_Aj='raw bunny meat'
_Ai='raw pork'
_Ah='raw beef'
_Ag='herb'
_Af='coal'
_Ae='thatch fabric'
_Ad='crude wooden wall'
_Ac='thatch'
_Ab='start_time'
_Aa='That nation does not exist'
_AZ='managerelations'
_AY='giveperms'
_AX="You don't have that"
_AW='dropped_items'
_AV='forest'
_AU='deep ocean'
_AT='online'
_AS='raw mutton'
_AR='raw chicken'
_AQ='mushroom'
_AP='cooked bunny meat'
_AO='cooked mutton'
_AN='cooked pork'
_AM='cooked beef'
_AL='cooked chicken'
_AK='crude medicine'
_AJ='mushroom soup'
_AI='origin'
_AH='natlevel'
_AG='down'
_AF='right'
_AE='left'
_AD='up'
_AC='claims'
_AB='wheat plant'
_AA='owners'
_A9='all'
_A8='temp'
_A7='ocean'
_A6='int level'
_A5='intelligence'
_A4='members'
_A3='raw fish'
_A2='has(id, "crude oak plank") and has(id, "nail")'
_A1='oak log'
_A0='has(id, "rope") and has(id, "rock")'
_z='crude furnace'
_y='dirt'
_x='You are not in a nation!'
_w='a'
_v='minerals'
_u='player'
_t='pine tree'
_s='oak tree'
_r='crude oak plank'
_q='nail'
_p='stone'
_o='s'
_n='⬛'
_m='🟦'
_l='tuft of grass'
_k='git'
_j='grass'
_i='biome'
_h='relationships'
_g='square'
_f='settings'
_e='placements'
_d='vis'
_c='fire'
_b='mud clump'
_a='has'
_Z='recipes'
_Y='station'
_X='owner'
_W='rope'
_V='health'
_U='rock'
_T='stick'
_S=' '
_R='overide'
_Q='\n'
_P='stats'
_O='permissions'
_N='name'
_M='intel'
_L='requires'
_K=True
_J=False
_I='pos'
_H='durability'
_G='recipe'
_F='amount'
_E='nations'
_D='terrain'
_C='inv'
_B='nation'
_A='users'
import asyncio,os,random
from perlin_noise import PerlinNoise
from math import floor,ceil
from numpy import sign
import time,re,subprocess
from better_profanity import profanity
profanity.load_censor_words(whitelist_words=['poop','shit','fuck','cum','boob','boobs'])
profanity.add_censor_words([])
import discord
from discord.ext import commands
from discord.ui import button,View,Button
from discord.interactions import Interaction
test=_K
intents=discord.Intents(messages=_K,guilds=_K,reactions=_K,members=_K,presences=_K)
client=commands.Bot(command_prefix='!',case_insensitive=_K,intents=intents)
client.remove_command('help')
if not test:subprocess.run([_k,'add',_Az],stdout=subprocess.DEVNULL);subprocess.run([_k,_A_,'-m',_B0],stdout=subprocess.DEVNULL);subprocess.run([_k,'pull',_AI,_B1],stdout=subprocess.DEVNULL);subprocess.run([_k,'push',_AI,_B1],stdout=subprocess.DEVNULL)
elif test:subprocess.run([_k,'add',_Az],stdout=subprocess.DEVNULL);subprocess.run([_k,_A_,'-m',_B0],stdout=subprocess.DEVNULL);subprocess.run([_k,'pull',_AI,'test'],stdout=subprocess.DEVNULL);subprocess.run([_k,'push',_AI,'test'],stdout=subprocess.DEVNULL)
task={}
global save
save=eval(open(_B2,'r',encoding='utf8').read())
if _Ab not in save[_D]:save[_D][_Ab]=round(time.time())
if _E not in save[_D]:save[_D][_E]={}
def write():File=open(_B2,'w',encoding='utf8');File.write(str(save));File.close()
tools={'hands':{'outputs':[_T,_U,_y],_F:1}}
items={}
recipes={_Ac:{_G:{_l:3},_L:'(True)',_M:0},_W:{_G:{_b:1,_Ac:2},_L:_BI,_M:3},_B3:{_G:{_W:1,_T:10},_L:'has(id, "rope")',_M:5},_Ad:{_G:{_B3:1,_b:5},_L:'has(id, "bundle of sticks")',_M:15},_B4:{_G:{_W:2,_T:2,_b:1,_U:3},_L:_A0,_M:10,_H:10},_B5:{_G:{_W:2,_T:1,_b:1,_U:4},_L:_A0,_M:10,_H:10},_B6:{_G:{_W:3,_T:2,_b:1,_U:1},_L:_A0,_M:10,_H:10},_B7:{_G:{_W:1,_T:3,_b:1,_U:3},_L:_A0,_M:10,_H:10},_B8:{_G:{_W:1,_T:1,_b:1,_U:3},_L:_A0,_M:10,_H:12},_B9:{_G:{_W:2,_T:1,_b:1,_U:4},_L:_A0,_M:10,_H:20},_p:{_G:{_U:10,_b:2},_M:18,_L:'has(id, "stone") or has(id, "crude oak plank")'},_z:{_G:{_p:10,_U:10,_b:5},_M:25,_L:'has(id, "stone")'},'iron':{_G:{_Af:1,_BJ:2},_M:20,_L:'has(id, "crude furnace")',_Y:_z},_q:{_G:{'iron':1},_M:15,_L:'has(id, "iron")',_Y:_z,_F:5},_r:{_G:{_U:2,_A1:1},_M:15,_L:'has(id, "crude axe")'},_BA:{_G:{_W:1,_r:3,_q:2},_L:_A2,_M:16,_H:35},_BB:{_G:{_W:1,_r:4,_q:3},_L:_A2,_M:16,_H:30},_BC:{_G:{_W:3,_r:2,_q:2},_L:_A2,_M:16,_H:40},_BD:{_G:{_W:1,_r:3,_q:2,_U:3},_L:_A2,_M:16,_H:35},_BE:{_G:{_W:1,_r:3,_q:2,_U:1},_L:_A2,_M:16,_H:40},_BF:{_G:{_W:1,_r:4,_q:3},_L:_A2,_M:16,_H:55},_Ae:{_G:{_Ac:5},_L:_BI,_M:12},_AJ:{_G:{_AQ:3,_Ae:1},_L:_BK,_M:12,_Y:_c},_AK:{_G:{_AQ:1,_Ag:5},_L:_BK,_M:12},_c:{_G:{_A1:1,_T:1,_W:1},_L:'has(id, "rock")',_M:15},'cooked fish':{_G:{_A3:3,_T:1},_L:'has(id, "fish")',_M:12,_Y:_c},_AL:{_G:{_AR:1,_T:2},_L:'has(id, "raw chicken")',_M:12,_Y:_c},_AM:{_G:{_Ah:1,_T:2},_L:'has(id, "raw beef")',_M:12,_Y:_c},_AN:{_G:{_Ai:1,_T:2},_L:'has(id, "raw pork")',_M:12,_Y:_c},_AO:{_G:{_AS:1,_T:2},_L:'has(id, "raw mutton")',_M:12,_Y:_c},_AP:{_G:{_Aj:1,_T:1},_L:'has(id, "raw bunny meat")',_M:12,_Y:_c},_BG:{_G:{'frog leg':2,_T:1},_L:'has(id, "raw frog leg")',_M:12,_Y:_c},_BH:{_G:{'what plant':5,_Af:1},_L:'has(id, "wheat plant")',_M:12,_Y:_z},'nation banner':{_G:{_U:10,_T:15,_Ae:5,_W:2},_L:'has(id, "rock") and has(id, "stick") and has(id, "thatch fabric") and has(id, "rope")',_M:12}}
async def user_check(id):
	A='alive'
	for i in dict(save[_D][_E]):
		if i not in save[_D][_E]:continue
		channel=client.get_channel(0xd22fb9868028033)
		if not save[_D][_E][i][_A4]:
			try:save[_D][_E].pop(i);await channel.send(f"{i} has 0 members and has been disbanded")
			except:pass
	defaults={_P:{A:_K,_A5:0,_A6:0,_AT:0},_f:{},_C:{},_Z:[]}
	try:
		save[_A][id]
		for i in defaults:
			if i not in save[_A][id]:save[_A][id][i]=defaults[i]
		if _V not in save[_A][id][_P]:save[_A][id][_P][_V]=100
		if _B not in save[_A][id]:save[_A][id][_B]={}
		if _E not in save[_D]:save[_D][_E]={}
	except:
		random.seed();pos=[random.randint(0,500)-250,random.randint(0,500)-250];x,y=-list(pos)[1],list(pos)[0];square=fetch_square(id,x,y)
		while square[_i]!=_Ak or square[_g]!=_j:pos=[random.randint(0,500)-250,random.randint(0,500)-250];x,y=-list(pos)[1],list(pos)[0];square=fetch_square(id,x,y)
		save[_A][id]={_P:{A:_K,_A5:0,_A6:0,_AT:0},_f:{},_I:pos,_C:{},_Z:[],_B:{}}
def fetch_square(id=0,x=0,y=0,zoom=1000):
	O='boar';N='cactus';M='grasslands';L='swamp';K='desert';J='sand';I='🟧';H='⬜';G='elevation';F='rocky';E='snow';D='mud';C='🟩';B='🟨';A='🟫';noise=PerlinNoise(octaves=5,seed=543);biomenoise=PerlinNoise(octaves=1,seed=558);time_tick=(round(time.time())-save[_D][_Ab])//5;elevation_scale='🟪🟪🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟨🟫🟫🟫🟫🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛⬛⬛⬜⬜';squares={'🟪':_AU,_m:_A7,B:J,A:_y,C:_j,_n:_p,H:E,I:D};biomes={K:{A:B,C:B,_m:B,'🟪':_m},F:{A:_n,C:_n,H:_n,_m:B},M:{A:C},_Ak:{},_AV:{C:A,B:I},L:{A:I,C:A,B:_m,'🟪':_m},E:{C:H,_n:H,A:_n}};has=[];minerals=[];animals=[];nation=None;pos=[x/zoom,y/zoom];elevation=noise(pos);biome=biomenoise(pos);random.seed(str(pos));a2=elevation+0.5;biome=biome+0.5;a2*=len(elevation_scale);biome*=len(list(biomes.keys()));vis=elevation_scale[max(0,min(floor(a2),len(elevation_scale)-1))];biome=list(biomes.keys())[max(0,min(floor(biome),len(list(biomes.keys()))-1))];square=squares[vis];temp=101-round((elevation+0.5)*101,2);wheatnoise=PerlinNoise(octaves=15,seed=558);chickennoise=PerlinNoise(octaves=700,seed=929);cownoise=PerlinNoise(octaves=600,seed=689);boarnoise=PerlinNoise(octaves=700,seed=919);ramnoise=PerlinNoise(octaves=500,seed=719);fishnoise=PerlinNoise(octaves=700,seed=671);bunnynoise=PerlinNoise(octaves=300,seed=611);frognoise=PerlinNoise(octaves=450,seed=919)
	if vis in biomes[biome]:vis=biomes[biome][vis];sqaure=squares[vis]
	if str(pos)in save[_D][_R]:changed=save[_D][_R][str(pos)]
	placements=[]
	if biome==F:
		for i in range(max(random.randint(-1,5),0)):
			if i==0:continue
			has.append(_U)
	if square in[_j,_y,D]:
		for i in range(max(random.randint(-1 if biome==_AV else-4,2),0)):
			if i==0:continue
			has.append(_T)
	if square in[D,_y]:
		if random.randint(0,100)==0:has.append(_AQ)
		if random.randint(0,3)==0:has.append(_b)
	if biome==L and square in[D,_y]:
		if random.randint(0,5)==0:
			for i in range(random.randint(1,3)):has.append(_Ag)
	if square==_j:
		if random.randint(0,max(round(a2-(21 if biome==M else 15)),0))==0:has.append(_l)
		for i in range(max(random.randint(-2,3),0)):
			if i==0:continue
			has.append(_U)
		if random.randint(0,5)==0:
			for i in range(random.randint(1,4)):has.append(_b)
	if not biome in[K,F,E]and square in[D,J]and wheatnoise(pos)>=0.3:has.append(_AB)
	if square in[_y,_j]:
		if random.randint(0,max(round(a2-(20 if biome==_AV else 19)),0))==0:placements.append(_s)
		for i in range(max(random.randint(-1,4),0)):
			if i==0:continue
			has.append(_U)
	if biome==K and square==J:
		if random.randint(0,max(round(a2-18),2))==0:placements.append(N)
		for i in range(max(random.randint(-5,2),0)):
			if i==0:continue
			has.append(_U)
	if square in[E,_p]:
		if random.randint(0,max(round(a2-34)+10,1))==round(a2-41)and biome!=F:placements.append(_t)
		elif random.randint(0,10 if biome==F else 15)==0:placements.append(_Al)
	random.seed(str(pos)+str(time_tick))
	if square in[_j]and chickennoise(pos+[time_tick/10**5])>=0.35:
		if random.randint(0,2)==0:animals.append(_Am)
	if square in[_j]and cownoise(pos+[time_tick/10**5])>=0.5:
		if random.randint(0,2)==0:animals.append(_An)
	if square in[_j]and boarnoise(pos+[time_tick/10**5])>=0.4:
		if random.randint(0,2)==0:animals.append(O)
	if square in[E,_p]and ramnoise(pos+[time_tick/10**5])>=0.3:
		if random.randint(0,2)==0:animals.append(_Ao)
	if square in[_A7]and fishnoise(pos+[time_tick/10**5])>=0.1:
		if random.randint(0,2)==0:animals.append(_Ap)
	if square in[_j]and bunnynoise(pos+[time_tick/10**5])>=0.5:
		if random.randint(0,2)==0:animals.append(_Aq)
	if biome in[L]and square in[_A7,D]and frognoise(pos+[time_tick/10**5])>=0.45:
		if random.randint(0,2)==0:animals.append(_Ar)
	random.seed(str(pos))
	if square==_p:
		mineral_chances={_U:4,_p:10,_BJ:30,'raw copper':40,_Af:50,'raw gold':60}
		for i in mineral_chances:
			if random.randint(0,mineral_chances[i])==0:
				for _ in range(random.randint(1,2)):minerals.append(i)
	if str(pos)in save[_D][_R]:
		if _d in changed:vis=changed[_d]
		if _g in changed:square=changed[_g]
		if _a in changed:has=changed[_a]
		if _A8 in changed:temp=changed[_A8]
		if _u in changed:player=changed[_u]
		if _i in changed:biome=changed[_i]
		if G in changed:elevation=changed[G]
		if _v in changed:minerals=changed[_v]
		if _e in changed:placements=changed[_e]
	if _AQ in has:vis='🍄'
	if _Ag in has:vis='🌿'
	if _l in has:vis='🌱'
	if _AB in has:vis='🌾'
	if _s in placements:vis='🌳'
	if N in placements:vis='🌵'
	if _t in placements:vis='🎄'if random.randint(0,500)==0 else'🌲'
	if _Al in placements:vis='\U0001faa8'
	if _Am in animals:vis='🐔'
	if _An in animals:vis='🐮'
	if O in animals:vis='🐗'
	if _Ao in animals:vis='🐏'
	if _Ap in animals:vis='🐟'
	if _Aq in animals:vis='🐰'
	if _Ar in animals:vis='🐸'
	if _Ad in placements:vis='🌰'
	if _z in placements:vis='🪔'
	if _c in placements:vis='🔥'
	if str(pos)in save[_D][_R]:
		if _AW in changed:vis='🧺'if changed[_AW]else vis
	player=_J
	for i in save[_A]:
		x,y=-list(save[_A][i][_I])[1],list(save[_A][i][_I])[0]
		if i==client.user.id or i==id:continue
		if str(f"[{x/1000}, {y/1000}]")==str(pos):player=_K
	if str(pos)in save[_D][_R]:
		if _d in changed:vis=changed[_d]
		if _g in changed:square=changed[_g]
		if _a in changed:has=changed[_a]
		if _A8 in changed:temp=changed[_A8]
		if _u in changed:player=changed[_u]
		if _i in changed:biome=changed[_i]
		if G in changed:elevation=changed[G]
		if _v in changed:minerals=changed[_v]
		if _e in changed:placements=changed[_e]
	for i in save[_D][_E]:
		for j in save[_D][_E][i][_AC]:
			claim_x,claim_y=tuple(j);claim_x,claim_y=claim_x/1000,claim_y/1000
			if(pos[0]<claim_x+6/1000 and pos[0]>=claim_x)and(pos[1]<claim_y+6/1000 and pos[1]>=claim_y):nation=i;break
		else:continue
		break
	return{_d:vis,_g:square,_a:has,_A8:temp,_u:player,_i:biome,G:elevation,_v:minerals,_e:placements,_As:animals,_B:nation}
def has(id,item):return item in save[_A][id][_C]
async def respawn(ctx,id):
	dropped=random.choice([item for item in list(save[_A][id][_C].keys())if save[_A][id][_C][item][_F]>0])
	if dropped:await drop(ctx,amount=save[_A][id][_C][dropped][_F]//2,item=dropped)
	await ctx.reply('You took too much damage and you died');random.seed();x,y=-list(save[_A][id][_I])[1],list(save[_A][id][_I])[0];pos=[random.randint(x-200,x+200),random.randint(y-200,y+200)];square=fetch_square(id,x,y)
	while square[_g]in[_A7,_AU]:pos=[random.randint(x-200,x+200),random.randint(y-200,y+200)];square=fetch_square(id,pos[0],pos[1])
	save[_A][id][_I]=[list(pos)[1],-list(pos)[0]];save[_A][id][_P][_V]=100
@client.event
async def on_ready():
	for developer in [0x941a8bbd8820032,0xb32066b0388001f]:
		me=await client.fetch_user(developer)
		try:await me.send('🟢 Bot online!')
		except:print('Unable to send message to developer:',me.name)
	print('Boot up complete')
@client.command(aliases=[_o])
async def surroundings(ctx,buttons=_K):
	A='📜';taskid=int(task[ctx.channel.id]);msg=await ctx.reply('Generating...')
	async def fetch_area(id,player=_J):
		x,y=-(list(save[_A][id][_I])[1]+3),list(save[_A][id][_I])[0]-3;print(-list(save[_A][id][_I])[1],list(save[_A][id][_I])[0]);player_square=fetch_square(id,-list(save[_A][id][_I])[1],list(save[_A][id][_I])[0]);temp=player_square[_A8];temp_emoji='🧊🥶😬😕🙂😐😞🥵🔥';temp_scale=['Extremely Cold','Very Cold','Cold','Chilly','Mild','Warm','Hot','Very Hot','Extremely Hot'];a=[]
		for i in range(7):
			b=[]
			for j in range(7):
				square=fetch_square(id,x+i,y+j)
				if(square[_u]or i==3 and j==3)and player:b.append('🙂')
				else:b.append(square[_d])
			a.append(''.join(b))
		h=round(save[_A][id][_P][_V]/10)*10;h_bar=''
		for i in range(1,10):
			if h-i*10<=0:h_bar+=_n
			else:h_bar+='🟥'
		nation=str(player_square[_B]);embed=discord.Embed(title=f"Map",description=_Q.join(a),color=65280);embed.add_field(name='Temperature',value=f"It feels {temp_scale[floor((temp+5)/110*9)]} {temp_emoji[floor((temp+5)/110*9)]}\n",inline=_J);embed.add_field(name='Biome',value=f"{player_square[_i]}",inline=_J);embed.add_field(name='Coordinates',value=f"{y+3}, {-x-3}",inline=_J);embed.add_field(name=_BL,value=f"{h_bar}",inline=_J);embed.add_field(name=_BM,value=nation,inline=_J);return embed
	class Dropdown(discord.ui.Select):
		def __init__(self):
			options=[]
			for i in save[_A][ctx.author.id][_Z]:
				can_craft=_K
				for j in recipes[i][_G]:
					if j not in save[_A][ctx.author.id][_C]:can_craft=_J
					elif save[_A][ctx.author.id][_C][j][_F]<recipes[i][_G][j]:can_craft=_J
				options.append(discord.SelectOption(label=i,description='You can craft this'if can_craft else"You can't craft this",emoji=A))
			if not options:options.append(discord.SelectOption(label='Nothing to craft',description='Click the button with the brain on it or use !think to think of a new recipe',emoji='❌'))
			super().__init__(placeholder='Craft something',min_values=1,max_values=1,options=options)
		async def callback(self,interaction):await craft(ctx,item=self.values[0])
	class ViewWithButton(View):
		def __init__(self):
			super().__init__(timeout=120)
			async def check(interaction):return interaction.user.id==ctx.author.id
			self.interaction_check=check;self.add_item(Dropdown())
		@button(style=discord.ButtonStyle.gray,emoji='📤')
		async def pickup(self,button,interaction):
			if task[ctx.channel.id]!=taskid:self.stop()
			await pickup(ctx);task[ctx.channel.id]+=1
			try:await msg.edit(view=View())
			except:pass
			await surroundings(ctx,buttons)
		@button(style=discord.ButtonStyle.blurple,emoji='🔼')
		async def up(self,button,interaction):
			if task[ctx.channel.id]!=taskid:self.stop()
			await walk(ctx,_AD,1,_K);await msg.edit(embed=await fetch_area(ctx.author.id))
		@button(style=discord.ButtonStyle.gray,emoji='🧠')
		async def think(self,button,interaction):
			if task[ctx.channel.id]!=taskid:self.stop()
			await think(ctx);task[ctx.channel.id]+=1
			try:await msg.edit(view=View())
			except:pass
			await surroundings(ctx,buttons)
		@button(style=discord.ButtonStyle.blurple,emoji='◀️',row=1)
		async def left(self,button,interaction):
			if task[ctx.channel.id]!=taskid:self.stop()
			await walk(ctx,_AE,1,_K);await msg.edit(embed=await fetch_area(ctx.author.id))
		@button(style=discord.ButtonStyle.gray,emoji='👁️',row=1)
		async def look(self,button,interaction):
			if task[ctx.channel.id]!=taskid:self.stop()
			await look(ctx);task[ctx.channel.id]+=1
			try:await msg.edit(view=View())
			except:pass
			await surroundings(ctx,buttons)
		@button(style=discord.ButtonStyle.blurple,emoji='▶️',row=1)
		async def right(self,button,interaction):
			if task[ctx.channel.id]!=taskid:self.stop()
			await walk(ctx,_AF,1,_K);await msg.edit(embed=await fetch_area(ctx.author.id))
		@button(style=discord.ButtonStyle.gray,emoji='🎒',row=2)
		async def inv(self,button,interaction):
			if task[ctx.channel.id]!=taskid:self.stop()
			await inv(ctx);task[ctx.channel.id]+=1
			try:await msg.edit(view=View())
			except:pass
		@button(style=discord.ButtonStyle.blurple,emoji='🔽',row=2)
		async def down(self,button,interaction):
			if task[ctx.channel.id]!=taskid:self.stop()
			await walk(ctx,_AG,1,_K);await msg.edit(embed=await fetch_area(ctx.author.id))
		@button(style=discord.ButtonStyle.gray,emoji=A,row=2)
		async def recipes(self,button,interaction):
			if task[ctx.channel.id]!=taskid:self.stop()
			await crafts(ctx);task[ctx.channel.id]+=1
			try:await msg.edit(view=View())
			except:pass
	if buttons:view=ViewWithButton()
	else:view=View()
	msg=await msg.edit(content='',embed=await fetch_area(ctx.author.id),view=view)
	for _ in range(60):
		for _ in range(25):
			time.sleep(0.01)
			if task[ctx.channel.id]!=taskid:return
		await msg.edit(embed=await fetch_area(ctx.author.id,_K),view=view)
		for _ in range(75):
			time.sleep(0.01)
			if task[ctx.channel.id]!=taskid:return
		await msg.edit(embed=await fetch_area(ctx.author.id),view=view)
@client.command(aliases=['move','w'])
async def walk(ctx,direction=random.choice([_AD,_AG,_AE,_AF]),amount=1,buttons=_J):
	B="You have seem to hit water, you can use !swim but if you get to far away from the shore you'll take damage for every step you take";A='boat';id=ctx.author.id;x,y=-list(save[_A][id][_I])[1],list(save[_A][id][_I])[0];ups=[_AD,_BN,'u','w'];downs=[_AG,_BO,'d',_o];lefts=[_AE,'east','l',_w];rights=[_AF,'west','r']
	if direction[0]=='>':
		direction=direction[1:];total=0;amounts=re.findall('[0-9]+',direction);directions=re.findall('[A-z]+',direction)
		if len(amounts)!=len(directions):await ctx.reply('For every direction you must specify how much you would like to walk in that direction (EX. u2r4d1)');return
		else:
			for i in range(len(amounts)):
				amount=int(amounts[i]);direction=directions[i]
				for i in range(min(abs(amount),10)):
					if total>=10:await ctx.reply('You have walked your max distance');break
					last=x,y
					if direction in lefts:y-=sign(amount)
					if direction in rights:y+=sign(amount)
					if direction in ups:x-=sign(amount)
					if direction in downs:x+=sign(amount)
					total+=1
					if fetch_square(id,x,y)[_d]==_m or fetch_square(id,x,y)[_d]=='🟪':
						x,y=last
						if has(id,A):0
						await ctx.reply(B);break
	else:
		for i in range(min(abs(amount),10)):
			last=x,y
			if direction in lefts:y-=sign(amount)
			if direction in rights:y+=sign(amount)
			if direction in ups:x-=sign(amount)
			if direction in downs:x+=sign(amount)
			if fetch_square(id,x,y)[_d]==_m or fetch_square(id,x,y)[_d]=='🟪':
				x,y=last
				if has(id,A):0
				await ctx.reply(B);break
	save[_A][id][_I]=[y,-x]
	if not buttons:await surroundings(ctx,_J)
@client.command(aliases=['sw'])
async def swim(ctx,direction=random.choice([_AD,_AG,_AE,_AF]),amount=1,buttons=_J):
	id=ctx.author.id;x,y=-list(save[_A][id][_I])[1],list(save[_A][id][_I])[0];ups=[_AD,_BN];downs=[_AG,_BO];lefts=[_AE,'east'];rights=[_AF,'west'];damage=0
	for i in range(min(abs(amount),10)):
		last=x,y
		if direction in lefts:y-=sign(amount)
		if direction in rights:y+=sign(amount)
		if direction in ups:x-=sign(amount)
		if direction in downs:x+=sign(amount)
		for i in range(5):
			for j in range(5):
				if fetch_square(id,x-2+i,y-2+j)[_g]not in[_A7,_AU]:break
			else:continue
			break
		else:damage+=1
	save[_A][id][_I]=[y,-x];save[_A][id][_P][_V]-=damage
	if save[_A][id][_P][_V]<=0:await respawn(ctx,id);return
	if damage:await ctx.reply(f"You took {damage} damage and you now have {save[_A][id][_P][_V]} health")
	if not buttons:await surroundings(ctx,_J)
@client.command(aliases=['l'])
async def look(ctx):
	A='and ';id=ctx.author.id;x,y=-list(save[_A][id][_I])[1],list(save[_A][id][_I])[0];items=list(fetch_square(id,x,y)[_a]+fetch_square(id,x,y)[_e])
	for i in range(len(items)):
		if type(items[i])is dict:
			item_dict=items[i]
			for i in range(item_dict[list(item_dict.keys())[0]][_F]):items.append(list(item_dict.keys())[0])
	items=[i for i in items if type(i)is not dict];readable=''
	if items==[]:readable='that you are standing on '+fetch_square(id,x,y)[_g]
	elif len(set(items))==1:readable=f"{items.count(items[0])if items.count(items[0])>1 else _w} {items[0]}{_o if items.count(items[0])>1 else''}"
	elif len(set(items))==2:readable=f"{items.count(items[0])if items.count(items[0])>1 else _w} {items[0]}{_o if items.count(items[0])>1 else''} ";readable+=A;readable+=f"{items.count(items[1])if items.count(items[1])>1 else _w} {items[1]}{_o if items.count(items[1])>1 else''} "
	else:
		for i in range(len(set(items))-2):readable+=f"{items.count(items[i])if items.count(items[i])>1 else _w} {items[i]}{_o if items.count(items[i])>1 else''}, "
		readable+=f"{items.count(items[len(set(items))-2])if items.count(items[len(set(items))-2])>1 else _w} {items[len(set(items))-2]}{_o if items.count(items[len(set(items))-2])>1 else''}, ";readable+=A;readable+=f"{items.count(items[len(set(items))-1])if items.count(items[len(set(items))-1])>1 else _w} {items[len(set(items))-1]}{_o if items.count(items[len(set(items))-1])>1 else''} "
	await ctx.reply(f"You see {readable}")
@client.command(aliases=['pu','p'])
async def pickup(ctx):
	id=ctx.author.id;x,y=-list(save[_A][id][_I])[1],list(save[_A][id][_I])[0];items=list(fetch_square(id,x,y)[_a]);random.seed()
	if items==[]:await ctx.reply('You see nothing to pickup');return
	item=random.choice(items)
	if type(item)is dict:
		if list(item.keys())[0]in save[_A][id][_C]:
			for i in item[list(item.keys())[0]]:
				if type(item[list(item.keys())[0]][i])==int:save[_A][id][_C][list(item.keys())[0]][i]+=item[list(item.keys())[0]][i]
		else:save[_A][id][_C][list(item.keys()[0])]=dict(item[list(item.keys())[0]])
	elif item in save[_A][id][_C]:save[_A][id][_C][item][_F]+=1
	else:save[_A][id][_C][item]={_F:1}
	items.remove(item)
	if not str(f"[{x/1000}, {y/1000}]")in save[_D][_R]:save[_D][_R][str(f"[{x/1000}, {y/1000}]")]={}
	save[_D][_R][str(f"[{x/1000}, {y/1000}]")][_a]=list(items);save[_D][_R][str(f"[{x/1000}, {y/1000}]")][_AW]=bool([x for x in items if type(x)is dict]);save[_A][id][_P][_A6]+=1
	if save[_A][id][_B]:save[_D][_E][save[_A][id][_B][_N]][_AH]+=1
	if type(item)is dict:
		if item[list(item.keys())[0]][_F]==1:await ctx.reply(f"You picked up a {list(item.keys())[0]}")
		else:await ctx.reply(f"You picked up a little bag with {item[list(item.keys())[0]][_F]} {list(item.keys())[0]}")
	else:await ctx.reply(f"You picked up a {item}")
@client.command(aliases=['inventory','pocket','i','items'])
async def inv(ctx,*,txt=_A9):
	class ViewWithButton(View):
		def __init__(self):
			super().__init__(timeout=120);self.num=1;self.disabled=_J
			async def check(interaction):return interaction.user.id==ctx.author.id
			self.interaction_check=check
		@button(style=discord.ButtonStyle.blurple,emoji='◀️')
		async def back(self,button,interaction):
			if self.num>1:button.disabled=_J;self.num-=1
			else:button.disabled=_K
			embed=discord.Embed(title=f"Inventory(Page {self.num})",description=pageinv[self.num-1])
			if id==ctx.author.id:embed.set_footer(text=ctx.author)
			else:embed.set_footer(text=ctx.message.mentions[0])
			await msg.edit(embed=embed,view=self)
		@button(style=discord.ButtonStyle.blurple,emoji='⏹')
		async def kill(self,button,interaction):self.stop();await msg.edit(embed=embed,view=None)
		@button(style=discord.ButtonStyle.blurple,emoji='▶️')
		async def next(self,button,interaction):
			if self.num<len(pageinv):button.disabled=_J;self.num+=1
			else:button.disabled=_K
			embed=discord.Embed(title=f"Inventory(Page {self.num})",description=pageinv[self.num-1])
			if id==ctx.author.id:embed.set_footer(text=ctx.author)
			else:embed.set_footer(text=ctx.message.mentions[0])
			await msg.edit(embed=embed,view=self)
	if ctx.message.mentions!=[]:
		id=ctx.message.mentions[0].id
		try:save[_A][id]
		except:await ctx.reply(_At);return
	else:
		id=ctx.author.id
		try:save[_A][id]
		except:await ctx.reply(_BP);return
	reg1=0;inv=[];pageinv=[];num=1
	if txt!=_A9:
		txt=txt.split(_S)
		for x in txt:
			if x[0:3]=='<@!'and x[-1]=='>':txt.remove(x)
		txt=_S.join(txt)
		try:embed=discord.Embed(title=txt,description=_Q.join((x.capitalize()+': '+str(save[_A][id][_C][txt][x])for x in save[_A][id][_C][txt])));embed.set_author(name=_S);embed.set_footer(text=_S);await ctx.reply(embed=embed);return
		except:
			if ctx.message.mentions!=[]:
				id=ctx.message.mentions[0].id
				try:save[_A][id]
				except:await ctx.reply(_At);return
			else:await ctx.reply("You don't have any of that item");return
	for i in sorted(sorted(list(save[_A][id][_C].keys())),key=lambda item:save[_A][id][_C][item][_F],reverse=_K):
		if save[_A][id][_C][i][_F]>0:inv.append(f"__**{i}**({save[_A][id][_C][i][_F]})__");reg1+=1
		if reg1==30:pageinv.append(_Q.join(inv));inv=[];reg1=0
	if reg1!=30:pageinv.append(_Q.join(inv))
	embed=discord.Embed(title='Inventory(Page 1)',description=_Q.join(pageinv))
	if id==ctx.author.id:embed.set_footer(text=ctx.author)
	else:embed.set_footer(text=ctx.message.mentions[0])
	msg=await ctx.reply(embed=embed,view=ViewWithButton())
@client.command(aliases=[_Z,'rs'])
async def crafts(ctx,*,txt=_A9):
	A='That person does not have any recipes'
	if ctx.message.mentions!=[]:
		id=ctx.message.mentions[0].id
		try:save[_A][id]
		except:await ctx.reply(A);return
	else:id=ctx.author.id
	reg1=0;inv=[];pageinv=[]
	class ViewWithButton(View):
		def __init__(self):
			super().__init__(timeout=120);self.num=1;self.disabled=_J
			async def check(interaction):return interaction.user.id==ctx.author.id
			self.interaction_check=check
		@button(style=discord.ButtonStyle.blurple,emoji='◀️')
		async def back(self,button,interaction):
			reg1=0;inv=[];pageinv=[]
			if self.num>1:button.disabled=_J;self.num-=1
			else:button.disabled=_K
			for i in sorted(save[_A][id][_Z],reverse=_K):
				if i!='':inv.append(f"**{i}**");reg1+=1
				if reg1==30:pageinv.append(_Q.join(inv));inv=[];reg1=0
			if reg1!=30:pageinv.append(_Q.join(inv))
			embed=discord.Embed(title=f"Recipes(Page {self.num})",description=pageinv[self.num-1]);embed.set_author(name=_S);embed.set_footer(text=_S);await msg.edit(embed=embed,view=self)
		@button(style=discord.ButtonStyle.blurple,emoji='⏹')
		async def kill(self,button,interaction):self.stop();await msg.edit(embed=embed,view=self)
		@button(style=discord.ButtonStyle.blurple,emoji='▶️')
		async def next(self,button,interaction):
			reg1=0;inv=[];pageinv=[]
			for i in sorted(save[_A][id][_Z],reverse=_K):
				if i!='':inv.append(f"**{i}**");reg1+=1
				if reg1==30:pageinv.append(_Q.join(inv));inv=[];reg1=0
			if self.num<len(pageinv):button.disabled=_J;self.num+=1
			else:button.disabled=_K
			if reg1!=30:pageinv.append(_Q.join(inv))
			embed=discord.Embed(title=f"Recipes(Page {self.num})",description=pageinv[self.num-1]);embed.set_author(name=_S);embed.set_footer(text=_S);await msg.edit(embed=embed,view=self)
	if txt!=_A9:
		try:embed=discord.Embed(title=txt,description=f"{txt}({save[_A][id][_Z][txt.lower()]})");embed.set_author(name=_S);embed.set_footer(text=_S);await ctx.reply(embed=embed,view=ViewWithButton())
		except:
			if ctx.message.mentions!=[]:
				id=ctx.message.mentions[0].id
				try:save[_A][id]
				except:await ctx.reply(A);return
			else:await ctx.reply("You don't have any of that recipe");return
	else:
		for i in sorted(save[_A][id][_Z],reverse=_K):
			if i!='':inv.append(f"**{i}**");reg1+=1
			if reg1==30:pageinv.append(_Q.join(inv));inv=[];reg1=0
		if reg1!=30:pageinv.append(_Q.join(inv))
		embed=discord.Embed(title='Recipes(Page 1)',description=pageinv[0]);embed.set_author(name=_S);embed.set_footer(text=_S);msg=await ctx.reply(embed=embed,view=ViewWithButton())
@client.command(aliases=['brain','t'])
async def think(ctx):
	id=ctx.author.id;possible=[]
	for i in recipes:
		if eval(recipes[i][_L])and i not in save[_A][id][_Z]:possible.append(i)
	random.shuffle(possible)
	if possible==[]:await ctx.reply('You have nothing to think about');return
	for i in possible:
		if random.randint(0,max(recipes[i][_M]-save[_A][id][_P][_A5],0))==0:unlocked=list(save[_A][id][_Z]);unlocked.append(i);save[_A][id][_Z]=unlocked;await ctx.reply(f"You thought of a way to craft {i} \nRecipe:"+_Q+_Q.join((x.capitalize()+': '+str(recipes[i][_G][x])for x in recipes[i][_G])));break
	else:await ctx.reply('You were on the verge of thinking of something but failed to!\nKeep trying!')
@client.command(aliases=['c','make'])
async def craft(ctx,*,item=''):
	id=ctx.author.id;unlocked=list(save[_A][id][_Z]);recipe=item.lower().strip();x,y=-list(save[_A][id][_I])[1],list(save[_A][id][_I])[0];items=list(fetch_square(id,x,y)[_a]);placements=list(fetch_square(id,x,y)[_e])
	if recipe=='':await ctx.reply('You need to specify what you would like to craft');return
	if recipe not in recipes or recipe not in unlocked:await ctx.reply(_BQ);return
	if _Y in recipes[recipe]:
		if not recipes[recipe][_Y]in placements:await ctx.reply(f"You need to be on a {recipes[recipe][_Y]} to craft this");return
	for i in recipes[recipe][_G]:
		if i not in save[_A][id][_C]:await ctx.reply(f"You don't have enough {i}");break
		if save[_A][id][_C][i][_F]<recipes[recipe][_G][i]:await ctx.reply(f"You don't have enough {i}");break
	else:
		for i in recipes[recipe][_G]:save[_A][id][_C][i][_F]-=recipes[recipe][_G][i]
		amount=1
		if _F in recipes[recipe]:amount=recipes[recipe][_F]
		if recipe in save[_A][id][_C]:save[_A][id][_C][recipe][_F]+=amount
		else:save[_A][id][_C][recipe]={_F:amount}
		if _H in recipes[recipe]:
			if _H in save[_A][id][_C][recipe]:save[_A][id][_C][recipe][_H]+=recipes[recipe][_H]
			else:save[_A][id][_C][recipe][_H]=recipes[recipe][_H]
		save[_A][id][_P][_A6]+=1
		if save[_A][id][_B]:save[_D][_E][save[_A][id][_B][_N]][_AH]+=1
		await ctx.reply(f"You crafted {amount if amount!=1 else''} {recipe}")
@client.command(aliases=['u'])
async def use(ctx,*,tool=''):
	K="There's nothing to use this on";J='wheat seeds';I='frog egg';H='wool';G='feather';F="You can't eat that";E='cooked frog legs';D="You don't have that tool";C='raw frog leg';B='pine log';id=ctx.author.id;x,y=-list(save[_A][id][_I])[1],list(save[_A][id][_I])[0];player_square=fetch_square(id,x,y);items=list(player_square[_a]);placements=list(player_square[_e]);minerals=list(player_square[_v])
	if tool=='':await ctx.reply('You need to specify which tool to use');return
	if tool not in save[_A][id][_C]:await ctx.reply(D);return
	if _H in save[_A][id][_C][tool]:
		if save[_A][id][_C][tool][_H]<=0:await ctx.reply(D);return
	elif save[_A][id][_C][tool][_F]<=0:await ctx.reply(D);return
	if tool in[_B4,_BA]:
		if _s in placements:
			placements.remove(_s)
			if _A1 in save[_A][id][_C]:save[_A][id][_C][_A1][_F]+=1
			else:save[_A][id][_C][_A1]={_F:1}
			await ctx.reply('You chopped down the oak tree and got an oak log')
		elif _t in placements:
			placements.remove(_t)
			if B in save[_A][id][_C]:save[_A][id][_C][B][_F]+=1
			else:save[_A][id][_C][B]={_F:1}
			await ctx.reply('You chopped down the pine tree and got an pine log')
		else:await ctx.reply('You must be standing on a tree to use this');return
	elif tool in[_B5,_BB]:
		if minerals==[]:await ctx.reply('There is nothing to mine here');return
		else:
			mineral=random.choice(minerals)
			if mineral in save[_A][id][_C]:save[_A][id][_C][mineral][_F]+=1
			else:save[_A][id][_C][mineral]={_F:1}
			minerals.remove(mineral);await ctx.reply(f"You mined and got {mineral}")
	elif tool in[_B6,_BC]:
		for i in range(3):
			for j in range(3):
				if fetch_square(id,x-1+i,y-1+j)[_g]in[_A7,_AU]:break
			else:continue
			break
		else:await ctx.reply('You need to be next to water to use this');return
		fishs={_A3:(1000,201),_T:(200,101),'sea weed':(100,21),_A1:(20,11),B:(10,1)}
		if player_square[_i]==_Ak:fishs['raw tropical fish']=1000,201;fishs[_A3]=0,0
		if player_square[_i]==_AV:fishs['salmon']=1000,451;fishs['cod']=450,301;fishs['catfish']=300,201;fishs[_A3]=0,0
		random.seed(time.time());A=random.randint(1,1000);matched=_J
		for fisz in fishs:
			if fishs[fisz][1]<=A<=fishs[fisz][0]:fish=fisz;matched=_K;break
		if not matched:fish=B
		await ctx.reply(f"You got a {fish}")
		if fish in save[_A][id][_C]:save[_A][id][_C][fish][_F]+=1
		else:save[_A][id][_C][fish]={_F:1}
		del A
	elif tool in[_AJ,_AK,_BG,_AL,_AN,_AM,_AP,_AO]:
		heal=0
		if tool in[_AJ,E,_AL,_AN,_AM,_AP,_AO]:
			if tool==_AJ:heal=random.randint(8,15)
			if tool==E:heal=random.randint(4,5)
			if tool==_AL:heal=random.randint(10,12)
			if tool==_AN:heal=random.randint(10,13)
			if tool==_AM:heal=random.randint(13,16)
			if tool==_AP:heal=random.randint(4,7)
			if tool==_AO:heal=random.randint(12,15)
			if tool==_BH:heal=14
			if save[_A][id][_P][_V]==100:await ctx.reply(F);return
			save[_A][id][_P][_V]+=10
			if save[_A][id][_P][_V]>100:save[_A][id][_P][_V]=100
		if tool in[_AK]:
			if tool==_AK:heal=12
			if save[_A][id][_P][_V]==100:await ctx.reply(F);return
			save[_A][id][_P][_V]+=10
			if save[_A][id][_P][_V]>100:save[_A][id][_P][_V]=100
		await ctx.reply(f"You gained {heal} HP and you now have {save[_A][id][_P][_V]} HP")
	elif tool in[_B7,_BD]:
		for i in range(3):
			for j in range(3):
				if fetch_square(id,x-1+i,y-1+j)[_As]:break
			else:continue
			break
		else:await ctx.reply('You need to be next to an animal');return
		animal=random.choice(fetch_square(id,x-1+i,y-1+j)[_As]);animal_drops={_Am:[G,G,_AR,_AR,_AR,'beak'],_An:[_Ah,_Ah],'pork':[_Ai,_Ai],_Ao:[H,H,_AS,_AS,_AS,'ram horn'],_Ap:[_A3,_A3],_Aq:[_Aj,_Aj],_Ar:[I,I,C,C,C,C]};drops=[]
		for i in range(random.randint(1,3)):drops.append(random.choice(animal_drops[animal]))
		for drop in drops:
			if drop in save[_A][id][_C]:save[_A][id][_C][drop][_F]+=1
			else:save[_A][id][_C][drop]={_F:1}
		if len(drops)==1:await ctx.reply(f"You killed a {animal} and got {drops[0]}")
		elif len(drops)==2:await ctx.reply(f"You killed a {animal} and got {drops[0]} and {drops[1]}")
		else:await ctx.reply(f"You killed a {animal} and got {', '.join(drops[0:len(drops)-2])} and {drops[len(drops)-1]}")
	elif tool in[_B8,_BE]:
		for i in items+placements:
			if i in[_s,_l,_t,_AB]:break
		else:await ctx.reply('Theres nothing to use this on');return
		if _l in items:knife=[_l,_l];items.remove(_l)
		elif _AB in items:knife=[J,J];items.remove(_AB)
		elif _t in placements:knife=['oak leaf']
		elif _s in placements:knife=['pine needle']
		for item in knife:
			if item in save[_A][id][_C]:save[_A][id][_C][item][_F]+=1
			else:save[_A][id][_C][item]={_F:1}
		knife=str(knife)[1:-1].replace("'",'');await ctx.reply(f"You got {knife}")
	elif tool in[_B9,_BF]:
		unhammerables=[_s,_t,_Al]
		for i in unhammerables:
			if i in placements:await ctx.reply(K);return
		if not placements:await ctx.reply(K);return
		item=placements[0];placements.remove(item)
		if item in save[_A][id][_C]:save[_A][id][_C][item][_F]+=1
		else:save[_A][id][_C][item]={_F:1}
		await ctx.reply(f"You picked up a {item}")
	else:await ctx.reply('Not a tool');return
	if _H in save[_A][id][_C][tool]:
		save[_A][id][_C][tool][_H]-=1
		if ceil(save[_A][id][_C][tool][_H]/recipes[tool][_H])<save[_A][id][_C][tool][_F]:save[_A][id][_C][tool][_F]-=1;await ctx.reply(f"Your {tool} broke")
	else:save[_A][id][_C][tool][_F]-=1
	if not str(f"[{x/1000}, {y/1000}]")in save[_D][_R]:save[_D][_R][str(f"[{x/1000}, {y/1000}]")]={}
	save[_D][_R][str(f"[{x/1000}, {y/1000}]")][_v]=list(minerals);save[_D][_R][str(f"[{x/1000}, {y/1000}]")][_e]=list(placements);save[_D][_R][str(f"[{x/1000}, {y/1000}]")][_a]=list(items)
@client.command(aliases=['r'])
async def recipe(ctx,*,recipe=''):
	id=ctx.author.id;unlocked=list(save[_A][id][_Z]);recipe=recipe.lower().strip()
	if recipe=='':await ctx.reply('You need to specify what recipe you would like to see');return
	if recipe not in recipes or recipe not in unlocked:await ctx.reply(_BQ);return
	await ctx.reply(_Q.join((x.capitalize()+': '+str(recipes[recipe][_G][x])for x in recipes[recipe][_G])))
@client.command(aliases=['pl'])
async def place(ctx,*,placement=''):
	placeables=[_z,_Ad,_c];id=ctx.author.id;x,y=-list(save[_A][id][_I])[1],list(save[_A][id][_I])[0];placements=list(fetch_square(id,x,y)[_e])
	if placement=='':await ctx.reply('You need to specify what to place down');return
	if placement not in save[_A][id][_C]:await ctx.reply(_AX);return
	if save[_A][id][_C][placement][_F]<=0:await ctx.reply(_AX);return
	if placement not in placeables:await ctx.reply(f"That item is not placable");return
	if placements:await ctx.reply(f"You can't place that there, there is a {placements[0]} already there");return
	placements.append(placement);save[_A][id][_C][placement][_F]-=1
	if not str(f"[{x/1000}, {y/1000}]")in save[_D][_R]:save[_D][_R][str(f"[{x/1000}, {y/1000}]")]={}
	save[_D][_R][str(f"[{x/1000}, {y/1000}]")][_e]=list(placements);await ctx.reply(f"You placed down a {placements[0]}")
@client.command(aliases=['d'])
async def drop(ctx,amount=1,*,item=''):
	id=ctx.author.id;x,y=-list(save[_A][id][_I])[1],list(save[_A][id][_I])[0];items=list(fetch_square(id,x,y)[_a])
	if item=='':await ctx.reply('You must specify the amount before the item (EX. !drop 1 rock)')
	if item not in save[_A][id][_C]:await ctx.reply(_AX);return
	if save[_A][id][_C][item][_F]<=0:await ctx.reply(_AX);return
	if save[_A][id][_C][item][_F]<amount:await ctx.reply("You don't have enough of that item");return
	dropped={item:{_F:amount}};save[_A][id][_C][item][_F]-=amount
	if _H in save[_A][id][_C][item]:
		if amount==save[_A][id][_C][item][_F]:dropped[item][_H]=save[_A][id][_C][item][_H];save[_A][id][_C][item][_H]=0
		else:dropped[item][_H]=amount*recipes[item][_H];save[_A][id][_C][item][_H]-=amount*recipes[item][_H]
	items.append(dropped)
	if not str(f"[{x/1000}, {y/1000}]")in save[_D][_R]:save[_D][_R][str(f"[{x/1000}, {y/1000}]")]={}
	save[_D][_R][str(f"[{x/1000}, {y/1000}]")][_a]=list(items);save[_D][_R][str(f"[{x/1000}, {y/1000}]")][_AW]=_K;await ctx.reply(f"Your dropped a {item}, {amount} times")
@client.command(aliases=['fr'])
async def forcerespawn(ctx):
	A='To confirm this @ yourself when using the command, also this respawn does have all the normal effects of a normal respawn'
	if not ctx.message.mentions:await ctx.reply(A);return
	if ctx.message.mentions[0].id==ctx.author.id:await respawn(ctx,ctx.author.id);return
	else:await ctx.reply(A);return
@client.event
async def on_message(txt):
	id=txt.author.id;await user_check(id)
	if id not in[0xb35bae289900020,0xd17d489b902100a]:
		if not txt.guild:await txt.reply('Hey! Outside is currently in beta and to make sure all bugs are squished and found playing outside in the dms is not allowed. Sorry! When the bot goes out of beta this will be allowed!\n if you are somehow playing this bot without being in the official outside server here is the invite link! https://discord.gg/CqdY897Qxm');return
		elif str(txt.guild)!='Outside':print('-------------',txt.guild)
		if txt.channel.id in task:task[txt.channel.id]+=1
		else:task[txt.channel.id]=1
	await client.process_commands(txt)
	for i in client.commands:
		if txt.content.lower()==f"!{i.name}":save[_A][id][_P][_AT]=round(time.time())
	if save[_A][id][_P][_A5]+1<=floor(save[_A][id][_P][_A6]**0.55):save[_A][id][_P][_A5]=floor(save[_A][id][_P][_A6]**0.55);await txt.reply('Your intelligence increased')
	if save[_A][id][_B]:
		if save[_D][_E][save[_A][id][_B][_N]][_B]+1<=floor(save[_D][_E][save[_A][id][_B][_N]][_AH]**0.4):save[_D][_E][save[_A][id][_B][_N]][_B]=floor(save[_D][_E][save[_A][id][_B][_N]][_AH]**0.4);await txt.reply(f"The nation level of {save[_A][id][_B][_N]} increased")
	if id==0x43119ab08800000:
		if str(txt.embeds[0].color)=='#24b7b7':
			if'Bump done! :thumbsup:'in txt.embeds[0].description:user_id=int(re.findall('(?<=<@)(.*?)(?=>)',txt.embeds[0].description)[0]);await txt.reply(f"Thank you <@{user_id}> for bumping the server!");user=discord.utils.get(client.get_all_members(),id=user_id);role=discord.utils.get(client.get_guild(0xb359ba74d90003d).roles,id=0xd159fd640820014);await user.add_roles(role)
	write();await user_check(id)
	for i in save[_A]:
		try:
			user=discord.utils.get(client.get_all_members(),id=i);role=discord.utils.get(client.get_guild(0xb359ba74d90003d).roles,id=0xd14d88b93c28000)
			if round(time.time())-save[_A][i][_P][_AT]<300:await user.add_roles(role)
			elif role in user.roles:await user.remove_roles(role)
		except:pass
@client.command(aliases=['in'])
async def info(ctx,user=''):
	if user=='':user=ctx.author
	id=user.id
	if id not in save[_A]:await ctx.reply('That user has not played Outside yet');return
	stats=save[_A][id][_P];pos=save[_A][id][_I];pos=str(round(pos[0],-1)),str(round(pos[1],-1));pos=f"{pos[0]}, {pos[1]}";hb='';h=stats[_V]
	for x in range(1,10):
		if h-x*10<=0:hb+=_n
		else:hb+='🟥'
	embed=discord.Embed(title=f"{user.name}",description=f"Average nature enthusist",color=65280);embed.add_field(name='Intelligence',value=stats[_A5],inline=_J);embed.add_field(name='Position',value=pos,inline=_J);embed.add_field(name=_BM,value=save[_A][id][_B][_N],inline=_J);embed.add_field(name=_BL,value=hb,inline=_J);await ctx.reply(embed=embed)
@client.command(aliases=['f'])
async def found(ctx,*,nation_name):
	B='invitemembers';A='kickmembers';id=ctx.author.id;x,y=-list(save[_A][id][_I])[1],list(save[_A][id][_I])[0];claim=5*floor(y/5),5*floor(-x/5)
	for nation in save[_D][_E]:
		if id in save[_D][_E][nation][_AA]:await ctx.reply('You already own a nation!');return
	if fetch_square(id,x,y)[_B]:await ctx.reply(f"This claim would intersect another claim");return
	if profanity.contains_profanity(nation_name):await ctx.reply('That nation name contains profanity');return
	if nation_name not in save[_D][_E]:save[_D][_E][nation_name]={_AC:[claim],_AA:[ctx.author.id],_AH:0,_B:0,_A4:[id],_f:{_BR:_J,_Au:{_X:_J,_Av:_J,_Aw:_J,_AY:_J,A:_J,B:_J,_AZ:_J}},_h:{_Ax:[],_Ay:[]},'invites':[]};save[_A][id][_B]={_N:nation_name,_O:{_X:_K,_Av:_K,_Aw:_K,_AY:_K,A:_K,B:_K,_AZ:_K}}
	else:await ctx.reply('That nation already exists!');return
	await ctx.reply(f"You founded {nation_name}!");channel=client.get_channel(0xd22fb9868028033);await channel.send(f"{ctx.author.mention} founded {nation_name}!")
@client.command(aliases=['n'])
async def nation(ctx,*,nation_name):owner=await client.fetch_user(save[_D][_E][nation_name][_X]);embed=discord.Embed(title=f"{nation_name}",description=f'A average "just-pretend" fictional nation microstate thing',color=65280);embed.add_field(name='Owner',value=owner.name,inline=_J);await ctx.reply(embed=embed)
@client.command(aliases=['j'])
async def join(ctx,*,nation_name):
	id=ctx.author.id
	if nation_name not in save[_D][_E]:await ctx.reply(_Aa);return
	nation=save[_D][_E][nation_name]
	if save[_A][id][_B]:
		try:await ctx.reply(f"You already belong to {save[_A][id][_B][_N]}");return
		except:pass
	nation[_A4].append(id);save[_A][id][_B]={_N:nation_name,_O:dict(save[_D][_E][nation_name][_f][_Au])};await ctx.reply(f"You joined {nation_name}!");channel=client.get_channel(0xd22fb9868028033);await channel.send(f"{ctx.author.mention} joined {nation_name}!")
@client.command(aliases=['le'])
async def leave(ctx):
	id=ctx.author.id
	if save[_A][id][_B][_O][_X]and len(save[_D][_E][save[_A][id][_B][_N]][_A4])>1 and len(save[_D][_E][save[_A][id][_B][_N]][_AA])==1:await ctx.reply('You cannot leave this nation as your people would be left without an owner!\n To elect new owners do !giveperm @someone owner\nOr you can disband your country with !disband');return
	if save[_A][id][_B]:nation_name=save[_A][id][_B][_N];await ctx.reply(f"You left {nation_name}!");nation=save[_D][_E][nation_name];nation[_A4].remove(id);save[_A][id][_B]={};channel=client.get_channel(0xd22fb9868028033);await channel.send(f"{ctx.author.mention} left {nation_name}!")
	else:await ctx.reply(_x)
@client.command(aliases=['ds'])
async def disband(ctx,*,nation_name):
	id=ctx.author.id
	if nation_name not in save[_D][_E]:await ctx.reply(_Aa);return
	for i in save[_D][_E][nation_name][_AA]:
		if i==id:break
	else:await ctx.reply('You do not own that nation!');return
	for member in save[_D][_E][nation_name][_A4]:save[_A][member][_B]={}
	save[_D][_E].pop(nation_name);await ctx.reply(f"You disbanded {nation_name}!");channel=client.get_channel(0xd22fb9868028033);await channel.send(f"{ctx.author.mention} disbanded {nation_name}!")
@client.command(aliases=['pe'])
async def permissions(ctx):
	id=ctx.author.id;x=[]
	for i in save[_A][id][_B][_O]:
		value=save[_A][id][_B][_O][i]
		if value:x.append(i)
	await ctx.reply(_Q.join(x))
@client.command(aliases=['gp'])
async def giveperm(ctx,user,*,perm):
	id=ctx.author.id;perm=perm.strip().replace(_S,'').lower()
	if not save[_A][id][_B]:await ctx.reply(_x);return
	if not save[_A][id][_B][_O][_AY]and not save[_A][id][_B][_O][_X]:await ctx.reply(_BS);return
	if perm not in save[_A][id][_B][_O]:await ctx.reply('Not a valid permission to give');return
	if not ctx.message.mentions:await ctx.reply('You must @ the person you would like to give permissions to (EX. !giveperm @someone make claims)');return
	perms_id=ctx.message.mentions[0].id
	if save[_A][id][_B][_N]!=save[_A][perms_id][_B][_N]:await ctx.reply(_BT);return
	if not save[_A][id][_B][_O][perm]and not save[_A][id][_B][_O][_X]:await ctx.reply('You must already have a permission to give it');return
	if save[_A][perms_id][_B][_O][perm]:await ctx.reply('That person already has that permision');return
	if perm==_X:save[_D][_E][save[_A][id][_B][_N]][_AA].append(perms_id)
	save[_A][perms_id][_B][_O][perm]=_K;await ctx.reply(f"You gave <!{perms_id}> the permission ``{perm}``")
@client.command(aliases=['tp'])
async def takeperm(ctx,user,*,perm):
	id=ctx.author.id;perm=perm.strip().replace(_S,'').lower().replace('delete','del')
	if not save[_A][id][_B]:await ctx.reply(_x);return
	if not save[_A][id][_B][_O][_AY]and not save[_A][id][_B][_O][_X]:await ctx.reply(_BS);return
	if perm not in save[_A][id][_B][_O]:await ctx.reply('Not a valid permission to take');return
	if not ctx.message.mentions:await ctx.reply('You must @ the person you would like to give permissions to (EX. !takeperm @someone make claims)');return
	perms_id=ctx.message.mentions[0].id
	if save[_A][id][_B][_N]!=save[_A][perms_id][_B][_N]:await ctx.reply(_BT);return
	if save[_A][id][_B][_O][_X]:await ctx.reply('You cannot take permissions away from an owner')
	if not save[_A][id][_B][_O][perm]:await ctx.reply('You must already have a permission to take it');return
	if not save[_A][perms_id][_B][_O][perm]:await ctx.reply("That person doesn't have that permission");return
	if perm==_X:save[_D][_E][save[_A][id][_B][_N]][_AA].remove(perms_id)
	save[_A][perms_id][_B][_O][perm]=_J;await ctx.reply(f"You took the ``{perm}`` permission away from <!{perms_id}>")
@client.command(aliases=['cl'])
async def claim(ctx):
	id=ctx.author.id;x,y=-list(save[_A][id][_I])[1],list(save[_A][id][_I])[0];print(x,y);claim=5*floor(y/5),5*floor(-x/5)
	if not save[_A][id][_B]:await ctx.reply(_BU);return
	if not save[_A][id][_B][_O][_Av]and not save[_A][id][_B][_O][_X]:await ctx.reply('You need the ``makeclaims`` permission to do that');return
	if fetch_square(id,x,y)[_B]:await ctx.reply(f"This claim would intersect another claim");return
	if len(save[_D][_E][save[_A][id][_B][_N]][_AC])<save[_D][_E][save[_A][id][_B][_N]][_B]+1:save[_D][_E][save[_A][id][_B][_N]][_AC].append(claim);await ctx.reply(f"You claimed this area for the nation of {save[_A][id][_B][_N]}");await surroundings(ctx,_J)
	else:await ctx.reply('Your nation does not have any available claims to use, to increase this, increase your nation level')
@client.command(aliases=['dcl'])
async def deleteclaim(ctx):
	id=ctx.author.id;x,y=-list(save[_A][id][_I])[1],list(save[_A][id][_I])[0];claim=5*floor(y/5),5*floor(-x/5)
	if not save[_A][id][_B]:await ctx.reply(_BU);return
	if not save[_A][id][_B][_O][_Aw]and not save[_A][id][_B][_O][_X]:await ctx.reply('You need the ``delclaims`` permission to do that');return
	if not fetch_square(id,x,y)[_B]:await ctx.reply(f"This area is not claimed!");return
	if fetch_square(id,x,y)[_B]==save[_A][id][_B][_N]:save[_D][_E][save[_A][id][_B][_N]][_AC].remove(claim);await ctx.reply(f"You deleted this claim for the nation of {save[_A][id][_B][_N]}")
	else:await ctx.reply('Another nation owns this claim!')
@client.command(aliases=['de'])
async def declare(ctx,stance='',*,nation_name):
	id=ctx.author.id;nation=save[_A][id][_B][_N];stance=stance.lower().strip().replace(_S,'')
	if not save[_A][id][_B]:await ctx.reply(_x);return
	if not stance:await ctx.reply(_BV);return
	if nation_name not in save[_D][_E]:await ctx.reply(_Aa);return
	if stance not in save[_D][_E][nation][_h]:await ctx.reply('Not a valid stance you can take')
	if not save[_A][id][_B][_O][_AZ]and not save[_A][id][_B][_O][_X]:await ctx.reply(_BW);return
	if stance==_Ay and nation_name in save[_D][_E][nation][_h][_Ax]:await ctx.reply("You can't declare war with a nation you are allies with!");return
	if stance==_Ax and nation_name in save[_D][_E][nation][_h][_Ay]:await ctx.reply("You can't declare allies with a nation you are war with!");return
	await ctx.reply(f"You have declared {stance} with {nation_name}")
	if save[_D][_E][nation][_h][stance]:await ctx.reply(f"You have already declared {stance} with {nation_name} ");return
	save[_D][_E][nation][_h][stance].append(nation_name);channel=client.get_channel(0xd22fb9868028033);await channel.send(f"{ctx.author.mention} declared {stance} with {nation_name}!")
@client.command(aliases=['ude'])
async def undeclare(ctx,stance='',*,nation_name):
	id=ctx.author.id;nation=save[_A][id][_B][_N];stance=stance.lower().strip().replace(_S,'')
	if not save[_A][id][_B]:await ctx.reply(_x);return
	if not stance:await ctx.reply(_BV);return
	if nation_name not in save[_D][_E]:await ctx.reply(_Aa);return
	if stance not in save[_D][_E][nation][_h]:await ctx.reply('Not a valid stance you can undeclare')
	if not save[_A][id][_B][_O][_AZ]and not save[_A][id][_B][_O][_X]:await ctx.reply(_BW);return
	if not save[_D][_E][nation][_h][stance]:await ctx.reply(f"You are not {stance} with {nation_name} ");return
	save[_D][_E][nation][_h][stance].remove(nation_name);await ctx.reply(f"You have undeclared {stance} with {nation_name}");channel=client.get_channel(0xd22fb9868028033);await channel.send(f"{ctx.author.mention} undeclared {stance} with {nation_name}!")
@client.command(aliases=['ns'])
async def nation_settings(ctx):
	A=' : ';id=ctx.author.id;nation=save[_A][id][_B][_N];x=[]
	if not save[_A][id][_B]:await ctx.reply(_x);return
	for i in save[_D][_E][nation][_f]:
		value=save[_D][_E][nation][_f][i]
		if type(value)is dict:
			x.append(i+A+_Q)
			for j in value:value2=value[j];x.append(' -'+j+A+f"```py\n-{str(value2)}```")
		else:x.append(i+A+f"```py\n{str(value)}```")
	await ctx.send("You're nations settings"+_Q.join(x))
@client.command(aliases=['cns'])
async def chnage_nation_setting(ctx,setting,new_value):
	C='This setting value must be True or False (EX. !chnage_nation_setting <setting> True)';B='Not a valid setting';A='-';id=ctx.author.id;new_value=eval(new_value);nation=save[_A][id][_B][_N];settings=save[_D][_E][nation][_f]
	if not save[_A][id][_B]:await ctx.reply(_x);return
	if not save[_A][id][_B][_O][_X]and not save[_A][id][_B][_O][_X]:await ctx.reply('You need the ``owner`` permission to do that');return
	if setting.split(A)[0]not in settings:await ctx.send(B)
	if setting.split(A)[0]==_Au:
		if len(setting.split(A))==1:await ctx.reply('You must sepcify which default permission you would like to change (EX. !change_nation_setting defaultpermissions-makeclaims True)');return
		setting=setting.split(A)
		if setting[1]not in save[_D][_E][nation][_f][setting[0]]:await ctx.reply(B);return
		if type(new_value)is not bool:await ctx.reply(C);return
		save[_D][_E][nation][_f][setting[0]][setting[1]]=new_value
	if setting==_BR:
		if type(new_value)is not bool:await ctx.reply(C);return
		save[_D][_E][nation][_f][setting]=new_value
@client.command(aliases=['re'])
async def relations(ctx):
	id=ctx.author.id;nation=save[_A][id][_B][_N];relationships=save[_D][_E][nation][_h];x=[]
	for i in relationships:
		if relationships[i]:
			x.append(i+':')
			for j in relationships[i]:x.append(' -**'+j+'**')
	if not x:await ctx.reply('Your nation has no relations');return
	await ctx.reply(_Q.join(x))
@client.command()
@commands.has_role('Has touched grass')
async def map(ctx,x=0,y=0,zoom=1000,size=10):
	a=[]
	for i in range(size):
		b=[]
		for j in range(size):square=fetch_square(id,-y+size//2+i,x-size//2+j,zoom);b.append(square[_d]if not square[_u]else'🙂')
		a.append(''.join(b))
	await ctx.reply(_Q.join(a))
@client.command()
async def give(ctx,amount=1,*,item):
	id=ctx.author.id
	if id not in[0xb32066b0388001f,0x941a8bbd8820032]:return
	recipe=item
	if _F in recipes[recipe]:amount=recipes[recipe][_F]
	if recipe in save[_A][id][_C]:save[_A][id][_C][recipe][_F]+=amount
	else:save[_A][id][_C][recipe]={_F:amount}
	if _H in recipes[recipe]:
		if _H in save[_A][id][_C][recipe]:save[_A][id][_C][recipe][_H]+=recipes[recipe][_H]
		else:save[_A][id][_C][recipe][_H]=recipes[recipe][_H]
@client.command(aliases=['h'])
async def help(ctx,*,txt=_A9):
	class ViewWithButton(View):
		def __init__(self):
			super().__init__(timeout=120);self.num=1;self.disabled=_J
			async def check(interaction):return interaction.user.id==ctx.author.id
			self.interaction_check=check
		@button(style=discord.ButtonStyle.blurple,emoji='◀️')
		async def back(self,button,interaction):
			if self.num>1:self.num-=1
			else:0
			embed=discord.Embed(title=f"Help(Page {self.num})",description=pageinv[self.num-1])
			if id==ctx.author.id:embed.set_footer(text=ctx.author)
			else:embed.set_footer(text=ctx.message.mentions[0])
			await msg.edit(embed=embed,view=self)
		@button(style=discord.ButtonStyle.blurple,emoji='⏹')
		async def kill(self,button,interaction):self.stop();await msg.edit(embed=embed,view=None)
		@button(style=discord.ButtonStyle.blurple,emoji='▶️')
		async def next(self,button,interaction):
			if self.num<len(pageinv):self.num+=1
			else:0
			embed=discord.Embed(title=f"Help(Page {self.num})",description=pageinv[self.num-1])
			if id==ctx.author.id:embed.set_footer(text=ctx.author)
			else:embed.set_footer(text=ctx.message.mentions[0])
			await msg.edit(embed=embed,view=self)
	if ctx.message.mentions!=[]:
		id=ctx.message.mentions[0].id
		try:save[_A][id]
		except:await ctx.reply(_At);return
	else:
		id=ctx.author.id
		try:save[_A][id]
		except:await ctx.reply(_BP);return
	reg1=0;inv=[];pageinv=[];num=1
	if txt!=_A9:
		txt=txt.split(_S)
		for x in txt:
			if x[0:3]=='<@!'and x[-1]=='>':txt.remove(x)
		txt=_S.join(txt)
		try:embed=discord.Embed(title=txt,description=_Q.join((x.capitalize()+': '+str(save[_A][id][_C][txt][x])for x in save[_A][id][_C][txt])));embed.set_author(name=_S);embed.set_footer(text=_S);await ctx.reply(embed=embed);return
		except:return
	for i in sorted(list(client.commands),key=lambda item:item.name):
		if not i.help:continue
		inv.append((f"-**{str(i.name)}**- "+('('+', '.join((aliase for aliase in i.aliases))+')')if i.aliases else'')+_Q+i.help);reg1+=1
		if reg1==10:pageinv.append(_Q.join(inv));inv=[];reg1=0
	if reg1!=10:pageinv.append(_Q.join(inv))
	embed=discord.Embed(title='Help(Page 1)',description=pageinv[0])
	if id==ctx.author.id:embed.set_footer(text='command prefix is !')
	else:embed.set_footer(text=ctx.message.mentions[0])
	msg=await ctx.reply(embed=embed,view=ViewWithButton())
@client.command()
async def temp(ctx):await pickup(ctx);await look(ctx)
if __name__=='__main__':client.run(open('bottoken.txt','r').read())