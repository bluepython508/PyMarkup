from __future__ import annotations
# from unittest.mock import patch
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class MLBuilder:
    element_name: str = 'html'
    build_context: List = field(default_factory=list)
    parent: MLBuilder = None
    params: Dict = field(default_factory=dict)

    def __getattr__(self, item):
        return MLBuilder(item, self.build_context)

    def __add__(self, other):
        if isinstance(other, MLBuilder):
            other.self_closing()
            return
        self.build_context.append(str(other))

    def __repr__(self):
        return "\n".join(self.build_context)

    def __enter__(self, **kwargs):
        self.build_context.append(f"<{' '.join([self.element_name] + self.param_string())}>")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.build_context.append(f"</{self.element_name}>")
        if self.parent:
            self.parent.build_context.extend(self.build_context)

    def param_string(self):
        return [f'{key}="{str(value)}"' for key, value in self.params.items()]

    def __call__(self, **kwargs):
        self.params = kwargs
        return self

    def self_closing(self):
        self.build_context.append(f"<{' '.join([self.element_name] + self.param_string())}/>")
