# -*- coding: utf-8 -*-
VERSION = '1.1.4'
__version__ = VERSION


RUN_VER = "open"


def get_run_ver():
    from django.conf import settings
    try:
        return settings.RUN_VER
    except AttributeError:
        return RUN_VER
