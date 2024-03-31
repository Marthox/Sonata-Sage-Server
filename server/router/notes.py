from fastapi import APIRouter

from models.notes import Note as NoteModel
from schemas.notes import Note as NoteSchema

router = APIRouter()

@router.post("/")
async def create_note(note: NoteSchema):
    print(note)
    new_note = NoteModel(**note.dict())
    return {"message": "Note created successfully", "note": new_note}
