from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hobbies')
def hobbies():
    title = "Hobbies"
    navbar_active = "hobbies"
    hobbies = [
    {
        "name": "Hobby 1",
        "caption": "Gaming",
        "img": "http://wallpapercave.com/wp/JzG4dZE.jpg",
        "active": "active"
    },
    {
        "name": "Hobby 2",
        "caption": "Coding",
        "img": "https://tse4.mm.bing.net/th?id=OIP.DzeDVoXTDb9TPJaGW18otQHaE8&pid=Api&P=0&h=180",
        "active": ""
    },
    {
        "name": "Hobby 3",
        "caption": "Cricket",
        "img": "https://www.latrobe.edu.au/news/images/articles/cricket-resized.jpg",
        "active": ""
    },
]


    return render_template('hobbies.html', title=title, navbar_active=navbar_active, hobbies=hobbies)




if __name__ == '__main__':
    app.run(debug=True)
