# bot.py

import os
import datetime
import time
from discord.channel import CategoryChannel
import board_list
import discord
from discord.ext import commands
import chan 

intents = discord.Intents.default()
intents.members = True

TOKEN = os.getenv('DISCORD_TOKEN')
color_embed = 0x7CFC00

bot = commands.Bot(intents=intents, command_prefix='_', help_command=None)

@bot.command()
async def help(ctx,*args):
    if len(args)==0:
        embed = discord.Embed(
            title='Help Command',
            color=color_embed,
            description=""" The default prefix is ``_``

                            ``_say``: To make the bot repeat your words
                            ``_img``: To get some images from 4chan
                            For more help on these, use '_help <the command name>'
                        """
            )
        embed.set_footer(text='made by AverageHedonismEnjoyer#3979')
        await ctx.send(embed=embed)
    else:
        if args[0]=='img':
            embed = discord.Embed(
            title='Help for Image Command',
            color=color_embed,
            description=""" This command brings up random images from a specified 4chan board

                            Use the format '_img <board code> <number of images>'
                            The <number of images> is optional, will provide 5 images if not specified
                            To get a list of topics of boards, use 'topics'
                            For more help on board codes, use the help command for 'boards'
                        """
            )
            await ctx.send(embed=embed)
        elif args[0]=='say':
            embed = discord.Embed(description='_say <whatever you want the bot to repeat>',color=color_embed)
            await ctx.send(embed=embed)
        elif args[0]=='topics':
            embed = discord.Embed(description='This command is used to get a list of board types available on 4chan',color=color_embed)
            await ctx.send(embed=embed)
        elif args[0]=='boards':
            embed = discord.Embed(
                description="""
                                This command is used to get a list of boards according to the specified code
                                Usage: _boards <Topic number>
                            """,
                color=color_embed)
            embed.set_footer('To get more info on topics, use \'_topics\'')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description='No such command exists!!',color=color_embed)
            await ctx.send(embed=embed)

@bot.command()
async def topics(ctx):
    topics = board_list.topics_list()
    topics_list = '\n'
    topics_list = topics_list.join(topics)
    embed = discord.Embed(
            title='List of Topics',
            color=color_embed,
            description= topics_list,
            )
    embed.set_footer(text='For the list of boards on a Topic, type \'_boards <Topic Number>\'')
    await ctx.send(embed=embed)

@bot.command()
async def boards(ctx, *args):
    if len(args)==0:    
        embed = discord.Embed(
                color=color_embed,
                description= 'Wrong usage of the command!! Check the help command for boards'
                )
        await ctx.send(embed=embed)
    else:
        if int(args[0])>0 and int(args[0])<8:
            if int(args[0])==6 or int(args[0])==7:
                color_embed2 = 0xFF0000
            else:
                color_embed2 = color_embed
            board = open('boards.txt','r')
            lines = board.readlines()
            index = board_list.index(int(args[0]))
            start = int(index[0])+1
            end = int(index[1])
            title = lines[index[0]-1]
            description = " "
            for i in range(start, end):
                description+=lines[i][:-1]+'\n'
            embed = discord.Embed(
                    title=title,
                    color=color_embed2,
                    description= description,
                    )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description='Invalid Board Number!!',color=color_embed)
            await ctx.send(embed = embed)


@bot.command()
async def img(ctx,*arg):
    '''
        To get images from 4chan boards using the Board's code
        To get a list of 4chan Boards along with their code, type _boards
    '''

    if len(arg)<1 or len(arg)>2:
        embed = discord.Embed(description='Wrong number of arguments!!',color=color_embed)
        await ctx.send(embed=embed)

    list_ = board_list.code_list()

    if arg[0] in list_:
        if len(arg)==2:
            try: 
                num = int(arg[1])
            except ValueError: 
                embed = discord.Embed(description='The entered character is not a number!!',color=color_embed)
                await ctx.send(embed=embed)
            if arg[0] in board_list.nsfw_code_list():
                if ctx.channel.is_nsfw()==False:
                    await ctx.send('Enable NSFW settings for the channel!!')
                    return
                else:
                    color_embed2 = 0xFF0000
            else:
                color_embed2 = color_embed
            material = chan.chan_images(arg[0],num)
            img_url_list = material[0]
            text_list = material[1]
            name = chan.board_name(arg[0])
            print(f'Board: {name} requested by {ctx.message.author.name} at {datetime.datetime.now().time()}')
            print(f'{num} images sent on channel: {ctx.message.channel.name} in Server: {ctx.message.guild.name}')
            for count,url in enumerate(img_url_list):
                if count==0:
                    embed = discord.Embed(title=name,color=color_embed2)
                else:
                    embed = discord.Embed(color=color_embed2)
                embed.set_footer(text=text_list[count])
                embed.set_image(url=url)
                await ctx.send(embed=embed)
        else:
            if arg[0] in board_list.nsfw_code_list():
                if ctx.channel.is_nsfw()==False:
                    await ctx.send('Enable NSFW settings for the channel!!')
                    return
                else:
                    color_embed2 = 0xFF0000
            else:
                color_embed2 = color_embed
            material = chan.chan_images(arg[0])
            img_url_list = material[0]
            text_list = material[1]
            name = chan.board_name(arg[0])
            print(f'Board:{name} requested by {ctx.message.author.name} at {datetime.datetime.now().time()}')
            print(f'5 images sent on channel: {ctx.message.channel.name} in Server: {ctx.message.guild.name}')
            for count,url in enumerate(img_url_list):
                if count==0:
                    embed = discord.Embed(title=name,color=color_embed2)
                else:
                    embed = discord.Embed(color=color_embed2)
                embed.set_footer(text=text_list[count])
                embed.set_image(url=url)
                await ctx.send(embed=embed)
            
    else:
        embed = discord.Embed(description='No such Board exists!!',color=color_embed)
        await ctx.send(embed=embed)

@bot.command()
async def embed(ctx):
    embed = discord.Embed(title='Alabama Jerry', color=color_embed)
    embed.set_image(url='https://cdn.discordapp.com/emojis/808640257015939083.png?v=1')
    await ctx.send(embed=embed)

@bot.command()
async def hi(ctx):
    await ctx.send('Helloo!')

@bot.command()
async def spam(ctx,text,num):
    if(ctx.message.author.id==784811914005315625):
        for i in range(int(num)):
            await ctx.send(text)
            time.sleep(0.1)
    else:
        await ctx.send('Nice try. But it\'ll only work for the bot author :)')

@bot.command()
async def say(ctx, *arg):
    '''
        Just repeats what you said :)
        Use it as _say <your text>
    '''
    sent  = " "
    if len(arg)==0:
        embed = discord.Embed(description='Provide the words to be repeated!!',color=color_embed)
        await ctx.send(embed = embed)
    for str in arg:
        sent+= str + " "
    if '@everyone' in sent or '@here' in sent:
        await ctx.send('Mass mentions are not allowed!!')
        return
    await ctx.send(sent) 

bot.run(TOKEN)
