from flask import Flask, render_template, request, session, jsonify
from main import engine, gas_tank, pedal

app = Flask(__name__)
app.secret_key = "engine-sim"


@app.route("/")
def homepage():
    """Display the homepage."""

    return render_template("index.html")

@app.route("/pedal")
def give_it_gas(duration, t_position):
    pedal.press(seconds=duration, how_hard=t_position)

def get_rotations(duration):
    rotations = engine.supply(seconds=duration, gas_portion=gas_tank)
    
    return jsonify({"rotations": rotations})