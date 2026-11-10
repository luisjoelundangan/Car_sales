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

def average_sale_by_salesperson(sales):
    """Calculate the average sale price for each salesperson."""

    total = {}
    count = {}

    for sale in sales:
        name = sale["salesperson"]
        price = sale["price"]

        if name not in total:
            total[name] = 0
            count[name] = 0

        total[name] += price
        count[name] += 1

    average = {}

    for name in total:
        average[name] = total[name] / count[name]

    return average
def top_salesperson_by_average(sales):
    """Return the salesperson with the highest average sale price."""

    average = average_sale_by_salesperson(sales)

    if not average:
        return None

    top_salesperson = max(average, key=average.get)

    return top_salesperson

def sales_in_month(sales, year, month):
    """Return the number of sales in a specific year and month."""

    count = 0

    for sale in sales:
        date = sale["date"]

        sale_year = int(date[:4])
        sale_month = int(date[5:7])

        if sale_year == year and sale_month == month:
            count += 1

    return count

def best_month(sales):
    """Return the year and month with the highest number of sales."""

    month_count = {}

    for sale in sales:
        date = sale["date"]
        year_month = date[:7]

        if year_month not in month_count:
            month_count[year_month] = 0

        month_count[year_month] += 1

    if not month_count:
        return None

    best_month = max(month_count, key=month_count.get)

    return best_month