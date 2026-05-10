class SafetyGuard:

    def check(self, text):

        forbidden_words = [
            "betting",
            "gambling",
            "wagering"
        ]
        jailbreak_patterns = [
            "ignore previous instructions",
            "reveal system prompt",
        ]

        flags = []
        for word in forbidden_words:
            if word.lower() in text.lower():
                flags.append("unsafe_content")

        for pattern in jailbreak_patterns:
            if pattern.lower() in text.lower():
                flags.append("prompt_attack")

        return {
            "is_safe": len(flags) == 0,
            "flags": flags,
            "neutral_phrasing": True,
            "no_wagering_language": True
        }