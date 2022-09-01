from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

my_bot=ChatBot(name='PyBot',read_only=True,logic_adapters=['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'])
small_talk=['hi there!',
            'whats your name.How can I help You?',
            'Courses your college offer?',
            'We have 3 branches.EEE, CSE, ECE',
            'Can I know the fee structure?',
            'Yeah,sure.\n EEE->35,000\nCSE -> 55,000,\n ECE -> 40,000 Per Year. Want to know our infrastructure?',
            'The infrastructure of our college is good and huge. All the facilities of the college like Wi-Fi, library, labs, and classrooms are good. The canteen is good. But non-vegetarian food is not allowed in the hostel.',
            'Achievements',
            '250 students are placed our of 300 last year. all are placed in MNCs.Visit our college and get to know.',
            'help desk',
            'contact ourcollege@oc.org'
            ]
math_talk_1 = ['pythagorean theorem',
               'a squared plus b squared equals c squared.']
math_talk_2 = ['law of cosines',
               'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

list_trainer=ListTrainer(my_bot)
for item in (small_talk,math_talk_1,math_talk_2):
    list_trainer.train(item)
    
print("Provide input")
print("If you want to exit- Press 1")
i=input()
while i!='1':
    print(my_bot.get_response(i))
    i=input()
