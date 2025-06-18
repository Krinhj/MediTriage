from datasets import load_dataset
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

print("Loading DDXPlus dataset...")
dataset = load_dataset("aai530-group6/ddxplus")
df = pd.DataFrame(dataset['train'])

# Step 1: Check EVIDENCES structure
print("Sample evidences:", df['EVIDENCES'].iloc[0])

# Step 2: Use MultiLabelBinarizer to encode symptoms
mlb = MultiLabelBinarizer()
symptom_vectors = mlb.fit_transform(df["EVIDENCES"])

# Step 3: Add encoded features to DataFrame
symptom_df = pd.DataFrame(symptom_vectors, columns=mlb.classes_)
processed_df = pd.concat([df[["PATHOLOGY"]], symptom_df], axis=1)

# Step 4: Save preprocessed data
processed_df.to_csv("ddxplus_encoded.csv", index=False)
print("Saved encoded dataset to ddxplus_encoded.csv")
print("Shape of feature matrix:", symptom_df.shape)
print("Example row:\n", processed_df.head(1))