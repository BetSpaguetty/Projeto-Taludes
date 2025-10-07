from dataclasses import dataclass
from enum import Enum
from typing import Callable
from PyQt5.QtWidgets import *

@dataclass
class DictButton :
    TITLE : str = None
    FUNCTION : Callable = None
    BUTTON : QPushButton = None







