"""Ivy configuration file."""

import os

# Abbreviation for this document.
abbrev = "sdxpy"

# GitHub repository.
repo = "https://github.com/gvwilson/sdxpy"

# Site settings.
lang = "en"
title = "Software Design by Example"
tagline = "a tool-based introduction with Python"
author = "Greg Wilson"
email = "gvwilson@third-bit.com"
domain = "third-bit.com"
plausible = True
archive = f"{abbrev}-examples.zip"
draft = False
isbn = "978-1032725253"
hardcopy = "https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"
cover = f"{abbrev}-cover.png"

# Website.
website = f"https://{domain}/{abbrev}/"

# Chapters.
chapters = {
    "intro": "Introduction",
    "oop": "Objects and Classes",
    "dup": "Finding Duplicate Files",
    "glob": "Matching Patterns",
    "parse": "Parsing Text",
    "test": "Running Tests",
    "interp": "An Interpreter",
    "func": "Functions and Closures",
    "protocols": "Protocols",
    "archive": "A File Archiver",
    "check": "An HTML Validator",
    "template": "A Template Expander",
    "lint": "A Code Linter",
    "layout": "Page Layout",
    "perf": "Performance Profiling",
    "persist": "Object Persistence",
    "binary": "Binary Data",
    "db": "A Database",
    "build": "A Build Manager",
    "pack": "A Package Manager",
    "ftp": "Transferring Files",
    "http": "Serving Web Pages",
    "viewer": "A File Viewer",
    "undo": "Undo and Redo",
    "vm": "A Virtual Machine",
    "debugger": "A Debugger",
    "finale": "Conclusion",
}

# Appendices (slugs in order).
appendices = {
    "bib": "Bibliography",
    "bonus": "Bonus Material",
    "syllabus": "Syllabus",
    "license": "License",
    "conduct": "Code of Conduct",
    "contrib": "Contributing",
    "glossary": "Glossary",
    "colophon": "Colophon",
    "contents": "Index",
}

# Files to copy verbatim.
copy = [
    "*.as",
    "*.mx",
    "*.tll",
    "*.xml",
]

# Exclusions (don't process).
exclude = copy + [
    "*.dot",
    "*.xml",
]

# Debug.
debug = False

# Warn about missing or unused entries.
warnings = False

# ----------------------------------------------------------------------

# Theme.
theme = "mccole"

# Enable various Markdown extensions.
markdown_settings = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "pymdownx.superfences",
    ]
}

# External files.
acknowledgments = "info/acknowledgments.yml"
bibliography = "info/bibliography.bib"
bibliography_style = "unsrt"
credits = "info/credits.yml"
dom = "lib/mccole/dom.yml"
glossary = "info/glossary.yml"
links = "info/links.yml"
thanks = "info/thanks.yml"

# Input and output directories.
src_dir = "src"
out_dir = os.getenv("MCCOLE", "docs")

# Use "a/" URLs instead of "a.html".
extension = "/"

# Files to copy verbatim.
copy += [
    "*.jpg",
    "*.js",
    "*.json",
    "*.out",
    "*.png",
    "*.py",
    "*.sh",
    "*.svg",
    "*.tll",
    "*.txt",
    "*.webp",
    "*.yml",
]

# Exclusions (don't process).
exclude += [
    "Makefile",
    "*.csv",
    "*.ht",
    "*.jpg",
    "*.js",
    "*.json",
    "*.mk",
    "*.out",
    "*.pdf",
    "*.png",
    "*.py",
    "*.pyc",
    "*.sh",
    "*.svg",
    "*.tll",
    "*.txt",
    "*.webp",
    "*.yml",
    "*~",
    "__pycache__",
    ".pytest_cache",
]

# ----------------------------------------------------------------------

# Display values for LaTeX generation.
if __name__ == "__main__":
    import sys
    assert len(sys.argv) == 2, "Expect exactly one argument"
    if sys.argv[1] == "--abbrev":
        print(abbrev)
    elif sys.argv[1] == "--chapters":
        print("\n".join(chapters))
    elif sys.argv[1] == "--lang":
        print(lang)
    elif sys.argv[1] == "--latex":
        print(f"\\title{{{title}}}")
        print(f"\\subtitle{{{tagline}}}")
        print(f"\\author{{{author}}}")
    elif sys.argv[1] == "--tagline":
        print(tagline)
    elif sys.argv[1] == "--title":
        print(title)
    else:
        assert False, f"Unknown flag {sys.argv[1]}"
