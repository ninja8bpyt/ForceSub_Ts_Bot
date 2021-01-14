from pyrogram import Client
from Config import Config


plugins = dict(
    root="plugins",
    include=[
        #"start",
        "help",
        "forceSubscribe"
    ]
)

app = Client(
     'ForceSubscribe',
      bot_token = Config.BOT_TOKEN,
      api_id = Config.APP_ID,
      api_hash = Config.API_HASH,
      plugins = plugins
)

app.run()
