import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Moderation Commands

    #Clear command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)

    #ban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason = reason)
        await ctx.send(f'***Swings ban hammer with superiority***{member.mention}')

    #unban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name , member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'***Unbanned*** {user.mention}')
                return

    #kick command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user:discord.Member, *, reason = None):
    	if not reason:
    		await user.kick()
    		await ctx.send(f'**{user}** has been kicked for **no reason**.')
    	else:
    		await user.kick(reason=reason)
    		await ctx.send(f'**{user} has been kicked for **{reason}**.')


    #error throws
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please provide Discord name and discriminator.')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please provide Discord name and discriminator.')

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please provide Discord name and discriminator.')



def setup(client):
    client.add_cog(Moderation(client))
