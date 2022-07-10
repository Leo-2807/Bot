import discord
import requests
import os

client=discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

def api():
    url = 'https://random-stuff-api.p.rapidapi.com/ai'
    params = {'msg': 'Hi there, how are you? (REQUIRED)'}
    headers = {
    'Authorization': os.getenv('API_KEY'),
    'X-RapidAPI-Key': 'f6ad8a5cfbmsh170c5fcdbd81fb2p1a3adajsn87510c811d5b',
    'X-RapidAPI-Host': 'random-stuff-api.p.rapidapi.com'}
    response = requests.get(url, headers=headers, params=params)
    jdata = response.json() 
    data = jdata['AIResponse']
    return data

def joke(cmd):
    url = 'https://random-stuff-api.p.rapidapi.com/joke'
    params =  {'tag' : cmd}
    headers = {
    'Authorization': os.getenv('API_KEY'),
    'X-RapidAPI-Key': 'f6ad8a5cfbmsh170c5fcdbd81fb2p1a3adajsn87510c811d5b',
    'X-RapidAPI-Host': 'random-stuff-api.p.rapidapi.com'}
    response = requests.get(url, headers=headers, params=params)
    jdata = response.json()
    data = jdata["joke"]
    return data

def meme():
    url = 'https://random-stuff-api.p.rapidapi.com/reddit/RandomMeme'
    params =  {'searchType': 'rising'}
    headers = {
    'Authorization': os.getenv('API_KEY'),
    'X-RapidAPI-Key': 'f6ad8a5cfbmsh170c5fcdbd81fb2p1a3adajsn87510c811d5b',
    'X-RapidAPI-Host': 'random-stuff-api.p.rapidapi.com'}
    response = requests.get(url, headers=headers, params=params)
    jdata = response.json()
    return jdata


@client.event
async def on_message(message):
    if message.content.startswith('?Hello'):
        msg = api()
        msg = discord.Embed(description='Hello {} '.format(message.author.mention)+msg, color=discord.Colour.blue())
        await message.channel.send(embed=msg)
    elif message.content.startswith('?joke'):
        cmd = message.content.split(" ", 1)
        msg = joke(cmd[1])
        msg = discord.Embed(title=cmd[1], description=msg, color=discord.Colour.red())
        await message.channel.send(embed=msg)
    elif message.content.startswith('?meme'):
        jdata = meme()
        title = jdata['title']
        image = jdata['image']
        msg = discord.Embed(title=title, color=discord.Colour.orange())
        msg.set_image(url=image)
        await message.channel.send(embed=msg)

client.run(os.getenv('TOKEN'))
