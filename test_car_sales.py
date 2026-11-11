from rules import (total_sales,
                   total_revenue,
                   sales_by_salesperson,
                   most_sold_make,
                   least_sold_model,
                   average_sale_by_salesperson,
                   top_salesperson_by_average,
                   sales_in_month,
                   best_month
            )

def test_total_sales():
    """Check that total_sales counts records correctly."""

    sales = [
        {"price": 10000},
        {"price": 20000},
        {"price": 30000}
    ]

    result = total_sales(sales)

    assert result == 3

def test_total_revenue():
    """Check that total_revenue calculates the correct total revenue."""

    sales = [
        {"price": 10000},
        {"price": 20000},
        {"price": 30000}
    ]

    result = total_revenue(sales)

    assert result == 60000

def test_sales_by_salesperson():
    """Test that sales are counted for each salesperson correctly."""

    sales = [
        {"salesperson": "Eve"},
        {"salesperson": "Chloe"},
        {"salesperson": "Eve"},
    ]

    result = sales_by_salesperson(sales)

    assert result == {"Eve": 2, "Chloe": 1}

def test_most_sold_make():
    """Test that the most sold make is identified correctly."""

    sales = [
        {"make": "Toyota"},
        {"make": "Honda"},
        {"make": "Toyota"},
        {"make": "BMW"}
    ]

    result = most_sold_make(sales)

    assert result == "Toyota"

def test_least_sold_model():
    """Test that the least frequently sold model is returned."""

    sales = [
        {"model": "Corolla"},
        {"model": "Civic"},
        {"model": "Corolla"},
        {"model": "Forester"},
        {"model": "Corolla"},
        {"model": "Civic"},
    ]

    result = least_sold_model(sales)

    assert result == "Forester"

def test_average_sale_by_salesperson():
    """TEst that average sale price for each salesperson."""

    sales = [
        {"salesperson": "Eve", "price": 10000},
        {"salesperson": "Chloe", "price": 30000},
        {"salesperson": "Eve", "price": 20000},
    ]

    result = average_sale_by_salesperson(sales)

    assert result == {"Eve": 15000, "Chloe": 30000}

def test_top_salesperson_by_average():
    """Test that the highest average salesperson is returned."""

    sales = [
        {"salesperson": "Eve", "price": 10000},
        {"salesperson": "Chloe", "price": 30000},
        {"salesperson": "Eve", "price": 20000},
    ]

    result = top_salesperson_by_average(sales)

    assert result == "Chloe"

def test_sales_in_month():
    """Test that the number of sales in a specific month is returned."""

    sales = [
        {"date": "2026-01-05"},
        {"date": "2026-01-15"},
        {"date": "2026-02-10"},
        {"date": "2025-01-20"},
    ]

    result = sales_in_month(sales, 2026, 1)

    assert result == 2

def test_best_month():
    """Test that the month with the highest sales is returned."""

    sales = [
        {"date": "2026-01-05"},
        {"date": "2026-01-15"},
        {"date": "2026-02-10"},
        {"date": "2026-01-20"},
        {"date": "2026-02-15"},
    ]

    result = best_month(sales)

    assert result == "2026-01"

def test_empty_sales():
    """Test that functions handle empty sales data correctly."""

    sales = []

    assert total_sales(sales) == 0
    assert total_revenue(sales) == 0
    assert sales_by_salesperson(sales) == {}
    assert most_sold_make(sales) is None
    assert least_sold_model(sales) is None
    assert average_sale_by_salesperson(sales) == {}
    assert top_salesperson_by_average(sales) is None
    assert sales_in_month(sales, 2026, 1) == 0
    assert best_month(sales) is None

