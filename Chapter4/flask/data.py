

descriptions = ['This project is in the form of web site for EDA, data visualisation and web scraping.\
                    As dataset top-1000 business books from Good Reads website are chosen and scraped. ',
                    'This fitness application created with Flask framework as web application. It can distinguish\
                        5 different type of actions using XGBoost ML model with accuracy of >80%.',
                    'Handwritten digits recognizer is powered by CNN model. It takes image containing a hand written\
                        digit or numbers. Using OpenCV functionalities image first be preprocessed, extracts individual\
                        digits then it passes it to CNN model as a input. Finally CNN model predicts and returns the output.',
                    'Med-Chat bot,as it s already obvious from the title, is dedicated to NLP. MLP model trained on\
                    different dialogs between patient and medical staff. It can handle various types of dialogs.\
                        It can greet, understand the what kind of symtoms and can offer to schedule an appointment if\
                        if needed.']
   

my_projects = [
        {
            "type":"Data Visualisation",
            'cover_image': 'https://i.insider.com/605367b3fe6a340019acf502?width=700',
            'title': 'Best Books',
            'text': descriptions[0],
            'link': 'https://github.com/S-Alikhonov/books'

        },
        {
            "type":"Machine Learning",
            'cover_image': 'https://www.mobindustry.net/wp-content/uploads/wearables-1.jpg',
            'title': 'AI powered Fitness App',
            'text': descriptions[1],
            'link': 'https://github.com/S-Alikhonov/AI_ML/tree/main/Chapter%202/challenge%20week%20-%20Fitness%20app'

        },
        {   
            'type': 'Deep Laerning',
            'cover_image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSrL0dDqsXjJR3E8lw7abs5pR0b2Ra6G7193NiXv2-UtoyDyOxGkCruGw8EU3idymiP7E&usqp=CAU',
            'title':'Digit Recognizer',
            'text':descriptions[2],
            'link':'https://github.com/S-Alikhonov/AI_ML/blob/main/Chapter%203/cotours%20:%20DNNs/handwriting.ipynb'
        },
        {   
            'type': 'NLP',
            'cover_image':'https://images.ctfassets.net/3viuren4us1n/5H2ZpQTLB7FrEJN869bjXJ/28ce98438c409a3a3502490179ee7dfe/Healthcare-Bots.jpg',
            'title':'Med-Chatbot',
            'text':  descriptions[3],
            'link':'https://github.com/S-Alikhonov/AI_ML/tree/main/Chapter%203/extra/Chatbot'
            
        }
    ]

bio = {

    'hobbies':{
        'title':'hobbies',
        'elements': ['Video editing','Photography']
    },
    'interests':{
        'title':'interests',
        'elements':['Technology','Space','Content creation']
    },
    'education':{
        'title':'Education',
        'elements':['BSc in Mechanical Engineering - 2014-2019','MSc in Engineering and Management - 2019 - present']
    },
    'techno':{   
        'title':'Technologies I Use',
        'elements':[
            'Python',
           'Sckit-Learn',
           'Pytorch',
           'Pandas',
           'Numpy',
           'OpenCV',
           'Matplotlib',
           'Seaborn',
           'Plotly',
           'Streamlit',
           'Spacy',
           'Flask',
           'Beautiful Soup',
           'Selenium',
        ]

    }
}

           