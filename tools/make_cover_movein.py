def main():
    import iso
    from cover import render

    render(
        "cover-movein.html",
        "cover-movein.png",
        iso.scene(10),
        "Moving In: Utilities &amp; Setup in Japan",
        "Gas, electricity, water, internet, address registration and your first 30 days",
        [("Illustrated PDF", False), ("5 email templates", False), ("Instant download", True)],
    )

if __name__ == "__main__":
    main()
