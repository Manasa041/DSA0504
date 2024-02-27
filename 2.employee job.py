import pandas as pd
employees = pd.read_csv('C:/Users/manas/OneDrive/Documents/DSA0504/employee job.csv')
employees['START_DATE'] = pd.to_datetime(employees['START_DATE'])
employees['END_DATE'] = pd.to_datetime(employees['END_DATE'])
jobs_count = employees.groupby('EMPLOYEE_ID')['JOB_ID'].nunique()
employees_with_multiple_jobs = jobs_count[jobs_count >= 2]
print("Employee IDs with two or more jobs in the past:")
print(employees_with_multiple_jobs.index.tolist())
