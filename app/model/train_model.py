import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Step 1: Load encoded data
df = pd.read_csv("ddxplus_encoded.csv")

# Step 2: Split features and labels
x = df.drop("PATHOLOGY", axis=1)
y = df["PATHOLOGY"]

# Step 3: Split into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y, random_state=42)

# Step 4: Train Model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(x_train, y_train)

# Step 5: Evaluate
y_pred = clf.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 6: Save model
joblib.dump(clf, "triage_model.pkl")
print("\nModel saved to 'triage_model.pkl'.")