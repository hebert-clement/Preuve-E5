import os
import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Désactive la commande help par défaut de Discord pour laisser place à la nôtre
bot.remove_command("help")

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
    
    # 1 chance sur 3 qu'Akane ait trop mangé
    indigestion = random.randint(1, 3) == 1
    
    if indigestion:
        # Ton nouveau GIF personnalisé pour l'indigestion
        gif_url = "https://cdn.discordapp.com/attachments/1552759796048855231/1553742660345536613/ezgif.com-cut.gif"
        description = f"🦊 *Oulah...* Akane a la digestion difficile après avoir avalé ces {len(deleted) - 1} message(s) ! Elle a un peu abusé... 😅💫"
    else:
        # GIF normal de repas
        gif_url = "https://cdn.discordapp.com/attachments/1374312514573176873/1378170745452101723/d8828e4b-6c05-4771-8daa-cc84ea89bb73.gif"
        description = f"🦊 *Miam !* Akane a dévoré ces {len(deleted) - 1} message(s) indésirable(s) ! 🍜✨"

    embed = discord.Embed(description=description, color=0x9b59b6)
    embed.set_image(url=gif_url)
    
    await ctx.send(embed=embed, delete_after=6)

@bot.command(name="salut")
async def salut(ctx, membre: discord.Member = None):
    if membre is None:
        await ctx.send(f"🦊 Coucou {ctx.author.mention} ! Bienvenue par ici ! ✨")
    else:
        await ctx.send(f"🦊 Akane fait un grand coucou à {membre.mention} de la part de {ctx.author.mention} ! 👋✨")

@bot.command(name="calin")
async def calin(ctx, membre: discord.Member = None):
    if membre is None:
        await ctx.send(f"{ctx.author.mention} fait un gros câlin à tout le monde ! 🦊🤗")
    else:
        await ctx.send(f"{ctx.author.mention} fait un gros câlin tout doux à {membre.mention} ! ✨🦊")

@bot.command(name="caresser")
async def caresser(ctx):
    # Lien direct optimisé pour que Tenor affiche le GIF dans le chat
    gif_url = "https://media.tenor.com/tH7rWcZl9e8AAAAC/neko-pat.gif"
    
    # Envoie le message et le GIF directement
    await ctx.send(f"🦊 *Nya~* {ctx.author.mention} fait de douces caresses à Akane... Ça a l'air de lui plaire ! ✨💖\n{gif_url}")
    
    await ctx.send(embed=embed)

@bot.command(name="help")
async def help_command(ctx):
    embed = discord.Embed(
        title="📜 Grimoire des commandes d'Akane",
        description="Voici la liste de tout ce que je peux faire pour t'aider sur le serveur :",
        color=0x9b59b6
    )
    embed.add_field(name="`!suivi`", value="Affiche le tableau de suivi des commissions et du mod Figura.", inline=False)
    embed.add_field(name="`!calin [membre]`", value="Fait un gros câlin (à toi-même ou à la personne mentionnée).", inline=False)
    embed.add_field(name="`!caresser`", value="Fait des caresses à Akane pour voir sa réaction !", inline=False)
    embed.add_field(name="`!salut [membre]`", value="Envoie un coucou chaleureux.", inline=False)
    embed.add_field(name="`!clear [nombre]`", value="Nettoie les derniers messages (avec un risque d'indigestion pour Akane !).", inline=False)
    
    embed.set_footer(text="Akane Bot • 24/7 Cloud Hosting")

    try:
        await ctx.author.send(embed=embed)
        await ctx.send(f"📬 {ctx.author.mention}, je t'ai envoyé la liste de mes commandes en message privé !", delete_after=4)
    except discord.Forbidden:
        await ctx.send(f"❌ {ctx.author.mention}, je n'ai pas réussi à t'envoyer de MP ! Vérifie tes paramètres de confidentialité.", delete_after=5)

bot.run(os.getenv("TOKEN"))