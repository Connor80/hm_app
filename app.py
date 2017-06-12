from flask import Flask, render_template, session, request, redirect, url_for
import random, sys, re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test';

def get_word():
    word_list = ["fruit", "train", "vacation", "hypnotist", "teacher",
                 "salad", "kick", "screw", "absurd", "woozy", "class",
                 "steel", "extend", "disastrous", "incredible", "ship",
                 "acoustic", "drum", "explain", "aggressive", "teeth",
                 "stew", "copy", "noiseless", "picayune", "brainy", "foamy",
                 "erratic", "numerous", "tightfisted", "bake", "interest",
                 "accurate", "annoy", "horn", "concentrate", "swift",
                 "straight", "fear", "crack", "breakable", "camera",
                 "abandoned","awful", "dazzling", "admit", "joke", "trace",
                 "shrill", "mother", "coach", "frog", "fearful", "telling",
                 "charge", "press", "crib", "cows", "knife", "simple",
                 "concerned", "wild", "lumber", "rock", "unbiased", "groan",
                 "delirious", "meat", "hydrant", "exist", "listen", "scrawny",
                 "obscene", "crush", "escape", "suck", "pull", "trip",
                 "continue", "nappy", "dull", "pinch",
                 "certain", "petite", "lettuce", "honey", "debonair",
                 "trade", "tame", "stiff", "size", "messy", "road",
                 "harsh", "reign", "match", "pray", "soda", "stir", "edge"
                 ]
    return random.choice(word_list).upper()

@app.route("/")
def index():
    session.clear()
    session['word'] = get_word()
    word = session['word']
    return render_template('hm.html', attempts = 0, word = word,
        incorrect = 0)

@app.route('/play', methods=['GET', 'POST'])
def play():
    word = session['word']
    session['incorrect'] = 0
    session['attempts'] = 0
    session['guessed_letters'] = []
    session['status'] = "_ " * len(word)
    return render_template('play.html', attempts = 0, word = word,
        incorrect = 0, guessed_letters = [], matches = 0,
        status = "_ " * len(word))

@app.route('/game', methods=['POST'])
def game():
    word = session['word']
    guess = request.form['guess'].upper()
    guessed_letters = session['guessed_letters']
    status = session['status']
    result = check_guess(word, guessed_letters, guess)

    if guess not in word:
        session['incorrect'] += 1
        session['attempts'] += 1
        session['guessed_letters'].append(guess)
    elif guess in word:
        session['guessed_letters'].append(guess)

    return render_template('play.html', word = word, guess = guess,
        attempts = session['attempts'],
        guessed_letters = session['guessed_letters'],
        incorrect = session['incorrect'], status = status,
        matches = session['matches'], result = result)

@app.route('/game', methods=['POST'])
def letters():
    if request.method == 'POST':
        letters = request.form['guessed_letters']
        return letters

def check_guess(word, guessed_letters, guess):
    session['status'] = ""
    session['matches'] = 0
    for letter in word:
        if letter in guessed_letters:
            session['status'] += letter
        else:
            session['status'] += "_ "
        if letter == guess:
            session['matches'] += 1
    return session['status']

if __name__ == "__main__":
    app.run(debug=True)
