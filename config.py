from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 4738242
    API_HASH = "2fc2577f2b0bb066149b2bc10b37edd2"
    # the name to display in your alive message
    ALIVE_NAME = "VICKY"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://jrycfssc:fEZMYWiOcO9vB8cIq1_Z97GhW3TiTppJ@tiny.db.elephantsql.com/jrycfssc"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "your session"
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "your token"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID =
    # command handler
    COMMAND_HAND_LER = "."
    VCMODE = "True"
    VC_SESSION = "your 2nd id telethon session" #note don't use maim account to vc player
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/rishabhanand2/tha_plugins"
    #don't edit this 
    THANOSABUSE = "False"#don't edit this else error in 
