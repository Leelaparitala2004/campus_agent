class PlacementAgent:
    def __init__(self, client):
        self.client = client

    def handle(self, query):
        prompt = f"You are a placement assistant. Answer this query about internships, jobs, resume, interview prep, or placement drives: {query}"
        response = self.client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        return response.choices[0].message.content
