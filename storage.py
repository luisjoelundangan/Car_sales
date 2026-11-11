from rules import (least_sold_model, 
                   most_sold_make, 
                   sales_by_salesperson, 
                   total_revenue,
                   average_sale_by_salesperson,
                   top_salesperson_by_average,
                   sales_in_month,
                   best_month
                )


def load_sales(filename):
    """Load car sales from a CSV file and return a list of dictionaries."""
    sales = []

    try:
        with open(filename) as file:
            lines = file.readlines()

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    
    if not lines:
        print("Error: The csv file is empty.")
        return []
    
    header = lines[0].strip().split(",")

    for line in lines[1:]:
        try:
            values = line.strip().split(",")

            if len(values) != 7:
                print("Skipping row: Incorrect number of columns.")
                continue

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

        except ValueError:
            print("Skipping row: Invalid number found.")

    return sales

def write_report(sales, filename):
    """Write the car sales and analytics results to a text file."""

    with open(filename, "w") as file:
        file.write("===== Car Sales Report =====\n\n")


        file.write(f"Total Sales: {len(sales)}\n")
        file.write(f"Total Revenue: ${total_revenue(sales):,.2f}\n")
        file.write(f"Most Sold Make: {most_sold_make(sales)}\n")
        file.write(f"Least Sold Model: {least_sold_model(sales)}\n")

        file.write("\n==== Sales by Salesperson ====\n\n")

        for name, count in sales_by_salesperson(sales).items():
            file.write(f"{name}: {count} sales\n")

        file.write("\n==== Average Sale by Salesperson ====\n\n")

        average = average_sale_by_salesperson(sales)

        for name, average in average.items():
            file.write(f"{name}: ${average:,.2f}\n")

        file.write("\n==== Extension Analytics ====\n\n")
        file.write(
            f"Top salesperson by Average: "
            f"{top_salesperson_by_average(sales)}\n"
        )
        file.write(f"Best Sales Month: {best_month(sales)}\n")



