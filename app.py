# import dependencies
from flask import Flask

# Create flask instance
app = Flask(__name__)

# create flask route
@app.route('/')

# create a function
def hello_world():
    return 'Hello World'

@app.route('/')

def stats():
    return 'statistics'