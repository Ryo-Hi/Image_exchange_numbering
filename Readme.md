# 🖼️ HEIC to JPEG Converter

このリポジトリは、指定したディレクトリ内の **.heic 画像を JPEG 形式に変換**し、ファイル名を `cristal_0.jpg`, `cristal_1.jpg` のように**連番で保存**する Python スクリプトを提供します。

---

## 🔧 必要なライブラリ

以下のコマンドで依存ライブラリをインストールしてください：

```bash
pip install -r requirements.txt
```

---
## 🛠️ 使い方（関数別）
### `rename_heic_files(input_dir, symbol_name, extension='heic')`

- **目的**：`input_dir` 内の `.heic` ファイルを `symbol_name_0.heic`, `symbol_name_1.heic`, ... の形式でリネームします。

- **引数**：
  - `input_dir`：HEIC画像が入っているフォルダのパス（例：`'input_dir'`）
  - `symbol_name`：リネーム後の接頭辞（例：`'cristal'`）
  - `extension`：（省略可能）ファイル拡張子。デフォルトは `'heic'`

- **動作**：
  - 指定フォルダ内の `.heic` ファイルを昇順にソートし、指定の接頭辞＋連番にリネームします。
  - リネーム後のファイルは、後続のJPEG変換処理と整合します。

    

### `convert_heic_to_jpeg(input_dir, output_dir)`

- **目的**：HEICファイルをJPEG形式に変換して `output_dir` に保存します。

- **引数**：
  - `input_dir`：変換対象の `.heic` ファイルがあるディレクトリ
  - `output_dir`：JPEGファイルの出力先ディレクトリ（存在しなければ自動作成されます）

- **動作**：
  - `input_dir` 内の `.heic` ファイルを1枚ずつ読み込み、拡張子のみ `.jpg` に変更したファイル名で `output_dir` に保存します。
  - `Pillow` と `pillow-heif` を使って読み込み・変換を行います。
  - 変換完了のログをコンソールに表示します。
