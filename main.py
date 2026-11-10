from storage import load_sales, write_report
from rules import (
        total_revenue,
        sales_by_salesperson,
        most_sold_make,
        least_sold_model,
        average_sale_by_salesperson,
        top_salesperson_by_average, 
        sales_in_month, 
        best_month
) 
import csv

def menu(sales):
    """Print the menu"""
    print("===== Car Sales Analytics Menu =====")
    print("Choose from 1-10")
    print("1. Total sales")
    print("2. Total revenue")
    print("3. Sales by salesperson")
    print("4. Most sold make")
    print("5. Least sold make")
    print("6. Average sale by salesperson")
    print("7. Top salesperson by average sale")
    print("8. Sales in a specific month")
    print("9. Best Sales month")
    print("10. Quit")

def run_menu(sales):
    """Run the show menu until the user choose to quit."""
    while True:
        menu(sales)
        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            print(f"Total sales: {len(sales)}")
        elif choice == "2":
            print(f"Total revenue: ${total_revenue(sales):,.2f}")
        elif choice == "3":
            print(f"Sales by salesperson: {sales_by_salesperson(sales)}")
        elif choice == "4":
            print(f"Most sold make: {most_sold_make(sales)}")
        elif choice == "5":
            print(f"Least sold model: {least_sold_model(sales)}")
        elif choice == "6":
            print(f"Average sale by salesperson: {average_sale_by_salesperson(sales)}")
        elif choice == "7":
            print(f"Top salesperson by average sale: {top_salesperson_by_average(sales)}")
        elif choice == "8":
            try:
                year = int(input("Enter the year (YYYY): "))
                month = int(input("Enter the month (MM): "))

                if month < 1 or month > 12:
                    print("Invalid month. Please enter a value between 1 and 12.")
                else:
                    count = sales_in_month(sales, year, month)
                    print(f"Number of sales in {year}-{month:02d}: {count}")

            except ValueError:
                print("Invalid input. Please enter valid numbers for year and month.")
        elif choice == "9":
            print(f"Best sales month: {best_month(sales)}")
        elif choice == "10":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 10.")


if __name__ == "__main__":
    sales = load_sales("car_sales.csv")
    write_report(sales, "car_sales_report.txt")
    run_menu(sales)

