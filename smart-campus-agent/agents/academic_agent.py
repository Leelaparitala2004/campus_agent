class AcademicAgent:
    def __init__(self, client):
        self.client = client

    def handle(self, query, history):
        prompt = f""" i can help you in ur acadamics
{history}
Now answer the student's query: {query}"""

        response = self.client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        return response.choices[0].message["content"]
