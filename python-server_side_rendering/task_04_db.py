from flask import Flask, request, render_template
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# ---------------- JSON OXUMA ----------------
def read_json():
    try:
        path = os.path.join(os.path.dirname(__file__), "products.json")
        with open(path, "r") as f:
            return json.load(f)
    except Exception:
        return None


# ---------------- CSV OXUMA ----------------
def read_csv():
    try:
        path = os.path.join(os.path.dirname(__file__), "products.csv")
        products = []
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products.append(row)
        return products
    except Exception:
        return None


# ---------------- SQLITE OXUMA ----------------
def read_sqlite():
    try:
        db_path = os.path.join(os.path.dirname(__file__), "products.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        conn.close()

        products = []
        for r in rows:
            products.append({
                "id": r[0],
                "name": r[1],
                "category": r[2],
                "price": r[3]
            })
        return products

    except Exception:
        return None


@app.route('/products')
def display_products():

    source = request.args.get("source")
    product_id = request.args.get("id")

    # ---------------- SOURCE yoxlanır ----------------
    if source not in ["json", "csv", "sql"]:
        return render_template("product_display.html", error="Wrong source")

    # ---------------- DATA OXUNUR ----------------
    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    else:
        data = read_sqlite()

    if data is None:
        return render_template("product_display.html", error="Could not read file or database")

    # ---------------- ID Filtri ----------------
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html", error="Invalid ID")

        filtered = [p for p in data if p["id"] == product_id]

        if not filtered:
            return render_template("product_display.html", error="Product not found")

        data = filtered

    # ---------------- Template Render ----------------
    return render_template("product_display.html", products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

