import csv
from collections import Counter
from pathlib import Path

data_file = Path(__file__).with_name("sample_data.csv")

with data_file.open(encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))

label_counts = Counter(row["label"] for row in rows)

print(f"Total labeled reports: {len(rows)}\n")
print("Label distribution:")

for label, count in sorted(label_counts.items()):
    percentage = count / len(rows) * 100
    print(f"- {label}: {count} ({percentage:.1f}%)")
