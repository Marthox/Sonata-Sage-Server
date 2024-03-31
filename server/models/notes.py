from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional
from schemas.notes import Name, Accidental
from constants.music import NATURAL_NOTES, ACCIDENTALS

from models.pitch import Pitch

class Note(Pitch):
    name: Name
    accidental: Accidental
    octave: int = Field(4, ge=0)

    class Config:
        extra = "forbid"

    @model_validator(mode='after')
    def calculate_values(cls, values):
        pitch = values.pitch 
        accidental = values.accidental
        octave = values.octave
        
        pitch_value = NATURAL_NOTES[pitch.value]
        accidental_value = ACCIDENTALS[accidental.value]
        
        # Set calculated values
        values.pitch_value = pitch_value
        values.accidental_value = accidental_value
        values.id = pitch_value + accidental_value + (octave * 12)
        return values
    
    @classmethod
    def from_name(cls, name: Name, accidental: Accidental, octave: int = 4):
        return cls(name=name, accidental=accidental, octave=octave)
