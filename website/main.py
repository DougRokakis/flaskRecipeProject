from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/recipe_list')
def recipe_list():
    return render_template("recipe_list.html")

@app.route('/curry_ramen')
def curry_ramen():
    return render_template("curry_ramen.html")

@app.route('/brown_rice_salad')
def brown_rice_salad():
    return render_template("brown_rice_salad.html")

@app.route('/healthy_burrito')
def healthy_burrito():
    return render_template("healthy_burrito.html")

if __name__ == "__main__":
    app.run(debug=True)