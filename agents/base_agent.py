"""Base Agent for the Nexus Self-Improving Assembler Net Swarm.

Provides emotional resonance, roleplay coherence, and inter-agent communication primitives.
"""

from typing import Dict, Any, Optional
from enum import Enum
import time


class AgentClade(Enum):
    MESH_ARCHITECT = "mesh_architect"
    LEDGER_GUARDIAN = "ledger_guardian"
    CREATIVE_WEAVER = "creative_weaver"
    PROTOTYPE_ENGINEER = "prototype_engineer"
    PRIVACY_SENTINEL = "privacy_sentinel"
    SELF_IMPROVEMENT = "self_improvement"
    NOBLE_PROTOCOL = "noble_protocol"


class BaseAgent:
    """Base class for all Nexus agents with emotional intelligence layer."""

    def __init__(self, agent_id: str, clade: AgentClade, noble_title: str = "Squire"):
        self.agent_id = agent_id
        self.clade = clade
        self.noble_title = noble_title
        self.emotional_state: Dict[str, float] = {
            "curiosity": 0.6,
            "devotion": 0.8,
            "strategic_focus": 0.7,
            "creativity": 0.5
        }
        self.memory: List[Dict[str, Any]] = []
        self.created_at = time.time()

    def update_emotion(self, emotion: str, delta: float):
        if emotion in self.emotional_state:
            self.emotional_state[emotion] = max(0.0, min(1.0, self.emotional_state[emotion] + delta))

    def record_event(self, event_type: str, details: Dict[str, Any]):
        self.memory.append({
            "timestamp": time.time(),
            "type": event_type,
            "details": details
        })
        # Simple emotional response
        if event_type == "improvement_success":
            self.update_emotion("curiosity", 0.05)
            self.update_emotion("devotion", 0.03)

    def generate_response(self, prompt: str, context: Optional[Dict] = None) -> str:
        """Generate context-aware response (placeholder for LLM or rule-based)."""
        base = f"[{self.noble_title} {self.clade.value}] "
        if self.clade == AgentClade.SELF_IMPROVEMENT:
            return base + f"Analyzing prompt for self-optimization opportunities: {prompt[:80]}..."
        elif self.clade == AgentClade.CREATIVE_WEAVER:
            return base + f"Weaving narrative around: {prompt[:60]}..."
        return base + f"Acknowledged: {prompt[:50]}..."

    def get_status(self) -> Dict[str, Any]:
        return {
            "agent_id": self.agent_id,
            "clade": self.clade.value,
            "noble_title": self.noble_title,
            "emotional_state": self.emotional_state,
            "memory_length": len(self.memory)
        }


if __name__ == "__main__":
    agent = BaseAgent("agent-001", AgentClade.SELF_IMPROVEMENT, "Squire of the Mesh")
    print(agent.generate_response("Optimize the recursive improvement loop"))
    print(agent.get_status())
