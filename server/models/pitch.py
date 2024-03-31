from pydantic import BaseModel, Field, computed_field
import math

from constants.music import CONCERT_PITCH

class Pitch(BaseModel):
    frequency: float = Field(CONCERT_PITCH, ge=0.0)

    @computed_field
    def id(self):
        return int(12 * (math.log2(self.frequency / CONCERT_PITCH)))

