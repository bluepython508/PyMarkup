Quickstart
==========

A basic example::

    from pymarkup import MarkupBuilder

    t = MarkupBuilder()

    with t:  # <html> tag
        with t.h1(id='HelloWorld'):  # Attribute access creates new element, and call adds attributes to tag
            t + 'Hello World!'  # Add child text to tag

        with t.a(href="github.com"):
           t + t.img(src="i_am_an_image.png")  # Self-closing tags are added with +

        with t.ul:
            for x in range(2):
                with t.li:
                    t + x

``repr(t)`` gives::
..

    <html>
    <h1 id="HelloWorld">
    Hello World!
    </h1>
    <a href="github.com"><img src="i_am_an_image.png"/>
    </a>
    <ul>
    <li>
    0
    </li>
    <li>
    1
    </li>
    </html>

