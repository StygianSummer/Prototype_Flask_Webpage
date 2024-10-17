from flask import Blueprint, render_template

views = Blueprint('views', __name__)
#this is a blueprint: which means that it has a bunch of URLs defined in it.
#A blueprint is a templates for generating a "section" of a web application. You can think of it as a mold

@views.route('/')
def home(): #function runs when you go to the URL above
    return render_template("home.html")
