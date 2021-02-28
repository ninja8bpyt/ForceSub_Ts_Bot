import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
  else:
    BOT_TOKEN = "1648439500:AAGRQX1fcj8YddQNKUtOzaC-r0qhuv3HADs"
    DATABASE_URL = "mongodb+srv://Trackstudio:Trackstudio@cluster0.1mrcj.mongodb.net/<dbname>?retryWrites=true&w=majority"
    APP_ID = "2179686"
    API_HASH = "e843e77278c40597cb6e143a69011b03"


class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribers**\nForce group members to join a specific channel before sending messages in the group.\n\n**Setup**\n**Step 1.** __Add me in a group(in which you are creator of the group) as admin.__\n**Step 2.** __Send__ `/ForceSubscribe {your channel username}`\n**Step 3.** __Add me to your channel as admin.__\n\n`All set ! I mute users who didn't joined your channel and ask them to join channel and unmute themself.`\n\n**Commands**\n\n/ForceSubscribe { off / no / disable} - To stop force subscriber\n\n/ForceSubscribe {Channel Username} - Set the Channel\n\n/ForceSubscribe - Get current Status",
        
        "**Developed by @Ninja8bpYt**\n\nJoin @Bots_Ki_Duniya**"
      ]

      START_MSG = "**Hey {message.chat.first_name}!\nI am a multifunctional group manager bot.\nLearn more at /help**"
      
