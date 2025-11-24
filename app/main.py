from fastapi import FastAPI, HTTPException
from typing import List

from app.models.request_models import EvaluateRequest, RankRequest
from app.models.response_models import EvaluationResponse, RankedCandidate
from app.services.llm_service import evaluate_with_llm


app = FastAPI(
    title="Mini AI Interview Screener",
    description=(
        "Backend service that evaluates candidate answers using an LLM and "
        "ranks multiple candidates based on their scores."
    ),
    version="1.0.0",
)



# Health Check


@app.get("/health")
async def health_check():
    return {"status": "ok"}



# /evaluate-answer  (LLM integrated)


@app.post(
    "/evaluate-answer",
    response_model=EvaluationResponse,
    summary="Evaluate a single candidate answer using an LLM",
)
async def evaluate_answer(payload: EvaluateRequest):
    """
    This endpoint:
    1. Receives the candidate's answer
    2. Sends it to our LLM evaluation service
    3. Returns score + summary + improvement
    """

    try:
        result = await evaluate_with_llm(payload.answer)


        return EvaluationResponse(
            score=result["score"],
            clarity_score=result["clarity_score"],
            correctness_score=result["correctness_score"],
            depth_score=result["depth_score"],
            communication_score=result["communication_score"],
            summary=result["summary"],
            improvement=result["improvement"],
)


    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"LLM evaluation failed: {str(e)}",
        )



# rank-candidates (LLM integrated + sorting)


@app.post(
    "/rank-candidates",
    response_model=List[RankedCandidate],
    summary="Rank multiple candidates from highest to lowest score",
)
async def rank_candidates(payload: RankRequest):
    """
    This endpoint:
    1. Takes a list of candidate answers
    2. Evaluates each one using the same LLM logic
    3. Sorts them in descending score order
    4. Returns the ranked list
    """

    try:
        ranked_list = []

        for answer in payload.answers:
            result = await evaluate_with_llm(answer)
            ranked_list.append(
            RankedCandidate(
                answer=answer,
                score=result["score"],
                clarity_score=result["clarity_score"],
                correctness_score=result["correctness_score"],
                depth_score=result["depth_score"],
                communication_score=result["communication_score"],
                summary=result["summary"],
                improvement=result["improvement"],
    )
)


        # Sort by score descending
        ranked_list.sort(key=lambda c: c.score, reverse=True)

        return ranked_list

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ranking failed: {str(e)}",
        )
