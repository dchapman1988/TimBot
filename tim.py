import discord
import os
import random
import json
import asyncio
from itertools import cycle

TOKEN = "Njg0MjM5ODczNjQwODkwNDg5.Xl3OmQ.bPS0qLWxsVNjf03SJDBUqoGTfnQ"
client = discord.Client()
status = json.loads(open('json/status.json').read())
# annoy_victor = ["Hey can I be a mod?"]        \\ Maybe later lol.
help_list = json.loads(open('json/help.json').read())

#
# Don't laugh at my shitty coding skills lol. IT WORKS
#


async def change_status():  # Change TimBot "Playing" status every minute. Too frequent? Meh.
    await client.wait_until_ready()
    msgs = cycle(status)

    while True:
        current_status = next(msgs)
        await client.change_presence(activity=discord.Game(name=current_status))
        await asyncio.sleep(60)


@client.event
async def on_ready():
    print('The autism has arrived!'.format(client))


@client.event
async def on_message(message):
    if message.content == "$help":
        await message.channel.send("\n".join(help_list))

    if client.user.mentioned_in(message) and message.mention_everyone is False:
        if '' in message.content.lower():
            await message.channel.send("Do you think I'm fat? Type **'$help'** to see what else I can do.") and await message.add_reaction("👀")

    if message.startswith( '$' )
        if message.content == "$dirtyclutching":
            await message.channel.send(file=discord.File("images/dirtyclutching/dirtyclutching.png"))

        elif message.content == "$stagex": # Random choice for more stageX related photos to be added later.
            stageX_list = os.listdir("stageX/")
            stageX_String = random.choice(stageX_list)
            stageX_Path = "stageX/" + stageX_String
            await message.channel.send(file=discord.File(stageX_Path))

        elif message.content == "$tim":
            imgList = os.listdir("images/")
            imgString = random.choice(imgList)
            imgPath = "images/" + imgString

            await message.channel.send(file=discord.File(imgPath))

        elif message.content == "$timquote":
            quoteList = json.loads(open('json/quotes.json').read())
            quoteSelect = random.choice(quoteList)

            await message.channel.send(quoteSelect)

        elif "dsg" in message.content:
            await message.channel.send("https://www.youtube.com/watch?v=v6wgLJjdOUc&feature=youtu.be")

        else
            await message.channel.send("I get used like a punching bag, and I never fire back. (TimBot doesn't have a response)")

client.loop.create_task(change_status())
client.run(TOKEN)
