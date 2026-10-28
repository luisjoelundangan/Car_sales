def total_sales(sales):
    """Calculate the total sales amount from a list of sales."""
    return len(sales)


def total_revenue(sales):
    """Return the sum of all the prices."""
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


def most_sold_make(sales):
    """Return the make of the car with the highest number of sales."""
    
    make_count = {}

    for sale in sales:
        make = sale["make"]
        if make not in make_count:
            make_count[make] = 0
        make_count[make] += 1

    most_sold = max(make_count, key=make_count.get)

    return most_sold

def least_sold_model(sales):
    """Return the model of a car with the lowest number of sales."""

    count = {}

    for sale in sales:
        model = sale["model"]
        if model not in count:
            count[model] = 0
        count[model] += 1
    least_sold = min(count, key=count.get)

    return least_sold