def main():
    import iso
    from cover import render

    render(
        "cover2.html",
        "cover.png",
        iso.cover_art("410 -40 570 510"),
        "Renting an Apartment in Japan",
        "Costs, contracts, email templates and move-in steps for foreigners",
        [("Illustrated PDF", False), ("Excel calculator", False), ("Instant download", True)],
    )

if __name__ == "__main__":
    main()
