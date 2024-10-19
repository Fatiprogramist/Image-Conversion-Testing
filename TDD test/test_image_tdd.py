import unittest
from PIL import Image
import os
from conv_image import convert_image
class TestImageConversion(unittest.TestCase):
    def setUp(self):
        # Пути для входных и выходных изображений
        self.input_path = 'sample.png'
        self.output_path = 'output.jpg'
        self.output_resized_path = 'output_resized.jpg'
        # Создаем простое изображение для тестирования
        with Image.new('RGB', (100, 100), color='red') as img:
            img.save(self.input_path, 'PNG')
    def tearDown(self):
        # Удаляем все файлы, созданные во время тестов
        if os.path.exists(self.output_path):
            os.remove(self.output_path)
        if os.path.exists(self.output_resized_path):
            os.remove(self.output_resized_path)
        if os.path.exists(self.input_path):
            os.remove(self.input_path)
    def test_image_conversion_to_jpeg(self):
        # Тестируем конвертацию изображения в формат JPEG
        convert_image(self.input_path, self.output_path, 'JPEG')
        # Проверяем, что выходной файл существует
        self.assertTrue(os.path.exists(self.output_path))
        # Проверяем, что формат выходного изображения — JPEG
        with Image.open(self.output_path) as img:
            self.assertEqual(img.format, 'JPEG')
    def test_resize_image(self):
        # Тестируем конвертацию изображения с изменением размера
        new_size = (800, 600)
        convert_image(self.input_path, self.output_resized_path, 'JPEG', new_size)
        
        # Проверяем, что выходной файл существует
        self.assertTrue(os.path.exists(self.output_resized_path))
        
        # Проверяем, что размер выходного изображения соответствует заданному
        with Image.open(self.output_resized_path) as img:
            self.assertEqual(img.size, new_size)
if __name__ == '__main__':
    unittest.main()
