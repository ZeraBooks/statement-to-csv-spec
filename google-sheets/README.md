# Bank statement CSV in Google Sheets

Google Sheets can't import a PDF, so a bank statement goes in as a CSV: set
the spreadsheet locale to United States, use File, Import, Upload with a comma
separator, and keep number conversion on. Then check that the opening balance
plus the Amount column equals the printed closing balance.

How to import a bank statement CSV into Google Sheets so dates and amounts
arrive as real values, and a set of formulas that check the rows against the
statement's printed balances. Step-by-step guide with screenshots:
[Bank statement to Google Sheets](https://www.zerabooks.com/bank-statement-to-google-sheets).

## Files

| File | What it is |
|---|---|
| `sample-standard.csv` | A fictional March 2026 checking statement, Standard layout: Date, Description, Amount. Opening balance 8,412.90, closing 8,675.55. One description contains a comma and is quoted. |

## Import settings

1. File, Settings, Locale: United States (the file uses MM/DD/YYYY and a period
   as the decimal mark). Set this before importing.
2. File, Import, Upload.
3. Separator type: Comma, or Detect automatically.
4. Keep "Convert text to numbers, dates, and formulas" ticked.
5. Import location: Insert new sheet(s), or Append to current sheet to stack
   months.

## Check formulas

Imported at A1: Date in A, Description in B, Amount in C (money out negative).
Type the printed opening balance in G1 and the printed closing balance in G2.

| Cell | Formula | Result on the sample |
|---|---|---|
| G3 | `=ROUND(G1+SUM(C2:C)-G2,2)` | 0 (every row arrived) |
| E2, filled down | `=$G$1+SUM($C$2:C2)` | last row 8675.55 |
| G5 | `=SUMIF(C2:C,">0")` | 6250.00 money in |
| G6 | `=SUMIF(C2:C,"<0")` | -5987.35 money out |
| G8 | `=SUMIFS(C2:C,A2:A,">="&DATE(2026,3,1),A2:A,"<"&DATE(2026,4,1))` | 262.65 net for March |

Delete row 6 (the 48.20 refund) and G3 shows -48.20: the check returns the
amount of the missing line.

## Common breakages

| Symptom | Cause | Fix |
|---|---|---|
| 03/02/2026 shows as 3 February; 03/14/2026 stays as text | Locale reads dates day first | Locale: United States, import again |
| -1234.56 arrives as text or 123456 | Locale uses a comma as the decimal mark | Same |
| SUM returns 0 | Conversion box unticked | Import again with it ticked |
| Everything in column A | Separator set to Tab or Custom | Comma |
| Last month replaced | Import location: Replace current sheet | Append or Insert new sheet(s) |

## Notes

- Group by month in QUERY with `month(A)+1`; the query language counts months
  from 0.
- A description beginning with `=` or `+` should carry a leading apostrophe so
  Sheets keeps it as text.

## FAQ

### Can Google Sheets import a PDF bank statement?

No. File, Import accepts CSV, TSV, text and spreadsheet files, not PDFs, so the
statement has to be converted to one of those first.

### Why are my dates wrong after importing a bank statement into Google Sheets?

The spreadsheet's locale reads dates day first. In a file written as MM/DD/YYYY,
03/02/2026 is March 2, so set File, Settings, Locale to United States and import
again.

### Can I add a category column to a bank statement in Google Sheets?

Yes. Add it after the import, to the right of Amount, so the check formulas keep
pointing at the right columns.
