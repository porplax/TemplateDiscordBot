# MODULES ===========================================================

# Discord-related modules.
import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions

# Custom modules.
from utils.read_toml import get_key

# VARIABLES =========================================================
resource = get_key('script', 'resource')
prefix = get_key('bot', 'prefix')
token = get_key('developer', 'token')

intents = discord.Intents.all()  # Enables all intents. In order to work, we need to turn on the intents in developers hub.
client = commands.Bot(command_prefix=prefix, intents=intents)  # TODO: Add command prefix.

# EVENTS ============================================================
@client.event
async def on_ready():
    # Executes when the bot is ready.
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    pass

# COMMANDS ==========================================================
"""
(Category moderation)
KICK : BAN : MUTE
"""

# Kicks a discord member from the current guild.
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    return await ctx.send(f"Successfully kicked {member} from the guild.")


# Error if user does not meet permissions for ban.
@kick.error
async def kick_err(ctx, error):
    if isinstance(error, MissingPermissions):
        return await ctx.send("You don't have the required permissions for kick!")


# Bans a discord member from the current guild.
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
    await member.ban()
    return await ctx.send(f"Sucessfully banned {member} from the guild.")


# Error if user does not meet permissions for ban.
@ban.error
async def ban_err(ctx, error):
    if isinstance(error, MissingPermissions):
        return await ctx.send("You don't have the required permissions for ban!")


# Temporary mutes a discord member in the current guild. (With the appropriate role ofc.)
@client.command()
@commands.has_permissions(mute_members=True)
async def mute(ctx, member: discord.Member, role: discord.Role):
    if role in member.roles:
        await member.remove_roles(role)
        return await ctx.send(f"Unmuted {member} from the guild!")
    else:
        await member.add_roles(role)
        return await ctx.send(f"Muted {member} from the guild!")


# Error if user does not meet permissions for ban.
@mute.error
async def mute_err(ctx, error):
    if isinstance(error, MissingPermissions):
        return await ctx.send("You don't have the required permissions for mute!")

# ====================================================================
client.run(token)
