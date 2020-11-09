# -*- coding: utf-8 -*-
"""Top-level package for topalias."""

__author__ = "Sergey Chudakov"
__email__ = "csredrat@gmail.com"
__version__ = "1.2.13"

import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__))),
)  # noqa: WPS221
# isort: split  # noqa: E800

# pylint: disable=wrong-import-position
# for . import
# pylint: enable=wrong-import-position
