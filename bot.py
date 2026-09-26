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
    
    # Création d'un joli embed aux couleurs d'Akane
    embed = discord.Embed(
        description=f"🦊 *Miam !* Akane a dévoré ces {len(deleted) - 1} message(s) indésirable(s) ! 🍜✨",
        color=0x9b59b6
    )
    # On intègre ton lien de GIF directement comme image dans l'embed
    embed.set_image(url="https://cdn-longterm.mee6.xyz/plugins/embeds/images/1467225393298931795/3e96ad70e5c5e551529e7de26e34446a5656469b1cd95de6cf86aac4110904e3.gif")
    
    await ctx.send(embed=embed)

@bot.command(name="salut")
async def salut(ctx, membre: discord.Member = None):
    if membre is None:
        # Si tu tapes juste !salut (salue la personne qui a écrit la commande)
        await ctx.send(f"🦊 Coucou {ctx.author.mention} ! Bienvenue par ici ! ✨")
    else:
        # Si tu tapes !salut @quelqu'un (salue la personne mentionnée)
        await ctx.send(f"🦊 Akane fait un grand coucou à {membre.mention} de la part de {ctx.author.mention} ! 👋✨")

bot.run(os.getenv("TOKEN"))