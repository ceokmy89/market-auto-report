from collect_market import fetch_data
from datetime import datetime

def generate_report():
    df = fetch_data()
    today = datetime.now().strftime("%Y-%m-%d")

    report = f"# Daily Market Report ({today})\n\n"

    for _, row in df.iterrows():
        emoji = "📈" if row["Change(%)"] > 0 else "📉"
        report += f"- {row['Index']}: {row['Close']} ({row['Change(%)']}%) {emoji}\n"

    with open("daily_report.md", "w") as f:
        f.write(report)

    print("Report generated.")

if __name__ == "__main__":
    generate_report()
