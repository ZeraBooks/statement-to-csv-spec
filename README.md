# Statement to CSV spec

A bank or credit card statement converts cleanly to CSV when each transaction
is one row with a date, a description and a single signed amount, money out
negative. For a bank account, the rows are complete when the opening balance
plus the sum of the amounts equals the closing balance printed on the
statement. This repo sets out those column layouts, with fictional sample files
that tie.

| Folder | What it is | Guide |
|---|---|---|
| [`google-sheets/`](google-sheets/) | A standard layout for statement rows in Google Sheets, import settings, check formulas and a sample file | [How to get a bank statement into Google Sheets](https://www.zerabooks.com/bank-statement-to-google-sheets) |
| [`credit-cards/`](credit-cards/) | Card statement rows with charges negative and payments positive, a tie-out formula and a sample that ties | [Converting a credit card statement to Excel](https://www.zerabooks.com/credit-card-statement-to-excel) |

All figures are fictional.

## How to use these files

- Each CSV has a header row and opens in Excel, Google Sheets or a text editor.
- Each folder README names the columns and gives the formula that proves the
  sample is complete. Swap in your own rows and the same formula checks them.
- Descriptions that contain a comma are quoted, so the file stays one row per
  transaction.

## License

The content and data in this repository are licensed under
[CC BY 4.0](LICENSE). Free to use and adapt with credit to ZeraBooks.

Maintained by [ZeraBooks](https://www.zerabooks.com).
