# Magazine Tools & Utilities

This folder contains Python scripts and maintenance utilities for managing Witchcraft Magazine comic pages, files, and metadata.

## Available Scripts

- **`metadata_enhancer.py`**: Batch audit and enhancement tool for `info.ini` files.
  - Automatically replaces placeholder `"I will write it out I promise..."` alt texts with meaningful, contextual descriptions.
  - Formats image filenames used as titles (e.g. `21.png`) into human-readable titles (e.g. `Issue 19 - Page 21`).
  - Supports `--dry-run` (default) and `--apply`.
  - Usage:
    ```bash
    python tools/metadata_enhancer.py --apply
    python tools/metadata_enhancer.py --apply --dir your_content/extras/comics
    ```

- **`fixini.py`**: Fixes malformed `Filename = Filename = ...` lines and extensions in older INI files.
- **`sortfiles.py`**: Organizes raw page images into comic folder structures with boilerplate `info.ini` and `post.txt`.
- **`mergeimages.py`**: Image stitching utility for multi-page spreads.
- **`script.py`, `script1.py`, `script3.py`**: Legacy batch import and formatting utilities.
