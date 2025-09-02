import argparse
from PIL import Image
from pathlib import Path
from pillow_heif import register_heif_opener


SUPPORTED_EXTENSIONS = ".heic"
DESTINATION_EXTENSION = ".jpg"

register_heif_opener()


def is_valid_image_file(file_path: Path) -> bool:
    return file_path.is_file() and file_path.suffix.lower() in SUPPORTED_EXTENSIONS


def convert(input_path: Path, output_path: Path):
    image = Image.open(input_path)
    image.save(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert HEIC images to JPG images")
    parser.add_argument(
        "input_path", help="Input file or directory containing images.", type=Path
    )
    parser.add_argument(
        "output_dir", help="Output directory to save resized images.", type=Path
    )

    args = parser.parse_args()

    input_path: Path = args.input_path
    output_dir: Path = args.output_dir

    if not output_dir.exists():
        create_dir = input(f"Output directory {output_dir} does not exist. Create it? (y/N): ")
        if create_dir.lower() == "y":
            output_dir.mkdir(parents=True, exist_ok=True)
        else:
            print("Exiting.")
            exit()

    elif any(output_dir.iterdir()):
        proceed = input(f"Output directory {output_dir} is not empty. Proceed? (y/N): ")
        if proceed.lower() == "y":
            pass
        else:
            print("Exiting.")
            exit()

    image_files: list[Path] = []
    if input_path.is_dir():
        image_files = [
            file for file in input_path.iterdir() if is_valid_image_file(file)
        ]
    elif is_valid_image_file(input_path):
        image_files.append(input_path)
    else:
        print(
            f"Invalid input path: {input_path}. Please provide a valid image file or directory."
        )
        exit()

    if not image_files:
        print(f"No valid image files found in {input_path}.")
        exit()

    for file in image_files:
        output_image_path_base = output_dir / file.name
        output_image_path = output_image_path_base.with_suffix(DESTINATION_EXTENSION)
        convert(file, output_image_path)
