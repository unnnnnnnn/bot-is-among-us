#-*- coding:utf-8 -*-

import discord
import asyncio
import time
import os
from discord.utils import get
from discord.ext import commands
from consts import *
from datetime import datetime

client = commands.Bot(command_prefix="au!")
client.remove_command("help")

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
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="They are among us")
    await member.add_roles(role)


@client.event
async def on_raw_reaction_add(event):

    emoji = event.emoji.name
    channel = client.get_channel(event.channel_id)
    logs = client.get_channel(755516613209620540)
    message = await channel.fetch_message(event.message_id)
    reaction = get(message.reactions, emoji=event.emoji)
    user = client.get_user(event.user_id)
    guild = client.get_guild(event.guild_id)
    member = event.member

    if user.bot:
        pass
    else:
        check = False
        if (channel.name == "get-roles") and (emoji in d):
            if emoji in Le:
                check =  any(r.name in Lr for r in member.roles)

            if check:
                await message.remove_reaction(reaction, user)
            else:
                role = discord.utils.get(guild.roles, name=d[emoji])
                await member.add_roles(role)
                await logs.send("⬆️ The **{}** role has been added to **{}**".format(role,user))
                if emoji in Le:
                    nbr = reaction.count
                    if nbr < 6:
                        role = discord.utils.get(guild.roles, name=dn[nbr])
                        await member.add_roles(role)
                        await logs.send("⬆️ The **{}** role has been added to **{}**".format(role,user))




@client.event
async def on_raw_reaction_remove(event):

    emoji = event.emoji.name
    channel = client.get_channel(event.channel_id)
    logs = client.get_channel(755516613209620540)
    user = client.get_user(event.user_id)
    guild = client.get_guild(event.guild_id)
    member = guild.get_member(event.user_id)

    if user.bot:
        pass
    else:

        if (channel.name == "get-roles"):
            
            if emoji in d:
                for r in member.roles:
                    if emoji in Le:
                        if r.name in list(dn.values()) and (d[emoji] in [ro.name for ro in member.roles]):
                            role = discord.utils.get(guild.roles, name=r.name)
                            try:
                                await member.remove_roles(role)
                                await logs.send("⬇️ The **{}** role has been removed from **{}**".format(role,user))
                            except:
                                pass
                            finally:
                                break

                role = discord.utils.get(guild.roles, name=d[emoji])
                try:
                    await member.remove_roles(role)
                    await logs.send("⬇️ The **{}** role has been removed from **{}**".format(role,user))
                except:
                    pass


@client.command()
@is_admin()
async def create(ctx):

    channel = client.get_channel(ctx.channel.id)
    
    if (channel.name == "get-roles"):

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
        await ctx.channel.send("❌ Wrong channel. You have to use this command in a channel called **#get-roles**")


client.run("NzUxOTE0ODc5NTUxNjY4MzI1.X1QBTQ.2SAAJV1yb7gP5fUA81NozcyjLqM")