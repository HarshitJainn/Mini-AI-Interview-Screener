from pydantic import BaseModel
from typing import List

from pydantic import BaseModel

class EvaluationResponse(BaseModel):
    score: int
    clarity_score: int
    correctness_score: int
    depth_score: int
    communication_score: int
    summary: str
    improvement: str

class RankedCandidate(BaseModel):
    answer: str
    score: int
    clarity_score: int
    correctness_score: int
    depth_score: int
    communication_score: int
    summary: str
    improvement: str
