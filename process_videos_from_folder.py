import os
import argparse
from convert_video import convert_to_hap

def process_videos_in_folder(input_folder, output_folder):
    """
    Process all video files in the input folder and convert them to Hap codec.

    This function iterates through all video files (with extensions .mp4, .avi, .mov, .mkv)
    in the input folder, converts them to Hap codec, and saves the converted files
    in the output folder.

    Args:
        input_folder (str): Path to the folder containing input video files.
        output_folder (str): Path to the folder where converted Hap videos will be saved.

    Example:
        To convert all videos in '/path/to/input' and save them in '/path/to/output':
        >>> process_videos_in_folder('/path/to/input', '/path/to/output')
    """
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Get all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):  # Add more video extensions if needed
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.hap'
            output_path = os.path.join(output_folder, output_filename)
            
            print(f"Converting {filename} to Hap codec...")
            convert_to_hap(input_path, output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert videos in a folder to Hap Codec")
    parser.add_argument("input_folder", help="Path to the input folder containing video files")
    parser.add_argument("output_folder", help="Path to the output folder for Hap video files")
    args = parser.parse_args()

    process_videos_in_folder(args.input_folder, args.output_folder)

    print("Example usage:")
    print("python process_videos_from_folder.py /path/to/input /path/to/output")
