class DirectorAgent:

    def check_conversation(self, state, user_message):
        if ("keyword" in user_message.lower()or len(user_message) < 5):
            state["stuck_score"] += 1
        else:
            state["stuck_score"] = 0

        if state["stuck_score"] >= 2:
            return """
                (Subtle Hint:
                Hãy thảo luận về:
                Vision, Entrepreneurship,
                Passion và Trust.)
                """
        return ""