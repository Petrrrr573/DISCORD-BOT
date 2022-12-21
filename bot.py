import discord
import responses
from discord.ext import commands
from discord import app_commands
import random
number = 0

# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message, str(message.author))
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    number = 0
    TOKEN = 'MTA1MzU4MzAzMzcwMzM1MDM1Mg.GS5m1F.JeEXsel5kGZGOVpamoySPXOlPV4iBfVXYvTR80'
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

    @client.tree.command(name="ahoj", description="Pozdrav mě")
    async def ahoj(interaction: discord.Interaction):
        await interaction.response.send_message(f'Ahoj `{interaction.user.display_name}`')

    @client.tree.command(name="řekni", description="Co bych měl říct?")
    @app_commands.describe(něco="Co bych měl říct?")
    async def řekni(interaction: discord.Interaction, něco: str):
        await interaction.response.send_message(f'`{interaction.user.display_name}` řekl: {něco}')

    @client.tree.command(name="kostky", description="Náhodné číslo od 1 do 6")
    async def kostky(interaction: discord.Interaction):
        rand = str(random.randint(1, 6))
        if rand == "1":
            await interaction.response.send_message('_1️⃣_')
        if rand == "2":
            await interaction.response.send_message('_2️⃣_')
        if rand == "3":
            await interaction.response.send_message('_3️⃣_')
        if rand == "4":
            await interaction.response.send_message('_4️⃣_')
        if rand == "5":
            await interaction.response.send_message('_5️⃣_')
        if rand == "6":
            await interaction.response.send_message('_6️⃣_')

    @client.tree.command(name="ping", description="Ping Pong")
    async def ping(interaction: discord.Interaction):
        embed = discord.Embed(title=f"Pong", color=65535)
        embed.add_field(name=f"Time: {round(client.latency*1000)}ms", value='\a')
        await interaction.response.send_message(embed=embed)

    @client.event
    async def on_message(message):
        global number
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        if channel == "123":
            if str(message.content).isnumeric():
                if str(message.content) == str(number + 1):
                    await message.add_reaction("✅")
                    number += 1
                else:
                    await message.add_reaction("❌")
                    number = 0
                    await message.channel.send(f"`{username}` to pojebal, protože neumí počítat")
            else:
                if username == "Petrrrrr#1030":
                    await message.add_reaction("🇳")
                    await message.add_reaction("🇪")
                await message.channel.purge(limit=1)



        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[0] == "?":
            user_message = user_message[1:]  # [1:] Removes the '?'
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)