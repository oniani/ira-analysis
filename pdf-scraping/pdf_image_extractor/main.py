import argparse
from pdf_image_extractor import PDFImageExtractor


def main():
    """The main function."""
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process the arguments.")

    # Number of slots in the Galton board
    parser.add_argument(
        "--organized",
        type=bool,
        default=False,
        help="determines whether the organization extraction",
    )

    # Get the arguments
    args = parser.parse_args()

    # Create the ImageExtractor object
    extractor = PDFImageExtractor(path="./pdf/")

    # If the keyword 'organized' is set to 'True'
    if args.organized:
        extractor.extract(organized=True)
    else:
        extractor.extract()


if __name__ == "__main__":
    main()
