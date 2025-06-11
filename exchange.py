import os
from PIL import Image
import pillow_heif

def rename_heic_files(input_dir, symbol_name, extension='heic'):
    """HEICファイルをcristal_{i}.heicの形式にリネームする"""
    heic_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.heic')]
    heic_files.sort()  # 任意の順にソート（必要なければ削除）

    for i, old_name in enumerate(heic_files):
        old_path = os.path.join(input_dir, old_name)
        new_name = f"{symbol_name}_{i}.{extension}"
        new_path = os.path.join(input_dir, new_name)

        os.rename(old_path, new_path)
        print(f"リネーム: {old_name} → {new_name}")

def convert_heic_to_jpeg(input_dir, output_dir):
    """HEICファイルをJPEGに変換し、出力フォルダに保存する"""
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.heic'):
            heic_path = os.path.join(input_dir, filename)
            jpeg_name = os.path.splitext(filename)[0] + '.jpg'
            jpeg_path = os.path.join(output_dir, jpeg_name)

            try:
                heif_file = pillow_heif.read_heif(heic_path)
                image = Image.frombytes(
                    heif_file.mode,
                    heif_file.size,
                    heif_file.data
                )
                image.save(jpeg_path, format="JPEG")
                print(f"変換: {filename} → {jpeg_name}")
            except Exception as e:
                print(f"変換失敗: {filename} ({e})")

# --- 実行 ---
symbol_name = 'cristal'
input_dir = 'input_dir'
output_dir = 'output_dir'

rename_heic_files(input_dir, symbol_name)
convert_heic_to_jpeg(input_dir, output_dir)
