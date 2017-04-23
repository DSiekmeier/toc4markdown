#!/usr/bin/env python3

"""
@package docstring
@brief   Create Table Of Contents (TOC) for files in Markdown languages.
@author  Dennis Siekmeier (contact@dsiekmeier.de)

@copyright Coffee-Ware: Feel free to use this software "as-is", but buy me a
           coffee if we ever meet each other.
"""

import argparse
import shutil
import sys
import time

__version__ = "1.0"

# Information about required and used Python versions
req_py_version = (3, 2)
cur_py_version = sys.version_info


def create_backup(src):
    """Copy the given file with metadata and append the current date / time."""

    try:
        postfix = time.strftime("_%Y%m%d_%H%M%S")
        shutil.copy2(src, src+postfix)
    except IOError:
        print("Error: could not create backup file.")
        sys.exit(1)


def read_file(cur_file, skip_leading):
    """Read the given file and return the toc and the whole file in lists."""

    toc = list()
    data = list()
    with open(cur_file, "r", encoding="utf-8") as f:
        for line in f:
            current_line = line
            data.append(current_line)
            if skip_leading:
                current_line = line.lstrip()
            if current_line.startswith("#"):
                toc.append(current_line)
    return toc, data


def modify_file(cur_file, toc, data):
    with open(cur_file, "w", encoding="utf-8") as modified:
        for row in toc:
            modified.write(row)
        modified.write("---\n")
        for row in data:
            modified.write(row)


def create_arg_parser():
    # Create the argument parser
    parser = argparse.ArgumentParser(
        description="TOC creator for lightweight markup languages")

    parser.add_argument("-sl", "--skip_leading",
                        help="ignore whitespaces in front of header tags",
                        action="store_true")

    parser.add_argument("-nb", "--no_backup",
                        help="do not create a backup of the processed file",
                        action="store_true")

    parser.add_argument("-t", "--test",
                        help="do not modify files, show results on screen",
                        action="store_true")

    parser.add_argument("files",
                        nargs="+",
                        help="<required> list of files to be processed")

    parser.add_argument("-v", "--version",
                        action="version",
                        version=__version__)

    return parser.parse_args()


def main():
    """Execute the main functionality of the program."""

    # Initialize the argument parser
    args = create_arg_parser()

    # process the given file list
    lst_len = len(args.files)
    for i, cur_file in enumerate(args.files):
        print("> File {0}/{1}: {2}".format(str(i+1), str(lst_len), cur_file))

        # Read the current file and return the toc and the whole file at once
        toc, data = read_file(cur_file, args.skip_leading)

        if args.test:
            for item in toc:
                print(item.rstrip())
            print("")
        else:
            # create a backup if neccessary
            if not args.no_backup:
                create_backup(cur_file)

            # prepend the TOC to the current file
            modify_file(cur_file, toc, data)


if __name__ == "__main__":

    # Check for correct Python version
    if cur_py_version >= req_py_version:
        main()
    else:
        print("Your Python interpreter is too old. Please consider upgrading.")

