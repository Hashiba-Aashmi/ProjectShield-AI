
import csv
from pathlib import Path

# Locate the dataset
file_path = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "sample_projects.csv"
)

# Read project data
with open(file_path, "r") as file:
    reader = csv.DictReader(file)

    print("PROJECTSHIELD AI")
    print("-------------------------")

    for project in reader:
        planned = float(project["planned_progress"])
        actual = float(project["actual_progress"])

        difference = planned - actual

        print("\nProject:", project["project_name"])
        print("Planned Progress:", planned, "%")
        print("Actual Progress:", actual, "%")
        print("Progress Gap:", difference, "percentage points")

        if difference > 10:
            print("Status: Needs Attention")
        else:
            print("Status: On Track")
