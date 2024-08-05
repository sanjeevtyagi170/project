import pandas as pd
import random
import time
from datetime import datetime, timedelta

# Define electronic products with corresponding names
products = [
    'iPhone', 'Macbook', 'Dell PC', 'Mouse', 'Adapter', 'Television', 'CPU'
]

# Initialize the product ID counter
product_id_counter = 1

# Function to generate a random date in July 2024
def generate_random_july_date():
    start_date = datetime(2024, 7, 1)
    end_date = datetime(2024, 7, 31)
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Function to generate a single row of sample data
def generate_sample_data():
    global product_id_counter
    product_name = random.choice(products)
    
    # Generate unique Product_ID
    product_id = product_id_counter
    product_id_counter += 1
    
    # Generate random data for other columns
    units_sold = random.randint(1, 500)
    unit_price = round(random.uniform(5.0, 1000.0), 2)  # Adjusted range for electronic products
    total_sales = round(units_sold * unit_price, 2)
    actual_anomaly = random.choice([0, 1])  # Randomly decide if it's an anomaly
    date = generate_random_july_date().strftime('%Y-%m-%d')
    
    return {
        'Date': date,
        'Product_ID': product_id,
        'Product_Name': product_name,
        'Units_Sold': units_sold,
        'Unit_Price': unit_price,
        'Total_Sales': total_sales,
        'Actual_Anomaly': 0
    }

# Function to append multiple rows to CSV
def append_rows_to_csv(rows, filename='sales_data.csv'):
    df = pd.DataFrame(rows)
    df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename), index=False)

# Main loop to generate and append data every second
try:
    while True:
        # Generate 3 records
        rows = [generate_sample_data() for _ in range(1)]
        append_rows_to_csv(rows)
        print(rows)
        time.sleep(1)  # Wait for 1 second
except KeyboardInterrupt:
    print("Data generation stopped by user.")
