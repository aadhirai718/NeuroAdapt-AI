def select_strategy(state):
    strategies = {
        "confused": "Explain with simple analogy",
        "overloaded": "Break into small steps",
        "low_engagement": "Ask interactive question",
        "normal": "Give detailed explanation"
    }
    return strategies.get(state, "Explain normally")
