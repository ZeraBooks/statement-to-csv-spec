# Credit card statement to CSV

A credit card statement becomes a usable CSV when every transaction is one row
with Date, Description, Amount, Cardholder and Source file, and the amounts are
flipped to the business's point of view: charges negative, payments and refunds
positive. The file is complete when previous balance + charges + fees +
interest - payments - credits equals the printed new balance. ZeraBooks' guide,
[Credit card statement to Excel](https://www.zerabooks.com/credit-card-statement-to-excel),
covers the lines that trip up a conversion and how different issuers lay out
their statements.

## Files

| File | What it is |
|---|---|
| `column-layout.md` | The five columns, the sign rule, which statement lines are not transactions, and the tie-out formula. |
| `sample-statement.csv` | A fictional business card statement for March 15 to April 14, 2026, with two cardholders, a payment, a refund, a foreign purchase with its fee, and an interest charge. The Staples row shows how a description with a comma is quoted. |

## The sample ties

All figures are fictional.

| Statement summary | Amount |
|---|---|
| Previous balance | 1,842.17 |
| + Charges | 1,526.15 |
| + Fees | 9.12 |
| + Interest | 6.83 |
| - Payments | 1,500.00 |
| - Credits | 38.50 |
| = New balance | 1,845.77 |

In the file, the amounts sum to -3.60, and 1,842.17 - (-3.60) = 1,845.77.

| Cardholder | Charges | Credits |
|---|---|---|
| J. Rivera 1004 | 401.77 | 38.50 |
| M. Chen 1012 | 1,124.38 | 0.00 |
| Account | 15.95 (fee and interest) | 1,500.00 (payment) |

## Check it in a spreadsheet

Open the CSV with Date in A and Amount in C, type the previous balance in G1
and the new balance in G2, then:

| Cell | Formula | Result on the sample |
|---|---|---|
| G3 | `=ROUND(G1-SUM(C2:C)-G2,2)` | 0 |
| G4 | `=-SUMIFS(C2:C,D2:D,"M. Chen 1012",C2:C,"<0")` | 1124.38 |

Delete the refund row and G3 shows 38.50, the amount of the missing line.
