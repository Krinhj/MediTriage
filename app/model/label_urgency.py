import pandas as pd

# Load encoded dataset
df = pd.read_csv("ddxplus_encoded.csv")

# Pathology to urgency mapping
urgency_map = {
    "Anaphylaxis": 2,
    "Acute pulmonary edema": 2,
    "Possible NSTEMI / STEMI": 2,
    "Pulmonary embolism": 2,
    "Myocarditis": 2,
    "Pericarditis": 2,
    "Spontaneous pneumothorax": 2,
    "Ebola": 2,
    "Guillain-Barré syndrome": 2,
    "Atrial fibrillation": 2,
    "Unstable angina": 2,
    "Acute COPD exacerbation / infection": 1,
    "Bronchospasm / acute asthma exacerbation": 1,
    "Pneumonia": 1,
    "Influenza": 1,
    "Croup": 1,
    "Tuberculosis": 1,
    "Acute laryngitis": 1,
    "Epiglottitis": 1,
    "Cluster headache": 1,
    "Bronchitis": 1,
    "Whooping cough": 1,
    "Acute dystonic reactions": 1,
    "Localized edema": 1,
    "GERD": 0,
    "Chronic rhinosinusitis": 0,
    "Allergic sinusitis": 0,
    "Stable angina": 0,
    "Larygospasm": 0,
    "Sarcoidosis": 0,
    "HIV (initial infection)": 0,
    "Myasthenia gravis": 0,
    "Inguinal hernia": 0,
    "SLE": 0,
    "Pancreatic neoplasm": 0,
    "Pulmonary neoplasm": 0,
    "Viral pharyngitis": 0,
    "URTI": 0,
    "Bronchiectasis": 0,
    "Chagas": 0,
    "Boerhaave": 0,
    "Panic attack": 0,
    "Spontaneous rib fracture": 0
}

# Add urgency column
df["URGENCY_LABEL"] = df["PATHOLOGY"].map(urgency_map).fillna(0).astype(int)

# Save updated dataset
df.to_csv("ddxplus_triage_labeled.csv", index=False)
print("✅ URGENCY_LABEL column added and dataset saved.")