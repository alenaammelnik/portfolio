import os
from transliterate import translit
import re

def transliterate_name(name):
    # Транслитерация русского текста → латиница
    name = translit(name, 'ru', reversed=True)
    # Заменим пробелы и спецсимволы подчёркиваниями
    name = re.sub(r'[^a-zA-Z0-9._-]', '_', name)
    name = re.sub(r'__+', '_', name).strip('_')
    return name

def rename_labs_transliterate(base_path):
    for root, dirs, files in os.walk(base_path, topdown=False):
        # Файлы
        for name in files:
            new_name = transliterate_name(name)
            if new_name != name:
                os.rename(os.path.join(root, name), os.path.join(root, new_name))
                print(f"Файл: {name} → {new_name}")

        # Папки
        for name in dirs:
            new_name = transliterate_name(name)
            if new_name != name:
                os.rename(os.path.join(root, name), os.path.join(root, new_name))
                print(f"Папка: {name} → {new_name}")

if __name__ == "__main__":
    rename_labs_transliterate("labs")  # Запускается на папке labs