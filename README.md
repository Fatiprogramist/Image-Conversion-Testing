# Image-Conversion-Testing
Here's a description of the functionality and structure of modules for image conversion testing:

---

# Image Conversion Testing

This repository contains a set of modules and tests for converting images between different formats and resizing them. The project implements both Test-Driven Development (TDD) and Behavior-Driven Development (BDD) methodologies to ensure the functionality and reliability of the image conversion process.

## Modules

### 1. Image Conversion Function (`convert_image.py`)

The `convert_image` function handles the conversion of images from one format to another and supports resizing. It uses the Python Imaging Library (PIL) to open, resize, and save images. The function includes error handling to manage any issues during the image processing.

#### Function Signature:
```python
def convert_image(input_path, output_path, output_format, new_size=None):
```

- **Parameters:**
  - `input_path`: Path to the input image.
  - `output_path`: Path to save the converted image.
  - `output_format`: Desired format for the output image (e.g., 'JPEG', 'PNG').
  - `new_size`: Optional tuple for resizing the image (width, height).

### 2. Test Module for TDD (`test_conversion.py`)

This module includes unit tests for the `convert_image` function using the `unittest` framework. The tests cover:
- Conversion of images to JPEG format.
- Resizing images during conversion.

#### Key Tests:
- **test_image_conversion_to_jpeg**: Verifies that an image is successfully converted to JPEG format.
- **test_resize_image**: Ensures that the image is resized correctly when converting.

### 3. Test Module for BDD (`bdd_test.py`)

This module implements behavior-driven tests using the `behave` framework. It provides scenarios for:
- Checking the existence of an image file.
- Converting images to different formats and sizes.
- Verifying the output format and dimensions of the converted images.

#### Key Steps:
- **Given**: Define the initial context (e.g., presence of an image).
- **When**: Perform actions (e.g., convert the image).
- **Then**: Assert expected outcomes (e.g., check output format and size).

## Usage

1. **Install Dependencies**:
   Ensure you have the required libraries installed. You can install them using pip:
   ```bash
   pip install Pillow behave
   ```

2. **Run TDD Tests**:
   Execute the TDD tests using:
   ```bash
   python -m unittest test_conversion.py
   ```

3. **Run BDD Tests**:
   To run the BDD tests, use the command:
   ```bash
   behave
   ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License.
