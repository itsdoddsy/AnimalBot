import discord

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='do cat!help for help'))
    print('Logged in as: {} - User ID: {}'.format(client.user.name, client.user.id))
    print('Server invite link: https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=3072'.format(client.user.id))

client.run('your_token_here')