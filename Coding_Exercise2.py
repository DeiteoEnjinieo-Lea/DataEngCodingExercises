"""
Problem:
You have been given two CSV files: 'sales.csv' and 'products.csv'. Your task is to create a data pipeline using Luigi that performs the following steps:

Read the 'sales.csv' file and extract the relevant columns: 'order_id', 'customer_id', 'product_id', and 'quantity'.

Read the 'products.csv' file and extract the relevant columns: 'product_id' and 'product_name'.

Clean the data by removing any rows with missing or invalid values.

Perform an inner join on the 'product_id' column to combine the 'sales' and 'products' data.

Calculate the total quantity sold for each product.

Calculate the total revenue for each product (revenue = quantity * unit price).

Generate a report that includes the 'product_id', 'product_name', 'total_quantity', and 'total_revenue' for each product.

Requirements:

Use Luigi to define the data pipeline tasks.
Each step should be implemented as a separate Luigi task.
Handle any potential errors or exceptions that may occur during the data processing.
You can assume that the CSV files have a header row and the relevant columns are present.
You can use any Python libraries, including pandas, to assist with data manipulation and analysis.
Your solution should include:

A Python script that defines the Luigi tasks and their dependencies to create the data pipeline.
Sample input data (sales.csv and products.csv) for testing your script.
A sample output report generated by your script.
"""
import luigi
import pandas as pd

sales_src = r"C:\Users\yourname\Documents\sales.csv"
products_src = r"C:\Users\yourname\Documents\products.csv"

class SalesProducts(luigi.Task):
    date_interval = luigi.DateIntervalParameter()

    def output(self):
        return luigi.LocalTarget("Documents/sales_data_%s.csv" % self.date_interval)

    def run(self):
        sales_df = pd.read_csv(sales_src)
        sales_file = sales_df[['order_id', 'customer_id', 'product_id', 'quantity']]
        product_df = pd.read_csv(products_src)
        product_file = product_df[['product_id', 'product_name', 'unit_price']]

        sales_file = sales_file.dropna()
        product_file = product_file.dropna()

        sales_products = pd.merge(sales_file, product_file, on='product_id')

        product_item_sales = sales_products.groupby('product_id')['quantity'].sum()
        product_item_revenue = sales_products.groupby('product_id')['quantity'].mul(sales_products['unit_price']).sum()

        report = pd.DataFrame({
            'product_id': product_item_sales.index,
            'product_name': sales_products['product_name'].unique(),
            'total_quantity': product_item_sales.values,
            'total_revenue': product_item_revenue
        })

        report.to_csv(self.output().path, index=False)

# Run the task
if __name__ == '__main__':
    luigi.build([SalesProducts(date_interval='2023-07-04')], local_scheduler=True)
