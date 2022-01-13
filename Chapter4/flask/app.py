from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    descriptions = ['This project is in the form of web site for EDA, data visualisation and web scraping.\
                    As dataset top-1000 business books from Good Reads website are chosen and scraped. ',
                    'This fitness application created with Flask framework as web application. It can distinguish\
                        5 different type of actions using XGBoost ML model with accuracy of >80%.']
    projects = [[
        'https://i.insider.com/605367b3fe6a340019acf502?width=700',
        'Best Books',
        descriptions[0],
        'https://github.com/S-Alikhonov/books'
    ],
    [
        'https://www.mobindustry.net/wp-content/uploads/wearables-1.jpg',
        'AI powered Fitness App',
        descriptions[1],
        'https://github.com/S-Alikhonov/AI_ML/tree/main/Chapter%202/challenge%20week%20-%20Fitness%20app'

    ]
        ]
    # my_projects = {
    #     'books':{
    #         'cover_image': 'https://i.insider.com/605367b3fe6a340019acf502?width=700',
    #         'title': 'Best Books',
    #         'text': descriptions[0],
    #         'link': 'https://github.com/S-Alikhonov/books'

    #     },
    #     'fitness_app':{
    #         'cover_image': 'https://www.mobindustry.net/wp-content/uploads/wearables-1.jpg',
    #         'title': 'AI powered Fitness App',
    #         'text': descriptions[1],
    #         'link': 'https://github.com/S-Alikhonov/AI_ML/tree/main/Chapter%202/challenge%20week%20-%20Fitness%20app'

    #     } 
    # }
    return render_template('projects.html',projects=projects)


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
    app.run(debug=True)