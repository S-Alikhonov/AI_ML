chats = {'intents':
    [
        {
            'tag':'Greeting',
            'patterns':[
                'Hi',
                'Hey!',
                'Hello!',
                'Good morning',
                'Good day',
                'good evening'
            ],
            'responses':[
                'Hey! Nice to have you here. How can I help you ?',
                'Hi, how can I help you ?',
                'Hello, thank you for visiting us. How can I help you?',
                'Good day, I am here to help you.'
            ]
        },
        {
            'tag':'Bye',
            'patterns':
            [
                'Bye',
                'See you later',
                'Have a good one',
                'Have a nice day',
                'Good bye'
            ],
            'responses':[
                'You too.',
                'Have a good one.',
                'Have a nice day'
            ]
        },
        {
            'tag':'Thanks',
            'patterns':[
                'Thanks',
                'Thank you',
                "Thanks, that's helpful!"
            ],
            'responses':[
                'Happy to help you',
                'My pleasure'
            ]
        },
        {
            'tag':'Feeling',
            'patterns':[
                "I don't feel well today",
                "I am exausted, I don't know what's wrong",
                "Something wrong with me"
            ],
            'responses':[
                "Can you tell me if you have any symtom?",
                "Do you have any symtoms?",
                "What kind of symtoms do you have?"
            ]
        },
        {
            'tag':'Symtoms',
            'patterns':[
                'I have high temperature',
                'I have headache',
                'I have temperature and nausea',
                'I a dry cough and temperature'
            ],
            'responses':[
                'Okay, you should get consulted. Do you want to book an appointment?',
                'Do you want me to book an appointment for you?',
                'Symtoms can be sign of multiple things, to diagnosis we need some tests. Do you want an anppointment booked ?'
            ]
        },
        {
            'tag':'Appoinment',
            'patterns':[
                'yes please, for tomorrow',
                'yes, if possible, tomorrow',
                'for tomorrow, please',
            ],
            'responses':[
                'Okay, your appoinment is for tomorrow',
                "you can come tomorrow",
                "okay, it has been done for you!"

            ]
        }
    ]
}