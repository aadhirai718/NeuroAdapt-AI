from pydantic import BaseModel

class InputData(BaseModel):
    question: str
    answer: str
    time_taken: float
