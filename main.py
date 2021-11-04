import discord
from discord import voice_client
from discord.ext import commands
import datetime
from datetime import *
import time
from time import sleep
import os



client = commands.Bot(command_prefix = "+")
client.remove_command("help")


heures = datetime.now().strftime("%H:%M:%S")

@client.event
async def on_ready():
    global heures
    print(f"[{heures}] Je suis en ligne !")
    await client.change_presence(activity = discord.Game("Dera TEAM"))


@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("1")
    time.sleep(1)
    await ctx.send("2")
    time.sleep(1)
    await ctx.send("3")
    time.sleep(1)
    msg = await ctx.send("Ter")
    await msg.edit(content = "Termi")
    await msg.edit(content = "Terminer")
    await ctx.bot.logout()


@client.command()
async def test(ctx):
    await ctx.send("Test reussi")


@client.command()
@commands.has_any_role("ScrimManager")
async def scrim(ctx):
    if ctx.channel.id == 889549859911258185:
        await ctx.channel.purge(limit=1000)
        check = discord.utils.get(client.emojis, name = "check")
        uncheck = discord.utils.get(client.emojis, name = "uncheck")
        await ctx.send("https://cdn.discordapp.com/attachments/889549859911258185/905848204191498251/image0-4.gif")
        embed=discord.Embed(title=f"Amnesia Contre ???", description="Disponibilité cochez juste ce qui vous convient", color=0x9814c8)
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/889539720575590401/9c8bc412f1f5111eed5205abb2f5f921.webp?size=96")
        embed.add_field(name="Heure UTC+1", value="**__21 heures 30__**\nLes règles de scrim sont dans <#889546660189970432>", inline=False)
        embed.set_footer(text="Dera©")
        emb = await ctx.send(embed=embed)
        await emb.add_reaction(check)
        await emb.add_reaction(uncheck)
        await ctx.send("https://cdn.discordapp.com/attachments/889549859911258185/905848204191498251/image0-4.gif")
        embed=discord.Embed(title=f"Amnesia Contre ???", description="Disponibilité cochez juste ce qui vous convient", color=0x9814c8)
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/889539720575590401/9c8bc412f1f5111eed5205abb2f5f921.webp?size=96")
        embed.add_field(name="Heure UTC+1", value="**__22 heures__**\nLes règles de scrim sont dans <#889546660189970432>", inline=False)
        embed.set_footer(text="Dera©")
        embe = await ctx.send(embed=embed)
        await embe.add_reaction(check)
        await embe.add_reaction(uncheck)
        await ctx.send("https://cdn.discordapp.com/attachments/889549859911258185/905848204191498251/image0-4.gif")
        embed=discord.Embed(title=f"Amnesia Contre ???", description="Disponibilité cochez juste ce qui vous convient", color=0x9814c8)
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/889539720575590401/9c8bc412f1f5111eed5205abb2f5f921.webp?size=96")
        embed.add_field(name="Heure UTC+1", value="**__22 heures 30__**\nLes règles de scrim sont dans <#889546660189970432>", inline=False)
        embed.set_footer(text="Dera©")
        embe = await ctx.send(embed=embed)
        await embe.add_reaction(check)
        await embe.add_reaction(uncheck)
        await ctx.send("https://cdn.discordapp.com/attachments/889549859911258185/905848204191498251/image0-4.gif")
        await ctx.send("@everyone")
    if ctx.channel.id != 889549859911258185:
        ctx.send("tu est dans le mauvais channel pour taper cette commande.")





@client.command()
async def help(ctx):
    await ctx.send("Pour l'instant il y a qu'une seule commande c'est +scrim (nom de la team adverse) et si elle n'ai pas deffini elle seras nommer d'un: ?")






client.run(os.environ["token"])