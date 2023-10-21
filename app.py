from flask import Flask

app = Flask(__name__)
import random
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

@app.route('/')
def homepage():
    """"Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    """Display a message to the user that changes based on their input."""
    return f'The {adjective} {noun} went on a walk to the park'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Display the product of inputted numbers"""
    
    if (number1.isdigit() and number2.isdigit()):
        num1 = int(number1)
        num2 = int(number2)
        result = num1 * num2
        return f'{num1} x {num2} = {result}'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def repeat_word(word, n):
    if (n.isdigit()):
        phrase = ''
        repeat = int(n)
        for _ in range(repeat):
            phrase += (word + ' ')
        return phrase
    else:
        return 'Invalid input. Please try again by entering a word and a number!'

@app.route('/dicegame')
def dicegame():
    number = random.randint(1, 6)
    if number == 6:
        return f'You rolled a {number}. You won!'
    else:
        return f'You rolled a {number}. You lost!'

if __name__ == '__main__':
    app.run(debug=True)