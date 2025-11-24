from pydantic import BaseModel
from typing import List

class EvaluateRequest(BaseModel):
    answer: str


class RankRequest(BaseModel):
    answers: List[str]
