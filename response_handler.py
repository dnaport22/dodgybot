import random

class ResponseHandler():

  def responseData(self, key):
    response = {
      "greeting": [
        "Whaddup Homie!",
        "Yo!",
        "You know who this is.",
        "Ghostbusters, whatya want?"
      ],
      "question": [
        "I can't complain... I've tried, but no one listens.",
		"You think I know what to say?",
		"My lawyer says I don't have to answer that question.",
		"Go Away!"
      ],
      "random": [
        "Heeey, baaaaaby.",
		"I like your face.",
		"Oh shit! u just broke my heart",
		"What are you saying brav!"
      ]
    }

    return random.choice(response[key])

  def sendResponse(self, user, me):
  	return ("\nYou Said: %s \nI Say: %s\n"%(user, me))

  def greetingHandler(self, msg):
	return self.sendResponse(msg, self.responseData('greeting'))

  def questionHandler(self, msg):
	return self.sendResponse(msg, self.responseData('question'))  

  def unknownResponse(self, msg):
  	return self.sendResponse(msg, self.responseData('random'))