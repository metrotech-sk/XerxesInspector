#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xerxes_protocol import DevId, DevIdMixin


def getDevIdTable() -> dict:
    devIdTable = dict()

    for idName in dir(DevId):
        if not idName.startswith("_"):
            id = getattr(DevId, idName)
            if isinstance(id, DevIdMixin):
                devIdTable[id] = idName

    return devIdTable


devIdTable = getDevIdTable()
