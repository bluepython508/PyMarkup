import pytest

from pyml import MLBuilder


@pytest.fixture
def t():
    return MLBuilder()


def test_basic_buildings(t):
    with t:
        t + 'Hello, World!'
        with t.h1:
            t + 'Hello!'

    assert repr(t) == '''<html>
Hello, World!
<h1>
Hello!
</h1>
</html>'''


def test_attributes(t):
    with t:
        t + t.img(src="abc", alt="abc")

    assert repr(t) == """<html>
<img src="abc" alt="abc"/>
</html>"""


def test_nesting_looping(t):
    with t:
        with t.head:
            pass
        with t.body:
            with t.ul:
                for x in range(5):
                    with t.li:
                        t + x

    assert repr(t) == '''<html>
<head>
</head>
<body>
<ul>
<li>
0
</li>
<li>
1
</li>
<li>
2
</li>
<li>
3
</li>
<li>
4
</li>
</ul>
</body>
</html>'''
