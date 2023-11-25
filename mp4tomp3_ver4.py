import os
from pydub import AudioSegment
from pydub.utils import make_chunks
from concurrent.futures import ThreadPoolExecutor

# 获取当前脚本所在文件夹路径
folder_path = os.path.dirname(os.path.abspath(__file__))

# 转换函数
def convert_mp4_to_mp3(mp4_file_path):
    # 将MP4文件转换为AudioSegment对象
    audio = AudioSegment.from_file(mp4_file_path, format="mp4")

    # 分割音频为小块，每块1秒
    chunks = make_chunks(audio, 1000)

    # 创建一个空的AudioSegment对象用于保存所有音频块
    output_audio = AudioSegment.empty()

    # 遍历分割后的音频块并追加到output_audio中
    for i, chunk in enumerate(chunks):
        output_audio += chunk

    # 构建要保存的MP3文件的完整路径
    mp3_file_path = os.path.join(folder_path, f"{os.path.splitext(os.path.basename(mp4_file_path))[0]}.mp3")

    # 保存完整的音频对象为MP3文件
    output_audio.export(mp3_file_path, format="mp3")

    print(f"Converted {os.path.basename(mp4_file_path)} to {os.path.basename(mp3_file_path)}")

# 遍历文件夹中的文件
for file_name in os.listdir(folder_path):
    if file_name.endswith(".mp4"):
        # 构建MP4文件的完整路径
        mp4_file_path = os.path.join(folder_path, file_name)

        # 使用线程池进行多线程转换
        with ThreadPoolExecutor() as executor:
            executor.submit(convert_mp4_to_mp3, mp4_file_path)

print("Conversion completed.")
