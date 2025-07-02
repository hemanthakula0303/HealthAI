def suggest_treatment():
    print("\n💊 Treatment Plan Generator")

    while True:
        condition = input("Enter your diagnosed condition (or type 'exit' to quit): ").lower().strip()

        if condition == "exit":
            print("👋 Exiting Treatment Plan Generator.")
            break

        if not condition:
            print("⚠️ Please enter a condition.")
            continue

        if "malaria" in condition:
            print("📋 Treatment Plan for Malaria:\n"
                  "- Medications: Chloroquine or ACT\n"
                  "- Lifestyle: Hydration and rest\n"
                  "- Tests: Blood smear, RDT")

        elif "dengue" in condition:
            print("📋 Treatment Plan for Dengue:\n"
                  "- Medications: Paracetamol (no aspirin)\n"
                  "- Lifestyle: Rest and fluids\n"
                  "- Tests: NS1, platelet count")

        elif "covid" in condition or "covid-19" in condition:
            print("📋 Treatment Plan for COVID-19:\n"
                  "- Medications: Paracetamol, antivirals if prescribed\n"
                  "- Lifestyle: Isolate, hydrate, monitor SPO2\n"
                  "- Tests: RT-PCR")

        elif "diabetes" in condition:
            print("📋 Treatment Plan for Diabetes:\n"
                  "- Medications: Metformin or insulin\n"
                  "- Lifestyle: Low sugar diet, exercise\n"
                  "- Tests: FBS, HbA1c")

        elif "typhoid" in condition:
            print("📋 Treatment Plan for Typhoid:\n"
                  "- Medications: Azithromycin or Cefixime\n"
                  "- Lifestyle: Soft food, fluids\n"
                  "- Tests: Widal, blood culture")

        elif "asthma" in condition:
            print("📋 Treatment Plan for Asthma:\n"
                  "- Medications: Inhalers (Salbutamol)\n"
                  "- Lifestyle: Avoid triggers\n"
                  "- Tests: Spirometry")

        else:
            print("❌ Condition not recognized. Please consult a healthcare provider.")

        print("\n------------------------------------------")
