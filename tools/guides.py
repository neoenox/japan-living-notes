"""Per-guide configuration for make_pdf.py."""
import figs2


def rental():
    import art
    return dict(
        md="rental-guide-en.md", out="Renting-an-Apartment-in-Japan.pdf",
        cover_title="Renting an<br>Apartment<br>in Japan",
        cover_sub="Costs, contracts, email templates and move-in steps for foreigners",
        badges=["PDF GUIDE", "EXCEL CALCULATOR", "6 EMAIL TEMPLATES"], ap_last="H", n_ch=10,
        toc_extra="Appendices: calculator, glossary, email templates, checklists, phrases, resources",
        scene_map={}, tags={},
        figs={0: figs2.flow(), 1: art.plan_1k_iso() + figs2.whois() + art._minis(), 2: figs2.costs(), 3: figs2.doccards(),
              4: figs2.maisoku(), 7: figs2.timeline(), 8: figs2.lease_timeline()},
        titles={0: "Quick Start", 1: "How Renting Works in Japan", 2: "Know Your Costs", 3: "Can a Foreigner Rent?", 4: "Finding a Place",
                5: "Viewing and Applying", 6: "The Contract", 7: "Move-in", 8: "Living and Moving Out", 9: "FAQ and Red Flags"},
        summary={0: "The 8-step process, how long it takes, and the typical upfront cost.",
                 1: "Who is who, how to read floor plans, building types, and the two kinds of leases.",
                 2: "Every initial cost, monthly costs, and ways to lower the total.",
                 3: "Whether you can rent, the documents you need, and what to do if you are rejected.",
                 4: "Where to search, how to set priorities, and how to read a listing sheet.",
                 5: "What to check at a viewing, how applying works, and what screening involves.",
                 6: "The explanation of important matters and the clauses to read before signing.",
                 7: "Utilities, address registration, garbage rules, and the first weeks.",
                 8: "Renewal, giving notice, move-out costs, and getting your deposit back.",
                 9: "Common questions and the warning signs to watch for."},
        tiles={0: [("3-6", "weeks", "first inquiry to keys"), ("4-6×", "rent", "typical upfront cost"), ("8", "steps", "from budget to keys")],
               1: [("20-25", "㎡", "a typical 1K"), ("2", "years", "usual lease term"), ("1981", "", "newer quake standard")],
               2: [("4-6×", "rent", "typical upfront cost"), ("1", "month + tax", "agency fee cap"), ("0-2", "months", "key money range")],
               3: [("Yes", "", "foreigners can rent"), ("2-7", "days", "typical screening"), ("1+", "year", "visa left is safer")],
               4: [("80", "m = 1 min", "station walk rule"), ("3", "priorities", "pick your top three"), ("1981", "", "ask building year")],
               5: [("3-4", "properties", "per viewing day"), ("2-7", "days", "screening time"), ("In writing", "", "refund of holding fee")],
               6: [("1", "month", "usual notice (sometimes 2)"), ("2", "years", "usual lease term"), ("Read", "first", "the special terms")],
               7: [("14", "days", "address registration"), ("2+", "weeks", "book gas in busy season"), ("1-4", "weeks", "internet installation")],
               8: [("2-4", "months", "renewal papers arrive"), ("1", "month", "usual notice to leave"), ("明細", "", "ask for an itemized bill")],
               9: [("6", "red flags", "to watch for"), ("5", "FAQs", "answered"), ("7", "days", "refund window")]},
        callout={2: ("warn", "Ask for a full written breakdown", "Ask what every line is for before you apply. Be careful with vague items such as &quot;support packages&quot; or &quot;cleaning fees&quot;."),
                 3: ("tip", "Use the right agency", "Start with agencies that say they accept foreign customers. It saves weeks of rejected inquiries."),
                 5: ("warn", "Do not pay large sums at the application stage", "If a small holding fee is requested, ask whether it is refundable and get that in writing."),
                 6: ("tip", "Photograph everything on key day", "Take photos of every scratch and stain and email them to the management company. This protects your deposit later."),
                 8: ("tip", "Ask for an itemized bill", "If the move-out charge seems too high, ask for a detailed breakdown (明細) and compare it with the official guideline.")},
        callout_before={6: "6.4", 8: "8.3"},
    )


def movein():
    f = figs2
    return dict(
        md="moving-in-guide-en.md", out="Moving-In-Utilities-and-Setup-in-Japan.pdf",
        cover_title="Moving In:<br>Utilities &amp;<br>Setup in Japan",
        cover_sub="Gas, electricity, water, internet, address registration and your first 30 days, for foreign residents",
        badges=["PDF GUIDE", "5 EMAIL TEMPLATES", "PRINTABLE CHECKLISTS"], ap_last="E", n_ch=8,
        toc_extra="Appendices: glossary, email templates, checklists, phrases, resources",
        scene_map={0: 0, 1: 5, 2: 10, 3: 3, 4: 2, 5: 11, 6: 9, 7: 7}, tags={7: "30 DAYS"},
        figs={0: f.columns("Your first 30 days", [
                  ("2 weeks before", ["Book gas opening", "Electricity, water", "Order internet", "Book movers"], "#1F3A5F"),
                  ("Key day", ["Photograph damage", "Check appliances", "Breaker on", "Be home for gas"], "#C8372D"),
                  ("Within 14 days", ["Address report", "Health insurance", "Residence card", "My Number card"], "#2E8B8B"),
                  ("Weeks 2-4", ["Mail forwarding", "Bank, phone, school", "Garbage rules", "Internet installed"], "#1F3A5F")],
                  "Three steps have deadlines. Gas is the one that needs you at home."),
              2: f.presence("Who needs to be at home?", [
                  ("Electricity", "電気", "apply online or by phone", False), ("Water", "水道", "waterworks bureau", False),
                  ("Gas", "ガス", "opening visit, about 10-20 min", True), ("Internet", "光", "installation visit may be needed", True)],
                  "Book gas 1-2 weeks ahead. Busy seasons (March, April) fill up."),
              3: f.bring("Bring to the office", [
                  ("id", "Residence card", "front and back"), ("passport", "Passport", "if requested"), ("form", "Notice form", "filled at the counter"),
                  ("seal", "Seal or signature", "ask if needed"), ("phone", "Phone", "for your contact number"), ("shield", "My Number card", "and PIN, if you have one")],
                  "Deadline: within 14 days of starting to live at the new address.")},
        titles={0: "Quick Start", 1: "Before the Move", 2: "Utilities, One by One", 3: "Official Registration", 4: "Money, Phone and Internet",
                5: "Garbage, Noise and Neighbors", 6: "When Something Breaks", 7: "Your First 30 Days"},
        summary={0: "Your first 30 days on one page, and the three steps that have deadlines.",
                 1: "What to book two weeks ahead, what to ask the management company, and key day.",
                 2: "Electricity, water, gas and internet: how to start each, and who must be home.",
                 3: "The 14-day address report, health insurance, My Number, and mail forwarding.",
                 4: "Updating your bank, getting a phone, seals and signatures, and insurance.",
                 5: "Sorting and putting out garbage, noise, neighbors, and building rules.",
                 6: "Who to call, who pays, emergency numbers, and keeping records.",
                 7: "A simple order of tasks from before the move to week four."},
        tiles={0: [("30", "days", "from key day to settled"), ("14", "days", "address report deadline"), ("3", "steps", "that have deadlines")],
               1: [("1-2", "weeks", "to book gas ahead"), ("Every", "scratch", "photograph on key day"), ("1-4", "weeks", "internet installation")],
               2: [("4", "utilities", "gas needs you home"), ("10-20", "min", "gas opening visit"), ("0", "visits", "usually for water and power")],
               3: [("14", "days", "address report"), ("14", "days", "health insurance, if needed"), ("1", "year", "free mail forwarding")],
               4: [("1", "card", "residence card for contracts"), ("Ask", "first", "bank requirements differ"), ("Seal?", "", "ask before you buy one")],
               5: [("4", "categories", "burnable, non, recycle, bulky"), ("AM", "", "put out on the day, by the set time"), ("粗大", "", "bulky waste: book first")],
               6: [("1st", "call", "management company"), ("110", "", "police"), ("119", "", "fire and ambulance")],
               7: [("15", "tasks", "in a simple order"), ("14", "days", "official deadline"), ("4", "weeks", "to be fully settled")]},
        callout={2: ("warn", "Be at home for the gas visit", "Gas opening cannot happen without you or a representative. Book early and choose a time after your main moving work."),
                 3: ("warn", "Do not miss the 14 days", "A late address report or insurance registration can mean back payments, full medical bills, or a fine in principle."),
                 5: ("tip", "Ask for the schedule on key day", "Garbage rules differ by city and building. Ask the management company for the schedule, bags, and station location."),
                 6: ("tip", "Call the management company first", "Not the landlord. Send photos and keep the replies in writing.")},
    )


CONFIGS = {"rental": rental, "movein": movein}
