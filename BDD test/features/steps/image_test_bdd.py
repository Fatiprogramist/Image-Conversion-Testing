from behave import given, when, then
from PIL import Image
import os
import sys

from conv_image import convert_image 



@given('I have an image "{image_name}"')
def step_given_image_exists(context, image_name):
    context.input_path = os.path.join('tests', image_name)
    assert os.path.exists(context.input_path)

@when('I convert the image to "{format}" format')
def step_when_convert_image(context, format):
    context.output_path = os.path.splitext(context.input_path)[0] + '.' + format.lower()
    convert_image(context.input_path, context.output_path, format)

@when('I convert the image to "{format}" format with size {width}x{height}')
def step_when_convert_and_resize_image(context, format, width, height):
    context.output_path = os.path.splitext(context.input_path)[0] + '_resized.' + format.lower()
    new_size = (int(width), int(height))
    convert_image(context.input_path, context.output_path, format, new_size)

@then('the output should be a "{format}" image')
def step_then_output_image_should_be(context, format):
    assert os.path.exists(context.output_path)
    with Image.open(context.output_path) as img:
        assert img.format == format

@then('the output image should have size {width}x{height}')
def step_then_output_image_should_have_size(context, width, height):
    assert os.path.exists(context.output_path)
    with Image.open(context.output_path) as img:
        assert img.size == (int(width), int(height))
