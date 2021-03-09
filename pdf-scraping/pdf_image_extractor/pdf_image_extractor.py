"""
File:   pdf_image_extractor.py
Author: David Oniani
(c) 2019
Created on May 28, 2019, 09:25 PM

License:
    The code is licensed under MIT License. Please read the LICENSE file in
    this distribution for details regarding the licensing of this code.

Description:
    This module implements 'PDFImageExctractor' class to extract images from an
    arbitrary number of PDF files. It relies on the 'fitz' module. In order to
    install the 'fitz' module, run the command: 'pip3 install pymupdf'. Also,
    make sure that the 'fitz' package is not installed. In other words, run the
    command the command 'pip3 uninstall fitz'. If there are still some errors
    with the package, try running: 'pip3 uninstall pymupdf; pip3 install
    pymupdf'.

NOTE: For historical reasons, 'pymupdf' package is called 'fitz'.
"""

import os
import shutil

from typing import Tuple
from PIL import Image

import fitz


class PDFImageExtractor:
    """This class helps to extract images from the PDF files."""

    def __init__(self, path=".") -> None:
        """Initializer handles the filename collection process."""
        # A path where all the PDF files are stored
        self._path = path

        # Get the list of all pdf filenames in the specified path
        self._filenames = [
            f
            for f in os.listdir(path)
            if os.path.isfile(os.path.join(path, f))
            and f.lower().endswith("pdf")
        ]

    @classmethod
    def crop(cls, imgpath: str, coords: Tuple[int], saveloc: str):
        """Crop an image.

        Parameters:
            imgpath: The path to the image to edit
            coords: A tuple of x/y coordinates (x1, y1, x2, y2)
            saved_location: Path to save the cropped image
        """
        image_obj = Image.open(imgpath)
        cropped_image = image_obj.crop(coords)
        cropped_image.save(saveloc)

    def extract(
        self, destination: str = "extracted", organized: bool = False
    ) -> None:
        """Extract images from PDF files.

        Parameters
        ----------
        destination : str
            Specifies the directory name for all the extracted images.

        organized: bool
            Note that if the 'organized' keyword is set to 'True', the
            function creates a new folder for each PDF file and puts
            its images in that folder. The destination folder 'extracted'
            will therefore contain folders instead of images. Below is
            the miniature demonstration of how the 'extracted' directory
            looks.

            /extracted
            /extracted/pdf_x/pdf_x_1.png
            /extracted/pdf_x/pdf_x_2.png
            /extracted/pdf_x/pdf_x_3.png
            ...
            /extracted/pdf_z/pdf_z_1.png
            /extracted/pdf_z/pdf_z_2.png
            /extracted/pdf_z/pdf_z_3.png

            If the 'organized' keyword is set to 'False', extract function
            creates one folder and drops all extracted images, regardless
            of where these images came from. Below is the miniature
            demonstration of how the 'extracted' directory looks.

            /extracted
            /extracted/pdf_x_1.png
            /extracted/pdf_x_2.png
            /extracted/pdf_x_3.png
            ...
            /extracted/pdf_z_1.png
            /extracted/pdf_z_2.png
            /extracted/pdf_z_3.png
        """
        # Delete the directory if it exists
        if os.path.isdir(destination):
            shutil.rmtree(destination)

        # The directory for keeping extracted images
        os.mkdir(destination)

        # One needs to have a folder with all PDF files in it
        os.chdir(self._path)

        # For each filename in the list of PDF filenames
        for index, filename in enumerate(self._filenames):
            document = fitz.open(filename)

            # Create the directory and go into it
            os.mkdir(f"{filename}_images")
            os.chdir(f"{filename}_images")

            # Extract and crop the images only if the PDF file has more than one page
            if len(document) > 1:
                # Get all the images
                for i in range(len(document) - 1, len(document)):
                    for img in document.getPageImageList(i):
                        xref = img[0]
                        pix = fitz.Pixmap(document, xref)
                        imgname = f"image-{index}-p{i}-{xref}.png"

                        # this is GRAY or RGB
                        if pix.n < 5:
                            pix.writePNG(imgname)
                            PDFImageExtractor.crop(
                                imgname, (435, 140, 2025, 3000), imgname
                            )

                        # CMYK: convert to RGB first
                        else:
                            pix1 = fitz.Pixmap(fitz.csRGB, pix)
                            pix1.writePNG(imgname)
                            PDFImageExtractor.crop(
                                imgname, (435, 140, 2025, 3000), imgname
                            )
                            pix1 = None

                        pix = None

            # For the organized implementation
            if organized:
                # Go one directory back when all images are extracted
                os.chdir("..")

                # Move the folder to the proper directory
                shutil.move(
                    f"{filename}_images", os.path.join("..", destination)
                )

            # For the unorganized implementation
            else:
                for image_name in os.listdir("."):
                    if os.path.isfile(os.path.join(".", image_name)):
                        shutil.copy(
                            image_name, os.path.join("../..", destination)
                        )

                # Go one directory back when all images are moved
                os.chdir("..")

                # Delete the folder
                shutil.rmtree(f"{filename}_images")
