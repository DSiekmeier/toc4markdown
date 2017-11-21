# TOC4MARKDOWN

## Author
Dennis Siekmeier

contact@dsiekmeier.de

Visit me on www.dsiekmeier.de

## DESCRIPTION
**toc4markdown** is a Python script written to parse markdown files and create
and prepend a table of contents in front of the file.

For this the script searches for lines beginning with the header tag #
(ATX style headings) and copies theese lines to the beginning of the file.
Currently Setext style tags (underlining headers) are not supported.

## USAGE
Execute *toc4markdown.py* followed by a list of markdown files which should be
processed.

By default the program creates a backup of the files. You can skip
this with the *-nb* argument. Lines with a header tag # are ignored if there are
leading whitespaces. You can change this behaviour with the *-sl* argument.

In case you just want to see the results on screen (and not change any file) you
can use the *-t* argument.

Execute *toc4markdown.py --help* to get the full list of commandline arguments.

## LICENCE
These source codes are under Coffee-Ware licence: feel free to use this software
"as-is", but buy me a coffee if we ever meet each other.
