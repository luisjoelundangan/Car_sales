from storage import load_sales
from rules import total_revenue, sales_by_salesperson, most_sold_make, least_sold_model
import csv

def menu(sales):
    """Print the menu"""
    print("Choose from 1-6")
    print("1. Total sales")
    print("2. Total revenue")
    print("3. Sales by salesperson")
    print("4. Most sold make")
    print("5. Least sold make")
    print("6. Quit")

def run_menu(sales):
    """Run the show menu until the user choose to quit."""
    while True:
        choise = input("Please choose from 1-6: ")
        if choise == "1":
            print(len(sales))
        elif choise == "2":
            print(total_revenue(sales))
        elif choise == "3":
            print(sales_by_salesperson(sales))
        elif choise == "4":
            print(most_sold_make(sales))
        elif choise == "5":
            print(least_sold_model(sales))
        elif choise == "6":
            print("Goodbye")
            break
        else:
            print("Invalid input. ")
            break



sales = load_sales("car_sales.csv")

menu(sales)
run_menu(sales)