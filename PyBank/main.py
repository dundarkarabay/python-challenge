#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Libraries
import os
import csv

# Establishing a path to the file using os library
csv_path = os.path.join(".", "Resources", "budget_data.csv")

# Setting up variables
total_months = 0
total = 0
profits = []
months = []

# (1) Opening the file using csv library. Notice that each row is now a list of two elements
# (2) Calculating the total number of months (3) Calculating the sum of all profit/loss amounts
# (4) Appending individual profit and month/year information into corresponding lists. 
with open(csv_path, "r", newline = "") as file_handler:
    csv_reader = csv.reader(file_handler, delimiter = ",")
    header = next(csv_reader) # This allows us to name the first row as a list called "header" and skip it. 
    for row in csv_reader:
        total_months += 1
        total += int(row[1])
        profits.append(row[1])
        months.append(row[0])
print(f"""Financial Analysis
-------------------------------------------------
Total Months: {total_months}
Total: ${total}""")

length = len(profits)
profits.append("") # Added "" to the end of profits list so that I can use it as a condition in the if statement while calculating the change values.

change_sum = 0
greatest_increase = float('-inf') # Initializing greatest_increase with a very low # so that first change will be assigned as the greatest_increase and everything will go from there
greatest_decrease = float('inf') # Initializing greatest_decrease with a very high # so that first change will be assigned as the greatest_decrease and everything will go from there

# (1) Calculating individual change amounts and summing them 
# (2) Determining geatest inrease and decrease along with index values that'll be used to find out corresponding month/year information  
for i in range(length):
    if profits[i+1] != "":    
        change = int(profits[i+1])-int(profits[i])
        change_sum = change_sum + change
        if change >= greatest_increase:
            greatest_increase = change
            greatest_increase_index = i+1 
        elif change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_index = i+1

# Calculating average change value
average_change = change_sum / (length-1) # Notice that number of changes is one less than the number of profits
average_change = round(average_change, ndigits =2)
print(f"Average Change: ${average_change}")
            
greatest_increase_month = months[greatest_increase_index]
greatest_decrease_month = months[greatest_decrease_index]
print(f"Greatest Increase in Profit: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profit: {greatest_decrease_month} (${greatest_decrease})")

# Writing the output into a text file called output.txt
output_path = os.path.join(".","Resources","output.txt")
with open(output_path, "w") as file_handler:
    output_writer = file_handler.write("""Financial Analysis
-------------------------------------------------
Total Months: """)
    output_writer = file_handler.write(str(total_months))
    output_writer = file_handler.write("""
Total: $""")
    output_writer = file_handler.write(str(total))
    output_writer = file_handler.write("""
Average Change: $""")
    output_writer = file_handler.write(str(average_change))
    output_writer = file_handler.write("""
Greatest Increase in Profit: """)
    output_writer = file_handler.write(str(greatest_increase_month))
    output_writer = file_handler.write(" ($")
    output_writer = file_handler.write(str(greatest_increase))
    output_writer = file_handler.write(")")
    output_writer = file_handler.write("""
Greatest Decrease in Profit: """)
    output_writer = file_handler.write(str(greatest_decrease_month))
    output_writer = file_handler.write(" ($")
    output_writer = file_handler.write(str(greatest_decrease))
    output_writer = file_handler.write(")")


# In[ ]:




