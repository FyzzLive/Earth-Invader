#!/usr/bin/python
# New Rot47 cipher for the the codex project
# created by : C0SM0 | Fyzz
import discord
from discord.ext import commands

class r13(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(__file__, ' Online')

    @commands.command()
    async def r13(self, ctx, action, *, text):

        # encode r13
        if action == "encode" or action == "e":
            output = ''
            key = 13
            exclude = "\n\t .?!,/\\<>|[]{}@#$%^&*()-_=+`~:;\"'0123456789"

            # encryption process
            if text and key:
                for character in text:
                    if character in exclude:
                        output += character
                    elif character.isupper():
                        output += chr((ord(character) + int(key) - 65) % 26 + 65)
                    else:
                        output += chr((ord(character) + int(key) - 97) % 26 + 97)
            await ctx.send(output)
            return [output, True]


        # decode r13
        if action == "decode" or action == "d":
            output = ''
            key = 13
            exclude = "\n\t .?!,/\\<>|[]{}@#$%^&*()-_=+`~:;\"'0123456789"

            # decryption process
            if text and key:
                for character in text:
                    if character in exclude:
                        output += character
                    elif character.isupper():
                        output += chr((ord(character) - int(key) - 65) % 26 + 65)
                    else:
                        output += chr((ord(character) - int(key) - 97) % 26 + 97)

            await ctx.send(output)
            return [output, True]

    @r13.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="SYNTAX ERROR", color=0xFE060A)
            embed.add_field(name="Syntax:",
                            value="`*r13 {encode/decode} {your text}`",
                            inline=False)
            embed.add_field(name="Example 1 - Encode longway:",
                            value="`*r13 encode some text`", inline=False)
            embed.add_field(name="Example 2 - Decode shortway:",
                            value="`*r13 d fbzr grkg`", )
            await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(r13(client))