import pandas as pd
from textblob.classifiers import NaiveBayesClassifier
from intent import intents
import json
from response_handler import ResponseHandler
from chatterbot import ChatBot

class DodgyBot():
  
  __msg = None

  def __init__(self, ResponseHandler):
    self.handler = ResponseHandler
    self.chatbot = None
    self.loadIntent()

  def listener(self, msg):
    self.__setMessage(msg)

  def loadIntent(self):
    self.chatbot = ChatBot(
      'Dodgy Bot',
      trainer= 'chatterbot.trainers.ChatterBotCorpusTrainer'
    )
    self.chatbot.train("chatterbot.corpus.english")

    with open("intent_data.json", "r") as fp:
      self.cl = NaiveBayesClassifier(fp, format="json")

  def getIntent(self):
    return self.cl.classify(self.getMessage())

  def loadResponse(self, intent):
    if (intent == "greeting"):
      return self.handler.greetingHandler(
          self.getMessage()
        )
    if (intent == "question"):
      return self.handler.questionHandler(
          self.getMessage()
        )

    #return self.chatbot.get_response(self.getMessage())

  def __setMessage(self, msg):
    DodgyBot.__msg = msg

  def getMessage(self):
    return DodgyBot.__msg

  def getChatBot(self):
    return self.chatbot

def main():
  handler = ResponseHandler()
  bot = DodgyBot(handler)

  print "Hello, I am a Dodgy Bot."

  while True:
    user_input = str(raw_input('Ask me dodgy stuff: '))
    user_input = user_input.lower().strip()
    bot.listener(user_input)

    if (user_input in ["goodbye", "bye", "exit"]):
      print "Bye!"
      exit()
    intent = bot.getIntent()
    print bot.loadResponse(intent)

if __name__ == "__main__":
  main()

