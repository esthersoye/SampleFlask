#import render_template function from flask
from flask import render_template

#import app variable from app package
from app import app

#create an association for the URL / 
@app.route('/')

#create an association for the URL /index
@app.route('/index')

#create the index page to display intro text
def index():
    
    #create a dictionary object to store user information
    user = {'username': 'Emily'}
    
    #create a list of dictionaries to hold author and comment information
    recentSightings = [
        {
            'author' : 'Jane',
            'body' : 'I saw a UFO in Macroom last Friday!'
        },
        {
            'author' : 'John',
            'body':'Anyone else see the triangle with lights in Youghal on Monday?'
        }
    ]
    
    return render_template('index.html', title='UFO/UAP Interactive Database',  user=user, posts=recentSightings)