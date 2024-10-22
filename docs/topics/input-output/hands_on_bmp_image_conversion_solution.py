import argparse
from typing import Tuple


def read_bmp(input_file: str) -> Tuple[bytes, bytearray]:
    """Reads a BMP file and returns the header and pixel data.

    Args:
        input_file: Path to the BMP file to be read.

    Returns:
        A tuple containing the BMP header (54 bytes) and the pixel data.
    """
    with open(input_file, 'rb') as bmp:
        header: bytes = bmp.read(54)  # BMP header is 54 bytes
        pixel_data: bytearray = bytearray(bmp.read())  # Read the rest as pixel data
    return header, pixel_data


def calculate_grayscale_value(red: int, green: int, blue: int) -> int:
    """Calculates the grayscale value from RGB components.

    Args:
        red: Red component of the pixel.
        green: Green component of the pixel.
        blue: Blue component of the pixel.

    Returns:
        The grayscale value as an integer.
    """
    return int((red + green + blue) / 3)


def convert_to_grayscale(pixel_data: bytearray) -> bytearray:
    """Converts the pixel data to grayscale.

    Args:
        pixel_data: A bytearray containing the BMP pixel data in BGR format.

    Returns:
        The modified bytearray where each pixel is converted to grayscale.
    """
    for i in range(0, len(pixel_data), 3):
        blue: int = pixel_data[i]
        green: int = pixel_data[i + 1]
        red: int = pixel_data[i + 2]
        
        # Calculate the grayscale value
        grayscale: int = calculate_grayscale_value(red, green, blue)
        
        # Set all color channels to the grayscale value
        pixel_data[i] = grayscale  # Blue
        pixel_data[i + 1] = grayscale  # Green
        pixel_data[i + 2] = grayscale  # Red
    return pixel_data


def write_bmp(output_file: str, header: bytes, pixel_data: bytearray) -> None:
    """Writes the header and pixel data to a BMP file.

    Args:
        output_file: Path to the output BMP file.
        header: The BMP file header.
        pixel_data: The modified pixel data to be written.
    """
    with open(output_file, 'wb') as bmp:
        bmp.write(header)  # Write the header
        bmp.write(pixel_data)  # Write the modified pixel data


def bmp_to_grayscale(input_file: str, output_file: str) -> None:
    """Converts a BMP file to grayscale and writes it to a new file.

    Args:
        input_file: Path to the input BMP file.
        output_file: Path to the output BMP file.
    """
    header, pixel_data = read_bmp(input_file)
    grayscale_pixel_data = convert_to_grayscale(pixel_data)
    write_bmp(output_file, header, grayscale_pixel_data)
    print("Grayscale conversion completed!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert a BMP image to grayscale.")
    parser.add_argument('input_file', type=str, help='Path to the input BMP file')
    parser.add_argument('output_file', type=str, help='Path to the output BMP file')

    args = parser.parse_args()
    bmp_to_grayscale(args.input_file, args.output_file)
