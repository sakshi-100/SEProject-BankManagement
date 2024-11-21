from flask import Flask, render_template, request, redirect, url_for, flash
import utils

app = Flask(__name__)
app.secret_key = "supersecretkey"  # For flash messages

@app.route("/")
def index():
    return render_template("index.html")

# Customer Management Routes
@app.route("/customers", methods=["GET", "POST"])
def customers():
    if request.method == "POST":
        customer = {
            "id": request.form["id"],
            "name": request.form["name"],
            "phone": request.form["phone"],
            "address": request.form["address"]
        }
        customers = utils.read_data("database/customers.json")
        customers.append(customer)
        utils.write_data("database/customers.json", customers)
        flash("Customer added successfully!", "success")
    customers = utils.read_data("database/customers.json")
    return render_template("customer.html", customers=customers)

# Transaction Management Routes
@app.route("/transactions", methods=["GET", "POST"])
def transactions():
    if request.method == "POST":
        transaction = {
            "id": request.form["id"],
            "customer_id": request.form["customer_id"],
            "type": request.form["type"],
            "amount": float(request.form["amount"])
        }
        transactions = utils.read_data("database/transactions.json")
        transactions.append(transaction)
        utils.write_data("database/transactions.json", transactions)
        flash("Transaction recorded successfully!", "success")
    transactions = utils.read_data("database/transactions.json")
    return render_template("transaction.html", transactions=transactions)

# Loan Management Routes
@app.route("/loans", methods=["GET", "POST"])
def loans():
    if request.method == "POST":
        loan = {
            "id": request.form["id"],
            "customer_id": request.form["customer_id"],
            "amount": float(request.form["amount"]),
            "duration": request.form["duration"]
        }
        loans = utils.read_data("database/loans.json")
        loans.append(loan)
        utils.write_data("database/loans.json", loans)
        flash("Loan application submitted successfully!", "success")
    loans = utils.read_data("database/loans.json")
    return render_template("loan.html", loans=loans)

if __name__ == "__main__":
    app.run(debug=True)
