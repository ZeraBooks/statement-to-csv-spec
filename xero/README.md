# Bank statement CSV for a Xero import

Xero imports a bank statement as CSV through Import a Statement on the bank
account, not as a PDF. A file that imports cleanly has five columns (Date,
Amount, Payee, Description, Reference), one signed Amount with money out
negative, plain numbers with no currency sign or thousands separator, and no
Balance or account number column. Before importing, check that the printed
opening balance plus the Amount column equals the printed closing balance.

The steps in Xero, the column assignment and what to look at after the import
are in ZeraBooks' guide,
[import a PDF bank statement into Xero](https://www.zerabooks.com/bank-statement-to-xero).
For the conversion itself, see
[convert a bank statement to CSV](https://www.zerabooks.com/convert-bank-statement-to-csv).

## Files

| File | What it is |
|---|---|
| `sample-xero-ready.csv` | A fictional March 2026 checking statement, account ending 2208, in the five-column layout. Opening balance 8,415.60, closing 7,987.15. |
| `check_xero_csv.py` | Checks a file in this layout before it goes to Xero: header, extra columns, date format, amount format, empty rows, ambiguous dates, and the tie to the printed balances. Python 3, standard library only. |

## Columns

| Column | What goes in it | Example |
|---|---|---|
| Date | MM/DD/YYYY | 03/05/2026 |
| Amount | One signed number, two decimals, money in positive and money out negative | -1180.00 |
| Payee | The merchant or person; if it is already a Xero contact, spell it exactly as the contact | Halvorsen Properties |
| Description | The line as the bank printed it | ACH DEBIT HALVORSEN PROPERTIES |
| Reference | The check number when there is one, otherwise empty | 2041 |

## Run the check

```
python3 check_xero_csv.py sample-xero-ready.csv --opening 8415.60 --closing 7987.15
```

On the sample it exits with 0 and prints:

```
5 lines, amounts sum to -428.45
3 of 5 dates would also read as a valid day-first date; confirm month first when you assign the columns in Xero
8415.60 + (-428.45) = 7987.15, printed closing 7987.15, difference 0.00
Ready to import.
```

The second line is the one people skip. 03/02, 03/05 and 03/11 are valid
dates either way round, so a day-first organisation would book them on 3
February, 3 May and 3 November without an error. Only 03/18 and 03/31 can't be
read day first. A file where every line falls on the 12th or earlier gives no
warning at all in Xero, which is why the script counts them.

## The sample ties

All figures are fictional.

| Line | Amount |
|---|---|
| Opening balance | 8,415.60 |
| ACH credit, Northgate Supply | 3,250.00 |
| Check 2041 | -1,180.00 |
| Comcast Business | -86.45 |
| ACH debit, Halvorsen Properties | -2,400.00 |
| Monthly service fee | -12.00 |
| Closing balance | 7,987.15 |

After the import, the account balance in Xero through March 31 should be
7,987.15. A difference of exactly 8,415.60 means the account started at zero.
A difference of 1,180.00 means the check is missing or in twice; 2,360.00, twice
the check, means it went in with the wrong sign.

## Check it in a spreadsheet

Open the CSV with Amount in column B, type the opening balance in H1 and the
closing balance in H2, then:

| Cell | Formula | Result on the sample |
|---|---|---|
| H3 | `=ROUND(H1+SUM(B2:B)-H2,2)` | 0 |
| H4 | `=SUMPRODUCT(--(DAY(A2:A6)<=12))` | 3 |

Look at the file in a text editor before importing it. Saving it again from
Excel can rewrite the dates and amounts the way Excel displays them, which is
how a clean file picks up a thousands separator.

## FAQ

### Does Xero need the Payee column?

Xero lets you assign each column to a statement field the first time you
import, and keeps that assignment for later files with the same headings. Payee is
worth keeping: it shows on each statement line while you reconcile, and it has to
match an existing contact's name exactly, or Xero treats it as a new one.

### Is this the same as Xero's precoded CSV?

No. A precoded file also carries account codes so Xero can create and
reconcile spend and receive money transactions in one step. This layout holds
only what the statement prints; the coding happens in Xero when you reconcile.

### Can several accounts go in one file?

Not for Xero. A statement import goes into one bank account, so make one file
per account and import each into its own account in Xero.
