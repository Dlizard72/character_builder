from flask import render_template, request
from flask import Flask
from creation import *
import json
import os

app = Flask(__name__)
DATA_FILE = "characters.json"

def load_characters():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            # Convert back into Attributes objects
            for char in data.values():
                stats_dict = char.get("stats", {})
                char["stats"] = Attributes(**stats_dict)
            return data
    else:
        return {}

saved_characters = load_characters()

def save_characters():
    # Convert Attributes to dict before saving
    to_save = {}
    for name, char in saved_characters.items():
        to_save[name] = {
            "name": char["name"],
            "race": char["race"],
            "Class": char["Class"],
            "background": char["background"],
            "stats": char["stats"].__dict__  # Convert Attributes to plain dict
        }
    with open(DATA_FILE, "w") as f:
        json.dump(to_save, f, indent=2)


@app.route("/", methods=["GET", "Post"])
def home():
    stats = None
    name = None
    race = None
    background = None
    Class = None
    editing = False
    editing_stats = False
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
            if name:
                saved_characters[name] = {
                "name": name,
                "race": race,
                "Class": Class,
                "background": background,
                "stats": stats
                }
            save_characters()
        elif action == "load":
            selected = request.form.get("selected_character", "").strip()
            selected = selected.strip() if selected else None
            char = saved_characters.get(selected)
            if char:
                name = char["name"]
                race = char["race"]
                Class = char["Class"]
                background = char["background"]
                stats = char["stats"]
        elif action == "change":
            editing_stats = True
            if all(request.form.get(k) for k in ["Str", "Int", "Wis", "Dex", "Con", "Cha"]):
                stats = get_stats_from_form()
            
            
    return render_template("test.html",stats=stats,name=name,race=race,background=background,Class=Class,editing=editing,editing_stats=editing_stats,saved_characters=saved_characters)
    
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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)