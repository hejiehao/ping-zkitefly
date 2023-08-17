import json
from khl import Bot, Message, Cert

def open_file(path: str):
    """打开path对应的json文件"""
    with open(path, 'r', encoding='utf-8') as f:
        tmp = json.load(f)
    return tmp

# 打开config.json
config = open_file('./config/config.json')

# 初始化机器人
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
        await msg.ctx.channel.send('(met)1750602971(met)') #ping zkitefly

@bot.command(name='ping_all')
async def world(msg: Message):
    for i in range(10):
        #while True:
        await msg.ctx.channel.send('(met)all(met)') #ping所有人

@bot.command(name='ping_here')
async def world(msg: Message):
    for i in range(10):
        #while True:
        await msg.ctx.channel.send('(met)here(met)') #ping在线成员

@bot.command(name='about')
async def world(msg: Message):
    await msg.reply('一个可以ping爆zkitefly的bot\n仓库地址：[https://github.com/hejiehao/ping-zkitefly](https://github.com/hejiehao/ping-zkitefly)')

@bot.command(name='help')
async def world(msg: Message):
    await msg.reply('`/help`：显示用法\n`/about`：关于\n`/ping_zkitefly`：ping爆zkitefly。\n`/ping_all`：ping爆所有人\n`/ping_here`：ping爆在线成员')

bot.run()