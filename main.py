import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s:%(name)s - %(message)s")
logger = logging.getLogger(__name__)

import re

from config import \
  SKYPE_EMAIL, \
  SKYPE_PASSWORD, \
  SKYPE_USER_ID, \
  SKYPE_REPORT_USER_ID, \
  SKYPE_CHAT_ID, \
  SKYPE_CLOCK_IN_MESSAGE, \
  SKYPE_CLOCK_OUT_MESSAGE, \
  SKYPE_LOOP_PERIOD, \
  MONEY_FORWARD_EMAIL, \
  MONEY_FORWARD_PASSWORD

from src.skype import SkypeMessageEvent
from src.money_forward import MoneyForward

def handler(sme, event):
  content = event.msg.content
  if event.msg.userId not in SKYPE_USER_ID: return

  try:
    if re.search(SKYPE_CLOCK_IN_MESSAGE, content):
      mf.clock_in()
      report = "出勤しました"
    elif re.search(SKYPE_CLOCK_OUT_MESSAGE, content):
      mf.clock_out()
      report = "退勤しました"
    else:
      return

    logger.info(report)
    if SKYPE_REPORT_USER_ID:
      sme.contacts[SKYPE_REPORT_USER_ID].chat.sendMsg(report)

  except Exception as e:
    error_message = f'エラー: 出退勤が完了していない可能性があります。\n{e}'
    logger.exception(error_message)
    if SKYPE_REPORT_USER_ID:
      sme.contacts[SKYPE_REPORT_USER_ID].chat.sendMsg(error_message)


logger.info('System startup')
mf = MoneyForward(MONEY_FORWARD_EMAIL, MONEY_FORWARD_PASSWORD)
while True:
  try:
    sme = SkypeMessageEvent(SKYPE_EMAIL, SKYPE_PASSWORD, SKYPE_CHAT_ID)

    logger.info('Monitoring SkypeMessageEvent...')
    sme.on_event(handler, SKYPE_LOOP_PERIOD)
  except Exception as e:
    logger.exception('SkypeMessageEvent connection lost...')
