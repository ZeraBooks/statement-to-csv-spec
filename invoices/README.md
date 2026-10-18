# Invoices, line by line

One row per line item, not one per invoice. The invoice number and date repeat
on every line so the file can be filtered and pivoted. Tax and the invoice
total sit on the last line of each invoice.

Two checks catch almost every misread:

1. Quantity x Unit Price = Line Total, on every line.
2. Sum of Line Totals + Tax = Invoice Total, on every invoice.

In `sample-line-items.csv` (fictional vendors): INV-2041 lines add to 240.75,
plus 19.26 tax is 260.01; INV-2042 lines add to 182.00, plus 14.56 tax is
196.56.

The full guide, including a bills-import layout, is ZeraBooks'
[Invoice PDF to Excel](https://www.zerabooks.com/invoice-to-excel).
