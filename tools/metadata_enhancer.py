#!/usr/bin/env python3
"""
Metadata Enhancer for Witchcraft Magazine (comic_git)

Scans `your_content/comics/` and `your_content/extras/comics/`:
1. Cleans placeholder Alt text ("I will write it out I promise...") with contextual descriptions.
2. Cleans filenames used as titles (e.g. "21.png") with clean issue and page numbering.
3. Supports --dry-run (default) and --apply modes.
"""

import os
import re
import argparse
from typing import Tuple

PLACEHOLDER_ALT = "I will write it out I promise..."

def parse_folder_name(folder_name: str) -> Tuple[str, str]:
    """
    Parses folder names like 'issue19-21' or 'trapdoorbandit-02' into (series/issue, page).
    """
    if "-" in folder_name:
        parts = folder_name.split("-", 1)
        series = parts[0]
        page = parts[1]
        # Match issue number
        m = re.match(r"issue(\d+)", series, re.IGNORECASE)
        if m:
            issue_num = int(m.group(1))
            return f"Issue {issue_num}", f"Page {int(page) if page.isdigit() else page}"
        return series.replace("_", " ").title(), f"Part {int(page) if page.isdigit() else page}"
    return folder_name, ""

def process_info_file(filepath: str, apply_changes: bool) -> dict:
    folder_name = os.path.basename(os.path.dirname(filepath))
    series, page = parse_folder_name(folder_name)

    changes = {}
    lines = []
    modified = False

    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if line.strip().startswith("Alt text ="):
            current_alt = line.split("=", 1)[1].strip()
            if current_alt == PLACEHOLDER_ALT or not current_alt:
                new_alt = f"{series} - {page}".strip(" - ")
                if new_alt:
                    new_line = f"Alt text = {new_alt}\n"
                    changes["alt_text"] = (current_alt, new_alt)
                    new_lines.append(new_line)
                    modified = True
                    continue

        if line.strip().startswith("Title ="):
            current_title = line.split("=", 1)[1].strip()
            # If title is just a filename like '21.png' or '04.jpg'
            if re.match(r"^\d+\.(png|jpg|jpeg|gif)$", current_title, re.IGNORECASE):
                new_title = f"{series} - {page}".strip(" - ")
                changes["title"] = (current_title, new_title)
                new_lines.append(f"Title = {new_title}\n")
                modified = True
                continue

        new_lines.append(line)

    if modified and apply_changes:
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

    return changes

def main():
    parser = argparse.ArgumentParser(description="Enhance comic info.ini metadata.")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default is dry-run)")
    parser.add_argument("--dir", default="your_content/comics", help="Target comics directory")
    args = parser.parse_args()

    mode = "APPLYING" if args.apply else "DRY-RUN (no changes made)"
    print(f"=== Running Metadata Enhancer ({mode}) on {args.dir} ===")

    total_checked = 0
    total_modified = 0

    for root, dirs, files in os.walk(args.dir):
        if "info.ini" in files:
            total_checked += 1
            filepath = os.path.join(root, "info.ini")
            changes = process_info_file(filepath, args.apply)
            if changes:
                total_modified += 1
                if total_modified <= 10 or args.apply:
                    print(f"[{os.path.basename(root)}] Changes: {changes}")

    print(f"\nDone! Checked: {total_checked} comics. Potential improvements: {total_modified}.")
    if not args.apply:
        print("To apply these changes, re-run with: python tools/metadata_enhancer.py --apply")

if __name__ == "__main__":
    main()
