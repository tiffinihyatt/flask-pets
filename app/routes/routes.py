from flask import Blueprint, jsonify

class Cat:
    def __init__(self, id, name, color, personality):
        self.id = id
        self.name = name
        self.color = color
        self.personality = personality
    
    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            color=self.color,
            personality=self.personality
        )

cats = [
    Cat(1, "Muna", "black", "mischevious"),
    Cat(2, "Matthew", "spotted", "cuddly"),
    Cat(3, "George", "Gray","Sassy")
]

bp = Blueprint("cats", __name__, url_prefix="/cats")

# GET /cats
@bp.route("", methods=("GET",))
def index_cats():
    result_list = [cat.to_dict() for cat in cats]

    return jsonify(result_list)

# GET /cats/id
@bp.route("/<cat_id>", methods=["GET"])
def get_cat_by_id(cat_id):
    try:
        cat_id = int(cat_id)
    except ValueError:
        return {"message": f"cat {cat_id} invalid"}, 400

    for cat in cats:
        if cat_id == cat.id:
            return cat.to_dict()