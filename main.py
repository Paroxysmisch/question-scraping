from scrape_sources import scrape_bowl


def main():
    scrape_bowl.scrape('./data/bowls/phys.pdf', 'PHYS-')
    scrape_bowl.scrape('./data/bowls/biol.pdf', 'BIOL-')
    scrape_bowl.scrape('./data/bowls/chem.pdf', 'CHEM-')

    breakpoint()


if __name__ == "__main__":
    main()
