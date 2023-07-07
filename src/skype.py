import time
import requests
from skpy import SkypeEventLoop


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

      self.handler(self, event)
      if self.autoAck:
          event.ack()

  def __loop(self, period = 1):
    while True:
      self.cycle()
      time.sleep(period)
  
  def on_event(self, handler, period = 1):
    self.handler = handler
    self.__loop(int(period))