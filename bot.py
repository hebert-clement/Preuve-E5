import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Akane est en ligne ! Connectée en tant que {bot.user}")

@bot.command(name="suivi")
async def suivi(ctx):
    embed = discord.Embed(
        title="🦊 Suivi des Commissions d'Akane & Foxia",
        color=0x9b59b6
    )
    embed.add_field(name="🎨 casynovartdesign", value="Ref Sheet + Nude : En cours de validation", inline=False)
    embed.add_field(name="👗 Callula", value="Tenues saisonnières (Half-body) : Prévu", inline=False)
    embed.add_field(name="⛏️ Mod Figura (Minecraft)", value="Réouverture des commissions : **Mars 2027**", inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name="clear")
async def clear(ctx, nombre: int = 5):
    # Supprime les messages demandés (+1 pour la commande elle-même)
    deleted = await ctx.channel.purge(limit=nombre + 1)
    
    # Message RP d'Akane avec un GIF de renard/manga
    gif_url = "https://cdn-longterm.mee6.xyz/plugins/embeds/images/1467225393298931795/3e96ad70e5c5e551529e7de26e34446a5656469b1cd95de6cf86aac4110904e3.gif"  # Tu peux remplacer ce lien par le GIF de ton choix !
    
    confirmation = await ctx.send(
        f"🦊 *Miam !* Akane a dévoré ces {len(deleted) - 1} message(s) indésirable(s) ! 🍜✨\n{gif_url}"
    )
    await confirmation.delete(delay=5)

bot.run(os.getenv("TOKEN"))