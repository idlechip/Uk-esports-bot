import discord
from discord.ext import commands

class Games(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    #8ball command
    @commands.command(aliases=['8ball','magic8ball'])
    async def _8ball(self, ctx, *, question):
        response = ['It is certain.',
                    'It is decidedly so.',
                    'Without a doubt.',
                    'Yes - definitely.',
                    'You may rely on it.',
                    'As I see it, yes.',
                    'Most likely.',
                    'Outlook good.',
                    'Yes.',
                    'Signs point to yes.',
                    'Reply hazy, try again.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    'Dont count on it.',
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Very doubtful.']

        await ctx.send(f'Question: {question}\nAnswer: {random.choice(response)}')


    #error throws
    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please provide a question.')


def setup(client):
    client.add_cog(Games(client))
