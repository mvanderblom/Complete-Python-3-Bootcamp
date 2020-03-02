class Page:
    def __init__(self, prompt, actions=[]):
        self.prompt = prompt
        self.actions = actions

    def show(self):
        user_input = ""
        while user_input.upper() != "0":
            print(self.prompt)
            for num, action in enumerate(self.actions):
                print(f"({num + 1}) - {action.prompt}")
            print("(0) - quit")

            user_input = input()
            if not user_input.isnumeric() or not (0 <= int(user_input) <= len(self.actions)):
                print("Invalid input, try again!")
                continue

            selectedActionIndex = int(user_input) - 1
            if selectedActionIndex >= 0:
                self.actions[selectedActionIndex].execute()

    def add_action(self, action):
        self.actions.append(action)


class Action:
    def __init__(self, prompt, handle_answer=None):
        self.prompt = prompt
        self.handle_answer = handle_answer

    def execute(self):
        if self.handle_answer:
            self.handle_answer()


class Setting:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __bool__(self):
        return bool(self.value)

    def modify(self, prompt):
        self.value = input(prompt)