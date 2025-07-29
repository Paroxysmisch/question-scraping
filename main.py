from scrape_sources import scrape_bowl


def main():
    scrape_bowl.scrape('bowls/phys.pdf', 'PHYS-')

    breakpoint()


if __name__ == "__main__":
    main()
