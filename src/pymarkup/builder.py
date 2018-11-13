from __future__ import annotations

# from unittest.mock import patch
from dataclasses import dataclass, field
from io import StringIO
from typing import Dict


@dataclass
class MarkupBuilder:
    element: str = "html"
    text: StringIO = field(default_factory=StringIO)
    attrs: Dict = field(default_factory=dict)

    def self_closing(self):
        self.text.write(f'<{self.element}{self.attr_string()}/>')

    def __enter__(self):
        self.text.write(f'\n<{self.element }{self.attr_string()}>')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.text.write(f'\n</{self.element}>')

    def __add__(self, other):
        if isinstance(other, MarkupBuilder):
            other.self_closing()
            return
        self.text.write(f'\n{str(other)}')

    def __getattr__(self, item):
        return MarkupBuilder(item, self.text)

    def __call__(self, **kwargs):
        self.attrs = kwargs
        return self

    def __repr__(self):
        return self.text.getvalue()[1:]

    def attr_string(self):
        val = ' '.join(f'{key}="{value}"' for key, value in self.attrs.items())
        val = ' ' + val if val else ''
        return val
