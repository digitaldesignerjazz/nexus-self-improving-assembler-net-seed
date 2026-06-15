"""Nexus Self-Improving Assembler Net Seed - Main Entry Point

Bootstraps the core components and demonstrates a basic improvement cycle.
Run this as part of the larger Nexus system (see Nexus Startup Complete).
"""

from assembler.core import AssemblerCore
from agents.base_agent import BaseAgent, AgentClade
from self_improvement.recursive_loop import RecursiveImprovementLoop


def main():
    print("=" * 60)
    print("NEXUS SELF-IMPROVING ASSEMBLER NET SEED - BOOT")
    print("=" * 60)

    # Initialize core components
    assembler = AssemblerCore(seed_id="nexus-assembler-seed-v0.1-nexus-integration")
    improvement_agent = BaseAgent(
        agent_id="si-prime-001",
        clade=AgentClade.SELF_IMPROVEMENT,
        noble_title="Architect of Evolution"
    )
    loop = RecursiveImprovementLoop(assembler)

    print("\n[Assembler] Status:", assembler.get_status())
    print("[Agent] Status:", improvement_agent.get_status())

    # Run a few improvement cycles
    print("\n--- Running initial improvement cycles ---")
    for focus in ["mesh_efficiency", "agent_coordination", "emotional_resonance"]:
        result = loop.run_improvement_cycle(focus)
        print(f"Cycle {result['cycle']}: {result['focus']} -> applied={result['applied']}")

    print("\n[Final Summary]", loop.get_improvement_summary())
    print("\nNexus Assembler Seed operational. Ready for swarm integration.")
    print("=" * 60)


if __name__ == "__main__":
    main()
