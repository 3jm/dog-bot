import discord
import requests
from discord.ext import commands

# setup our bot
bot = commands.Bot(command_prefix='!')

# create a on ready event to tell me when the bot is online
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# create a embed that gets random images of dogs from a api and sets the image url to the picture of the dog
@bot.command()
async def dog(ctx):
    url = "https://dog.ceo/api/breeds/image/random"
    r = requests.get(url)
    data = r.json()
    embed = discord.Embed(title="Here is your dog!", color=0x00ff00)
    embed.set_image(url=data["message"])
    await ctx.send(embed=embed)

# create a command not found error handler that mentions the user that the command was not found
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"{ctx.author.mention}, Command does not exist / typed incorrectly")
    # create another error handler that if a arguement is missing it will tell the user to use the command correctly
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"{ctx.author.mention}, Missing required argument")

@bot.command()
async def about(ctx):
    # create a embed
    embed = discord.Embed(description="dog was created with github copilot! There may be some flaws as copilot was trained on a older version of discord py. Please let the developer know by doing the `!report (your report)` command.", color=0x00ff00)
    # set the author icon url to the bot icon and the author name to the bot name
    embed.set_author(name="dog#4389", icon_url=bot.user.avatar_url)
    # get a list of commands and set it as the first field
    embed.add_field(name="Commands", value="`!dog` - returns a random dog picture\n`!about` - returns the about section of the bot")
    # send the embed
    await ctx.send(embed=embed)

# login to our bot
bot.run('OTU2NTE3ODQzOTI5ODIxMTk1.YjxYqQ.JVgamx2iuOzkISMUAmokgYIHy5Y')