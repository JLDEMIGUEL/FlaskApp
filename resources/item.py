import uuid

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items, stores

blp = Blueprint("Items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Items(MethodView):

    def get(self, item_id):
        try:
            return items[item_id], 200
        except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted"}, 200
        except KeyError:
            abort(404, message="Item not found")

    def put(self, item_id):
        item_data = request.get_json()
        if "price" not in item_data or "name" not in item_data:
            abort(404, message="'price' or 'name' missing")
        try:
            item = items[item_id]
            item |= item_data
            return item, 200
        except KeyError:
            abort(404, message="Item not found")


@blp.route("/item")
class ItemsList(MethodView):

    def get(self):
        return {"items": list(items.values())}, 200

    def post(self):
        item_data = request.get_json()
        if "price" not in item_data or "name" not in item_data or "store_id" not in item_data:
            abort(404, message="The attributes: price, name and store_id must be specified in the request body")
        for item in items.values():
            if item["name"] == item_data["name"]:
                abort(404, message="The item already exists")
        if item_data["store_id"] not in stores:
            abort(404, message="Store not found")
        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item
        return item, 201
