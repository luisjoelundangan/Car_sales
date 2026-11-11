Testing and Debugging
Test Case 1: Empty Sales Dataset
test: test_empty_sales()
Purpose: To check wheather the analytics function can handle an empty dataset without crashing
Initial Result: Faild
Error Encounterd:
    ValueError: max() iterable argument is empty, occurred in most_sold_make().
    ValueError: min() iterable argument is empty, occurred in least_sold_model().
Cause: The most_sold_make() function attempted to use max() on an empty dictionary
Solution: Add a condition to check wheather the dictionary is empty before calling max() or min(). If it is empty, the functions return None.
Final Result