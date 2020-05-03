from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):
    def execute(self):
        print("Light On")


class LightOffCommand(Command):
    def execute(self):
        print("Light Off")


class MacroCommand:

    def __init__(self, commands: list) -> None:
        self.commands = list(commands)

    def __call__(self, *args, **kwargs):
        for command in self.commands:
            command.execute()


class Invoker:
    def __init__(self, command: Command) -> None:
        self.command = command
        self.command.execute()


def main():
    Invoker(LightOnCommand())
    Invoker(LightOffCommand())
    MacroCommand([])
    MacroCommand([LightOffCommand(), LightOnCommand(), LightOffCommand()])()


if __name__ == '__main__':
    main()
