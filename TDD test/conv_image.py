from PIL import Image

def convert_image(input_path, output_path, output_format, new_size=None):
    try:
        # Открыть изображение
        with Image.open(input_path) as img:
            # Изменить размер, если указано
            if new_size:
                img = img.resize(new_size)
            
            # Сохранить изображение в новом формате
            img.save(output_path, format=output_format)
            print(f'Файл сохранен: {output_path}')
    except Exception as e:
        print(f"Ошибка при обработке файла {input_path}: {e}")
