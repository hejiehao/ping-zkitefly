import logging
from khl import Bot, Message, Cert, MessageTypes
from utils.open_json import *

logging.basicConfig(level='INFO')

# 初始化机器人
# 打开config.json
config = open_json('./config/config.json')
bot = Bot(token=config['token'])  # 默认采用 websocket
"""main bot"""
if not config['using_ws']:  # webhook
    # 当配置文件中'using_ws'键值为false时，代表不使用websocket
    # 此时采用webhook方式初始化机器人
    print(f"[BOT] using webhook at port {config['webhook_port']}")
    bot = Bot(cert=Cert(token=config['token'],
                        verify_token=config['verify_token'],
                        encrypt_key=config['encrypt_token']),
              port=config['webhook_port'])

@bot.command(name='ping_zkitefly')
async def world(msg: Message):
    for i in range(10):
    #while True:
        await msg.ctx.channel.send('(met)1750602971(met)'*5) #ping zkitefly

@bot.command(name='ping_pomelopig')
async def world(msg: Message):
    for i in range(10):
        #while True:
        await msg.ctx.channel.send('(met)2085267025(met)'*5) #ping Pomelopig

@bot.command(name='ping_all')
async def world(msg: Message):
    for i in range(10):
        #while True:
        await msg.ctx.channel.send('(met)all(met)'*5) #ping所有人

@bot.command(name='ping_here')
async def world(msg: Message):
    for i in range(10):
        #while True:
        await msg.ctx.channel.send('(met)here(met)'*5) #ping在线成员

about = [
    {
        "type": "card",
        "theme": "info",
        "size": "lg",
        "modules": [
            {
                "type": "section",
                "text": {
                    "type": "kmarkdown",
                    "content": "一个可以ping爆zkitefly的bot\n仓库地址：[https://github.com/hejiehao/ping-zkitefly](https://github.com/hejiehao/ping-zkitefly)"
                },
                "mode": "left",
                "accessory": {
                    "type": "image",
                    "src": "https://img.kookapp.cn/assets/2023-09/6hnT8Fq71W03k03k.png",
                    "size": "sm"
                }
            }
        ]
    }
]

@bot.command(name='about')
async def world(msg: Message):
    await msg.reply(about,type=MessageTypes.CARD)

help = [
    {
        "type": "card",
        "theme": "info",
        "size": "lg",
        "modules": [
            {
                "type": "section",
                "text": {
                    "type": "kmarkdown",
                    "content": "`/help`：显示用法\n`/about`：关于\n`/ping_zkitefly`：ping爆zkitefly。\n`/ping_pomelopig`：ping爆pomelopig。\n`/ping_all`：ping爆所有人\n`/ping_here`：ping爆在线成员"
                },
                "mode": "right",
                "accessory": {
                    "type": "image",
                    "src": "https://img.kookapp.cn/assets/2023-09/6hnT8Fq71W03k03k.png",
                    "size": "lg"
                }
            }
        ]
    }
]

@bot.command(name='help')
async def world(msg: Message):
    await msg.reply(help,type=MessageTypes.CARD)

bot.run()