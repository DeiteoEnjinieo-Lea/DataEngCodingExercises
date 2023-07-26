: << 'COMMENT'
Exercise: Data Cleaning and Transformation with csvkit

You have been provided with a CSV file named "sales_data.csv," which contains sales data for a company. 
Your task is to clean and transform the data using csvkit to answer specific questions.

The "sales_data.csv" file contains the following columns:

Date: The date of the sale (format: "YYYY-MM-DD").
Product: The name of the product sold.
Units_Sold: The number of units sold for the product.
Revenue: The revenue generated from the sale.
Tasks:

Use csvlook to inspect the contents of the "sales_data.csv" file and understand its structure.
Use csvclean to clean the data. Remove any rows with missing or invalid values. Make sure to handle any 
possible errors appropriately.
Use csvsort to sort the data in ascending order based on the "Date" column.
Use csvcut to extract only the "Date" and "Revenue" columns into a new CSV file named "sales_revenue.csv."
Use csvsql to perform an SQL query on the data to find the total revenue earned for each product. Save the 
results in a new CSV file named "product_revenue.csv" with the following columns: "Product" and "Total_Revenue."
COMMENT

# use csvlook to view contents of a file 
csvlook sales_data.csv

# use csvclean to data cleanse your csv 
csvclean sales_data.csv

# sort your data in ascending order within the Date column
csvsort - c "Date" sales_data.csv 

# extract two fields of data and place into a new file 
csvcut -c "Date", "Revenue" sales_data.csv > sales_revenue.csv

# write a sql query to retrieve data 
csvsql --query "SELECT product, SUM(revenue) as Total_Revenue FROM sales_data GROUP BY product" sales_data.csv > product_revenue.csv 
