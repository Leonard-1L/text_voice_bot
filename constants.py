import logging

PROJECT_PATH = "my_secret_impressive_bot"
LOGS_PATH = f'{PROJECT_PATH}/LOGS.txt'
DATABASE_PATH = f'{PROJECT_PATH}/users'

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=LOGS_PATH,
    filemode="w"
)

try:
    with open(f'{PROJECT_PATH}/secrets_config/BOT_TOKEN', 'r') as bot_token:
        BOT_TOKEN = bot_token.read().strip()
except FileNotFoundError:
    error = 'constants.py: токен от бота не обнаружен.'
    logging.warning(error)
    print(error)
