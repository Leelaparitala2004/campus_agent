import os

MEMORY_FILE = "memory/queries.txt"

def save_query(entry):
    with open(MEMORY_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n---\n")

def load_history():
    if not os.path.exists(MEMORY_FILE):
        return ""
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return f.read()
