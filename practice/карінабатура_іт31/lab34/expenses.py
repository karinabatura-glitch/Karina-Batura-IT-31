# Karina Batura, IT-31
import csv
from collections import defaultdict

def parse_line(line: str) -> dict:
    parts = line.strip().split(';')
    if len(parts) != 4:
        raise ValueError("Неправильна кількість полів у рядку")
    
    date, category, amount_str, comment = parts
    try:
        amount = float(amount_str)
    except ValueError:
        raise ValueError("Сума повинна бути числом")
        
    return {
        "date": date.strip(),
        "category": category.strip(),
        "amount": amount,
        "comment": comment.strip()
    }

def load_expenses(path) -> list:
    """Читає файл (роздільник коми або крапки з комою), пропускає коментарі та порожні рядки."""
    records = []
    with open(path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue
            
            line_joined = ",".join(row).strip()
            if line_joined.startswith('#') or line_joined.lower().startswith('category') or line_joined.lower().startswith('категорія'):
                continue
            if len(row) >= 4:
                line_str = f"{row[0].strip()};{row[1].strip()};{row[2].strip()};{row[3].strip()}"
            else:
                line_str = ";".join(row)

            try:
                record = parse_line(line_str)
                records.append(record)
            except ValueError:
                continue
    return records

def total_by_category(records: list) -> dict:
    """Приймає список словників і повертає словник {category: total}, суми округлені до двох знаків."""
    totals = defaultdict(float)
    for record in records:
        totals[record["category"]] += record["amount"]
    
    return {cat: round(val, 2) for cat, val in totals.items()}