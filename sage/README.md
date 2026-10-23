# Statement CSV for a Sage Accounting import

Sage Accounting imports bank statements from Banking, the arrow beside Connect
to bank, Import statement. It takes CSV, XLS, XLSX, OFX, QIF, ASO, BAI2 and
CAMT053 files into chequing, savings and credit card accounts. It does not read
PDFs. A CSV needs its headers in Sage's order: Date, Description, Money in,
Money out (or Date, Description, Amount with payments out negative). Extra
columns are allowed only under Sage's accepted header names, such as Reference.

The steps, how imported lines are processed and what changed for U.S. users are
in ZeraBooks' guide, [Sage bank statement import](https://www.zerabooks.com/import/sage-bank-statement-import).
ZeraBooks' converter has a Sage-ready format that writes this layout from a PDF
statement: [bank statement converter](https://www.zerabooks.com/bank-statement-converter).

Rules checked against Sage's knowledge base in October 2026.

## Files

| File | What it is |
|---|---|
| `sample-sage-4-column.csv` | A fictional September 2026 chequing statement, account ending 3318, CAD. Opening balance 12,860.40, closing 15,221.05. |

## Columns

| Column | What goes in it | Example |
|---|---|---|
| Date | Separated with slashes, one format for the whole file | 09/05/2026 |
| Description | Text, never blank, on one line | Cheque, parts supplier |
| Money in | Positive number, blank when the line is money out | 3450.00 |
| Money out | Positive number, blank when the line is money in | 1925.00 |
| Reference | Optional: the cheque number | 1043 |

At upload Sage shows a sample line and asks whether it is money entering or
leaving the account. That answer applies to the whole file, so a wrong click
books every payment as a receipt.

## The sample ties

All figures are fictional.

| Line | Money in | Money out | Balance |
|---|---|---|---|
| Opening balance | | | 12,860.40 |
| Deposit, Lonsdale Cycling Club | 3,450.00 | | 16,310.40 |
| Cheque 1043 | | 1,925.00 | 14,385.40 |
| Hydro bill | | 286.15 | 14,099.25 |
| Deposit, card settlements | 1,140.75 | | 15,240.00 |
| Monthly service fee | | 18.95 | 15,221.05 |
| Totals | 4,590.75 | 2,230.10 | |

12,860.40 + 4,590.75 - 2,230.10 = 15,221.05, the printed closing balance.

## FAQ

### Can I import an XLSX instead of CSV?

Yes, but Sage reads only the first tab, and the same header rules apply.

### Can one file hold several accounts?

No. For OFX or ASO files with several accounts, Sage imports only the first.
Make one file per account.
