from DEADLYSPAM import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from DEADLYSPAM import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/b65785536183c1ffb2279.jpg"

DEAD_Help = "ð¥ DÊá´É¢á´ Sá´á´á´ Bá´á´ ð¥\n\n"
 
DEAD_Help += f"__á´á´É´á´s á´á´ á´ÉªÊá´ÊÊá´ ÉªÉ´ á´á´á´á´ÊÊ Êá´á´__\n\n"

DEAD_Help += f" â§ sá´á´á´Êá´á´ ð²ð¼ð³ð â§\n\n"

DEAD_Help += f" `!ping` - to check ping\n `!alive` - to check bot alive/version (only main userbot will reply)\n !`restart` - to restart all spam bots \n `!addecho` - to addecho \n `!rmecho` - To remove Echo \n `!addsudo` - To add sudo user using spam bot \n\n"
 
DEAD_Help += f" â§ ð»ð´ð°ðð´ ð²ð¼ð³ â§\n\n"

DEAD_Help += f" `!leave` - to leave public/private channel/groups\n\n"
 
DEAD_Help += f" â§ ðð¿ð°ð¼ ð²ð¼ð³ð â§\n\n"

DEAD_Help += f" `!raid` - to raid\n `!replyraid` - to active reply raid\n `!dreplyraid` - to de-active reply raid\n `!spam` - this cmd use for Normal spam\n `!bigspam` - this cmd use for big spam\n `!bspam` - this cmd use for spamming on someone birthday!!\n `!delayspam` - this cmd use for delay spam\n\n"

DEAD_Help += f" !pornspam - Éª á´¡ÉªÊÊ ê±á´É¢É¢á´ê±á´ á´á´É´'á´ á´ê±á´ á´ÊÉªê± á´á´á´á´á´É´á´ð â§\n\n"

DEAD_Help += f"Â© @DragoXServer\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=DEAD_Help,
                                  buttons=[
        [
        Button.url("á´Êá´É´É´á´Ê", "https://t.me/DragoXServer"),
        Button.url("sá´á´á´á´Êá´", "https://t.me/DragoXServerChat")
        ] 
        ]
        )
