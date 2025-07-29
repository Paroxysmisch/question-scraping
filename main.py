import pdfplumber


def main():
    pdf = pdfplumber.open("jmc_25")
    page = pdf.pages[1]
    lines = page.extract_text_lines()

    im = page.to_image(resolution=163)
    im.draw_rects(lines)
    im.show()


    breakpoint()


if __name__ == "__main__":
    main()
