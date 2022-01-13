from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():

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
            "name":"books",
            'cover_image': 'https://i.insider.com/605367b3fe6a340019acf502?width=700',
            'title': 'Best Books',
            'text': descriptions[0],
            'link': 'https://github.com/S-Alikhonov/books'

        },
        {
            "name":"fitness_app",
            'cover_image': 'https://www.mobindustry.net/wp-content/uploads/wearables-1.jpg',
            'title': 'AI powered Fitness App',
            'text': descriptions[1],
            'link': 'https://github.com/S-Alikhonov/AI_ML/tree/main/Chapter%202/challenge%20week%20-%20Fitness%20app'

        },
        {
            'cover_image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSrL0dDqsXjJR3E8lw7abs5pR0b2Ra6G7193NiXv2-UtoyDyOxGkCruGw8EU3idymiP7E&usqp=CAU',
            'title':'Digit Recognizer',
            'text':descriptions[2],
            'link':'https://github.com/S-Alikhonov/AI_ML/blob/main/Chapter%203/cotours%20:%20DNNs/handwriting.ipynb'
        },
        {
            'cover_image':'https://images.ctfassets.net/3viuren4us1n/5H2ZpQTLB7FrEJN869bjXJ/28ce98438c409a3a3502490179ee7dfe/Healthcare-Bots.jpg',
            'title':'Med-Chatbot',
            'text':  descriptions[3],
            'link':'https://github.com/S-Alikhonov/AI_ML/tree/main/Chapter%203/extra/Chatbot'
            
        }
    ]
    return render_template('projects.html',projects=my_projects)


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
    app.run(debug=True)


    