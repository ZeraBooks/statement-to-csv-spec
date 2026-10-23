# Statement CSV for a Zoho Books import

Zoho Books imports CSV, TSV, OFX, QIF, CAMT.053, CAMT.054 and MT940 statements
into bank and credit card accounts you created by hand, from Banking, the
account, the Gear icon, Import Statement. Its PDF import works only for a short
list of named banks. For a CSV, pick the Amount Column Type that matches the
file: Single Column with Negative Values for one signed amount column, Double
Column for separate deposit and withdrawal columns. Zoho rejects minus signs
with the other two settings.

The steps, every import error Zoho documents and its fix are in ZeraBooks'
guide, [Zoho Books bank statement import](https://www.zerabooks.com/import/zoho-books-bank-statement-import).
For a PDF from any bank, see the
[ZeraBooks bank statement converter](https://www.zerabooks.com/bank-statement-converter).

Rules checked against Zoho's help pages in October 2026.

## Files

| File | What it is |
|---|---|
| `sample-zoho-single-column.csv` | A fictional October 2026 checking statement, account ending 2207, for the Single Column with Negative Values setting. Opening balance 6,420.18, closing 7,792.43. |

## Columns

| Column | What goes in it | Example |
|---|---|---|
| Date | One format for the whole file. If Zoho reports "Incorrect date format", its fix is DD-MM-YYYY | 10/03/2026 |
| Description | The line as the bank printed it | Paper supplier ACH |
| Amount | One signed number: deposits positive, withdrawals negative | -415.60 |

Zoho matches these headers to its fields on the Map Fields step. Tick "Save
these selections for use during future imports" if you import monthly.

## The sample ties

All figures are fictional.

| Line | Amount | Balance |
|---|---|---|
| Opening balance | | 6,420.18 |
| Deposit, Ridgeway School District | 2,300.00 | 8,720.18 |
| Paper supplier ACH | -415.60 | 8,304.58 |
| Rent, online transfer | -1,180.00 | 7,124.58 |
| Deposit, card settlements | 760.25 | 7,884.83 |
| Phone bill | -92.40 | 7,792.43 |

The Amount column sums to 1,372.25, and 6,420.18 + 1,372.25 = 7,792.43, the
printed closing balance.

## FAQ

### Why are some lines missing after the import?

Zoho excludes duplicates of lines already in the account by default. The count
shows under Duplicates on the account's Dashboard tab.

### How do I undo a wrong import?

Gear icon, Undo Last Import, check the lines it lists, then Undo Import.
