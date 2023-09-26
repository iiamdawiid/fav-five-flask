from flask import Flask, render_template
from config import Config 

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def base():
    return render_template("base.html")

@app.route("/bodybuilders")
def bodybuilders():
    bodybuilders = ['Kevin Levrone', 'Mike Mentzer', 'Tom Platz', 'Dorian Yates', 'Nasser El Sonbaty']
    return render_template("bodybuilders.html", bodybuilders=bodybuilders)

@app.route("/cars")
def cars():
    cars = ['Lamborghini Aventador SVJ', 'BMW F82 M4', 'Nissan R34 GTR', 'Nissan R32 GTR', 'Koenigsegg Jesko']
    return render_template("cars.html", cars=cars)