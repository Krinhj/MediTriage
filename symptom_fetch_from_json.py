import json

# Load symptom questions
with open("data/release_evidences.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Sort by keys to match model input
symptom_codes = list(data.keys())

# Interactive prompt for each symptom
symptoms_input = []
for code in symptom_codes:
    question = data[code].get("question_en", f"Symptom {code}")
    answer = input(f"{question} (1 for yes, 0 for no): ")
    symptoms_input.append(int(answer.strip() or "0"))

# Output JSON for Postman
output = {
    "symptoms": symptoms_input
}

print("\nCopy this JSON into Postman:")
print(json.dumps(output, indent=4))