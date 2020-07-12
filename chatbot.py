from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
'Yo',
)

trainer = ListTrainer(chatbot)

training_quesans = open('training_data/ques.txt').read().splitlines()
training_personal = open('training_data/personal.txt').read().splitlines()
training_menu = open('training_data/menu.txt').read().splitlines()

training_data = training_quesans + training_personal + training_menu

trainer.train(training_data)

# training
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.spanish'
)


#while True:
 #  usuario = input(">>> ")
  # respuesta = chatbot.get_response(usuario)
   #print("Charin: "+str(respuesta))
