#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module defines the models of the project
"""


class MeliProduct(object):

    def __init__(self):
        self._title = None
        self._category = None
        self._description = None
        self._price = 0.0
        self._quantity = 0
        self._images = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    def add_image(self, image_url):
        self._images.append(image_url)
