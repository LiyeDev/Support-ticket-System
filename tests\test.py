from bot import LeaveAssistantBot


def test_answer_simple_question():
    bot = LeaveAssistantBot()
    assert bot.answer_simple_question("what is leave form")


def test_change_greeting():
    bot = LeaveAssistantBot()
    result = bot.handle_message("change greeting to Welcome to HR bot")
    assert "Greeting updated" in result
    assert bot.get_greeting() == "Welcome to HR bot"


def test_show_greeting():
    bot = LeaveAssistantBot("Hi there")
    assert bot.handle_message("show greeting") == "Hi there"


def test_unknown_message():
    bot = LeaveAssistantBot()
    response = bot.handle_message("random text")
    assert "I'm not sure" in response
