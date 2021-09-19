from flask import Flask, request
app = Flask(__name__)

"""
Greet has three routes:
    /welcome
        displays "welcome" on page
    /welcome/home
        displays "welcome home" on page
    /welcome/back
        displays "welcome back" on page
"""   

def generate_html(message):
    """generates html with the passed message for the requested page"""
    return f"<html><body><h1>{message}</h1></body></html>"

@app.route('/')
def show_homepage():
    msg = "TO THE URL:<br><br>add /welcome for a welcome message.<br>add /welcome/n, where n=some sub-page, for a custom welcome message!"
    return generate_html(msg)

@app.route('/welcome')
def show_welcome():
    """returns the page html with the welcome message"""
    return generate_html('welcome')

@app.route('/welcome/<other>')
def show_welcome_other(other):
    """returns the page html with the welcome n message, where n=some sub-page"""
    msg = 'welcome ' + other
    return generate_html(msg)