import csv

def load_sales(filename):
    """Load car sales from a CSV file and return a list of dictionaries."""
    sales = []

    with open(filename) as file:
        lines = file.readlines()
    header = lines[0].strip().split(",")
    for line in lines[1:]:
        values = line.strip().split(",")
        sale = {
            "sale_id": int(values[0]),
            "date": values[1],
            "salesperson": values[2],
            "make": values[3],
            "model": values[4],
            "year": int(values[5]),
            "price": float(values[6]),
        }
        sales.append(sale)
    return sales

def total_sales(sales):
    """Calculate the total sales amount from a list of sales."""
    return len(sales)


def total_revenue(sales):
    """Calculate the total revenue from a list of sales."""
    revenue = 0

    for sale in sales:
        revenue += sale["price"]
    return revenue


def sales_by_salesperson(sales):
    """Return the sales made by each salesperson as a dictionary."""

    count = {}

    for sale in sales:
        salesperson = sale["salesperson"]
        if salesperson not in count:
            count[salesperson] = 0
        count[salesperson] += 1

    return count


def most_solid_make(sales):
    """Return the make of the car with the highest number of sales."""
    make_count = {}

    for sale in sales:
        make = sale["make"]
        if make not in make_count:
            make_count[make] = 0
        make_count[make] += 1

    most_solid = max(make_count, key=make_count.get)
    return most_solid


sales = load_sales("car_sales.csv")

print("Total sales:", total_sales(sales))
print("Total revenue:", total_revenue(sales))
print("Sales by salesperson:", sales_by_salesperson(sales))
print("Most sold make:", most_solid_make(sales))