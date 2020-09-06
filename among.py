#-*- coding:utf-8 -*-

import discord
import asyncio
import time
import os
from discord.utils import get
from discord.ext import commands
from consts import *
from datetime import datetime

os.chdir(os.path.dirname(__file__))
client = commands.Bot(command_prefix="au!")
client.remove_command("help")

with open('token.txt' ,'r') as f:
    TOKEN = f.readline()


def is_admin():
    def check_admin(ctx):
        return ctx.author.guild_permissions.administrator
    return commands.check(check_admin)


@client.event
async def on_ready():

    await client.wait_until_ready()
    await client.change_presence(activity=discord.Game(name="The bot is among us"))

    online = client.get_channel(742095974033260611)

    print('✅ {0.user} connecté à {1}'.format(client, datetime.now().strftime("%H:%M:%S")))
    await online.send('✅ **{0.user}** connecté à ``{1}``'.format(client, datetime.now().strftime("%H:%M:%S")))


@client.event
async def on_raw_reaction_add(event):

    emoji = event.emoji.name
    channel = client.get_channel(event.channel_id)
    message = await channel.fetch_message(event.message_id)
    reaction = get(message.reactions, emoji=event.emoji)
    user = client.get_user(event.user_id)
    guild = client.get_guild(event.guild_id)
    member = event.member

    if user.bot:
        pass
    else:
        check = False
        if (event.channel_id == 751945996828672032) and (emoji in d):
            if emoji in Le:
                check =  any(r.name in Lr for r in member.roles)

            if check:
                await message.remove_reaction(reaction, user)
            else:
                role = discord.utils.get(guild.roles, name=d[emoji])
                await member.add_roles(role)
                if emoji in Le:
                    nbr = reaction.count
                    if nbr < 5:
                        role = discord.utils.get(guild.roles, name=dn[nbr])
                        await member.add_roles(role)




@client.event
async def on_raw_reaction_remove(event):

    emoji = event.emoji.name
    user = client.get_user(event.user_id)
    guild = client.get_guild(event.guild_id)
    member = guild.get_member(event.user_id)

    if user.bot:
        pass
    else:

        if event.channel_id == 751945996828672032:
            
            if emoji in d:
                for r in member.roles:
                    if r.name in list(dn.values()) and (d[emoji] in [ro.name for ro in member.roles]):
                        role = discord.utils.get(guild.roles, name=r.name)
                        try:
                            await member.remove_roles(role)
                        except:
                            pass
                        finally:
                            break

                role = discord.utils.get(guild.roles, name=d[emoji])
                try:
                    await member.remove_roles(role)
                except:
                    pass


@client.command()
@is_admin()
async def create(ctx):
    
    if ctx.channel.id == 751945996828672032:

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

        await ctx.channel.purge(limit=10)
        panel = await ctx.channel.send(embed=embed)
        for emoji in ctx.guild.emojis:
            if emoji.name in Le:
                await panel.add_reaction(emoji)
        for emoji in L:
            await panel.add_reaction(emoji)

    else:
        await ctx.channel.send("❌ Wrong channel. You have to use this command in <#{}>".format(751945996828672032))


client.run(TOKEN)