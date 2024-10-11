# Video Converter to Hap Codec

This Python project contains scripts to convert video files to the Hap codec format using FFmpeg, either individually or in bulk from a folder.

## Prerequisites

- Python 3.x
- FFmpeg
- ffmpeg-python library

## Installation

1. Install FFmpeg on your system. You can download it from [FFmpeg's official website](https://ffmpeg.org/download.html).

2. Install the required Python library:

   ```
   pip install ffmpeg-python
   ```

## Usage

### Converting a Single Video

Run the script from the command line with the following syntax:

```
python convert_video.py <input_file> <output_file>
```

Replace `<input_file>` with the path to your input video file and `<output_file>` with the desired path for the output Hap video file.

## Example

Convert a video file named `example.mp4` to Hap codec format and save it as `example.hap`:

```
python convert_video.py example.mp4 example.hap
```

### Converting Multiple Videos

To convert multiple videos in a folder, run the following command:

```
python process_videos_from_folder.py <input_folder> <output_folder>
```

Replace `<input_folder>` with the path to the folder containing your input video files and `<output_folder>` with the desired path for the output Hap video files.

## Example

Convert all video files in the `input_videos` folder and save them in the `output_videos` folder:

```
python process_videos_from_folder.py input_videos output_videos
```

## Notes

- The script uses the `ffmpeg` command-line tool to perform the conversion.
- Ensure that the FFmpeg executable is correctly installed and accessible from your system's PATH.
- The script assumes that the input video file is in a format supported by FFmpeg. If the input format is not supported, you may need to install additional codecs or use a different conversion tool.

