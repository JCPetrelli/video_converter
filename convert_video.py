import ffmpeg
import os
import argparse

def convert_to_hap(input_file, output_file):
    try:
        # Run the FFmpeg command
        (
            ffmpeg
            .input(input_file)
            .output(output_file, vcodec='hap', format='mov')
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        print(f"Conversion completed. Hap video saved as {output_file}")
    except ffmpeg.Error as e:
        print(f"An error occurred: {e.stderr.decode()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert video to Hap Codec")
    parser.add_argument("input_file", help="Path to the input video file")
    parser.add_argument("output_file", help="Path to the output Hap video file")
    args = parser.parse_args()

    convert_to_hap(args.input_file, args.output_file)