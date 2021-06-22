import os
from config import Config

class Translation(object):
  START_TXT = """<b>🖐🏻Hey {}!</b>
<i>I'm a Simple Auto file Forward Bot.
This Bot forwards all files from One Public Channel to your Personal Channel.
For more details click /help</i>"""
  CAPTION = "`{}`\n\n" + str(Config.CAPTION)
  HELP_TXT = """<b>Follow These Steps!!</b>
<b>• Correctly fill your Heroku Config Vars</b> <code>FROM_CHANNEL</code> and <code>TO_CHANNEL</code> <b>and other Vars</b>
<b>• Then give Admin permissions in your personal Telegram Channel</b>
<b>• Then send any message in your personal Telegram Channel</b>
<b>• Then use /run command in your bot</b>

<b><u>Available Command</b></u>

* /start - <b>Bot Alive</b>
* /help - <b>Get Help</b>
* /run - <b>Start Forwarding</b>
* /about - <b>About Me</b>"""
  ABOUT_TXT = """<b><u>My Info</b></u>

<b>Name :</b> <i>SidRobot</i>
<b>Creator :</b> @HalkatManus
<b>Language :</b> <code>Python3</code>
<b>Lybrary :</b> <code>Pyrogram v1.2.9</code>
<b>Server :</b> <code>Heroku</code>
<b>Build :</b> <code>V0.1</code>"""
