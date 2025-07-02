from predict_disease import predict
from treatment_plan import suggest_treatment
from chat_interface import ask_ai
from health_analytics import analyze_health

def main():
    while True:
        print("\n💡 Welcome to HealthAI Terminal Version")
        print("1. Disease Prediction")
        print("2. Treatment Plan Generator")
        print("3. Patient Chat (AI)")
        print("4. Health Analytics (CSV)")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            predict()
        elif choice == '2':
            suggest_treatment()
        elif choice == '3':
            ask_ai()
        elif choice == '4':
            analyze_health()
        elif choice == '5':
            print("Exiting... Stay Healthy!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
