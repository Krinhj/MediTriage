import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load dataset
df = pd.read_csv("ddxplus_triage_labeled.csv")

# Separate features and target
X = df.drop(columns=["PATHOLOGY", "URGENCY_LABEL"])
y = df["URGENCY_LABEL"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\n✅ Accuracy: {accuracy:.4f}")
print("\n🩺 Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Routine", "Urgent", "Emergency"]))

# Save model
joblib.dump(clf, "urgency_model.pkl")
print("\n💾 Model saved to 'urgency_model.pkl'")