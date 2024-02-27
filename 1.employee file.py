import pandas as pd

# Assuming your data is stored in a CSV file named 'employees.csv'
# Read the CSV file into a DataFrame
employees = pd.read_csv('C:/Users/manas/OneDrive/Documents/DSA0504/employee.csv')

# Select distinct department IDs
distinct_department_ids = employees['DEPARTMENT_ID'].unique()

# Print the distinct department IDs
print("Distinct Department IDs:")
for department_id in distinct_department_ids:
    print(department_id)
