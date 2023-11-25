import os
from pydub import AudioSegment

# 获取当前脚本所在文件夹路径
folder_path = os.path.dirname(os.path.abspath(__file__))

# 遍历文件夹中的文件
for file_name in os.listdir(folder_path):
    if file_name.endswith(".mp4"):
        # 构建MP4文件的完整路径
        mp4_file_path = os.path.join(folder_path, file_name)

        # 将MP4文件转换为AudioSegment对象
        audio = AudioSegment.from_file(mp4_file_path, format="mp4")

        # 构建要保存的MP3文件的完整路径
        mp3_file_path = os.path.join(folder_path, f"{os.path.splitext(file_name)[0]}.mp3")

        # 将AudioSegment对象保存为MP3文件
        audio.export(mp3_file_path, format="mp3")

        print(f"Converted {file_name} to {os.path.basename(mp3_file_path)}")
