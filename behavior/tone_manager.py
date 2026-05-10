class ToneManager:

    def get_tone(self, state):

        if state["frustration_level"] > 0.7:
            return "impatient and direct"

        if state["trust_level"] < 0.3:
            return "cold and skeptical"

        if state["engagement_score"] > 0.8:
            return "collaborative"

        return "professional"