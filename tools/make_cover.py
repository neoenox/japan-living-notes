import iso
from cover import render

render(
    "cover2.html",
    "cover.png",
    iso.cover_art().replace("410 10 570 460", "410 -40 570 510", 1),
    "Renting an Apartment in Japan",
    "Costs, contracts, email templates and move-in steps for foreigners",
    [("Illustrated PDF", False), ("Excel calculator", False), ("Instant download", True)],
)
