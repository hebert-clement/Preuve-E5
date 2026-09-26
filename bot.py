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
    # Supprime le nombre de messages spécifié (+1 pour supprimer aussi la commande tapée)
    deleted = await ctx.channel.purge(limit=nombre + 1)
    
    # Envoie un petit message temporaire qui se supprime tout seul (optionnel)
    confirmation = await ctx.send(f"🧹 {len(deleted) - 1} message(s) supprimé(s) avec succès !")
    await confirmation.delete(delay=3)

bot.run(os.getenv("TOKEN"))