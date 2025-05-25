from pathlib import Path
import argparse
from collections import defaultdict


def read_csv(file_path: Path):
    if not file_path.exists():
        raise FileNotFoundError(f"Файл {file_path} не найден")
    with open(file_path, "r") as f:
        lines = f.readlines()
    headers = [header.strip() for header in lines[0].split(",")]
    rows = []
    for line in lines[1:]:
        row = [col.strip() for col in line.split(",")]
        rows.append(dict(zip(headers, row)))
    return headers, rows


def get_salary_columns(headers):
    rate_keys = ["hourly_rate", "rate", "salary"]
    hours_key = "hours_worked"
    rate_key = next((key for key in rate_keys if key in headers), None)
    return hours_key, rate_key


def process_employee(row, hours_key, rate_key):
    try:
        if rate_key == "salary":
            salary = float(row[rate_key])
            hours = 1
        else:
            hours = float(row[hours_key])
            rate = float(row[rate_key])
            salary = hours * rate
        department = row["department"]
        return {"department": department, "salary": salary}
    except KeyError as e:
        raise ValueError(f"Missing column: {e}")


def generate_payout_report(files):
    departments = defaultdict(lambda: {"total": 0.0, "count": 0})
    for file in files:
        headers, rows = read_csv(file)
        hours_key, rate_key = get_salary_columns(headers)
        if not hours_key or not rate_key:
            raise ValueError(f"Invalid columns in file {file}")
        for row in rows:
            data = process_employee(row, hours_key, rate_key)
            departments[data["department"]]["total"] += data["salary"]
            departments[data["department"]]["count"] += 1
    return departments


def print_payout_report(report_data):
    print("department,employees,total")
    for dept, data in sorted(report_data.items()):
        total = int(data["total"]) if data["total"].is_integer() else data["total"]
        print(f"{dept},{data['count']},{total}")


def main():
    parser = argparse.ArgumentParser(description="Generate employee reports.")
    parser.add_argument("files", nargs="+", help="CSV files with employee data")
    parser.add_argument("--report", required=True, help="Type of report to generate")
    args = parser.parse_args()

    files = [Path(file) for file in args.files]

    for file in files:
        if not file.exists():
            raise FileNotFoundError(f"File '{file}' does not exist.")

    if args.report != "payout":
        raise ValueError("Unsupported report type")

    report_data = generate_payout_report(files)
    print_payout_report(report_data)


if __name__ == "__main__":
    main()
