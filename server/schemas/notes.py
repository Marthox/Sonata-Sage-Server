from pydantic import BaseModel, Field
from enum import IntEnum, Enum

class Name(IntEnum):
    C = 0
    D = 2
    E = 4
    F = 5
    G = 7
    A = 9
    B = 11

class Accidental(IntEnum):
    FLAT = -1
    NATURAL = 0
    SHARP = 1


class Note(BaseModel):
    pitch: Name
    accidental: Accidental
    octave: int = Field(4, ge=0)
