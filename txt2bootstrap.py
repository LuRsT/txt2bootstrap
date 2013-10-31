from sys import argv
from webbrowser import open as browser_open


MARKDOWN_EXTENSIONS = [ 'md' ]
REST_EXTENSIONS = [ 'rst' ]

TEMPLATE_CONTENTS = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>{filename}</title>
        <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container">
            {file_contents}
        </div>
  </body>
</html>
"""


def bootstrap_text(filenames):
    if not len(filenames):
        raise TypeError('Needs at least one argument.')

    file_contents = ''
    for filename in filenames:
        with open(filename) as file:
            file_extension = filename[filename.rfind('.') + 1:]
            file_contents += text_to_html(
                file.read(),
                extension=file_extension,
            )

    return TEMPLATE_CONTENTS.format(
        filename=filename,
        file_contents=file_contents,
    )


def text_to_html(text, extension=None):
    if extension in MARKDOWN_EXTENSIONS:
        try:
            from markdown import markdown
            return markdown(text)
        except:
            print "Couldn't import markdown."
            return text
    elif extension in REST_EXTENSIONS:
        try:
            from docutils.core import publish_string
            return publish_string(text, writer_name='html')
        except:
            print "Couldn't import docutils."
            return text
    else:
        return text


if __name__=='__main__':
    if len(argv) < 2:
        raise TypeError('Needs at least one argument.')

    output_filename = "{}.html".format(argv[1])
    with open(output_filename, 'w') as output_file:
        output_content = bootstrap_text(argv[1:])
        output_file.write(output_content)

    browser_open(output_filename)