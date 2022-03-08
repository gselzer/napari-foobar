"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/plugins/stable/guides.html#widgets

Replace code below according to your needs.
"""
from typing import Optional
from magicgui import magic_factory

@magic_factory(img_layer = {"choices": ['a', 'b']}, max=None)
def example_magic_widget(img_layer: Optional[str] = None):
    print(f"you have selected {img_layer}")
