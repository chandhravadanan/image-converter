#!/usr/bin/env python

import os
import argparse
import cv2
import imghdr
import asyncio

SUPPORTED_FORMATS = ['bmp', 'jpeg', 'jpg', 'png']

class ImageConverter:
    def __init__(self, input_image, output_directory):
        if not self.is_valid_path(input_image):
            raise ValueError(f"Invalid input image path: {input_image}")

        if not self.is_valid_path(output_directory) or not os.path.isdir(output_directory):
            raise ValueError(f"Invalid output directory path: {output_directory}")

        if not self.is_supported_format(input_image):
            raise ValueError(f"Unsupported image format: {input_image}")
        
        self.input_image = input_image
        self.output_directory = output_directory
        self.original_image = cv2.imread(input_image)
        self.input_filename = os.path.basename(input_image)
        self.file_name, self.file_extension = os.path.splitext(self.input_filename)

    def is_valid_path(self, path):
        return os.path.exists(path)

    def is_supported_format(self, filename):
        file_format = imghdr.what(filename)
        return file_format in SUPPORTED_FORMATS

    async def convert_to_bw(self):
        bw_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        output_filename = self.file_name + '_bw' + self.file_extension
        bw_output_path = os.path.join(self.output_directory, output_filename)
        cv2.imwrite(bw_output_path, bw_image)

    async def create_thumbnail(self):
        thumbnail_size = (100, 100)
        thumbnail = cv2.resize(self.original_image, thumbnail_size)
        thumb_output_filename = self.file_name + '_thumbnail' + self.file_extension
        thumb_output_path = os.path.join(self.output_directory, thumb_output_filename)
        cv2.imwrite(thumb_output_path, thumbnail)

async def main(input_image, output_directory):
    try:
        converter = ImageConverter(input_image, output_directory)
        
        # Create tasks for both asynchronous operations
        tasks = [
            asyncio.create_task(converter.convert_to_bw()),
            asyncio.create_task(converter.create_thumbnail())
        ]
        
        # Wait for both tasks to complete
        await asyncio.gather(*tasks)
        
        print("Conversion and thumbnail creation successful!")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert an image to black and white and create a thumbnail.')
    parser.add_argument('input', help='Input image path')
    parser.add_argument('output_directory', help='Output directory path')
    args = parser.parse_args()

    asyncio.run(main(args.input, args.output_directory))
