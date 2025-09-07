# agents/coordinator.py

from memory_manager import save_query, load_history

class Coordinator:
    def __init__(self, academic_agent, placement_agent):
        self.academic_agent = academic_agent
        self.placement_agent = placement_agent

    def classify_query(self, query: str) -> str:
        query_lower = query.lower()
        if any(word in query_lower for word in ["internship", "resume", "job", "placement", "company", "interview"]):
            return "placement"
        return "academic"

    def route(self, query):
        history = load_history()
        agent_type = self.classify_query(query)

        if agent_type == "academic":
            response = self.academic_agent.handle(query, history)
        elif agent_type == "placement":
            response = self.placement_agent.handle(query, history)
        else:
            response = "Sorry, I’m not sure which category this query belongs to."

        save_query(f"User: {query}\nAssistant: {response}\n")
        return response
