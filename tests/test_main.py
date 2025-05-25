from main import generate_payout_report


def test_payout_report(tmp_path):
    file1 = tmp_path / "data1.csv"
    file1.write_text(
        "id,email,name,department,hours_worked,hourly_rate\n"
        "1,alice@example.com,Alice Johnson,Marketing,160,50\n"
        "2,bob@example.com,Bob Smith,Design,150,40\n"
    )
    report = generate_payout_report([file1])
    assert report["Marketing"]["total"] == 8000
    assert report["Design"]["total"] == 6000
