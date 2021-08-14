from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = [
    {
    "name": "iphone",
    "price": 2000.00
    },
    {
    "name": "laptop",
    "price": 2400.90
    },
    {
    "name": "watch",
    "price": 1500.00
    }
]

class ItemList(Resource):
    def get(self):
        return {"items": items}


class Item(Resource):
    def get(self, name):
        for item in items:
            if item["name"] == name:
                return item
        return {"message": "Item not found"}, 404

    def post(self, name):
        req = request.get_json()
        if req["name"] == name:
            item = {"name": name,"price": req["price"]}
            items.append(item)
            return item


api.add_resource(Item, "/item/<string:name>")   #http://127.0.0.1:5000/item/<string:name>
api.add_resource(ItemList, "/items")   #http://127.0.0.1:5000/items


if __name__ == "__main__":
     app.run(port=5000, debug=True)
