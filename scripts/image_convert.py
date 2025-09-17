from PIL import Image
import os
import sys

def convert_images_to_webp(folder_path, quality=80):
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid folder.")
        return

    count = 0
    # Add all formats you want to handle
    valid_extensions = (".png", ".jpg", ".jpeg", ".webp")

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(valid_extensions):
            img_path = os.path.join(folder_path, filename)
            base, ext = os.path.splitext(filename)
            webp_path = os.path.join(folder_path, base + ".webp")

            try:
                with Image.open(img_path) as img:
                    img.save(webp_path, "WEBP", quality=quality, optimize=True)
                count += 1
                print(f"Processed: {filename} → {os.path.basename(webp_path)}")
            except Exception as e:
                print(f"⚠️ Skipped {filename}: {e}")

    print(f"\nDone! Processed {count} image(s) in '{folder_path}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_to_webp.py <folder_path>")
    else:
        folder = sys.argv[1]
        convert_images_to_webp(folder)
