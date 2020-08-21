# -*- coding: utf-8 -*-
import copy
class Node:
    def __init__(self,ar,level,parent,empty_house,expanded=False,promissing=False,child=[]):
        self.ar = copy.deepcopy(ar)
        self.level = level
        self.parent = parent
        self.empty_house = empty_house
        self.expanded = expanded
        self.promissing = promissing
        self.child = child