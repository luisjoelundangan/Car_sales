import csv

def load_sales(filename):
    """Load car sales from a CSV file and return a list of dictionaries."""
    sales = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            sale = dict(zip(header, row))

            sale["sale_id"] = int(sale["sale_id"])
            sale["year"] = int(sale["year"])
            sale["price"] = float(sale["price"])

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