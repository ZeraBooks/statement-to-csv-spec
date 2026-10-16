# Credit card statement rows: column layout

One row per transaction, with amounts signed from the business's point of view,
so a card file reads the same way as a checking file and the two can be stacked
in one sheet.

## Columns

| Column | Format | Rule |
|---|---|---|
| Date | MM/DD/YYYY | The transaction date, the day the purchase was made. If the statement prints a posting date as well, use the transaction date. |
| Description | Text | As printed on the statement. Quote it if it contains a comma. Leave out the extra line under a foreign purchase that shows the foreign amount and rate; it is detail, not a second charge. |
| Amount | Number, two decimals, no currency symbol, no thousands separator | Charges, fees and interest are negative (money out). Payments and refunds are positive (money in). |
| Cardholder | Text | The name and card ending the charge is printed under. Payments, interest and account-level fees use `Account`. |
| Source file | Text | The PDF file name the row came from, so any row can be traced back to its statement. |

An optional Type column (Charge, Payment, Credit, Fee, Interest) helps when a
statement mixes refunds and payments in one block: a refund is a credit against
an expense, while a payment is a transfer from your bank account.

## What not to turn into rows

- The previous balance, new balance and minimum payment lines
- Year-to-date fee and interest totals
- The interest rate table
- Cardholder subtotal lines (use them to check, not as rows)

## The sign flip

The statement treats your balance as a debt, so a purchase prints as a positive
number and a payment prints with a minus sign or CR. This layout reverses both.

| On the statement | In the file |
|---|---|
| Purchase 86.40 | -86.40 |
| Payment -1,500.00 or 1,500.00 CR | 1500.00 |
| Refund -38.50 | 38.50 |
| Interest charge 6.83 | -6.83 |

## How to tie the file to the statement

The statement's own summary must add up:

    previous balance + charges + fees + interest - payments - credits = new balance

Because the file's amounts are signed the other way, the same check on the
file is:

    previous balance - SUM(Amount) = new balance

If that is off, the difference is usually one missing or doubled line, or a
payment that kept its minus sign. Then check each cardholder: the charges
under their name should equal the subtotal printed for their card.
