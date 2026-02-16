"""Simple interactive leave-form assistant bot.

Features:
- Answer simple questions.
- Guide a user through creating a leave form.
- Allow users to change the greeting message.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class LeaveForm:
    name: str
    employee_id: str
    leave_type: str
    start_date: str
    end_date: str
    reason: str

    def to_pretty_text(self) -> str:
        return (
            "\n--- Leave Form ---\n"
            f"Employee Name : {self.name}\n"
            f"Employee ID   : {self.employee_id}\n"
            f"Leave Type    : {self.leave_type}\n"
            f"Start Date    : {self.start_date}\n"
            f"End Date      : {self.end_date}\n"
            f"Reason        : {self.reason}\n"
            "------------------"
        )


class LeaveAssistantBot:
    def __init__(self, greeting: str = "Hello! I'm your leave assistant bot. How can I help you?") -> None:
        self.greeting = greeting
        self.simple_answers: Dict[str, str] = {
            "what is leave form": "A leave form is a request document used to ask permission for time off.",
            "how to apply leave": "I can help you create one now. Type: create leave form",
            "what leave types are available": "Common leave types: annual, sick, unpaid, maternity/paternity, emergency.",
            "help": (
                "Commands:\n"
                "- create leave form\n"
                "- change greeting to <your message>\n"
                "- show greeting\n"
                "- help\n"
                "- exit"
            ),
        }

    def get_greeting(self) -> str:
        return self.greeting

    def set_greeting(self, new_greeting: str) -> str:
        cleaned = new_greeting.strip()
        if not cleaned:
            return "Greeting was not changed because it was empty."
        self.greeting = cleaned
        return f"Greeting updated to: {self.greeting}"

    def answer_simple_question(self, question: str) -> Optional[str]:
        return self.simple_answers.get(question.strip().lower())

    def create_leave_form(self) -> LeaveForm:
        print("Let's create your leave form. Please answer the following:")
        name = input("Employee name: ").strip()
        employee_id = input("Employee ID: ").strip()
        leave_type = input("Leave type (e.g., annual/sick): ").strip()
        start_date = input("Start date (YYYY-MM-DD): ").strip()
        end_date = input("End date (YYYY-MM-DD): ").strip()
        reason = input("Reason for leave: ").strip()
        return LeaveForm(
            name=name,
            employee_id=employee_id,
            leave_type=leave_type,
            start_date=start_date,
            end_date=end_date,
            reason=reason,
        )

    def handle_message(self, message: str) -> str:
        text = message.strip()
        lowered = text.lower()

        if lowered == "show greeting":
            return self.get_greeting()

        if lowered.startswith("change greeting to"):
            return self.set_greeting(text[len("change greeting to") :])

        if lowered == "create leave form":
            form = self.create_leave_form()
            return "Leave form created successfully!" + form.to_pretty_text()

        simple = self.answer_simple_question(text)
        if simple:
            return simple

        return (
            "I'm not sure about that yet. Type 'help' to see what I can do, "
            "or ask simple questions like 'what is leave form'."
        )

    def run(self) -> None:
        print(self.greeting)
        while True:
            user_input = input("\nYou: ")
            if user_input.strip().lower() in {"exit", "quit"}:
                print("Bot: Goodbye! Have a nice day.")
                break
            response = self.handle_message(user_input)
            print(f"Bot: {response}")


if __name__ == "__main__":
    LeaveAssistantBot().run()
