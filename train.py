import pandas as pd
from textblob.classifiers import NaiveBayesClassifier
from intent import intents
import json
from response_handler import ResponseHandler
import speech_recognition as sr
import os
# from chatterbot import ChatBot

class DodgyBot():
  
  __msg = None

  def __init__(self, ResponseHandler):
    self.recogniser = sr.Recognizer()
    self.microphone = sr.Microphone()
    self.handler = ResponseHandler
    self.chatbot = None
    self.loadIntent()

  def listen(self, listen_freq=0):
    while listen_freq == 0:
      with self.microphone as source:
        
        self.audio = self.recogniser.listen(source)

      return True

  def recogniseAudio(self):
    print 'Recognising...'
    response = self.recogniser.recognize_google(self.audio)

    return self.setMessage(response) 

  def loadIntent(self):
    # self.chatbot = ChatBot(
    #   'Dodgy Bot',
    #   trainer= 'chatterbot.trainers.ChatterBotCorpusTrainer'
    # )
    # self.chatbot.train("chatterbot.corpus.english")

    with open("intent_data.json", "r") as fp:
      self.cl = NaiveBayesClassifier(fp, format="json")

  def getIntent(self):
    return self.cl.classify(self.getMessage())

  def loadResponse(self, intent):
    if (intent == "greeting"):
      return os.system("say '%s'"%(self.handler.greetingHandler(
          self.getMessage()
        )))
    if (intent == "question"):
      return os.system("say '%s'"%(self.handler.questionHandler(
          self.getMessage()
        )))

    return os.system("say '%s'"%(self.handler.unknownResponse(self.getMessage())))

  def setMessage(self, msg):
    DodgyBot.__msg = msg

  def getMessage(self):
    return DodgyBot.__msg

  def getChatBot(self):
    return self.chatbot

def main():
  handler = ResponseHandler()
  bot = DodgyBot(handler)
  print "Hello I am a Dodgy Bot"
  os.system("say 'Hello I am a Dodgy Bot'")

  while True:
    bot.listen()
    print bot.recogniseAudio()
    # user_input = bot.recogniseAudio().lower().strip()

    # if (user_input in ["goodbye", "bye", "exit"]):
    #   os.system("say 'Bye'")
    #   exit()

    intent = bot.getIntent()
    print bot.loadResponse(intent)

if __name__ == "__main__":
  main()

