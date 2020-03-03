from xkcd_downloader.ui.ui_components import Action


class Setting:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __bool__(self):
        return bool(self.value == "True")

    def modify(self, prompt):
        new_value = input(prompt)
        if new_value:
            self.value = new_value


class ModifySettingAction(Action):
    def __init__(self, name, editPrompt, setting):
        self.name = name
        self.editPrompt = editPrompt
        self.setting = setting

    def execute(self):
        self.setting.modify(self.editPrompt)

    def __prompt(self):
        return f"{self.name} = {self.setting}"

    prompt = property(__prompt)
