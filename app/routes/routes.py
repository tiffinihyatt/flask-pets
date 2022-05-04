from app import db
from flask import Blueprint, jsonify, abort, make_response, request
from ..models.cat import Cat

bp = Blueprint("cats", __name__, url_prefix="/cats")

# post a new cat
@bp.route("", methods=["POST"])
def create_new_cat():
    request_body = request.get_json()

    new_cat = Cat(name=request_body["name"], color=request_body["color"], 
    personality=request_body["personality"])

    db.session.add(new_cat)
    db.session.commit()

    return make_response(f"Cat {new_cat.name} successfully created")

# get all cats
@bp.route("", methods=("GET",))
def get_all_cats():
    color_param = request.args.get("color")

    if color_param:
        cats = Cat.query.filter_by(color=color_param)
    else:
        cats = Cat.query.all()
    
    result_list = [cat.to_dict() for cat in cats]

    return jsonify(result_list)

# get cat by id
@bp.route("/<cat_id>", methods=["GET"])
def get_cat_by_id(cat_id):
    cat = validate_cat(cat_id)

    return jsonify(cat.to_dict())

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