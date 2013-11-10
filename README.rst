txt2bootstrap
=============

Translates one or many  Text/Markdown/Rest/HTML to html with bootstrap
and opens the browser for you.

Instructions
------------

Install it throught pip::

    pip install txt2bootstrap

Or, if you want to hack on this repo::

    git clone https://github.com/LuRsT/txt2bootstrap
    python setup.py install

Threre's no requirement, unless you want to view markdown or ReST files,
which if you do, you'll need to install each needed module::

    Markdown files -> Markdown
    ReST files     -> docutils

If you don't have any of them, the script will fallback to simple text,
printing it directly (if there's any html, it will be shown prettier
by your browser).

If you have a problem with the selected browser, change the env var
$BROWSER to the browser that you want to be opened.

How to use
----------

One file::

    txt2bootstrap file.md

Multiple files::

    txt2bootstrap file.md file.rst file.txt #...

Ways to use it
--------------

Joe is a writter who likes markdown and is not afraid of the terminal, so he
writes his markdown file and previews it using this script, to check if he
still remembers how to bold a word.

Rose is a front-end developer who wants a quick and dirty prototype, so she
will write a simple html file not caring about the `<body>` or `<head>` tags or
any of that gibberish and then view it using this script.

Michael is a pro developer who stumbled upon this script and actually found a
bug so fixed it and sent a pull request.
