""" Извлекаем аудиодорожку из видео файла.
    Название видеофайла прописываем вручную.
    Название аудиофайла генерируеться автоматически
"""
import moviepy.editor                                   # модуль для работы с видеофайлами
from pathlib import Path                                # модуль для работы с файлами, путь к файлу

video_file = Path('video-1.mp4')                        # присваиваем переменной путь к видеофайлу
video = moviepy.editor.VideoFileClip(f'{video_file}')   # инициируем объект VideoFileClip, привязываем к нему видеофайл
audio = video.audio                                     # назначаем переменной audio метод .audio
audio.write_audiofile(f'{video_file.stem}.mp3')         # сохраняем аудиодорожку в файл, используя метод stem (путь к фалу без расширения)

