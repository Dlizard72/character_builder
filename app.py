from flask import render_template, request
from flask import Flask
from creation import *
app = Flask(__name__)


@app.route("/", methods=["GET", "Post"])
def home():
    stats = None
    name = None
    race = None
    if request.method == "POST":
        name = request.form.get("name")
        race = request.form.get("race")
        stats = Attributes(
            Str=drop_lowest(),
            Int=drop_lowest(),
            Wis=drop_lowest(),
            Dex=drop_lowest(),
            Con=drop_lowest(),
            Cha=drop_lowest()
        )
    return render_template("test.html",stats=stats,name=name,race=race)
    


if __name__ == "__main__":
    app.run(debug=True)