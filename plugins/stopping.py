#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import sys
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.types import CallbackQuery

@Client.on_callback_query(filters.regex(r'^stop_btn$'))
async def stop_button(c: Client, cb: CallbackQuery):
    await cb.message.delete()
    await cb.answer()
    msg = await c.send_message(
        text="<i>Trying To Stop.....</i>",
        chat_id=cb.message.chat.id
    )
    await asyncio.sleep(5)# await m.delete()
    
    buttons = [[
        InlineKeyboardButton('View Files', url='https://t.me/c/1578872431/123456789')
    ],[
        InlineKeyboardButton('Change Settings', url='https://dashboard.heroku.com/apps/sidrobot/settings')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await msg.edit(
        text=f"<i>File Forward Stopped Successfully 👍</i>\n\n<b>Thanks For Using Me ❤️</b>",
        reply_markup=reply_markup
    )
    os.execl(sys.executable, sys.executable, *sys.argv)
    
@Client.on_callback_query(filters.regex(r'^close_btn$'))
async def close(bot, update):
    await update.answer()
    await update.message.delete()
