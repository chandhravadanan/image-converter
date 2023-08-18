# Image Converter CLI Application

This is a Python CLI application that converts an image to black and white.

## Steps to run the application

1. Clone the repository.
   ```
   git clone https://github.com/chandhravadanan/image-converter.git
   cd image-converter
   ```
2. Create and activate a virtual environment.
    ```
    python3 -m venv venv
    source venv/bin/activate  # On macOS and Linux
    venv\Scripts\activate     # On Windows
    ```
3. Install the required packages.
    ```
    pip install -r requirements.txt
    ```
4. Run the CLI application with the following command.
    ```
    python image_converter.py input_image.png output_directory
    ```
5. The converted image will be saved in the specified output directory with the same name and same type as the input image, but with "_bw" and "_thumbnail" added to the filename.