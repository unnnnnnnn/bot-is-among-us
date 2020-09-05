#-*- coding:utf-8 -*-

#================================

import discord
import asyncio
import emoji
import sys
import time
import os
import random
from discord.utils import get
from discord.ext import commands
from datetime import datetime

os.chdir(os.path.dirname(__file__))
client = commands.Bot(command_prefix="au!")
client.remove_command("help")

with open('token.txt' ,'r') as f:
    TOKEN = f.readline()

d = {'j_yellow': 'Reserved Yellow Color', 
    'i_lime': 'Reserved Lime Color', 
    'f_blue': 'Reserved Blue Color', 
    'e_purple': 'Reserved Purple Color', 
    'd_pink': 'Reserved Pink Color', 
    'c_brown': 'Reserved Brown Color', 
    'a_white': 'Reserved White Color', 
    'h_green': 'Reserved Green Color', 
    'k_orange': 'Reserved Orange Color', 
    'b_black': 'Reserved Black Color', 
    'g_cyan': 'Reserved Cyan Color', 
    'l_red': 'Reserved Red Color',
    "🇦": "Asia", 
    "🇧": "Africa",
    "🇨": "Europe", 
    "🇩": "North America",
    "🇪": "South America",
    "🇫": "Oceania"
}

de = {
    "🇦": "Asia", 
    "🇧": "Africa",
    "🇨": "Europe", 
    "🇩": "North America",
    "🇪": "South America",
    "🇫": "Oceania"
}

L = ["🇦", "🇧", "🇨", "🇩", "🇪", "🇫"]
Le = ['j_yellow', 'i_lime', 'f_blue', 'e_purple', 'd_pink', 'c_brown', 'a_white', 'h_green', 'k_orange', 'b_black', 'g_cyan', 'l_red']
Lr = ['Reserved Yellow Color', 'Reserved Lime Color',  'Reserved Blue Color', 'Reserved Purple Color', 'Reserved Pink Color', 'Reserved Brown Color', 'Reserved White Color', 'Reserved Green Color', 'Reserved Orange Color', 'Reserved Black Color', 'Reserved Cyan Color', 'Reserved Red Color']

def is_admin():
    def check_admin(ctx):
        return ctx.author.guild_permissions.administrator
    return commands.check(check_admin)


@client.event
async def on_ready():

    await client.wait_until_ready()
    await client.change_presence(activity=discord.Game(name="The bot is among us"))
    print('✅ {0.user} connecté à {1}'.format(client, datetime.now().strftime("%H:%M:%S")))


@client.event
async def on_raw_reaction_add(event):

    reaction = event.emoji
    user = client.get_user(event.user_id)
    guild = client.get_guild(event.guild_id)
    member = event.member

    with open('reactmsg.txt' ,'r') as f:
        MESSAGE_ID = int(f.readline())

    if event.message_id == MESSAGE_ID:
        
        if reaction.name in d:
            
            check = False
            if reaction.name in Le:
                for r in member.roles:
                    if r.name in Lr:
                        channel = client.get_channel(event.channel_id)
                        msg = await channel.fetch_message(event.message_id)
                        await msg.remove_reaction(reaction, user)
                        check = True
                        break

            if check == False:
                role = discord.utils.get(guild.roles, name=d[reaction.name])
                await member.add_roles(role)


@client.event
async def on_raw_reaction_remove(event):

    reaction = event.emoji
    user = client.get_user(event.user_id)
    guild = client.get_guild(event.guild_id)
    member = guild.get_member(event.user_id)

    with open('reactmsg.txt' ,'r') as f:
        MESSAGE_ID = int(f.readline())

    if event.message_id == MESSAGE_ID:
        
        if reaction.name in d:
            role = discord.utils.get(guild.roles, name=d[reaction.name])
            try:
                await member.remove_roles(role)
            except:
                pass


@client.command()
@is_admin()
async def create(ctx):
    
    embed = discord.Embed(
        colour = discord.Color.from_rgb(54, 57, 63),
    ).set_footer(
        text = "Bot Is Among Us",
        icon_url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(client.user)
    ).add_field(
        name = "{} Get your roles here".format(ctx.guild.emojis[11]),
        value = "Choose a crewmate color to reserve for the games. \nYou will receive a colored role according to your choice \n \n \n{} \nGet a **Crewmate color** role. You can only have **one** assigned color. \n \n \n{}".format(' '.join(["{}".format(ce) for ce in ctx.guild.emojis if ce.name in Le]), '\n'.join(["{}: Get the **{}** role.".format(e, d[e]) for e in de])),
        inline = False
    )

    panel = await ctx.channel.send(embed=embed)
    for emoji in ctx.guild.emojis:
        if emoji.name in Le:
            await panel.add_reaction(emoji)
    for emoji in L:
        await panel.add_reaction(emoji)

    with open('reactmsg.txt' ,'w') as f:
        f.write(str(panel.id))


client.run(TOKEN)