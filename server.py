"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""
    
    return "<!doctype html><html>Hi! This is the home page. <p><a href=\"http://localhost:5000/hello\">Hello</a></p> </html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name.
    
    <p>Choose a melon:
    <select> name="melon"
        <option selected="watermleon" value="Watermleon">Watermleon</option>
        <option value="Canteloupe">Canteloupe</option>
        <option value="Honeydew">Honeydew</option>
        </select></p>
    
    """

    options_dropdown = ""
    for awesome in AWESOMENESS:
      options_dropdown += f"<option value=\"{awesome}\">{awesome}</option>"


    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
      <br><br>
        What's your best quality?
      <select name="compliment">
        {options_dropdown}
      </select>
      </form>
      
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
