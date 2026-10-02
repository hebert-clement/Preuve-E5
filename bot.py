import os
import datetime
import random
import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Désactive la commande help par défaut de Discord
bot.remove_command("help")

# ID du salon où l'annonce du 28 décembre sera postée (Remplace par l'ID de ton salon)
# Pour trouver l'ID d'un salon, active le mode développeur sur Discord, puis fais un clic droit sur le salon -> "Copier l'identifiant"
ANNOUNCE_CHANNEL_ID = 1552759677740126248  # <--- À remplacer par ton vrai ID de salon !

@bot.event
async def on_ready():
    print(f"Akane est en ligne ! Connectée en tant que {bot.user}")
    # Lance la boucle de vérification de la date si elle n'est pas déjà lancée
    if not verifier_date_commission.is_running():
        verifier_date_commission.start()

# Tâche de fond qui tourne en permanence pour vérifier la date
@tasks.loop(hours=24)
async def verifier_date_commission():
    maintenant = datetime.datetime.now()
    
    # Vérifie si on est le 28 décembre
    if maintenant.month == 12 and maintenant.day == 28:
        channel = bot.get_channel(ANNOUNCE_CHANNEL_ID)
        if channel:
            # Crée l'embed d'annonce
            embed = discord.Embed(
                title="🚨 C'est le grand jour ! Début des commissions !",
                description="🦊 C'est parti ! La commission de **casynovartdesign** (Ref Sheet + Nude) commence officiellement aujourd'hui ! Akane a hâte de voir le résultat ! ✨🎨",
                color=0x9b59b6
            )
            embed.set_image(url="https://github.com/hebert-clement/Preuve-E5/raw/main/repas.gif")
            embed.set_footer(text="Akane Bot • Annonce Automatique")
            
            # Envoie l'annonce dans le salon (avec une mention @everyone ou un rôle si tu veux)
            await channel.send("@everyone", embed=embed)

@bot.command(name="suivi")
async def suivi(ctx):
    embed = discord.Embed(
        title="🦊 Suivi des Commissions d'Akane & Foxia",
        color=0x9b59b6
    )
    embed.add_field(name="🎨 casynovartdesign", value="Ref Sheet + Nude : **Début le 28 Décembre !**", inline=False)
    embed.add_field(name="👗 Callula", value="Tenues saisonnières (Half-body) : Prévu", inline=False)
    embed.add_field(name="⛏️️ Mod Figura (Minecraft)", value="Réouverture des commissions : **Mars 2027**", inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name="clear")
async def clear(ctx, nombre: int = 5):
    deleted = await ctx.channel.purge(limit=nombre + 1)
    indigestion = random.randint(1, 3) == 1
    
    if indigestion:
        gif_url = "https://github.com/hebert-clement/Preuve-E5/raw/main/indigestion.gif"
        description = f"🦊 *Oulah...* Akane a la digestion difficile après avoir avalé ces {len(deleted) - 1} message(s) ! Elle a un peu abusé... 😅💫"
    else:
        gif_url = "https://github.com/hebert-clement/Preuve-E5/raw/main/repas.gif"
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
    gif_url = "https://github.com/hebert-clement/Preuve-E5/raw/main/caresse.gif"
    await ctx.send(f"🦊 *Nya~* {ctx.author.mention} fait de douces caresses à Akane... Ça a l'air de lui plaire ! ✨💖\n{gif_url}")

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