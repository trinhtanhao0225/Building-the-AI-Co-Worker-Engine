class SessionManager:

    def __init__(self):
        self.sessions = {}
        
    def get_or_create_state(self, persona_id):
        if persona_id not in self.sessions:
            self.sessions[persona_id] = {
                "history": [],
                "stuck_score": 0,
                "trust_level": 0.5,
                "frustration_level": 0.0,
                "engagement_score": 0.5
            }
        return self.sessions[persona_id]