import pandas as pd

# Load only the header
df = pd.read_csv("ddxplus_triage_labeled.csv", nrows=1)

# Get column names and clean them
columns = df.columns.tolist()
symptom_features = [col for col in columns if col not in ["PATHOLOGY", "URGENCY_LABEL"]]

# Print or save them
print("Number of symptoms:", len(symptom_features))
print(symptom_features)