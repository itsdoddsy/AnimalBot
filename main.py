import discord
import aiohttp
import requests

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='do cat!help for help'))
    print('Logged in as: {} - User ID: {}'.format(client.user.name, client.user.id))
    print('Server invite link: https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=3072'.format(client.user.id))

@client.event
async def on_message(message):
    if message.content.startswith('!cat'):
        async with aiohttp.get('http://random.cat/meow') as r:
            if r.status == 200:
                js = await r.json()
                await client.send_message(message.channel, js['file'])

    elif message.content.startswith('!dog'):
        while True:
            try:
                r = requests.get('https://random.dog/woof')
                r.text.index('mp4') #separate mp4 from the rest
            except ValueError: #if not mp4
                await client.send_message(message.channel, 'https://random.dog/{}'.format(r.text))
                break
            else: #if mp4, redo r = requests.get(...)
                continue

    elif message.content.startswith('cat!help'):
        await client.send_message(message.channel, '''
it's literally super simple, all you gotta do is
`!cat` or `!dog`
doesn't get much easier than that buddy''')

client.run('your_token_here')