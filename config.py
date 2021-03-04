from sample_config import Config


class Development(Config):
  # get this values from my.telegram.org. 
  # 6 is just a placeholder. Fill your own api id & hash.
  APP_ID = 1578500
  API_HASH = "389c31460416db3085cfd478b946f8f6"

  # the name to display in your alive message.
  # If not filled anything then default value is Hell User.
  ALIVE_NAME = "Your Daddy"

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "postgres://pcydassb:WAmY2LVHV3ieLJabswDxpjJIw6AeZLgN@ziggy.db.elephantsql.com:5432/pcydassb"
  DATABASE_URL = "postgres://pcydassb:WAmY2LVHV3ieLJabswDxpjJIw6AeZLgN@ziggy.db.elephantsql.com:5432/pcydassb"
  # After cloning the repo and installing requirements...
  # Do python string_session.py and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  STRING_SESSION = "1BVtsOHwBu2tnAI4gB92B0yerB4RTVqTa60ZMvd38ZEhods1A1wqnruFlIVgMzt85aYbZ6X90p8nxq9pi0K-xqHn1hgNRUIWemmoxL3jK7ZIWL48EgKVWk4cduIsGXs-fyZOIVClVT8rEIV6FuqSyKHD4WA5QoCBg6Fsi1wGNvSRTLZMcwd-yAarjUJpdWvVBp1OxIvk6D6oCtfqvz7ojxNyo1JD8JxOB28kQeG8lqinMwJLjzpIm_KSIHeB1ZVVnVaWgHqU6CcGZf59HYEY8ImejWquh95IQ0nc7RB7YrCGzHnU0JbzoLb0TWo48g2epJ2Ldm1PfoAm4f7OXJin4E-j044WqY1E="

  # Create a bot in @botfather and fill the following values with bot token and username.
  BOT_TOKEN = "1215484550:AAF5SZ1DvPCQkFxB14EukPSIUwEuaMLPPu4" #token
  BOT_USERNAME = "@Baap_HellBot" #username

  # Create a private group and add rose bot to it.
  # and type /id and paste that id here.
  # replace that -100 with that group id.
  LOGGER = -1001476244007

  # enter the userid of sudo users.
  # you can add multiple ids by separating them by space.
  # fill values in [] only.
  SUDO_USERS = []
