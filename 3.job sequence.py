import pandas as pd
jobs_df = pd.read_csv('C:/Users/manas/OneDrive/Documents/DSA0504/job sequence.csv')
sorted_jobs = jobs_df.sort_values(by='JOB_TITLE', ascending=False)
print(sorted_jobs)
