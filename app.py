from flask import render_template, request
from flask import Flask
from creation import *
app = Flask(__name__)


@app.route("/", methods=["GET", "Post"])
def home():
    stats = None
    name = None
    race = None
    background = None
    Class = None
    editing = False
    if request.method == "POST":
        action = request.form.get("action")
        name = request.form.get("name")
        race = request.form.get("race")
        background = request.form.get("background")
        Class = request.form.get("Class")
        if action == "edit":
            editing = True
            stats = Attributes(
                Str=int(request.form.get("Str") or 0),
                Int=int(request.form.get("Int") or 0),
                Wis=int(request.form.get("Wis") or 0),
                Dex=int(request.form.get("Dex") or 0),
                Con=int(request.form.get("Con") or 0),
                Cha=int(request.form.get("Cha") or 0)
            )
        elif action == "save":
            stats = Attributes(
                Str=int(request.form.get("Str") or 0),
                Int=int(request.form.get("Int") or 0),
                Wis=int(request.form.get("Wis") or 0),
                Dex=int(request.form.get("Dex") or 0),
                Con=int(request.form.get("Con") or 0),
                Cha=int(request.form.get("Cha") or 0)
            )
        elif action == "roll":
            stats = Attributes(
            Str=drop_lowest(),
            Int=drop_lowest(),
            Wis=drop_lowest(),
            Dex=drop_lowest(),
            Con=drop_lowest(),
            Cha=drop_lowest()
        )
    return render_template("test.html",stats=stats,name=name,race=race,background=background,Class=Class,editing=editing)
    


if __name__ == "__main__":
    app.run(debug=True)