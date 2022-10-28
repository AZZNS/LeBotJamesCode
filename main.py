import discord
from discord.ext import commands, tasks
import random
import asyncio
import youtube_dl
import nacl

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

BAN_WORDS = ["jul", "gab", "xead", "\u0040Frozwayy"]
HELLO_WORDS = ["bonjour", "salut", "yo ", "hello", "allo", "ciao", "bonsoir", "coucou", "cc ", "hey"]
NIGHT_TIME = ["bonne nuit", "bn "]
MEMBERS_LIST = {}

num = []
for i in range(1, 41):
    i + 1
    num.append(i)
NUMBERS_SPAM = [str(x) for x in num]
del num


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="!help"))
    print("wesh le sang")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # BAN WORDS
    if not message.author.bot:
        for word in BAN_WORDS:
            if word in message.content:
                await message.delete()
                await message.channel.send(
                    "**Je déteste " + word + ", n'en parle plus jamais**" + message.author.mention)
        for hello in HELLO_WORDS:
            if hello in message.content:
                await message.channel.send("Coucou " + message.author.mention)
        for bye in NIGHT_TIME:
            if bye in message.content:
                await message.channel.send("Déjà ? Oh non bébou :( Bonne nuit ! " + message.author.mention)

    # PIERRE FEUILLE CISEAUX
    async def pfc():
        CHOICES = ["pierre", "feuille", "ciseaux"]
        bot_choice = random.randint(0, 2)
        bot_choice = CHOICES[bot_choice]
        print(bot_choice)

        async def check(m):
            return (m.content in NUMBERS_SPAM) and (m.channel.send == message.channel.send)

        msg = await client.wait_for("message", check=check)
        user_choice = msg.content
        print(user_choice)

        '''CHOICES = ["pierre", "feuille", "ciseaux"]'''
        if bot_choice == CHOICES[0] and user_choice == CHOICES[0]:
            await message.channel.send("**Pierre !** \n**Égalité !** Rejoue frère !")
        elif bot_choice == CHOICES[1] and user_choice == CHOICES[1]:
            await message.channel.send("**Feuille !** \n**Égalité !** Rejoue frère !")
        elif bot_choice == CHOICES[2] and user_choice == CHOICES[2]:
            await message.channel.send("**Ciseaux !** \n**Égalité !** Rejoue frère !")

        elif bot_choice == CHOICES[0] and user_choice == CHOICES[1]:
            await message.channel.send("**Pierre !** \n Ah bien joué ! La prochaine je t'encule...")
        elif bot_choice == CHOICES[1] and user_choice == CHOICES[0]:
            await message.channel.send("**Feuille !** \n**Perdu !** Ton level m'extermine...")

        elif bot_choice == CHOICES[0] and user_choice == CHOICES[2]:
            await message.channel.send("**Pierre !** \n**Perdu !** Ton level m'extermine...")
        elif bot_choice == CHOICES[2] and user_choice == CHOICES[0]:
            await message.channel.send("**Ciseaux** ! \nAh bien joué ! La prochaine je t'encule...")

        elif bot_choice == CHOICES[1] and user_choice == CHOICES[2]:
            await message.channel.send("**Feuille** ! \nAh bien joué ! La prochaine je t'encule...")
        elif bot_choice == CHOICES[2] and user_choice == CHOICES[1]:
            await message.channel.send("**Ciseaux !** \n**Perdu !** Ton level m'extermine...")

    # HELP
    async def helpme():
        embed = discord.Embed(title="Commandes de LeBot ",
                              description="Tu aimerais utiliser ton Bot préféré, mais tu ne connais pas les commandes ?"
                                          " Lis-ça !",
                              color=0x3a88fe)
        embed.set_author(name="LeBot James", icon_url="https://cdn.nba.com/headshots/nba/latest/1040x760/2544.png")
        embed.add_field(name="`!help`", value="T'y es donc à priori t'es pas con t'as compris", inline=True)
        embed.add_field(name="`!spam`",
                        value="Tu veux jouer avec ton meilleur pote mais ce chien de la casse te répond pas ? "
                              "\nEnvoie `!spam [@la victime]` ",
                        inline=False)
        embed.add_field(name="`!pfc`",
                        value="Ton meilleur pote ne répond toujours pas ? Joue avec LeBot au \nPierre Feuille Ciseaux !",
                        inline=False)
        embed.add_field(name="`!gay`",
                        value="Tu as des doutes sur ton orientation sexuelle ou sur celle d'un de tes potes ? \nPas de "
                              "soucis ! `!gay` pour toi-même et `!gay [@la victime]` !",
                        inline=False)
        embed.add_field(name="`!pdp`",
                        value="Wow ! Ton pote a une photo de profil incroyable ! Il te la faut ! "
                              "\nAffiche-la en grand avec `!pdp [@la personne]`",
                        inline=False)
        embed.add_field(
            name="-----------------------------------------------------------------------------------------------",
            value="**-----------------------------------------------------------------------------------------------**",
            inline=True)

        embed.set_footer(text=f"DM @Mess pour des recommandations aux oignons t'as capté ahaha tsais")
        await message.channel.send(embed=embed)

    # PLAY
    async def play(url="", channel=""):
        try:
            url = message.content.split(" ", 1)[1]
            voice_client = message.author.voice.channel
            await voice_client.connect()
        except IndexError or AttributeError:
            await message.channel.send(
                message.author.mention + " T'es con ou quoi faut que tu sois dans un channel fdp")

    # SPAM
    async def spamming():

        # GET MENTION ID
        user_id = MEMBERS_LIST.values()

        try:
            m = message.content.split(" ", 1)
            a = m[1]
            a = a.replace("<", "")
            a = a.replace(">", "")
            a = a.replace("@", "")
        except IndexError:
            await message.channel.send(message.author.mention + " **T'es con fréro...**\n"
                                                                "**Entre la commande comme ça :**\n`!spam [@la victime]`")

        id = int(a)
        if id in user_id:
            await message.channel.send(
                message.author.mention + "** Encore ce pd... combien de fois je le spam ? (0 à 40)**")

        # TIMES USED
        def check(m1):
            return (m1.content in NUMBERS_SPAM) and (m1.channel.send == message.channel.send)

        msg = await client.wait_for("message", check=check)
        p = msg.content
        spam_times = int(p)

        await message.channel.send("Ta beuteu est gigantesque, j'y vais de suite...")
        print("spam launching...")
        for j in range(0, spam_times):
            await asyncio.sleep(1)
            await message.channel.send(f"<@{id}> **viens gros tu nous manques :(**")
        print("spam ended.")

    # GAY TARGET GETTER
    async def gay_level():
        lvl = random.randint(0, 100)
        try:
            target = message.content.split(" ", -1)[1]
            target = target.replace("<", "")
            target = target.replace("@", "")
            target = target.replace(">", "")
            print(lvl)
            await message.channel.send(f"**Selon les estimations, <@{target}> est gay à environ " + str(lvl) + "% !**")
        except IndexError:
            target = message.author.id
            print(lvl)
            await message.channel.send(
                f"<@{target}>** Selon les estimations, tu es gay à environ " + str(lvl) + "% !**")

    # PROFILE PICTURE FINDER
    async def pfp():
        try:
            pers = message.content.split(" ", -1)[1]
            pers = pers.replace("<", "")
            pers = pers.replace("@", "")
            pers = pers.replace(">", "")
            pers_id = int(pers)
            pers_pic = client.get_user(pers_id)
            for user in MEMBERS_LIST.values():
                if pers_id == user:
                    p = list(MEMBERS_LIST.values()).index(pers_id)
                    user_name = list(MEMBERS_LIST.keys())[p]
            pic = pers_pic.avatar_url
            embed = discord.Embed(title=f"Photo de profil de {user_name}",
                                  color=0x3a88fe)
            embed.set_image(url=pic)
            await message.channel.send(embed=embed)

        except IndexError:
            authorProfilePicture = message.author.avatar_url
            a = message.author.name
            em = discord.Embed(title=f"Photo de profil de {a}",
                               color=0x3a88fe)
            em.set_image(url=authorProfilePicture)
            await message.channel.send(embed=em)

    # MORPION
    async def morpion():
        tab = [
            ["", "|", "", "|", ""],
            ["-", "+", "-", "+", "-"],
            ["", "|", "", "|", ""],
            ["-", "+", "-", "+", "-"],
            ["", "|", "", "|", ""]
        ]

    # COMMAND CHECKER
    if message.content.startswith("!spam"):
        await spamming()
    elif message.content == "!pfc":
        await message.channel.send("Ok lesgo petit pierre feuille ciseaux \n**Allez à mon décompte:**")
        await message.channel.send("**3**")
        await asyncio.sleep(1)
        await message.channel.send("**2**")
        await asyncio.sleep(1)
        await message.channel.send("**1**")
        await pfc()
    elif message.content == "!help":
        await helpme()
    elif message.content.startswith("!play"):
        await play()
    elif message.content.startswith("!gay"):
        await gay_level()
    elif message.content.startswith("!pdp"):
        await pfp()
    elif message.content == "!morpion":
        await morpion()


# WELCOME
@client.event
async def on_member_join(member):
    ran = random.randint(17, 50)
    beuteu = str(ran)
    await client.get_channel(1004155437228236951).send(
        f"{member.mention} vient d'arriver ! Sa beuteu excède la moyenne ! "
        + beuteu + "cm selon les estimations !")
    print(f"{member} vient de rejoindre le serveur")


# GOODBYE
@client.event
async def on_member_remove(member):
    await client.get_channel(1004155437228236951). \
        send(f"{member} vient de nous quitter ! Personnellement, je m'en blc")
    print(f"{member} vient de quitter le serveur")


# GET USERNAMES
@tasks.loop(count=1)
async def get_users():
    await client.wait_until_ready()

    for user in client.users:
        if user.name != "LeBotJames":
            MEMBERS_LIST[user.name] = user.id
    print(MEMBERS_LIST)


get_users.start()

client.run("*")
