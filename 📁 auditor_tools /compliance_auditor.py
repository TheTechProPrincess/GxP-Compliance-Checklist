```python
import json
import os

def load_checklist(file_path):
    """Load a GxP checklist from a JSON file."""
    if not os.path.exists(file_path):
        print("Error: Checklist file not found!")
        return []
    
    with open(file_path, "r") as file:
        return json.load(file)["questions"]

def evaluate_compliance(questions):
    """Ask user for responses and calculate compliance score."""
    score = 0
    total = len(questions)

    for q in questions:
        response = input(f"{q['question']} (Yes/No): ").strip().lower()
        if response == "yes":
            score += 1
    
    compliance_percentage = (score / total) * 100
    print(f"\n✅ Compliance Score: {compliance_percentage:.2f}%")

    if compliance_percentage < 80:
        print("⚠️ Warning: Compliance is below recommended standards.")
    else:
        print("✅ You are in compliance!")

def main():
    print("Select a GxP Checklist:")
    print("1. GMP Compliance")
    print("2. GCP Compliance")
    print("3. GLP Compliance")
    
    choice = input("Enter your choice (1/2/3): ").strip()

    checklists = {
        "1": "checklists/gmp_checklist.json",
        "2": "checklists/gcp_checklist.json",
        "3": "checklists/glp_checklist.json"
    }

    if choice in checklists:
        questions = load_checklist(checklists[choice])
        if questions:
            evaluate_compliance(questions)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()