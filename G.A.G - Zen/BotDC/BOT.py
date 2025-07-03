import discord
import subprocess

TOKEN = 'MTM5MDE1ODQxNTY5MDcyNzU1NQ.GctVCZ.hGw784DXgVJQeHKrO5-dTeuifTk1181i87I0oM'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == "!rejoin":
        await message.channel.send("Rejoining the VIP server...")
        subprocess.Popen([r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\AutoHotkey64.exe", r"C:\Users\33616\Desktop\G.A.G\AHK\RejoinGAG.ahk"])

    if message.content == "!screenshot":
        await message.channel.send("Screenshot ...")
        subprocess.Popen([r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\AutoHotkey64.exe", r"C:\Users\33616\Desktop\G.A.G\AHK\ScreenDiscordWebhook.ahk"])

    if message.content == "!ss":
        await message.channel.send("Screenshot ...")
        subprocess.Popen([r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\AutoHotkey64.exe", r"C:\Users\33616\Desktop\G.A.G\AHK\ScreenDiscordWebhook.ahk"])

    if message.content.startswith("!write"):
        text_to_type = message.content[len("!write"):].strip() 
        if not text_to_type:
            await message.channel.send("Write a message")
            return

        subprocess.Popen([r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\AutoHotkey64.exe", r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\TypeMessage.ahk", text_to_type])
        await asyncio.sleep(2)
        subprocess.Popen([r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\AutoHotkey64.exe", r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\ScreenDiscordWebhook.ahk"])

    if message.content == "! ss":
        await message.channel.send("Screenshot ...")
        subprocess.Popen([r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\AutoHotkey64.exe", r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\ScreenDiscordWebhook.ahk"])

    if message.content == "!wrench":
        await message.channel.send("Wrench slot 2...")
        subprocess.Popen([r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\AutoHotkey64.exe", r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\Wrench.ahk"])
        
    if message.content == "!roblox":
        await message.channel.send("Opening Roblox...")
        subprocess.Popen([r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\AutoHotkey64.exe", r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\RobloxWindow.ahk"])

    if message.content == "!inv":
        await message.channel.send("Inventory...")
        subprocess.Popen([r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\AutoHotkey64.exe", r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\Inventory.ahk"])

    if message.content == "!cos":
        await message.channel.send("Stoping...")
        subprocess.Popen([r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\AutoHotkey64.exe", r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\Cosmetics.ahk"])

    if message.content == "!f4":
        await message.channel.send("Stoping the autoclick...")
        subprocess.Popen([r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\AutoHotkey64.exe", r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\F4.ahk"])

    if message.content == "!fs":
        await message.channel.send("Windows Full Screen")
        subprocess.Popen([r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\AutoHotkey64.exe", r"C:\Users\33616\Desktop\G.A.G - Zen\AHK\FullScreen.ahk"])

client.run(TOKEN)