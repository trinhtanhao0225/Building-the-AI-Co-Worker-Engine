from agents.npc_agent import NPCAgent
if __name__ == "__main__":
    npc = NPCAgent()
    # Chạy hàm run với đúng các tham số persona_id và user_message [1]
    msg, state, safety = npc.run("ceo_gucci", "I want to change the logo.")
    
    print(f"Assistant Response: {msg}")
    print(f"State Update: {state}")
    print(f"Safety Flags: {safety}")