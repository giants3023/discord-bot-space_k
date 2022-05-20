from email import message
from http import client
from pydoc import cli
from re import I
from sqlite3 import Timestamp
from turtle import Turtle, title
import discord
import os
token = "access_token"
client = discord.Client()

@client.event
async def on_ready():
    print("봇 준비 완료!")
    print(client.user)
    print("============================")

@client.event
async def on_message(message):
    if message.content == "!스페이스 봇":
        await message.channel.send("안녕하십니까 저는 Space_k 봇입니다^^")
    
    if message.content == "!마약 가격":
        embed = discord.Embed(Timestamp=message.created_at, colour=discord.Colour.green(), title="포리의 마약가게 가격표")
        embed.add_field(name="1.대마초", value="한 갑당 가격:20,000원", inline=False)
        embed.add_field(name="2.코카인", value="20g당 가격:40,000원", inline=False)
        embed.add_field(name="3.필로폰", value="20g당 가격:30,000원", inline=False)
        embed.add_field(name="4.프로포폴", value="한 팩당 가격:100,000원", inline=False)
        embed.add_field(name="5.LSD", value="20g당 가격:250,000원", inline=False)
        await message.channel.send(embed=embed)

    if message.content == "!포리의 마약가게":
        embed = discord.Embed(Timestamp=message.created_at, colour=discord.Colour.green(), title="마약가게 정보")
        embed.set_image(url="https://cdn.discordapp.com/attachments/819856449068990524/976798798313586748/20220519_194933.jpg")
        embed.add_field(name="사장", value="포리", inline=True)
        embed.add_field(name="직원", value="핑삼,흐어어어", inline=True)
        embed.add_field(name="마약 종류", value="5가지", inline=True)
        embed.add_field(name="적자", value="50,000,000원", inline=True)
        embed.add_field(name="개점일", value="2022년 5월 16일", inline=True)
        await message.channel.send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(token)
