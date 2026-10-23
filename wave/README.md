# Statement CSV for a Wave upload

Wave uploads statement files from Accounting, Transactions, More, Upload
transactions. It takes OFX, QBO, QFX and ASO files, and CSV when none of those
is available. It does not take PDFs. A CSV that uploads cleanly has three or
four columns (date, description, and one amount column or separate deposit and
withdrawal columns), column titles in the top row, one currency, no balance or
total rows, and dates Wave can read (YYYY-MM-DD is the safe choice). On a
credit card file Wave wants purchases positive and payments negative, the
opposite of most exports.

The full steps, every CSV error message Wave lists and its fix are in
ZeraBooks' guide, [Wave bank statement import](https://www.zerabooks.com/import/wave-bank-statement-import).
For turning the PDF into rows, see the
[ZeraBooks bank statement converter](https://www.zerabooks.com/bank-statement-converter).

Rules checked against Wave's help center in October 2026.

## Files

| File | What it is |
|---|---|
| `sample-wave-card.csv` | A fictional September 2026 Visa statement, card ending 4410, in Wave's card sign convention. Previous balance 1,245.30, new balance 1,042.44. |

## Columns

| Column | What goes in it | Example |
|---|---|---|
| Date | YYYY-MM-DD, one date column only, no future dates | 2026-09-04 |
| Description | Words, not only numbers | Booking software |
| Amount | Plain number. Bank account: deposits positive, withdrawals negative. Credit card: purchases positive, payments negative | 312.45 |

More than four columns gives "Wave is having difficulty reading the file you
uploaded". Delete balance, type and reference columns before uploading.

## The sample ties

All figures are fictional.

| Line | Statement | Wave Amount |
|---|---|---|
| Previous balance | 1,245.30 | |
| Grooming supply order | purchase 312.45 | 312.45 |
| Booking software | purchase 89.99 | 89.99 |
| Payment, thank you | payment 1,245.30 | -1245.30 |
| Hydraulic table repair | purchase 640.00 | 640.00 |
| New balance | 1,042.44 | |

The Amount column sums to -202.86, which is the change in the balance owed:
1,042.44 - 1,245.30. If the sum comes out as +202.86, the signs are the bank
convention and every card line will land backwards in Wave.

## FAQ

### Can I upload a PDF statement to Wave?

No. Convert the PDF to CSV first, then flip the signs on a card file and
change the dates to YYYY-MM-DD if Wave can't read them.

### Why use one amount column?

Wave reads separate deposit and withdrawal columns, but its help says to merge
them into one column if the upload fails. One signed column avoids the problem.
