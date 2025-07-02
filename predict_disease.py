def predict():
    print("\n🩺 Disease Predictor")
    symptoms = input("Enter your symptoms (comma-separated): ").lower()

    if "fever" in symptoms and "cough" in symptoms:
        print("🤖 Prediction: You might have COVID-19 or Flu.")
    elif "headache" in symptoms and "vomiting" in symptoms:
        print("🤖 Prediction: Possible migraine or food poisoning.")
    else:
        print("❌ Unable to predict. Please consult a doctor.")
