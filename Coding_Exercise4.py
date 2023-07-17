import sqlite3
import pandas as pd 

sales_db = sqlite3.connect('yourdatabase.db')

# create the db cursor 
sales_cursor = sales_db.cursor()

# creating the queries 
def create_tbl_query(table_name):
	global table_name 
	create = f"""
		CREATE TABLE {table_name}()
	"""
	return create 

def alter_tbl_query(table, column, data_type):
	table = table_name
	alter = f"""
		ALTER TABLE {table} ADD COLUMN {column} {data_type}
	"""
	return alter 

def drop_column(table, column):
	table = table_name
	drop = f"""ALTER TABLE {table} DROP COLUMN {column}"""
	return drop

def rename_column(table, column, new_name)
table = table_name
renamed = f"""ALTER TABLE {table} RENAME COLUMN {column} TO {new_name}"""
return renamed

def update_tbl_query(table, column, val, new_val):
	table = table_name
	updated = f"""
		UPDATE {table} SET {column}={new_val} WHERE {column}={val}
	"""
	return updated

def insert_query(table, column, val):
table = table_name
inserted = f"""
	INSERT INTO {table}{column} VALUES{val}
"""
return inserted

def run_query(query):
	sales_cursor.execute(query)


# load our datset
src_file = "orders.csv"
df = pd.read_csv(src_file)


#create a new table to hold this data 
run_query(create_tbl_query('transformed_orders'))
run_query(alter_tbl_query('transformed_orders','order_id', 'int'))
run_query(alter_tbl_query('transformed_orders','customer_id', 'int'))
run_query(alter_tbl_query('transformed_orders','product_id', 'int'))
run_query(alter_tbl_query('transformed_orders','quantity', 'int'))
run_query(alter_tbl_query('transformed_orders','price', 'float'))

# transformed the data and clean it 
df.query('quantity > 1000') # quantity of product is over 1000
total_prices_sum = df['price'].sum() # Calculate the sum of prices 
df.sort_values(by=['quantity','price']) # sorting values based on amount and cost

# Print the transformed and cleaned DataFrame 
print(df)
print("Total Price Sum:", total_prices_sum)

# data cleansing 
updated_sales = df.dropna() # no empty values

# removing null values 
updated_sales_wo_null = updated_sales.dropna(inplace=True)

# adding a new column 
updated_sales_2023 = updated_sales_wo_null
updated_sales_2023['total_orders'] = updated_sales['price'].sum()
updated_sales_2023['customers_sales_orders'] = updated_sales['customer_id'].agg(updated_sales['price'])

# load this into the new table
updated_sales_2023.to_sql('transformed_orders', con=sales_db)

# export the transformed data from sqlite to CSV 
sales_report_2023 = pd.read_sql_table('transformed_orders', con=sales_db)

# transform into csv 
sales_report_2023.to_csv('documents/subfolder/sales_report_2023.csv')
