from flask import Flask, render_template, request, redirect, url_for
import os
from modules.queue import Queue
from modules.dequeue import DeQueue

app = Flask(__name__)

queue_structure = Queue()
deque_structure = DeQueue()

@app.route('/')
def home_redirect():
    return redirect(url_for('index'))

# Home page
@app.route('/home')
def index():
    index_data = {
        "message": "GROUP 11",
        "message_1": "Hello everyone we are the Group 11 and this is our Group Portfolio project in DSA."
    }
    return render_template('home.html', index=index_data, active_page='home')

# Project page
@app.route('/works')
def works():
    return render_template('works.html',  active_page='works')

# Profile and Contact page
@app.route('/contacts')
def members_contact():
    people = [
    {
        "name": "Mark Christian Abucejo",
        "image": "static/images/members/mark.jpg",
        "links": {
                "facebook": "https://www.facebook.com/mrkchrstnsbcj",
                "email": "mailto:abucejomark11905@gmail.com",
                "github": "https://github.com/nug3tsss",
            }
    },
    {
        "name": "Zy Banez",
        "image": "static/images/members/zy.jpg",
        "links": {
                "facebook": "https://www.facebook.com/zyescote.banez.5",
                "email": "mailto:zyescotebanez@gmail.com",
                "github": "https://github.com/ITZMEXYZ",
            }
    }, 
    {
        
            "name": "Kyle Isaac Celin",
            "image": "static/images/members/pic_2.png",
            "links": {
                "facebook": "https://www.facebook.com/cee.the.lin.e",
                "email": "https://youtube.com/@zybanezz",#need update
                "github": "https://tiktok.com/@zybanezz",#need update
        }
    }, 
    {
        
            "name": "John Luke Fabillan",
            "image": "static/images/members/pic_3.png",
            "links": {
                "facebook": "https://facebook.com/zybanezz",#need update
                "email": "https://youtube.com/@zybanezz",#need update
                "github": "https://tiktok.com/@zybanezz",#need update
        }
    }, 
    {
        
            "name": "Princess Sophia Manalo",
            "image": "static/images/members/pic_4.png",
            "links": {
                "facebook": "https://facebook.com/zybanezz",#need update
                "email": "https://youtube.com/@zybanezz",#need update
                "github": "https://tiktok.com/@zybanezz",#need update
        }
    }, 
    {
        
            "name": "Isaac Christian Pelingen",
            "image": "static/images/members/pic_5.png",
            "links": {
                "facebook": "https://www.facebook.com/share/1FmtJqYkC4/",
                "email": "Mail to: pelingenisaac@gmail.com",
                "github": "https://github.com/xiin112",
        }
    }, 
    {
        
            "name": "Gian Carlos Tumanan",
            "image": "static/images/members/pic_6.png",
            "links": {
                "facebook": "https://facebook.com/zybanezz",#need update
                "email": "https://youtube.com/@zybanezz",#need update
                "github": "https://tiktok.com/@zybanezz",#need update
        }
    }
    ]
    
    return render_template("contacts.html", people=people)


# Queue visualizer page
@app.route('/works/queue-visualizer', methods=['GET', 'POST'])
def queue_visualizer():
    if request.method == "POST":
        value = request.form.get("value")

        if "enqueue" in request.form:
            queue_structure.enqueue(value)
        elif "dequeue" in request.form:
            queue_structure.dequeue()

    if request.args.get("dequeue"):
        queue_structure.dequeue()

    return render_template(
        "queuevisualizer.html",
        items=queue_structure.get_items(),
        active_page="works"
    )

# DeQueue visualizer page
@app.route('/works/dequeue-visualizer', methods=['GET', 'POST'])
def dequeue_visualizer():
    if request.method == "POST":
        action = request.form.get("action")

        if action == "left":  # Insert Left
            value = request.form.get("value")
            if value:
                deque_structure.insert_left(value)
        elif action == "right": 
            value = request.form.get("value")
            if value:
                deque_structure.insert_right(value)
        elif action == "remove_left":
            deque_structure.remove_left()
        elif action == "remove_right":
            deque_structure.remove_right()

    return render_template(
        "dequeuevisualizer.html",
        items=deque_structure.get_items(),
        active_page="works")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
