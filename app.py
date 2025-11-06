from flask import Flask, render_template, request
import math, os
from modules.queue import Queue
from modules.dequeue import DeQueue

app = Flask(__name__)

@app.route('/')
def home_redirect():
    return index()

#home page
@app.route('/home')
def index():
    index_data = {
        "message": "GROUP 11",
        "message_1": "Hello everyone we are the Group 11 and this is our Group Portfolio project in DSA"
    }
    return render_template('home.html', index=index_data, active_page='home')

#project page
@app.route('/works', methods=['GET', 'POST'])
def works():
    return render_template('works.html',  active_page='works')

#profile and contact page
@app.route('/contacts')
def members_contact():
    people = [
    {
        "name": "Mark Christian Abucejo",
        "image": "static/images/pic_1.png",
        "links": {
                "facebook": "https://www.facebook.com/mrkchrstnsbcj",
                "email": "https://www.facebook.com/mrkchrstnsbcj",
                "github": "https://www.facebook.com/mrkchrstnsbcj",
            }
    },
    {
        "name": "Zy Banez",
        "image": "static/images/zy.jpg",
        "links": {
                "facebook": "https://www.facebook.com/zyescote.banez.5",
                "email": "zyescotebanez@gmail.com",
                "github": "https://github.com/ITZMEXYZ",
            }
    }, 
    {
        
            "name": "Kyle Isaac Celin",
            "image": "static/images/pic_2.png",
            "links": {
                "facebook": "https://www.facebook.com/cee.the.lin.e",
                "email": "https://youtube.com/@zybanezz",
                "github": "https://tiktok.com/@zybanezz",
        }
    }, 
    {
        
            "name": "John Luke Fabillan",
            "image": "static/images/pic_3.png",
            "links": {
                "facebook": "https://facebook.com/zybanezz",
                "email": "https://youtube.com/@zybanezz",
                "github": "https://tiktok.com/@zybanezz",
        }
    }, 
    {
        
            "name": "Princess Sophia Manalo",
            "image": "static/images/pic_4.png",
            "links": {
                "facebook": "https://facebook.com/zybanezz",
                "email": "https://youtube.com/@zybanezz",
                "github": "https://tiktok.com/@zybanezz",
        }
    }, 
    {
        
            "name": "Isaac Christian Pelingen",
            "image": "static/images/pic_5.png",
            "links": {
                "facebook": "https://facebook.com/zybanezz",
                "email": "https://youtube.com/@zybanezz",
                "github": "https://tiktok.com/@zybanezz",
        }
    }, 
    {
        
            "name": "Gian Carlos Tumanan",
            "image": "static/images/pic_6.png",
            "links": {
                "facebook": "https://facebook.com/zybanezz",
                "email": "https://youtube.com/@zybanezz",
                "github": "https://tiktok.com/@zybanezz",
        }
    }
    ]
    
    return render_template("contacts.html", people=people)


# "Queue Visualizer" PAGE
@app.route('/works/queue-visualizer', methods=['GET', 'POST'])
def queue_visualizer():
    return render_template('queuevisualizer.html')

# "DeQueue Visualizer" PAGE
@app.route('/works/dequeue-visualizer', methods=['GET', 'POST'])
def dequeue_visualizer():
    return render_template('dequeuevisualizer.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
