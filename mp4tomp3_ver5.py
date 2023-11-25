import os
import subprocess
import concurrent.futures

def convert_to_mp3(file):
    mp4_file = file
    mp3_file = os.path.splitext(mp4_file)[0] + '.mp3'
    command = ['ffmpeg', '-i', mp4_file, '-acodec', 'libmp3lame', '-q:a', '0', mp3_file]
    subprocess.call(command)

def main():
    # Get the current directory
    folder = os.getcwd()

    # Get all the mp4 files in the folder
    mp4_files = [file for file in os.listdir(folder) if file.endswith('.mp4')]

    # Create a ProcessPoolExecutor
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Submit the conversion tasks
        futures = [executor.submit(convert_to_mp3, os.path.join(folder, file)) for file in mp4_files]

        # Process the completed tasks
        for future, file in zip(concurrent.futures.as_completed(futures), mp4_files):
            try:
                # Get the result of the task
                result = future.result()
                if result == 0:
                    print(f"Conversion successful for {file}")
                else:
                    print(f"Conversion failed for {file}")
            except Exception as e:
                print(f"Conversion failed for {file} with error: {e}")

if __name__ == '__main__':
    main()
