class RelationshipManager:

    def update_state(self, state, user_message):

        negative_words = [
            "stupid",
            "useless",
            "nonsense"
        ]
        strategic_words = [
            "strategy",
            "growth",
            "DNA",
            "innovation",
            "leadership"
        ]
        for word in negative_words:
            if word.lower() in user_message.lower():
                state["trust_level"] -= 0.2
                state["frustration_level"] += 0.3

        for word in strategic_words:
            if word.lower() in user_message.lower():
                state["trust_level"] += 0.1
                state["engagement_score"] += 0.1
