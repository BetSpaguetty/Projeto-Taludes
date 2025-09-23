from dataclasses import dataclass
from enum import Enum


class Materiais(Enum) :
    COARSE = 'Coarse'
    GRANULAR_MEDIUM = 'Granular medium'
    GRANULAR_FINE = 'Granular fine'
    MEDIUM = 'Medium'
    MEDIUM_FINE = 'Medium fine'
    FINE = 'Fine'
    VERY_FINE = 'Very fine'

class Parameters(Enum) :
    H      = 'H'
    HW     = 'HW'
    ALPHA  = 'ALPHA'
    C      = 'C'
    PHI    = 'PHI'
    THETAI = 'THETAI'


@dataclass
class Parameter :
    min : float = None
    max : float = None


@dataclass
class Material :
    TYPE : str
    THETA_R : float
    THETA_S : float
    THETA_500 : float
    VG_N : float
    VG_M : float
    VG_K : float
    VG_ALPHA : float


