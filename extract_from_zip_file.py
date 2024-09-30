import os
from zipfile import ZipFile
import datetime

def extract_from_zip_file(path_to_archive, path_to_extract):
    files = os.listdir(path_to_archive)
    for file in files:
        if "takeout" in file and file.endswith(".zip"):
            print(f"Переношу данные из архива:{file}")
            with ZipFile(path_to_archive + file, "r") as myzip:
                for item in myzip.namelist():
                    if item.endswith((".mp4", ".jpg")) and ".json" not in item:
                        try:
                            myzip.extract(item, path=path_to_extract)
                        except:
                            print(
                                f"Не смог извлечь файл: {item.split('/')}, из архива {file}")
            print(f"Закончил перенос из архива: {file} ")

def main():
    path_to_archive = "путь до папки с вашим архивом"
    path_to_extract = "путь куда нужно положить разархивированные файлы"
    extract_from_zip_file(path_to_archive, path_to_extract)

if __name__ == '__main__':
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    print(f"Перенос файлов закончен, потраченное время: {end-start}")
    
# Время выполнения: 0:31:57.554542 
# Количество фото: 9961
# Количество видео: 684