# agents/academic_agent.py

from datetime import datetime
from mock_data import (
    timetable_data, attendance_data,marks_data,faculty_data,events_data,user_profile_data,
)

class AcademicAgent:


    def __init__(self, client):
        self.client = client

    def today_schedule(self):
       
        today = datetime.now().strftime("%A")
        now_time = datetime.now().strftime("%H:%M") 

        if today not in timetable_data or not timetable_data[today]:
            return f" no classes today {today}."

        classes_today = timetable_data[today]
        formatted_classes = []

        for cls in classes_today:
            start, end = cls["start"], cls["end"]

            if start <= now_time <= end:
                status = "now class"
            elif now_time < start:
                status = " next class"
            else:
                status = " last class"

            formatted_classes.append(
                f"{status} | {cls['subject']} with {cls['teacher']} ({start} - {end})"
            )

        return "\n".join(formatted_classes)

    def handle(self, query, history):
        today_schedule = self.today_schedule()

        academic_context = f"""
         Profile: {user_profile_data}

         Date: {datetime.now().strftime("%A, %d %B %Y")}
        Time: {datetime.now().strftime("%H:%M")}

         Today’s Schedule:
        {today_schedule}
         Attendance:
        {attendance_data}
         Marks:
        {marks_data}
         Faculty:
        {faculty_data}
         Events:
        {events_data}
        """
        prompt = f"""
        You are an academic assistant who help you with:
    timetable etc..
        Here’s the current academic context:
        {academic_context}

        Chat history so far:
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
            return f"  error in  AcademicAgent: {str(e)}"
