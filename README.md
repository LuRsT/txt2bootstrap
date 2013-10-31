txt2bootstrap
=============

Translates one or many  Text/Markdown/Rest/HTML to html with bootstrap
and opens the browser for you.

## Instructions

Threre's no requirement, unless you want to view markdown or ReST files,
which if you do, you'll need to install each needed module:

    Markdown files -> Markdown
    ReST files     -> docutils

If you don't have any of them, the script will fallback to simple text
printing it directly (if there's any html, it will be shown prettier
by your browser.

If you have a problem with the selected browser, change the env var
$BROWSER to the browser that you want to be opened.

## How to use

    # One file
    python txt2bootstrap.py file.md
    # Multiple files
    python txt2bootstrap.py file.md file.rst file.txt #...
