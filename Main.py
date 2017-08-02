import discord.ext
from discord.ext import commands
import logging
import asyncio

client = discord.Client()

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome to {1.name}, {0.mention}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)

@client.event
async def on_message(message):
    if message.content.startswith('!deleteme'):
        msg = await client.send_message(message.channel, 'I will delete myself now...')
        await client.delete_message(msg)

async def on_message_delete(message):
@client.event
    fmt = '{0.author.name} has deleted the message:\n{0.content}'
    await client.send_message(message.channel, fmt.format(message))


@client.event
async def on_message(message):
    if message.content.lower().startswith('!hello'):
        fmt = 'Hello, {0.author.name}!'
        await client.send_message(message.channel, fmt.format(message))



# @client.event
# async def on_message(message, member, channel):
#     if message.content.lower().startswith('!move'):


client.run("MzM3Mjk4NDg4MzE0Mjk4Mzcx.DFE4Lw.1NsKTP_vf0Nam-Q6Xx5s0-LhomQ")