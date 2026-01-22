# Excel — Lecture Notes

## What is Excel?
- **Microsoft Excel** is a spreadsheet application used to organize, analyse, visualize, and store tabular data. It supports formulas, functions, charts, pivot tables, and basic automation (macros).

## Workbook terminology
- **Workbook:** The Excel file (e.g., `file.xlsx`).
- **Worksheet (sheet):** A single tab within a workbook containing a grid of cells.
- **Cell:** Intersection of a row and column (e.g., `A1`).
- **Range:** A group of cells (e.g., `A1:B10`).
- **Formula bar:** Enter and edit formulas.
- **Named range:** A human-readable name pointing to a range.

## Data Types
- Number (integers, decimals)
- Text (strings)
- Date / Time
- Boolean (TRUE / FALSE)
- Error values (`#DIV/0!`, `#N/A`, `#REF!`, etc.)

## Basic Operations
- Enter values directly in cells, use Autofill to extend sequences.
- Sort and Filter data via the Data tab or `Ctrl+Shift+L` (Windows) / `Cmd+Shift+F` (macOS variant).
- Format cells (number format, font, borders, conditional formatting).
- Freeze panes (keep headers visible) and split windows for navigation.

## Formulas & References
- Formulas start with `=`. Example: `=A1+B1`.
- **Relative reference:** `A1` — changes when copied.
- **Absolute reference:** `$A$1` — fixed when copied.
- Mixed references: `$A1` or `A$1`.

## Important Functions (with examples)
- Aggregation: `SUM`, `AVERAGE`, `MIN`, `MAX`, `COUNT`, `COUNTA`
```text
=SUM(A1:A10)
=AVERAGE(B1:B20)
```
- Conditional: `IF`, `IFS`, `SUMIF`, `SUMIFS`, `COUNTIF`, `COUNTIFS`
```text
=IF(C2>100,"High","Low")
=SUMIFS(Sales!C:C, Sales!A:A, "2025", Sales!B:B, "Region1")
```
- Lookup & reference: `VLOOKUP`, `HLOOKUP`, `XLOOKUP`, `INDEX`, `MATCH`
```text
=VLOOKUP("Key", A2:D100, 4, FALSE)
=XLOOKUP(E2, A2:A100, C2:C100, "Not found")
=INDEX(C2:C100, MATCH(E2, A2:A100, 0))
```
- Text functions: `CONCAT`, `TEXTJOIN`, `LEFT`, `RIGHT`, `MID`, `LEN`, `TRIM`
- Date functions: `TODAY()`, `NOW()`, `DATE`, `EDATE`, `DATEDIF`
- Logical & error handling: `AND`, `OR`, `NOT`, `IFERROR`

## Tables & Structured References
- Convert ranges to a Table (`Insert > Table`) to get filtering, structured references, and automatic expansion.
- Example structured reference: `=SUM(Table1[Amount])`.

## PivotTables & Charts
- **PivotTable:** Summarize and aggregate large datasets interactively (drag fields to Rows/Columns/Values/Filters).
- **Charts:** Create visualizations (column, line, pie, scatter). Use `Recommended Charts` for suggestions.

## Data Tools
- **Data Validation:** Restrict allowed values in cells (drop-down lists).
- **Conditional Formatting:** Apply visual rules (color scales, icon sets) based on cell values.
- **What-If Analysis:** Goal Seek, Data Tables, Scenario Manager for exploring outcomes.
- **Power Query (Get & Transform):** Extract, transform, and load (ETL) data from files, databases, and web sources.

## Automation & Advanced
- **Macros / VBA:** Automate repetitive tasks via recorded macros or VBA scripting.
- **Power Pivot / DAX:** Advanced data modelling and measures for large datasets.
- **Office Scripts (online) / Add-ins:** Modern automation and extensions.

## Collaboration & Sharing
- Co-authoring in OneDrive/SharePoint allows simultaneous editing.
- Protect sheets/workbook and set permissions when sharing.

## Common Shortcuts (Windows / macOS)
- Copy: `Ctrl+C` / `Cmd+C`  — Paste: `Ctrl+V` / `Cmd+V`
- Undo: `Ctrl+Z` / `Cmd+Z`
- Jump to last cell: `Ctrl+End` / `Cmd+Down` (macOS variants exist)
- Select entire column/row: `Ctrl+Space` / `Shift+Space`
- Insert new row: `Ctrl+Shift+Plus` / `Cmd+Shift+K` (app-specific)

## Best Practices
- Keep raw data in a separate sheet; do calculations in another sheet.
- Use named ranges and Tables for clarity and robustness.
- Avoid hard-coding values inside formulas; use references.
- Document assumptions and keep a changelog for critical workbooks.
- Validate data and use checksums / totals to detect errors.

## Sample Scenarios
- Calculate monthly revenue growth:
```text
Previous = B2
Current  = C2
Growth   = (C2-B2)/B2
```
- Basic lookup for product price:
```text
=XLOOKUP(E2, Products[ID], Products[Price], "Not found")
```

## Resources
- Microsoft Excel documentation: https://support.microsoft.com/excel
- Free tutorials: Excel Easy, Chandoo.org, YouTube walkthroughs

---

Prepared as concise lecture notes on Microsoft Excel for classroom or self-study.

