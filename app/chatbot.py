from app.triage_dummy import classify_urgency

def run_chat():
    print("Welcome to MediTriage - Your Symptom Checker!")
    name = input("Please enter your name: ")
    print(f"Hello, {name}! Let's get started with your symptoms.")

    symptoms = input("Please describe your symptoms: ")

    urgency = classify_urgency(symptoms)
    print(f"Based on your symptoms, the urgency level is: ***{urgency.upper()}***")

    print("Thank you for using MediTriage. Please consult a healthcare professional for further assistance.")