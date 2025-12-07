from flask import Flask, request, render_template
import json
import csv
import os

app = Flask(__name__)

# ------------ JSON oxuma funksiyası ------------
def read_json():
    try:
        path = os.path.join(os.path.dirname(__file__), "products.json")
        with open(path, "r") as f:
            return json.load(f)
    except Exception:
        return None

# ------------ CSV oxuma funksiyası ------------
def read_csv():
    try:
        path = os.path.join(os.path.dirname(__file__), "products.csv")
        products = []
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # CSV-də id stringdir, int-ə çeviririk
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
        return products
    except Exception:
        return None


@app.route('/products')
def display_products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # ----- SOURCE yoxlanışı -----
    if source not in ["json", "csv"]:
        return render_template("product_display.html", error="Wrong source")

    # ----- Fayl oxuma -----
    data = read_json() if source == "json" else read_csv()

    if data is None:
        return render_template("product_display.html", error="Could not read file")

    # ----- ID filtr -----
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html", error="Invalid ID")

        filtered = [p for p in data if p.get("id") == product_id]

        if not filtered:
            return render_template("product_display.html", error="Product not found")

        data = filtered

    # ----- Template render -----
    return render_template("product_display.html", products=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

