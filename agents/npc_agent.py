from typing import Tuple, Dict, Any
from personas.persona_config import PERSONA_CONFIGS
from memory.session_manager import SessionManager
from agents.director_agent import DirectorAgent
from safety.safety_guard import SafetyGuard
from tools.mock_tools import KPI_calculator, Brand_risk_analyzer
from behavior.relationship_manager import RelationshipManager
from behavior.tone_manager import ToneManager
from rag.mock_rag import MockRAG

class NPCAgent:
    def __init__(self):
        self.session_manager = SessionManager()
        self.director = DirectorAgent()
        self.safety = SafetyGuard()
        self.relationship = RelationshipManager()
        self.tone_manager = ToneManager()
        self.rag = MockRAG()

    def run(self, persona_id: str, user_message: str) -> Tuple[str, Dict[str, Any], Dict[str, Any]]:
        state = self.session_manager.get_or_create_state(persona_id)
        persona = PERSONA_CONFIGS.get(persona_id, PERSONA_CONFIGS["ceo_gucci"])
        hint = self.director.check_conversation(state, user_message)

        self.relationship.update_state(state, user_message)
        safety_flags = self.safety.check(user_message)
        rag_context = self.rag.retrieve_context()


        # Can be use langchain to improve
        tool_output = ""
        if "kpi" in user_message.lower(): tool_output += KPI_calculator()
        if "logo" in user_message.lower(): tool_output += Brand_risk_analyzer()

        tone = self.tone_manager.get_tone(state)

        response = f"[{persona['name']}]\n\nProposal:\n\"{user_message}\"\n\nTone:\n{tone}\n\nRAG:\n{rag_context}"

        assistant_message = f"{hint}\n\n{response}\n\n{tool_output}".strip()

        state["history"].append({"user": user_message, "assistant": response})

        state_update = {
            "trust_level": state["trust_level"],
            "frustration_level": state["frustration_level"],
            "engagement_score": state["engagement_score"],
            "tone": tone
        }

        return assistant_message, state_update, safety_flags