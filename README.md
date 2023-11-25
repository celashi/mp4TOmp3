# MP4 to MP3 Converter

This script converts all MP4 files in a specified folder to MP3 format using the ffmpeg library. It provides a simple and efficient way to convert multiple MP4 files to MP3 files in bulk.

## Prerequisites

Before running the script, make sure you have the following prerequisites installed on your system:

- Python 3.x
- ffmpeg

## Installation

1. Clone or download this repository to your local machine.
2. Install the required Python packages by running the following command:
   ```
   pip install -r requirements.txt
   ```
3. Make sure ffmpeg is installed on your system. You can download it from the official website: [https://ffmpeg.org/](https://ffmpeg.org/)

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the following command to convert the MP4 files in the current directory to MP3:
   ```
   python mp4tomp3_ver3.py
   ```
   The script will convert all the MP4 files in the current directory and save the resulting MP3 files in the same location.

   **Note:** Make sure the MP4 files you want to convert are located in the same directory as the script or its subdirectories.

## Customization

You can customize the script behavior by modifying the following variables in the `mp4tomp3_ver3.py` file:

- `folder`: Specify the folder path where the MP4 files are located. By default, it uses the current working directory.

- `output_folder`: Specify the folder path where the converted MP3 files will be saved. By default, it uses the same folder as the input files.

- `output_format`: Specify the output format for the converted files. By default, it uses MP3 format.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This script utilizes the ffmpeg library for audio conversion. Visit the official website for more information: [https://ffmpeg.org/](https://ffmpeg.org/)

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
