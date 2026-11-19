
import csv
from pathlib import Path

file_path = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "sample_projects.csv"
)

with open(file_path, "r") as file:

    reader = csv.DictReader(file)

    print("PROJECTSHIELD AI")
    print("BUDGET ANALYSIS")
    print("------------------------")

    for project in reader:

        name = project["project_name"]
        budget = float(project["budget"])
        spent = float(project["spent"])

        utilization = (spent / budget) * 100

        print("\nProject:", name)
        print("Budget Utilization:", round(utilization, 2), "%")

        if utilization >= 90:
            print("Status: High Budget Utilization")

        elif utilization >= 75:
            print("Status: Moderate Budget Utilization")

        else:
            print("Status: Low Budget Utilization")
