from flask import Flask, request, render_template

app = Flask(__name__)

orders = {"orders": []}

nextId = 0

def getId():
    global nextId

    id = nextId
    nextId += 1
    return id

@app.route("/")
def main():
    return render_template("home.html")

@app.route("/orders")
def getOrders():
    return "Orders"

@app.route("/new-order")
def newOrder():
    return "New Orders"

@app.route("/api/orders", methods=["GET"])
def apiOrders():
    return orders

@app.route("/api/new-order", methods=["POST"])
def apiNewOrder():
    data = request.get_json()

    data["order_id"] = getId()

    returnData = {"order_id": data["order_id"]}
    
    orders["orders"].append(data)

    return f"Order added successfully", returnData

@app.route("/api/delete-order", methods=["DELETE"])
def apiDeleteOrder():
    data = request.get_json()
    orderId = data["order_id"]

    deleted = False

    for order in orders["orders"]:
        if order["order_id"] == orderId:
            orders["orders"].remove(order)
            deleted = True

    return f"Deleted order {orderId}" if deleted else f"Order {orderId} not found"

if __name__ == "__main__":
    app.run(port=6969)