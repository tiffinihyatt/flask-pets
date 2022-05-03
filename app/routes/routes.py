from attr import validate
from flask import Blueprint, jsonify, abort, make_response
from ..models.cat import Cat

bp = Blueprint("cats", __name__, url_prefix="/cats")

# GET /cats
@bp.route("", methods=("GET",))
def index_cats():
    cats = Cat.query.all()
    
    result_list = [cat.to_dict() for cat in cats]

    return jsonify(result_list)

@bp.route("/<cat_id>", methods=["GET"])
def get_cat_by_id(cat_id):
    pass

# helper function to check for valid cat id or return cat dict if id is valid
def validate_cat(cat_id):
    try:
        cat_id = int(cat_id)
    except ValueError:
        abort(make_response({"message": f"cat {cat_id} invalid"}, 400))

    cat = Cat.query.get(cat_id)

    if not cat:
        abort(make_response({"message": f"cat {cat_id} not found"}, 404))
    
    return cat

# GET /cats/id
@bp.route("/<cat_id>", methods=["GET"])
def get_cat_by_id(cat_id):
    cat = validate_cat(cat_id)
    return cat