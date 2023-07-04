"""
You have been tasked with acquiring data from a sample operational system and preparing it for consumption in both cloud and 
on-premises environments. The data comes from a fictional e-commerce platform and consists of customer orders and product information.

Tasks
Data Acquisition:

Connect to the operational system's database and extract the following tables:
customers: Contains information about the customers, including their ID, name, email, and address.
orders: Contains information about customer orders, including the order ID, customer ID, order date, and total amount.
products: Contains information about the products, including the product ID, name, price, and category.
Store the extracted data in separate CSV files for each table.
Data Preparation:

Perform data transformations on the extracted data to prepare it for consumption:
Clean the data by removing any duplicate records and handling missing values.
Create a new table order_details that combines information from the orders and products tables. The order_details table should include the order ID, customer ID, order date, total amount, and product details (product name, price, and category).
Export the transformed data to a new CSV file.
Requirements
Use Python and any necessary libraries (e.g., pandas, SQLAlchemy) to complete the tasks.
Use appropriate data processing techniques to clean and transform the data.
Write reusable and maintainable code.
Include comments and documentation where necessary.
Demonstrate error handling and validation of the data.
Create a clear and organized directory structure for the project.
Provide a README file with instructions on how to run the code and any additional information.
"""
# Connect to an operational systems database and extract tables
import psycopg
import csv 
import pandas as pd 

# connecting to the src db
with psycopg.connect("dbname='sales2023' user=yourusername password=yourpassword") as conn:

	# open the cursor 
	with conn.cursor() as cur_sql:
		# perform the query 
		# open and read file
		#f = open(query_src, "r")
		#sql_query = f.read()
		# Execute a query 

		#CUSTOMERS
		cur_sql.execute(""" SELECT * FROM customers """)
		# once done, return result 
		rows = cur.fetchall()
		customers_csv = open('Documents/sales_data/customers.csv','w')
		cust_file = csv.writer(customers_csv, lineterminator='\n')
		cust_file.writerows(rows)
		cust_file.close()

		# ORDERS
		cur_sql.execute(""" SELECT * FROM orders """)
		rows = cur.fetchall()
		orders_csv = open('Documents/sales_data/orders.csv','w')
		order_file = csv.writer(orders_csv, lineterminator='\n')
		order_file.writerows(rows)
		order_file.close()

		# PRODUCTS
		cur_sql.execute(""" SELECT * FROM products """)
		rows = cur.fetchall()
		products_csv = open('Documents/sales_data/products.csv','w')
		prod_file = csv.writer(products_csv, lineterminator='\n')
		prod_file.writerows(rows)
		prod_file.close()

		conn.close()

customers = pd.read_csv(r'Documents/sales_data/customers.csv')
orders = pd.read_csv(r'Documents/sales_data/orders.csv')
products = pd.read_csv(r'Documents/sales_data/products.csv')

# Data Cleansing of the Data Sets 
# Clean data by removing any rows with missing or invalid values
customers = customers.dropna()
orders = orders.dropna()
products = products.dropna()

# Removing any existing duplicates 
customers.drop_duplicates(inplace=True)
orders.drop_duplicates(inplace=True)
products.drop_duplicates(inplace=True)

# Create a new table that combines info from orders + products; 
order_details = pd.concat([orders, products], ignore_index=True)

# Export the new transformed datasets 
customers.to_csv('customers_2023.csv')
orders.to_csv('orders_2023.csv')
products.to_csv('products_2023.csv')
order_details.to_csv('order_details2023.csv')
