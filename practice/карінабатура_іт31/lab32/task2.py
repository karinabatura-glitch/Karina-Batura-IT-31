# Karina Batura, IT-31
import csv
from collections import defaultdict
from tabulate import tabulate

def main():
    print("Karina Batura, IT-31")

    categories_count = defaultdict(int)
    categories_total = defaultdict(float)
    total_count = 0
    total_sum = 0.0

    try:
        with open('data/expenses.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if not row or row[0].strip().startswith('#'):
                    continue
                if row[0].strip().lower() in ('category', 'категорія'):
                    continue

                category = row[0].strip()
                try:
                    amount = float(row[1].strip())
                except (ValueError, IndexError):
                    continue

                categories_count[category] += 1
                categories_total[category] += amount
                total_count += 1
                total_sum += amount
    except FileNotFoundError:
        print("Помилка: файл data/expenses.csv не знайдено.")
        return

    table_data = []
    for cat in sorted(categories_count.keys()):
        table_data.append([cat, categories_count[cat], round(categories_total[cat], 2)])

    table_data.append(["TOTAL", total_count, round(total_sum, 2)])

    headers = ["category", "count", "total"]
    print(tabulate(table_data, headers=headers, tablefmt="github"))

if __name__ == "__main__":
    main()