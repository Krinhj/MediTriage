def classify_urgency(symptom_description):
    #Dummy Logic based on keywords
    keywords = {
        "emergency": ["chest pain", "shortness of breath", "severe headache", "unconscious", "severe bleeding"],
        "urgent": ["fever", "persistent vomiting", "severe pain", "difficulty breathing", "swelling"],
        "routine": ["cough", "cold", "mild headache", "sore throat", "minor cuts", "checkup"],
    }

    symptom_description = symptom_description.lower()

    for word in keywords["emergency"]:
        if word in symptom_description:
            return "Emergency"
        
    for word in keywords["urgent"]:
        if word in symptom_description:
            return "Urgent"
        
    for word in keywords["routine"]:
        if word in symptom_description:
            return "Routine"
        
    return "Unclear / Further evaluation needed"
    