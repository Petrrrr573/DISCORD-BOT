import discord
import main
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View
import random
import praw
import datetime, time
from main import reddit, giphy_key
import requests
from jokeapi import Jokes

channel_dict = {}

games_dict = {}

class Game:
    def __init__(self):
        self.reactions = ["⬆️", "⬇️", "⬅️", "➡️" , "🔄", "❌"]
        self.borders = ["⬜", "🟪", "🟥", "🟧" , "🟨", "🟩", "🟦"]
        self.gs = "⬛"
        self.bs = random.choice(self.borders)
        self.bbs = "🟫"
        self.sc = "❎"
        self.head = "😳"
        self.x = 1
        self.y = 1
        self.rows = 7
        self.columns = 10
        self.squares = []
        self.crosses = []

        self.level = 1

        self.possible_squares = []
        self.possible_crosses = []

    def reset(self):
        self.bs = random.choice(self.borders)
        self.x = 1
        self.y = 1
        self.squares = []
        self.crosses = []
        self.possible_squares = []
        self.possible_crosses = []

        self.grid()
    
    def place_squares(self):
        for i in range(self.rows-2):
            for j in range(self.columns-2):
                if i+1 != 1 and j+1 != 1:
                    self.possible_crosses.append([i+1, j+1])
                    
        for i in range(self.level):
            rand_cr = random.choice(self.possible_crosses)
            self.crosses.append(rand_cr)
            x, y = rand_cr
            self.possible_crosses.remove([x, y])
            self.levelOne[x][y] = self.sc

        for i in range(self.rows-4):
            for j in range(self.columns-4):
                if i+2 != 1 and j+2 != 1 and [i+2, j+2] not in self.crosses:
                    self.possible_squares.append([i+2, j+2])
        
        for i in range(self.level):
            rand_sq = random.choice(self.possible_squares)
            self.squares.append(rand_sq)
            x, y = rand_sq
            self.possible_squares.remove([x, y])
            self.levelOne[x][y] = self.bbs
        
        self.possible_squares = []
        self.possible_crosses = []

    def make_string(self):
        self.square_str = "\n".join("".join(row) for row in self.levelOne)

    def grid(self):
        self.levelOne = [[self.gs for _ in range(self.columns)] for _ in range(self.rows)]
        self.build_walls()
        self.levelOne[self.x][self.y] = self.head
        self.place_squares()

    def build_walls(self):
        for i in range(self.rows):
            self.levelOne[i][0] = self.bs
            self.levelOne[i][self.columns-1] = self.bs
        for j in range(1, self.columns-1):
            self.levelOne[0][j] = self.bs
            self.levelOne[self.rows-1][j] = self.bs

    def move(self, side):
        if side == "up":
            if self.levelOne[self.x-1][self.y] != self.bs and self.levelOne[self.x-1][self.y] != self.sc:
                if self.levelOne[self.x-1][self.y] == self.bbs:
                    if self.levelOne[self.x-2][self.y] == self.sc:
                        self.levelOne[self.x-2][self.y] = self.bs
                        self.squares.remove([self.x-1, self.y])
                        self.crosses.remove([self.x-2, self.y])
                    elif self.levelOne[self.x-2][self.y] != self.bs:
                        self.levelOne[self.x-2][self.y] = self.bbs
                        index = self.squares.index([self.x-1, self.y])
                        self.squares[index] = [self.x-2, self.y]
                self.levelOne[self.x][self.y] = self.gs
                self.x -= 1

        if side == "down":
            if self.levelOne[self.x+1][self.y] != self.bs and self.levelOne[self.x+1][self.y] != self.sc:
                if self.levelOne[self.x+1][self.y] == self.bbs:
                    if self.levelOne[self.x+2][self.y] == self.sc:
                        self.levelOne[self.x+2][self.y] = self.bs
                        self.squares.remove([self.x+1, self.y])
                        self.crosses.remove([self.x+2, self.y])
                    elif self.levelOne[self.x+2][self.y] != self.bs:
                        self.levelOne[self.x+2][self.y] = self.bbs
                        index = self.squares.index([self.x+1, self.y])
                        self.squares[index] = [self.x+2, self.y]
                self.levelOne[self.x][self.y] = self.gs
                self.x += 1
        if side == "left":
            if self.levelOne[self.x][self.y-1] != self.bs and self.levelOne[self.x][self.y-1] != self.sc:
                if self.levelOne[self.x][self.y-1] == self.bbs:
                    if self.levelOne[self.x][self.y-2] == self.sc:
                        self.levelOne[self.x][self.y-2] = self.bs
                        self.squares.remove([self.x, self.y-1])
                        self.crosses.remove([self.x, self.y-2])
                    elif self.levelOne[self.x][self.y-2] != self.bs:
                        self.levelOne[self.x][self.y-2] = self.bbs
                        index = self.squares.index([self.x, self.y-1])
                        self.squares[index] = [self.x, self.y-2]
                self.levelOne[self.x][self.y] = self.gs
                self.y -= 1
        if side == "right":
            if self.levelOne[self.x][self.y+1] != self.bs and self.levelOne[self.x][self.y+1] != self.sc:
                if self.levelOne[self.x][self.y+1] == self.bbs:
                    if self.levelOne[self.x][self.y+2] == self.sc:
                        self.levelOne[self.x][self.y+2] = self.bs
                        self.squares.remove([self.x, self.y+1])
                        self.crosses.remove([self.x, self.y+2])
                    elif self.levelOne[self.x][self.y+2] != self.bs:
                        self.levelOne[self.x][self.y+2] = self.bbs
                        index = self.squares.index([self.x, self.y+1])
                        self.squares[index] = [self.x, self.y+2]
                self.levelOne[self.x][self.y] = self.gs
                self.y += 1
        
        self.levelOne[self.x][self.y] = self.head

        if self.crosses == []:
            self.level += 1
            self.levelOne[self.x][self.y] = self.gs
            self.x = 1
            self.y = 1
            self.grid()

def run_discord_bot(token):
    TOKEN = token
    start_time = time.time()
    # intents = discord.Intents.default()
    # intents.message_content = True
    # intents.members = True
    # client = discord.Client(intents=intents)
    client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        try:
            synced = await client.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)

        await client.change_presence(status=discord.Status.online,activity=discord.Game('/pomoc'))

        for server in client.guilds:
            channel = discord.utils.get(server.channels, name="123")
            if channel:
                channel_dict[channel.id] = 0
                # await channel.send("Bot byl znovu zapnut, počítání se restartvovalo. Napište `1` abyste začali")

    @client.tree.command(name="ahoj", description="Pozdrav mě")
    async def ahoj(interaction: discord.Interaction):
        await interaction.response.send_message(f'Ahoj `{interaction.user.display_name}`')

    @client.tree.command(name="řekni", description="Co bych měl říct?")
    @app_commands.describe(něco="Co bych měl říct?")
    async def řekni(interaction: discord.Interaction, něco: str):
        await interaction.response.send_message(něco)

    @client.tree.command(name="kostky", description="Náhodné číslo od 1 do 6")
    async def kostky(interaction: discord.Interaction):
        rand = str(random.randint(1, 6))
        if rand == "1":
            await interaction.response.send_message('||_1️⃣_||')
        if rand == "2":
            await interaction.response.send_message('||_2️⃣_||')
        if rand == "3":
            await interaction.response.send_message('||_3️⃣_||')
        if rand == "4":
            await interaction.response.send_message('||_4️⃣_||')
        if rand == "5":
            await interaction.response.send_message('||_5️⃣_||')
        if rand == "6":
            await interaction.response.send_message('||_6️⃣_||')

    @client.tree.command(name="ping", description="Ping Pong")
    async def ping(interaction: discord.Interaction):
        embed = discord.Embed(title=f"Pong", color=65535)
        embed.add_field(name="Čas:", value=f" {round(client.latency*1000)}ms")
        embed.timestamp = datetime.datetime.now()
        await interaction.response.send_message(embed=embed)

    @client.tree.command(name="vtip", description="Řeknu ti vtip")
    async def vtip(interaction: discord.Interaction, language: str, cat: str):
        j = await Jokes()
        joke = await j.get_joke(category=cat, lang=language)
        message = ""
        if joke["type"] == "single":
            message = joke["joke"]
        else:
            message = f'{joke["setup"]} ||{joke["delivery"]}||'
        interaction.response.send_message(message)
    
    @vtip.autocomplete("language")
    async def vtip_autocompletion(
        interaction: discord.Interaction,
        current: str
        ) -> list[app_commands.Choice[str]]:
        data = []
        for lang in ["en", "cs"]:
            if current.lower() in lang.lower():
                data.append(app_commands.Choice(name=lang, value=lang))
        return data
    
    # @vtip.autocomplete("cat")
    # async def vtip_autocompletion2(
    #     interaction: discord.Interaction,
    #     current: str
    #     ) -> list[app_commands.Choice[str]]:
    #     data2 = []
    #     for cat in ["Any", "Misc", "Programming", "Dark", "Pun", "Spooky", "Christmas"]:
    #         if current.lower() in cat.lower():
    #             data2.append(app_commands.Choice(name=cat, value=cat))
    #     return data2
    

    @client.tree.command(name="pomoc", description="Pomůžu ti")
    async def pomoc(interaction: discord.Interaction):
        embed = discord.Embed(title=f"Příkazy", color=65535)
        embed.add_field(name="/ahoj", value="Pozdravím tě")
        embed.add_field(name="/řekni", value="Řeknu vše co budeš chtít")
        embed.add_field(name="/koskty", value="Řeknu ti náhodné číslo od 1 od 6")
        embed.add_field(name="/ping", value="Zjistíš za jak dlouho mi trvá ti odpovědět")
        embed.add_field(name="/vtip", value="Řeknu ti jeden ze 100 vtipů")
        embed.add_field(name="/reddit", value="Vezmu náhody post z redditu, který vybereš")
        embed.add_field(name="/uptime", value="Zjistíš jak dlouho už jsem online")
        embed.add_field(name="/gif", value="Pomocí Giphy API pošlu gif podle názvu v Angličtině")
        embed.add_field(name="/pomoc", value="Pomůžu ti")

        embed.timestamp = datetime.datetime.now()
        
        await interaction.response.send_message(embed=embed)

    @client.tree.command(name="reddit", description="Random post z redditu")
    @app_commands.describe(název="Z jakého subredditu mám vzít post?")
    async def meme(interaction: discord.Interaction, název: str):
        subreddit = reddit.subreddit(název)

        hot_posts = subreddit.hot(limit=50)

        post = random.choice(list(hot_posts))

        title = post.title
        url = post.url

        embed = discord.Embed(title=title, color=65535)
        embed.set_image(url=url)
        embed.timestamp = datetime.datetime.now()


        embed_link = discord.Embed(title="Odkaz:", color=65535, description=f"<https://www.reddit.com{str(post.permalink)}>")
        embed_link.timestamp = datetime.datetime.now()

        await interaction.response.send_message(embed=embed)
        await interaction.followup.send(embed=embed_link)
    
    @client.tree.command(name="gif", description="Gif podle tvého zadání (v Angličtině")
    @app_commands.describe(název="Název? (v Angličtině)")
    async def gif(interaction: discord.Interaction, název: str):

        # Make a request to the Giphy API to search for GIFs
        api_key = giphy_key
        r = requests.get(f'http://api.giphy.com/v1/gifs/search?api_key={api_key}&q={název}')

        # Get the first GIF from the search results
        gif_url = r.json()['data'][random.randint(1, 25)]['images']['original']['url']

        embed = discord.Embed(title=název, color=65535)
        embed.set_image(url=gif_url)
        embed.timestamp = datetime.datetime.now()

        # Send the GIF in the channel
        await interaction.response.send_message(embed=embed)

    @client.tree.command(name="uptime", description="Jak dlouho jsem už online")
    async def uptime(interaction: discord.Interaction):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(color=65535)
        embed.add_field(name="Doba", value=text)
        embed.timestamp = datetime.datetime.now()
        await interaction.response.send_message(embed=embed)
    
    @client.tree.command(name="soko-hra", description="HRA")
    async def soko_hra(interaction: discord.Interaction, emoji: str = "😳"):
        global reactions, games_dict
        embed = discord.Embed(title="SOKO-HRA", color=65535)
        games_dict[interaction.application_id] = Game()
        game = games_dict[interaction.application_id]
        game.head = emoji
        game.grid()
        game.make_string()
        embed.add_field(name=f"Level {game.level}", value=game.square_str)
        button1 = Button(style=discord.ButtonStyle.gray, emoji=game.reactions[0])
        button2 = Button(style=discord.ButtonStyle.gray, emoji=game.reactions[1])
        button3 = Button(style=discord.ButtonStyle.gray, emoji=game.reactions[2])
        button4 = Button(style=discord.ButtonStyle.gray, emoji=game.reactions[3])
        button5 = Button(style=discord.ButtonStyle.gray, emoji=game.reactions[4])
        button6 = Button(style=discord.ButtonStyle.gray, emoji=game.reactions[5])

        async def button1_callback(interaction):
            game.move("up")
            game.make_string()
            embed = discord.Embed(title="SOKO-HRA", color=65535)
            embed.add_field(name=f"Level {game.level}", value=game.square_str)
            await interaction.response.edit_message(content=f"Poslední pohyb: {game.reactions[0]}", embed=embed)
        async def button2_callback(interaction):
            game.move("down")
            game.make_string()
            embed = discord.Embed(title="SOKO-HRA", color=65535)
            embed.add_field(name=f"Level {game.level}", value=game.square_str)
            await interaction.response.edit_message(content=f"Poslední pohyb: {game.reactions[1]}", embed=embed)
        async def button3_callback(interaction):
            game.move("left")
            game.make_string()
            embed = discord.Embed(title="SOKO-HRA", color=65535)
            embed.add_field(name=f"Level {game.level}", value=game.square_str)
            await interaction.response.edit_message(content=f"Poslední pohyb: {game.reactions[2]}", embed=embed)
        async def button4_callback(interaction):
            game.move("right")
            game.make_string()
            embed = discord.Embed(title="SOKO-HRA", color=65535)
            embed.add_field(name=f"Level {game.level}", value=game.square_str)
            await interaction.response.edit_message(content=f"Poslední pohyb: {game.reactions[3]}", embed=embed)
        async def button5_callback(interaction):
            embed = discord.Embed(title="SOKO-HRA", color=65535)
            game.reset()
            game.make_string()
            embed.add_field(name=f"Level {game.level}", value=game.square_str)
            await interaction.response.edit_message(embed=embed)
        async def button6_callback(interaction):
            embed = discord.Embed(title="SOKO-HRA", color=65535)
            embed.add_field(name="KONEC HRY", value=f"Hra byla ukončena na levelu {game.level}")
            await interaction.response.edit_message(embed=embed)
        
        button1.callback = button1_callback
        button2.callback = button2_callback
        button3.callback = button3_callback
        button4.callback = button4_callback
        button5.callback = button5_callback
        button6.callback = button6_callback

        view = View()
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)
        view.add_item(button5)
        view.add_item(button6)

        if game.level == 8:
            embed = discord.Embed(title="GAME-TEST", color=65535)
            embed.add_field(name="KONEC HRY", value=f"Vyhrál si")    

        await interaction.response.send_message(embed=embed, view=view)

    @client.tree.command(name="soko-help", description="Informace o hře jménem Soko")
    async def soko_help(interaction: discord.Interaction):
        embed = discord.Embed(title=f"SOKO-HELP", color=65535)
        embed.add_field(name="**Ovládání:**", value="⬆️ NAHORU\n\n ⬇️ DOLU \n\n ⬅️ DOLEVA \n\n ➡️ DOPRAVA \n\n 🔄 RESTART \n\n ❌ KONEC")

        embed.add_field(name="**Cíl:**", value="Posouvej oranžové čtverce na zelené křížky")

        embed.timestamp = datetime.datetime.now()
        
        await interaction.response.send_message(embed=embed)

    @client.tree.command(name="ඞ")
    async def funny(interaction: discord.Interaction, str: str):
        str = str.split("$")
        id = str[0]
        num = str[1]
        message = str[2]
        if interaction.user.id != 602833928705015818:
            await interaction.response.send_message("NE", delete_after=.01)
        else:
            for _ in range(0, int(num)):
                user = await client.fetch_user(id)
                await user.send(message, delete_after=1.00)
            commander = await client.fetch_user(interaction.user.id)
            await commander.send("🗿__**HOTOVO**__🗿", delete_after=3.00)       

    @client.event
    async def on_message(message):
        global number, reactions

        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")
        if message.channel.id in channel_dict:
            if str(message.content).isnumeric():
                if str(message.content) == str(channel_dict[message.channel.id] + 1):
                    await message.add_reaction("✅")
                    channel_dict[message.channel.id] += 1
                else:
                    await message.add_reaction("❌")
                    channel_dict[message.channel.id] = 0
                    await message.channel.send(f"`{username}` to pokazil, počítání se resetovalo. Napište `1` abyste začali")
            else:
                await message.add_reaction("🇳")
                await message.add_reaction("🇪")
                await message.channel.purge(limit=1)

    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)