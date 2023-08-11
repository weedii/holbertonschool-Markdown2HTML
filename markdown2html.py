#!/usr/bin/python3
"""This script converts a markdown file into an html file."""

import sys
import markdown

def convert_markdown_to_html(input_file, output_file):
    """
    Converts a markdown file to an HTML file.

    Args:
        input_file (str): Path to the input Markdown file.
        output_file (str): Path to the output HTML file.
    """
    try:
        with open(input_file, 'r') as md_file:
            markdown_content = md_file.read()
            html_content = markdown.markdown(markdown_content)
            with open(output_file, 'w') as html_file:
                html_file.write(html_content)
    except FileNotFoundError:
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)
