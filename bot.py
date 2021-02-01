#!/usr/bin/python3
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from wallstreet import Stock
from telegram.ext import CommandHandler
import logging
import os, stat
import time

#Format number
def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

updater = Updater(token='<TOKEN do BOT>', use_context=True)

dispatcher = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
updater.start_polling()

# Caps
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)
# Stock
def stockreturn(update, context):
    s = Stock(context.args[0])
    texto = "<b>" + s.ticker + "</b>: " + str(s.price) + "\r\n<b>Variação: </b>" + human_format(s.change) + " (" + human_format(s.cp) + "%)"
    context.bot.send_message(chat_id=update.effective_chat.id, text=texto, parse_mode='HTML')

stock_handler = CommandHandler('stock', stockreturn)
dispatcher.add_handler(stock_handler)

# Dolar
def dolarreturn(update, context):
    s = Stock('USDBRL=X')
    texto = "<b>Dolar agora:</b> " + str(s.price) + "\r\n<b>Variação: </b>" + human_format(s.change) + " (" + human_format(s.cp) + "%)"
    context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://br.advfn.com/p.php?pid=staticchart&s=FX^USDBRL&t=0&p=0&width=300&height=200&t=24&time='+str(int(time.time())), caption=texto, parse_mode='HTML')
    #context.bot.send_message(chat_id=update.effective_chat.id, text=texto, parse_mode='HTML')
    #context.bot.send_message(chat_id=update.effective_chat.id, text="Comentários do Willian abaixo:", parse_mode='HTML')

dolar_handler = CommandHandler('dolar', dolarreturn)
dispatcher.add_handler(dolar_handler)

#bitcoin
def bitcoinreturn(update, context):
    s = Stock('BTCUSD=X')
    texto = "<b>Bitcoin agora:</b> " + str(s.price) + "\r\n<b>Variação: </b>" + human_format(s.change) + " (" + human_format(s.cp) + "%)"
    context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://br.advfn.com/p.php?pid=staticchart&s=COIN%5EBTCUSD&t=0&p=0&width=300&height=200&t=24&time='+str(int(time.time())), caption=texto, parse_mode='HTML')
    #context.bot.send_message(chat_id=update.effective_chat.id, text=texto, parse_mode='HTML')

bitcoin_handler = CommandHandler('bitcoin', bitcoinreturn)
dispatcher.add_handler(bitcoin_handler)
# IBOV
def ibovreturn(update, context):
    s = Stock('^BVSP')
    texto = "<b>IBOV agora:</b> " + human_format(s.price) + "\r\n<b>Variação: </b>" + human_format(s.change) + " (" + human_format(s.cp) + "%)"
    context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://br.advfn.com/p.php?pid=staticchart&s=IBOV&t=0&p=0&width=300&height=200&t=24&time='+str(int(time.time())), caption=texto, parse_mode='HTML')
    #context.bot.send_message(chat_id=update.effective_chat.id, text=texto, parse_mode='HTML')

ibov_handler = CommandHandler('ibov', ibovreturn)
dispatcher.add_handler(ibov_handler)

# VIX
def vixreturn(update, context):
    s = Stock('^VIX')
    texto = "<b>VIX agora:</b> " + human_format(s.price) + "\r\n<b>Variação: </b>" + human_format(s.change) + " (" + human_format(s.cp) + "%)"
    context.bot.send_message(chat_id=update.effective_chat.id, text=texto, parse_mode='HTML')

vix_handler = CommandHandler('vix', vixreturn)
dispatcher.add_handler(vix_handler)

# SP500
def sp500return(update, context):
    s = Stock('^GSPC')
    texto = "<b>SP500 agora:</b> " + human_format(s.price) + "\r\n<b>Variação: </b>" + human_format(s.change) + " (" + human_format(s.cp) + "%)"
    context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://br.advfn.com/p.php?pid=staticchart&s=SPI%5ESP500&t=0&p=0&width=300&height=200&t=24&time='+str(int(time.time())), caption=texto, parse_mode='HTML')
    #context.bot.send_message(chat_id=update.effective_chat.id, text=texto, parse_mode='HTML')

sp500_handler = CommandHandler('sp500', sp500return)
dispatcher.add_handler(sp500_handler)

# NASDAQ
def nasdaqreturn(update, context):
    s = Stock('^IXIC')
    texto = "<b>NASDAQ agora:</b> " + human_format(s.price) + "\r\n<b>Variação: </b>" + human_format(s.change) + " (" + human_format(s.cp) + "%)"
    context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://br.advfn.com/p.php?pid=staticchart&s=NI%5EI%5CCOMP&t=0&p=0&width=300&height=200&t=24&time='+str(int(time.time())), caption=texto, parse_mode='HTML')
    #context.bot.send_message(chat_id=update.effective_chat.id, text=texto, parse_mode='HTML')

nasdaq_handler = CommandHandler('nasdaq', nasdaqreturn)
dispatcher.add_handler(nasdaq_handler)

# unknown
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

# FOTO

def foto(context):
    directory = '/home/stefan/mariana_piimentel/'
    chat_id= -434688882
    for filename in os.listdir(directory):
#        logging.info(os.path.join(directory, filename))
        if filename.endswith(".jpg"):
            context.bot.send_photo(chat_id, photo=open(os.path.join(directory, filename), 'rb'))
            os.remove(os.path.join(directory, filename))
            continue
        if filename.endswith(".mp4"):
            context.bot.send_photo(chat_id, photo=open(os.path.join(directory, filename), 'rb'))
            context.bot.send_video(chat_id, video=open(os.path.join(directory, filename), 'rb'), supports_streaming=True)
            os.remove(os.path.join(directory, filename))

 #   send_photo(chat_id, photo=open('path', 'rb'))
 #   context.bot.send_message(chat_id=-434688882, text='PlEaSe wOrK!')

def podcast(context):
    #Onde ficam os arquivos mp3
    directory = '/home/bot/podcast/'
    #chat_id= -434688882 Desonesto
    #Grupo que estou mandando o podcast
    chat_id= -371259633
    for filename in os.listdir(directory):
        #logging.info(oct(stat.S_IMODE(os.lstat(os.path.join(directory, filename)).st_mode)))
        if filename.endswith(".mp3") and (os.access(os.path.join(directory, filename), os.R_OK)):
            if os.path.getsize(os.path.join(directory, filename)) < 51380224:
                context.bot.send_audio(chat_id, audio=open(os.path.join(directory, filename), 'rb'), timeout=30)
            #os.remove(os.path.join(directory, filename))
            #with open(os.path.join(directory, filename),'w'): pass
            os.chmod(os.path.join(directory, filename), 000)
            #context.bot.send_message(chat_id, text="Novo podcast!")
            continue

#podcast_handler = CommandHandler('podcast', podcast)
#dispatcher.add_handler(podcast_handler)
updater.job_queue.run_repeating(podcast, 60)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

