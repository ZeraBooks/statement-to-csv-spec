"""Check a bank statement CSV before importing it into Xero.

Looks for the things that make a Xero statement import go wrong: an
unexpected header, a Balance or account number column, dates that aren't
MM/DD/YYYY, amounts with a currency sign or thousands separator, and empty
rows. It also counts dates whose day is 12 or lower, the ones a day-first
organisation would read as a different date without complaint.

With --opening and --closing (the printed statement balances) it also checks
that the file ties: opening + sum of Amount = closing.

Usage:
  python3 check_xero_csv.py sample-xero-ready.csv --opening 8415.60 --closing 7987.15
Python 3, standard library only.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from datetime import datetime
from decimal import Decimal

EXPECTED = ["Date", "Amount", "Payee", "Description", "Reference"]
PLAIN_AMOUNT = re.compile(r"^-?\d+\.\d{2}$")


def check(path: str, opening: Decimal | None, closing: Decimal | None) -> bool:
    problems = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    if header != EXPECTED:
        problems.append(f"Header is {header}, expected {EXPECTED}")
    for name in header:
        if name.strip().lower() in ("balance", "running balance", "account", "account number"):
            problems.append(f"Remove the {name} column; Xero works out the balance itself")

    total = Decimal("0")
    ambiguous = 0
    for n, row in enumerate(rows, start=2):
        if not any(cell.strip() for cell in row):
            problems.append(f"Row {n} is empty")
            continue
        record = dict(zip(header, row))
        date, amount = record.get("Date", ""), record.get("Amount", "")
        try:
            parsed = datetime.strptime(date, "%m/%d/%Y")
            if parsed.day <= 12 and parsed.day != parsed.month:
                ambiguous += 1
        except ValueError:
            problems.append(f"Row {n}: date {date!r} is not MM/DD/YYYY")
        if PLAIN_AMOUNT.match(amount):
            total += Decimal(amount)
        else:
            problems.append(f"Row {n}: amount {amount!r} is not a plain number with two decimals")

    print(f"{len(rows)} lines, amounts sum to {total}")
    if ambiguous:
        print(f"{ambiguous} of {len(rows)} dates would also read as a valid day-first date; "
              "confirm month first when you assign the columns in Xero")
    if opening is not None and closing is not None:
        diff = opening + total - closing
        print(f"{opening} + ({total}) = {opening + total}, printed closing {closing}, difference {diff}")
        if diff != 0:
            problems.append(f"File does not tie to the statement; off by {diff}")

    for p in problems:
        print("Problem:", p)
    print("Ready to import." if not problems else "Fix the problems above before importing.")
    return not problems


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_file")
    ap.add_argument("--opening", type=Decimal)
    ap.add_argument("--closing", type=Decimal)
    a = ap.parse_args()
    sys.exit(0 if check(a.csv_file, a.opening, a.closing) else 1)
