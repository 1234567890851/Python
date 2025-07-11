from flask import Flask, render_template, request, redirect
import csv
from datetime import date

app = Flask(__name__)
CSV_FILE = 'expenses.csv'

# Ensure CSV file has header
try:
    with open(CSV_FILE, 'r') as f:
        pass
except FileNotFoundError:
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Amount', 'Category', 'Note', 'Date'])

@app.route('/')
def index():
    expenses = []
    total = 0
    with open(CSV_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            expenses.append(row)
            total += float(row['Amount'])
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/add', methods=['POST'])
def add_expense():
    amount = request.form['amount']
    category = request.form['category']
    note = request.form['note']
    today = date.today().isoformat()

    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([amount, category, note, today])

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
