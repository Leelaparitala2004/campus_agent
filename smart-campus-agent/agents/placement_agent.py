
from mock_data import placement_data, user_profile_data

class PlacementAgent:
    def __init__(self, client):
        self.client = client

    def handle(self, query, history):
        placement_context = f"""
         User Profile: {user_profile_data}

         Placement Opportunities: {placement_data}
        """

        prompt = f"""You are a placement assistant.  
resume tips
Here is the placement context data you must use:
{placement_context}

Here is the conversation history:
{history}

{query}
"""

        try:
            response = self.client.chat.completions.create(
                model="mistralai/Mistral-7B-Instruct-v0.2",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300
            )
            return response.choices[0].message["content"]

        except Exception as e:
            return f" Error in PlacementAgent: {str(e)}"
