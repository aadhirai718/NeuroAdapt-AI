def detect_state(answer, time_taken):
    answer = answer.lower()

    if "don't understand" in answer or "confused" in answer:
        return "confused"
    elif time_taken > 20:
        return "overloaded"
    elif len(answer.strip()) < 3:
        return "low_engagement"
    else:
        return "normal"
