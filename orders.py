from flask import Flask, request, render_template
import json

app = Flask(__name__)

items = {}

orders = {"orders": []}

nextId = 0

def getId():
    global nextId

    id = nextId
    nextId += 1
    return id

def loadItems():
    with open("items.json") as f:
        items = json.load(f)
        f.close()
        print(items)

@app.route("/")
def main():
    return render_template("home.html")

@app.route("/orders")
def getOrders():
    return "Orders"

@app.route("/new-order")
def newOrder():
    f = open("items.json")
    items = json.load(f)["items"]
    f.close()


    return "New Orders"

@app.route("/api/orders", methods=["GET"])
def apiGetOrders():
    return orders

@app.route("/api/new-order", methods=["POST"])
def apiNewOrder():
    data = request.get_json()

    data["order_id"] = getId()

    returnData = {"order_id": data["order_id"]}
    
    orders["orders"].append(data)

    return returnData, 201

@app.route("/api/delete-order", methods=["DELETE"])
def apiDeleteOrder():
    data = request.get_json()
    orderId = data["order_id"]

    for order in orders["orders"]:
        if order["order_id"] == orderId:
            orders["orders"].remove(order)
            return order, 200

    return f"Order {orderId} not found.", 404

if __name__ == "__main__":
    loadItems()
    app.run(host="0.0.0.0", port=6969)