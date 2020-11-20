import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from api import gw2api
from tools import emojis

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

client = commands.Bot(command_prefix=".")
api = gw2api()
emoji = emojis()

def dailyHelp():
    msg = "```"
    msg += ".daily <argument>\n\n"
    msg += "Arguments available:\n"
    msg += "  tomorrow  Show Daily tasks for tomorrow"
    msg += "```"
    return msg

@client.command()
async def daily(ctx, *arg):
    #https://wiki.guildwars2.com/wiki/Category:Achievement_icons
    newline = "\n"
    thumbnail = discord.File("resources/images/Daily_Achievement.png", filename="Daily_Achievement.png")
    global tomorrowf
    tomorrowf = False

    if ",".join(arg) == "tomorrow":
        tomorrowf = True  
    elif len(arg) > 0:
        await ctx.send(dailyHelp())
        return
    else:
        pass
        
    if ctx.author.bot: return

    daily_pve = client.get_emoji(id=emoji.daily_pve)
    daily_wvw = client.get_emoji(id=emoji.daily_pvp)
    daily_fractals = client.get_emoji(id=emoji.daily_fractals)
    daily_fractals_recs = client.get_emoji(id=emoji.daily_fractals_recs)

    pveList, pvpList, wvwList, fractalsList, fractalsRecsList = api.getDailyAchievements(tomorrowf)
    pveList = [f'{daily_pve} {e}' for e in pveList]
    pvpList = [f'{daily_pve} {e}' for e in pvpList]
    wvwList = [f'{daily_wvw} {e}' for e in wvwList]
    fractalsList = [f'{daily_fractals} {e}' for e in fractalsList]
    fractalsRecsList = [f'{daily_fractals_recs} {e}' for e in fractalsRecsList]

    e = discord.Embed(title=f"Dailies {'Tomorrow' if tomorrowf else ''}", color=0x731bd1)
    e.set_thumbnail(url="attachment://Daily_Achievement.png")
    e.add_field(name="PVE", value=f'{newline.join(pveList)}', inline=False)
    e.add_field(name="PVP", value=f'{newline.join(pvpList)}', inline=False)
    e.add_field(name="WVW", value=f'{newline.join(wvwList)}', inline=False)
    e.add_field(name="Fractals", value=f'{newline.join(fractalsList)}', inline=True)
    e.add_field(name="Recommended", value=f'{newline.join(fractalsRecsList)}', inline=True)
    e.set_footer(text="Created by Dzoki")
    await ctx.send(embed=e,file=thumbnail)

client.run(TOKEN)