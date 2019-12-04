import discord  
import os  

client = discord.Client()  
TOKEN = os.environ['DISCORD_BOT_TOKEN']  
ID_CHANNEL_QUESTION = # 質問チャンネルID  
ID_CATEGORY_QA = # 質問スレカテゴリID  


@client.event  
async def on_message(message):  
    if message.channel.id == ID_CHANNEL_QUESTION:  
        await qa_thread(message)  


async def qa_thread(message):  
    category_qa = client.get_channel(ID_CATEGORY_QA)  
    channel_name = f'q{len(category_qa.text_channels)}'  
    payload = {'name': channel_name, 'category': category_qa, 'position': 0}  
    channel_qa = await message.guild.create_text_channel(**payload)  
    await channel_qa.send(message.jump_url)  
    await client.get_channel(ID_CHANNEL_QUESTION).edit(position=0)  


client.run(TOKEN)  
