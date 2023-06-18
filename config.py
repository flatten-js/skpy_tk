from dotenv import load_dotenv
load_dotenv()

import os

SKYPE_EMAIL = os.environ.get('SKYPE_EMAIL', '')
SKYPE_PASSWORD = os.environ.get('SKYPE_PASSWORD', '')
SKYPE_USER_ID = os.environ.get('SKYPE_USER_ID', '').split(',')
SKYPE_REPORT_USER_ID = os.environ.get('SKYPE_REPORT_USER_ID', '')
SKYPE_CHAT_ID = os.environ.get('SKYPE_CHAT_ID', '')
SKYPE_CLOCK_IN_MESSAGE = os.environ.get('SKYPE_CLOCK_IN_MESSAGE', 'おはようございます')
SKYPE_CLOCK_OUT_MESSAGE = os.environ.get('SKYPE_CLOCK_OUT_MESSAGE', '^今日の進捗')
SKYPE_LOOP_PERIOD = os.environ.get('SKYPE_LOOP_PERIOD', 1)

MONEY_FORWARD_EMAIL = os.environ.get('MONEY_FORWARD_EMAIL', '')
MONEY_FORWARD_PASSWORD = os.environ.get('MONEY_FORWARD_PASSWORD', '')