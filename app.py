from flask import render_template, request
from flask import Flask
from creation import *
app = Flask(__name__)
saved_characters = {}

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
            stats = get_stats_from_form()
        elif action == "save":
            stats = get_stats_from_form()
        elif action == "roll":
            stats = Attributes(
            Str=drop_lowest(),
            Int=drop_lowest(),
            Wis=drop_lowest(),
            Dex=drop_lowest(),
            Con=drop_lowest(),
            Cha=drop_lowest()
        )
        elif action == "save_character":
            stats = get_stats_from_form()
            saved_characters[name] = {
            "name": name,
            "race": race,
            "Class": Class,
            "background": background,
            "stats": stats
            }
        elif action == "load":
            selected = request.form.get("selected_character")
            selected = selected.strip() if selected else None
            char = saved_characters.get(selected)
            if char:
                name = char["name"]
                race = char["race"]
                Class = char["Class"]
                background = char["background"]
                stats = char["stats"]
    return render_template("test.html",stats=stats,name=name,race=race,background=background,Class=Class,editing=editing,saved_characters=saved_characters)
    
def get_stats_from_form():
    return Attributes(
        Str=int(request.form.get("Str") or 0),
        Int=int(request.form.get("Int") or 0),
        Wis=int(request.form.get("Wis") or 0),
        Dex=int(request.form.get("Dex") or 0),
        Con=int(request.form.get("Con") or 0),
        Cha=int(request.form.get("Cha") or 0)
    )

if __name__ == "__main__":
    app.run(debug=True)