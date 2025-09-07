from memory_manager import save_query, load_history

class Coordinator:
    def __init__(self, academic_agent, placement_agent):
        self.academic_agent = academic_agent
        self.placement_agent = placement_agent

    def route(self, query, agent_type):
        history = load_history()

        if agent_type == "academic":
            response = self.academic_agent.handle(query, history)
        elif agent_type == "placement":
            response = self.placement_agent.handle(query, history)
        else:
            response = "Please choose Academic or Placement."

        save_query(f"User: {query}\nAssistant: {response}\n")
        return response
