import re
import sys

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

sme = SkypeMessageEvent(SKYPE_EMAIL, SKYPE_PASSWORD, SKYPE_CHAT_ID)
mf = MoneyForward(MONEY_FORWARD_EMAIL, MONEY_FORWARD_PASSWORD)

def handler(event):
  content = event.msg.content
  if event.msg.userId != SKYPE_USER_ID: return

  try:
    if re.search(SKYPE_CLOCK_IN_MESSAGE, content):
      mf.clock_in()
      report = "出勤しました"
    elif re.search(SKYPE_CLOCK_OUT_MESSAGE, content):
      mf.clock_out()
      report = "退勤しました"

    print(report)
    if SKYPE_REPORT_USER_ID:
      sme.contacts[SKYPE_REPORT_USER_ID].chat.sendMsg(report)

  except Exception as e:
    error_message = f'エラー: 出退勤が完了していない可能性があります。\n{e}'
    print(error_message)
    if SKYPE_REPORT_USER_ID:
      sme.contacts[SKYPE_REPORT_USER_ID].chat.sendMsg(error_message)
 
sme.on_event(handler)
sme.loop(SKYPE_LOOP_PERIOD)