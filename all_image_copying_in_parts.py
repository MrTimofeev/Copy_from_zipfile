import os
from zipfile import ZipFile
import datetime

CHUNK_SIZE = 16 * 1024  # 4 KB

def extract_directly(zip_file, item, path_to_extract):
    try:
        target_path = os.path.join(path_to_extract, item)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        with zip_file.open(item) as source, open(target_path, 'wb') as target:
            # Копируем данные по кусочкам, чтобы минимизировать использование памяти
            while True:
                chunk = source.read(CHUNK_SIZE)  # Чтение по 4KB за раз
                if not chunk:
                    break
                target.write(chunk)
    except Exception as e:
        print(f"Не смог извлечь файл: {item.split('/')}, ошибка: {e}")

def process_zip_file(file, path_to_archive, path_to_extract):
    try:
        with ZipFile(os.path.join(path_to_archive, file), "r") as myzip:
            extractable_items = [
                item for item in myzip.namelist()
                if item.endswith((".mp4", ".jpg")) and ".json" not in item
            ]
            for item in extractable_items:
                extract_directly(myzip, item, path_to_extract)
    except Exception as e:
        print(f"Ошибка обработки архива {file}: {e}")

def extract_from_zip_file(path_to_archive, path_to_extract):
    files = os.listdir(path_to_archive)
    for file in files:
        if "takeout" in file and file.endswith(".zip"):
            print(f"Переношу данные из архива: {file}")
            process_zip_file(file, path_to_archive, path_to_extract)
            print(f"Закончил перенос из архива: {file}")

def main():
    path_to_archive = "E:\\"
    path_to_extract = "E:\\test\\"
    extract_from_zip_file(path_to_archive, path_to_extract)

if __name__ == '__main__':
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    print(f"Перенос файлов закончен, потраченное время: {end-start}")


# Время выполнения: 0:23:57.554542 # Чтение по 4KB за раз
# Время выполнения: 0:24:23.488513 # Чтение по 16KB за раз
# Время выполнения: 0:39:13.625933 # Чтение по 128KB за раз
# Количество фото: 9961
# Количество видео: 684