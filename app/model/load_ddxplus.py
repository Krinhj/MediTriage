from datasets import load_dataset
import pandas as pd

#Step 1: Load the dataset
print("Loading DDXPlus dataset...")
dataset = load_dataset("aai530-group6/ddxplus")

#Step 2: Convert the 'train' split to a DataFrame
df = pd.DataFrame(dataset['train'])

#Step 3: Show dataset info
print("\nColumns:", df.columns.tolist())
print("\nSample rows:")
print(df.head())

#Step 4: Analyze unique conditions
print("\nTop 10 Most Common Diagnoses:")
print(df['PATHOLOGY'].value_counts().head(10))

#Optional: Save a sample of 500 rows for offline use
df.sample(500).to_csv("ddxplus_sample.csv", index=False)
print("\nSample saved to 'ddxplus_sample.csv'.")