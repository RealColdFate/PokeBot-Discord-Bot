import pType as pokemonType
import commandDescriptionParser as CDP
import pokemonObjectList as POL
from discord.ext import commands
import secret

client = commands.Bot(command_prefix='!')
command_descriptions = CDP.command_dict()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
    print(f'{member} has joined the sever')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 100)}ms")


@client.command()
async def type(ctx, *, list_of_types):
    command_out = pokemonType.run(list_of_types)
    if command_out is None:
        command_out = "Invalid input"
    await ctx.send(command_out)


@client.command()
async def mon(ctx, *, mon):
    mon = mon.lower()
    if mon in POL.MON_DICT:
        await ctx.send(POL.MON_DICT[mon.strip()].string_summary())
    else:
        await ctx.send("Invalid Mon")


client.run(secret.TOKEN)
