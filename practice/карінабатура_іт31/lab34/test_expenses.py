# Karina Batura, IT-31
import pytest
from expenses import parse_line, load_expenses, total_by_category

def test_parse_line_valid():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert record["category"] == "food"
    assert record["amount"] == 85.5
    assert record["date"] == "2026-09-21"
    assert record["comment"] == "lunch"

# Завдання 3. 
def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;abc;lunch")

def test_parse_line_bad_fields_count():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50") # замало полів

# Завдання 4. Параметризований тест для parse_line на 5 рядках
@pytest.mark.parametrize(
    "line, expected_category, expected_amount",
    [
        ("2026-09-21;food;85.50;lunch", "food", 85.50),
        ("2026-09-22;transport;50.00;bus", "transport", 50.00),
        ("2026-09-23;fun;300.50;cinema", "fun", 300.50),
        ("2026-09-24;food;120.00;groceries", "food", 120.00),
        ("2026-09-25;transport;35.00;metro", "transport", 35.00),
    ]
)
def test_parse_line_parametrized(line, expected_category, expected_amount):
    record = parse_line(line)
    assert record["category"] == expected_category
    assert record["amount"] == expected_amount

# Завдання 5. Тест з тимчасовим файлом (tmp_path)
def test_total_by_category_tmp(tmp_path):
    path = tmp_path / "expenses.csv"
    path.write_text(
        "# date;category;amount;comment\n"
        "2026-09-21;food;85.50;lunch\n"
        "\n"
        "2026-09-22;food;14.50;coffee\n",
        encoding="utf-8",
    )
    totals = total_by_category(load_expenses(path))
    assert totals == {"food": 100.0}

# Перевірка на реальному файлі data/expenses.csv
def test_total_by_category_real_file():
    path = "data/expenses.csv"
    records = load_expenses(path)
    totals = total_by_category(records)
    # Перевіряємо, що словник не порожній та категорії пораховані
    assert isinstance(totals, dict)
    assert len(totals) > 0