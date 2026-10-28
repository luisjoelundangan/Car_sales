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

