import json

def load_compliance_data(file_path):
    """Load compliance checklist data from a JSON file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading compliance data: {e}")
        return None

def audit_compliance(data):
    """Check compliance based on the loaded data and return results."""
    results = {"passed": [], "failed": []}

    for category, checks in data.items():
        for check, status in checks.items():
            if status.lower() == "yes":
                results["passed"].append(f"{category}: {check}")
            else:
                results["failed"].append(f"{category}: {check}")

    return results

def generate_report(results):
    """Generate and print a compliance report."""
    print("\n🔍 GxP Compliance Audit Report")
    print("=" * 40)

    print("\n✅ Passed Checks:")
    for check in results["passed"]:
        print(f" - {check}")

    print("\n❌ Failed Checks:")
    for check in results["failed"]:
        print(f" - {check}")

    print("\n📌 Compliance Audit Complete.\n")

if __name__ == "__main__":
    compliance_data = load_compliance_data("compliance_data.json")
    
    if compliance_data:
        audit_results = audit_compliance(compliance_data)
        generate_report(audit_results)
