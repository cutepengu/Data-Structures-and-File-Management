import numpy as np  # Import NumPy library

# 1. Create a 2D NumPy array to represent sales data for each year.
# Each row represents a year, and each column represents a month's sales.

sales_data = np.array([
    [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100],  # 2015 sales data
    [1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950, 2050, 2150],  # 2016 sales data
])

# 2. Print the sales for the second year (index 1).
 # Output will be the sales for 2016
print(sales_data[1])

# 3. Change the sales for July in the first year (2015) to a new value.
# Set July sales for 2015 to 1650
sales_data[0, 6] = 1650

# 4. Add a new row for another year (2017).
# Note: NumPy arrays have fixed size, so to add new rows, use np.append or recreate the array.
sales_data = np.append(sales_data,[1100, 1200, 1250, 1350, 1500, 1650, 1700, 1800, 1850, 1950, 2000, 2200])

# 5. Print the updated sales data.
print(sales_data)