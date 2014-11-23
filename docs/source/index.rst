Welcome to txt2bootstrap's documentation!
=========================================

Description
-----------

Translates one or many  Text/Markdown/Rest/HTML to html with bootstrap

Instructions
------------

Install it throught pip::

    pip install txt2bootstrap

Or, if you want to hack on this repo::

    git clone https://github.com/LuRsT/txt2bootstrap
    python setup.py install

Threre's no requirement, unless you want to view Markdown or ReST files,
which if you do, you'll need to install each needed module::

    Markdown files -> Markdown
    ReST files     -> docutils

If you don't have any of them, the script will fallback to simple text,
printing it directly inside the template with bootstrap included.

How to use
----------

One file::

    txt2bootstrap file.md

Multiple files::

    txt2bootstrap file.md file.rst file.txt #...

Those commands will print the resulting HTML, you can then create a new
file and open it in the browser::

    txt2boostrap file.md > file.html && firefox file.html

Or you can use the script ``browser`` (https://gist.github.com/defunkt/318247) to open it::

    txt2bootstrap file.md | browser

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
