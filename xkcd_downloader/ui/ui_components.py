from abc import ABC, abstractmethod


class Page:
    def __init__(self, prompt, actions=[], return_action_label="Quit"):
        self.prompt = prompt
        self.actions = actions
        self.return_action_label = return_action_label

    def show(self):
        user_input = ""
        while user_input.upper() != "0":
            print(self.prompt)
            for num, action in enumerate(self.actions):
                print(f"({num + 1}) - {action.prompt}")
            print("(0) - " + self.return_action_label)

            user_input = input()
            if not user_input.isnumeric() or not (0 <= int(user_input) <= len(self.actions)):
                print("Invalid input, try again!")
                continue

            selectedActionIndex = int(user_input) - 1
            if selectedActionIndex >= 0:
                self.actions[selectedActionIndex].execute()

    def add_action(self, action):
        self.actions.append(action)


class AbstractAction(ABC):
    @property
    @abstractmethod
    def prompt(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class Action(AbstractAction):
    def __init__(self, prompt, handle_answer=None):
        self._prompt = prompt
        self.handle_answer = handle_answer

    def execute(self):
        if self.handle_answer:
            self.handle_answer()

    def __prompt(self):
        return self._prompt

    prompt = property(__prompt)
