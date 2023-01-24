#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List


class Administrator(object):
    def __init__(self, login):
        self.login: str = login
        self.type: str = "admin"
