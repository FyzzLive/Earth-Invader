#!/usr/bin/python
# New Rot47 cipher for the the codex project
# created by : Fyzz
import discord
from discord.ext import commands

class r47(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(__file__, ' Online')

    @commands.command()
    async def r47(self, ctx, action, *, text):

        # encode r47
        if action == "encode" or action == "e":
            output = ''

            for index in text:
                encoded = ord(index)
                if encoded >= 33 and encoded <= 126:
                    output += chr(33 + ((encoded + 14) % 94))
                else:
                    output += index
            await ctx.send(output)
            return [output, True]


        # decode r47
        if action == "decode" or action == "d":
            output = ''

            for index in text:
                encoded = ord(index)
                if encoded >= 33 and encoded <= 126:
                    output += chr(33 + ((encoded + 14) % 94))
                else:
                    output += index
            await ctx.send(output)
            return [output, True]

    @r47.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="SYNTAX ERROR", color=0xFE060A)
            embed.add_field(name="Syntax:",
                            value="`*r47 {encode/decode} {your text}`",
                            inline=False)
            embed.add_field(name="Example 1 - Encode longway:",
                            value="`*r47 encode some text`", inline=False)
            embed.add_field(name="Example 2 - Decode shortway:",
                            value="`*r47 d D@>6 E6IE`", )
            await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(r47(client))