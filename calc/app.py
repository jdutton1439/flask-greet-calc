from operations import add, sub, mult, div
from flask import Flask, request
app = Flask(__name__)
# Put your app in here.

"""
performs math operations on user-submitted data
"""

def generate_html(msg):
    """generates page html and displays passed parameters"""
    return f"<html><body><h1>{msg}</h1></body></html>"

@app.route('/')
def show_homepage():
    msg = "visit /math for more information!"
    return generate_html(msg)

@app.route('/math')
def show_operations():
    msg = """INFO:<br>
    <ul>Operations are
        <li>/add</li>
        <li>/sub</li>
        <li>/mult</li>
        <li>/div</li>
    </ul><br>
    Query string format   ?a=&b="""
    return generate_html(msg)

@app.route('/math/<operation>')
def perform_operation(operation):
    """
    performs the requested operation and displays result
    displays "No such operation!" if operation is not found
    """

    ops = {
        "add": "+",
        "sub": "-",
        "mult": "*",
        "div": "/",
    }

    if operation == "add":
        op = " + "
    elif operation == "sub":
        op = " - "
    elif operation == "mult":
        op = " * "
    elif operation == "div":
        op = " / "
    else:
        return generate_html("No such operation!")
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    result = eval(operation+"(a, b)")

    msg = f"{a} {ops[operation]} {b} = {result}"

    #return f"{result}"
    return generate_html(msg)