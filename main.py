import os
from khl import Bot, Message, Cert
from utils.open_json import *
import logging.handlers

if os.path.exists("./ping.log"):
    os.remove("./ping.log")

logger = logging.getLogger('khl')
logging.basicConfig(level='INFO')

handler = logging.handlers.RotatingFileHandler(
    filename='ping.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

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
async def zkitefly(msg: Message):
    for i in range(10):
    #while True:
        await msg.ctx.channel.send('(met)1750602971(met)'*5) #ping zkitefly

@bot.command(name='ping_pomelopig')
async def pomelopig(msg: Message):
    for i in range(10):
        #while True:
        await msg.ctx.channel.send('(met)2085267025(met)'*5) #ping Pomelopig

@bot.command(name='ping_all')
async def all(msg: Message):
    for i in range(10):
        #while True:
        await msg.ctx.channel.send('(met)all(met)'*5) #ping所有人

@bot.command(name='ping_here')
async def here(msg: Message):
    for i in range(10):
        #while True:
        await msg.ctx.channel.send('(met)here(met)'*5) #ping在线成员

@bot.command(name='about')
async def about(msg: Message):
    about = open_json("./about.json")
    await msg.reply([about])

@bot.command(name='help')
async def help(msg: Message):
    help = open_json("./help.json")
    await msg.reply([help])

bot.run()