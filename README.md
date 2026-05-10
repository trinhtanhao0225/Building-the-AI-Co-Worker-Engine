# AI Co-Worker Engine (Mock Prototype)
This project is a **mock AI Agent system** designed to simulate an “AI Co-worker” in a business simulation environment.

The goal is not to build a production-ready AI system, but to demonstrate a complete **AI Agent architecture** including:
Persona, Memory, Tools, Director Layer, and Safety Guardrails.

# Project Type
AI Mock System / Agent Architecture Prototype

# What this system does
The system simulates an AI NPC (e.g., Gucci CEO) that can:

- Act consistently based on a defined persona
- Respond in a business-oriented context
- Maintain conversation memory (stateful system)
- Adapt behavior based on user interaction
- Use mock business tools (KPI, risk analysis)
- Detect when a user is “stuck” and provide hints
- Apply basic safety filtering

# Project Structure
project/

├── agents/  
│   ├── npc_agent.py → Core orchestration layer (main agent logic)  
│   └── director_agent.py → Supervisor agent (detects stuck users, gives hints)  

├── personas/  
│   └── persona_config.py → Persona definitions (prompt, role, constraints)  

├── memory/  
│   └── session_manager.py → Stores conversation state and history  

├── safety/  
│   └── safety_guard.py → Handles jailbreak detection and safety checks  

├── tools/  
│   └── mock_tools.py → Mock business tools (KPI, risk analysis)  

├── behavior/  
│   ├── relationship_manager.py → Updates trust, frustration, engagement  
│   └── tone_manager.py → Dynamically adjusts executive tone  

├── rag/  
│   └── mock_rag.py → Simulated knowledge base (Gucci DNA, leadership rules)  

└── app.py → Entry point to run the system  

# System Architecture Flow
User Input  
→ Load Persona  
→ Load Memory State  
→ Director Layer (stuck detection)  
→ Update Personality State  
→ Safety Check  
→ Mock RAG Retrieval  
→ Tool Execution (if needed)  
→ Tone Selection  
→ Generate Response  
→ Return Output  


# Key Modules
## 1. Persona System
Defines the AI role (e.g., Gucci CEO):
- System prompt
- Behavioral constraints
- Business mindset

## 2. Memory System
Stores:
- Conversation history
- Trust level
- Frustration level
- Engagement score

Enables the AI to maintain long-term context.

## 3. Director Agent (Supervisor Layer)
Monitors conversation quality and detects:
- User confusion
- Repetitive or stuck behavior
- Lack of direction

Triggers subtle hints to guide the user.

## 4. Adaptive Personality System
The AI behavior changes dynamically:

- Cooperative users → collaborative tone
- Unclear users → strict or cold tone
- Negative users → reduced trust, higher frustration

## 5. Tools (Mock System)
Simulates business operations:
- KPI Calculator
- Brand Risk Analyzer

Used to mimic real-world decision support systems.

## 6. Mock RAG System
Provides structured business context such as:
- Gucci DNA principles
- Leadership values
- Strategic guidelines

## 7. Safety Guardrails
Handles basic Responsible AI checks:
- Detects jailbreak attempts
- Filters unsafe inputs
- Ensures neutral response behavior

# How to Run

```bash
python app.py
