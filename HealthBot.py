convo1 = [
    "I'd like to make an appointment",
    "Sure, would you like to book an appointment with a specifc doctor?",
    "Yes, Dr. X",
    "Okay, Please specify the date and time",
    "April 5th, 10 am",
    "Can you tell me the age of the patient?",
    "23",
    "Can I get the patient's name?",
    "Kuragane",
    "Can I get the patient's gender?",
    "Male",
    "Okay. Can I get your email id?",
    "xxx@gmail.com",
    "Thank you. An appointment at 10 am on April 5th for Kurogane has been confirmed. An email has been sent to you",
    "Thanks",
    "The pleasure is mine"
]

convo2 = [
    "Appointment booking",
    "Sure, would you like to book an appointment with a specifc doctor?",
    "No",
    "Okay, I'll need to ask you some questions so I can find the right specialist for you. Can you tell me the health problem for which you need a doctor?",
    "Stomach ache",
    "One a scale of 1 - 10, how intense is it? 10 meaning very intense.",
    "7",
    "Can you tell me the region where you feel the pain?",
    "All over the stomach",
    "How long have you been in pain?",
    "It comes and goes",
    "Your best option is to see a Gastroenterologist. Can you tell me the age of the patient?",
    "45",
    "Can I get the patient's name?",
    "Orihime",
    "Can I get the patient's gender?",
    "Female",
    "Okay, Please specify the date and time",
    "April 9th, 12 pm",
    "Okay. Can I get your email id?",
    "yyy@gmail.com",
    "Thank you. An appointment at 12 pm on April 9th for Orihime has been confirmed. An email has been sent to you"
]

convo3 = [
    "I would like a general health check",
    "Sure, Can you tell me the age of the patient?",
    "32",
    "We have two types: The express health check and a personalised health check. Which do you prefer?",
    "The express health check is good enough",
    "Okay. I shall set an appointment. Can you specify the date and time?",
    "April 10, 11 am",
    "Okay. Can I get the patient's name?",
    "Toshinori",
    "Can I get your gender?",
    "Male",
    "Okay. Can I get your email id?",
    "zzz@gmail.com",
    "An express health checkup at 11 am on April 10th for Toshinori has been confirmed. An email has been sent to you."
]

convo4 = [
    "I need health check",
    "Sure, is there a specific checkup that you'd like?",
    "No",
    "A full body checkup then?",
    "Yes",
    "We have two types: The express health check and a personalised health check. Which do you prefer?",
    "Which is better?",
    "Befor we proceed, Can you tell me the age of the patient?",
    "29",
    "Okay. The express health check is a general test that covers all your basic tests. In the personalised test, we take a look at your entire medical history and base the test around that.",
    "What are the prices?",
    "The basic check up is 3000rs and the personalised check up is 7500rs",
    "I will take the personalised test.",
    "Okay. I shall set an appointment. Can you specify the date and time?",
    "April 8, 12 pm",
    "Okay. Can I get the patient's name?",
    "Sakura",
    "Can I get your gender?",
    "Female",
    "Okay. Can I get your email id?",
    "aaa@gmail.com",
    "An express health checkup at 12 pm on April 8th for Sakura has been confirmed. An email has been sent to you."    
]

convo5 = [
    "Medical Query",
    "Sure, can you tell me the patient's health problem?",
    "Fever",
    "Can you tell me the patient's temperature?",
    "101F",
    "Since when have you been observing fever?",
    "1-2 days",
    "Do you have any other symptoms?",
    "Chills, fatigue, abdominal pain and loss of apetite",
    "Your best option is to seen an Internal medicine specialist. Shall I set up an appointment?",
    "No",
    "Okay. Thank you for enquiring with me"
]

convo6 = [
    "I have a medical query",
    "Sure, can you tell me the patient's health problem?",
    "Hand pain",
    "Your best option is to see an Orthopedician. Shall I set up an appointment?",
    "Okay",
    "Can you tell me the age of the patient?",
    "23",
    "Okay. I shall set an appointment. Can you specify the date and time?",
    "April 7, 1 pm",
    "Okay. Can I get the patient's name?",
    "Mikasa",
    "Can I get your gender?",
    "Female",
    "Okay. Can I get your email id?",
    "bbb@gmail.com",
    "Thank you. An appointment at 1 pm on April 7th for Mikasa has been confirmed. An email has been sent to you"
]

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("HealthBot", logic_adapters=['chatterbot.logic.BestMatch'])
trainer = ListTrainer(chatbot)

trainer.train(convo1)
trainer.train(convo2)
trainer.train(convo3)
trainer.train(convo4)
trainer.train(convo5)

print("Hi! I'm HealthBot. How can I help you today?")

while True:
    try:
        user_input = input()
        print("\n")
        bot_response = chatbot.get_response(user_input)
        print(bot_response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break