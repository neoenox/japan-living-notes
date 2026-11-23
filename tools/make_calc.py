def main():
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter as L
    import pathlib

    wb = Workbook(); ws = wb.active; ws.title = "Calculator"
    hdr = PatternFill("solid", fgColor="1F3A5F"); inp = PatternFill("solid", fgColor="FFF8DC")
    sec = PatternFill("solid", fgColor="E8EEF5"); tot = PatternFill("solid", fgColor="DDF0DD")
    thin = Side(style="thin", color="BBBBBB"); bd = Border(left=thin, right=thin, top=thin, bottom=thin)
    white = Font(bold=True, color="FFFFFF"); bold = Font(bold=True)
    Y = '"¥"#,##0'

    ws["A1"] = "Japan Rental Initial Cost Calculator"; ws["A1"].font = Font(bold=True, size=16)
    ws["A2"] = "Fill the yellow cells. Amounts in yen. Months = number of months of rent. Estimates only: confirm with your agent."
    ws["A2"].font = Font(italic=True, color="555555")
    ws["A4"] = "Consumption tax rate"; ws["B4"] = 0.10; ws["B4"].number_format = "0%"; ws["B4"].fill = inp; ws["B4"].border = bd

    cols = range(2, 7)  # B..F = 5 properties
    r = 6
    ws.cell(r, 1, "Item").font = white; ws.cell(r, 1).fill = hdr
    for i, c in enumerate(cols, 1):
        x = ws.cell(r, c, f"Property {i}"); x.font = white; x.fill = hdr; x.alignment = Alignment(horizontal="center")

    rows = [
     ("sec", "INPUTS"),
     ("name", "Property name", None, "text"),
     ("rent", "Monthly rent", 0, Y),
     ("mgmt", "Management / common fee (monthly)", 0, Y),
     ("dep_m", "Security deposit (shikikin), months", 0, "0.0"),
     ("key_m", "Key money (reikin), months", 0, "0.0"),
     ("ag_m", "Agency fee, months of rent (max 1, before tax)", 1, "0.0"),
     ("gu_p", "Guarantor company fee, % of 1 month (rent+mgmt)", 0.5, "0%"),
     ("ins", "Fire insurance (2 years)", 20000, Y),
     ("keyx", "Key exchange fee", 15000, Y),
     ("other", "Other fees (cleaning, support pack, etc.)", 0, Y),
     ("free_m", "Free rent months (negative effect on cost)", 0, "0.0"),
     ("ren_m", "Renewal fee, months (every 2 years)", 0, "0.0"),
     ("sec", "INITIAL COSTS"),
     ("c_first", "First month rent + management fee"),
     ("c_dep", "Security deposit"),
     ("c_key", "Key money"),
     ("c_ag", "Agency fee (incl. tax)"),
     ("c_gu", "Guarantor company fee"),
     ("c_ins", "Fire insurance"),
     ("c_keyx", "Key exchange"),
     ("c_other", "Other fees"),
     ("c_free", "Free rent discount"),
     ("TOTAL", "TOTAL INITIAL COST"),
     ("mult", "Total / monthly rent (x)"),
     ("sec", "COMPARISON"),
     ("month", "Monthly cost (rent + management)"),
     ("y2", "2-year total (initial + 23 more months + renewal fee)"),
     ("y2m", "2-year average per month"),
    ]
    pos = {}
    r += 1
    for row in rows:
        if row[0] == "sec":
            for c in range(1, 7):
                ws.cell(r, c).fill = sec
            ws.cell(r, 1, row[1]).font = bold
        else:
            pos[row[0]] = r
            ws.cell(r, 1, row[1])
            if len(row) > 2:
                for c in cols:
                    x = ws.cell(r, c, row[2]); x.fill = inp; x.number_format = row[3] if row[3] != "text" else "General"
                    x.border = bd
        r += 1

    for c in cols:
        letter = L(c)
        ref = lambda n: f"{letter}{pos[n]}"
        f = {
         "c_first": f"={ref('rent')}+{ref('mgmt')}",
         "c_dep": f"={ref('rent')}*{ref('dep_m')}",
         "c_key": f"={ref('rent')}*{ref('key_m')}",
         "c_ag": f"={ref('rent')}*{ref('ag_m')}*(1+$B$4)",
         "c_gu": f"=({ref('rent')}+{ref('mgmt')})*{ref('gu_p')}",
         "c_ins": f"={ref('ins')}",
         "c_keyx": f"={ref('keyx')}",
         "c_other": f"={ref('other')}",
         "c_free": f"=-{ref('rent')}*{ref('free_m')}",
         "TOTAL": f"=SUM({letter}{pos['c_first']}:{letter}{pos['c_free']})",
         "mult": f'=IF({ref("rent")}>0,{ref("TOTAL")}/{ref("rent")},"")',
         "month": f"={ref('rent')}+{ref('mgmt')}",
         "y2": f"={ref('TOTAL')}+{ref('month')}*23+{ref('rent')}*{ref('ren_m')}",
         "y2m": f"={ref('y2')}/24",
        }
        for n, v in f.items():
            x = ws.cell(pos[n], c, v); x.number_format = "0.0" if n == "mult" else Y; x.border = bd
            if n == "TOTAL": x.fill = tot; x.font = bold
    ws.cell(pos["TOTAL"], 1).font = bold; ws.cell(pos["TOTAL"], 1).fill = tot

    ws.column_dimensions["A"].width = 52
    for c in cols: ws.column_dimensions[L(c)].width = 17
    ws.freeze_panes = "B7"

    n = r + 1
    notes = ["Notes:",
     "- Agency fee: legal cap is 1 month's rent plus tax. Some agencies charge half. Enter the actual figure.",
     "- Deposit is partly returned at move-out after repairs, but it is counted as cash you must pay upfront.",
     "- Mid-month move-in usually prorates the first month. Adjust 'Other fees' or rent if needed.",
     "- Guarantor fee is often 50-100% of one month; some also charge a yearly renewal fee."]
    for i, t in enumerate(notes): ws.cell(n + i, 1, t).font = Font(italic=True, color="555555") if i else bold

    e = wb.create_sheet("Example")
    e["A1"] = "Example: rent ¥80,000, management ¥5,000, deposit 1, key money 1, agency 1, guarantor 50%"; e["A1"].font = bold
    ex = [("First month rent + mgmt",85000),("Deposit",80000),("Key money",80000),("Agency fee (incl. 10% tax)",88000),
          ("Guarantor fee",42500),("Fire insurance",20000),("Key exchange",15000)]
    for i,(a,b) in enumerate(ex, 3):
        e.cell(i,1,a); e.cell(i,2,b).number_format = Y
    e.cell(10,1,"TOTAL").font = bold; e.cell(10,2,"=SUM(B3:B9)").number_format = Y; e.cell(10,2).font = bold
    e.cell(11,1,"As multiple of rent"); e.cell(11,2,"=B10/80000").number_format = "0.0"
    e.column_dimensions["A"].width = 40; e.column_dimensions["B"].width = 16
    wb.save(str(pathlib.Path(__file__).resolve().parent.parent / "initial-cost-calculator.xlsx"))

if __name__ == "__main__":
    main()
