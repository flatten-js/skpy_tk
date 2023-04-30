import time
import requests
from skpy import Skype, SkypeEventLoop


class SkypeMessageEvent(SkypeEventLoop):

  def __init__(self, email, password, chat_id):
    super().__init__(email, password, autoAck=True)
    self.chat_id = chat_id
    self.handler = lambda: None

  def cycle(self):
    try:
      events = self.getEvents()
    except requests.ConnectionError:
      return
    
    for event in events:
      if event.__class__.__name__ != 'SkypeNewMessageEvent': continue
      if event.msg.chatId != self.chat_id: continue

      self.__onEvent(event)
      if self.autoAck:
          event.ack()

  def loop(self, period = 1):
    while True:
      self.cycle()
      time.sleep(int(period))
  
  def on_event(self, handler):
    self.handler = handler

  def __onEvent(self, event):
    self.handler(event)