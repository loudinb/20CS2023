import argparse
from typing import Tuple


def read_bmp(input_file: str) -> Tuple[bytes, bytearray]:
    """Reads a BMP file and returns the header and pixel data.

    Args:
        input_file: Path to the BMP file to be read.

    Returns:
        A tuple containing the BMP header (54 bytes) and the pixel data.
    """
    
    # TODO: Open the input file in binary read mode
    #       Read the file and return the header and pixel data
    pass


def calculate_grayscale_value(red: int, green: int, blue: int) -> int:
    """Calculates the grayscale value from RGB components.

    Args:
        red: Red component of the pixel.
        green: Green component of the pixel.
        blue: Blue component of the pixel.

    Returns:
        The grayscale value as an integer.
    """
    # TODO: Calculate the grayscale value from RGB components
    #       Grayscale value = (R + G + B) / 3
    pass


def convert_to_grayscale(pixel_data: bytearray) -> bytearray:
    """Converts the pixel data to grayscale.

    Args:
        pixel_data: A bytearray containing the BMP pixel data in BGR format.

    Returns:
        The modified bytearray where each pixel is converted to grayscale.
    """

    # TODO: Iterate over the pixel data in steps of 3 bytes
    #       Call calculate_grayscale_value with the BGR values
    #       Set the BGR values to the grayscale value
    #       Return the modified pixel data
    #       Note: BMP pixel data is in BGR format, so the order is blue, green, red
    pass
    


def write_bmp(output_file: str, header: bytes, pixel_data: bytearray) -> None:
    """Writes the header and pixel data to a BMP file.

    Args:
        output_file: Path to the output BMP file.
        header: The BMP file header.
        pixel_data: The modified pixel data to be written.
    """
    # TODO: Open output file in binary write mode 
    #       Write header and pixel data to file
    pass


def bmp_to_grayscale(input_file: str, output_file: str) -> None:
    """Converts a BMP file to grayscale and writes it to a new file.

    Args:
        input_file: Path to the input BMP file.
        output_file: Path to the output BMP file.
    """
    # TODO-1: Call read_bmp to get the header and pixel data
    # TODO-2: Call convert_to_grayscale to modify the pixel data
    # TODO-3: Call write_bmp to write the modified data to the output file
     
    pass


if __name__ == '__main__':

    # TODO-1: Create a parser with a decription of the program
    # TODO-2: Add argument for input_file
    # TODO-3: Add argument for output_file
    
    # TODO-4: Parse the arguments
    
    # TODO-5: Call the bmp_to_grayscale function with the input and output file paths
    pass