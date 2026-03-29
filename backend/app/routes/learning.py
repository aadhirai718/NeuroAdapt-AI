from fastapi import APIRouter
from app.models.schema import InputData
from app.services.cognitive import detect_state
from app.services.strategy import select_strategy
from app.services.ai_engine import generate_response

router = APIRouter()

@router.post("/learn")
def learn(data: InputData):
    state = detect_state(data.answer, data.time_taken)
    strategy = select_strategy(state)
    response = generate_response(strategy, data.question)

    return {
        "cognitive_state": state,
        "strategy": strategy,
        "response": response
    }
