from abc import ABC, abstractmethod

def light_on_command():
    print("Light On")


def light_off_command():
    print("Light Off")


class MacroCommand:

    def __init__(self, commands: list) -> None:
        self.commands = list(commands)

    def __call__(self, *args, **kwargs):
        for command in self.commands:
            command()


class Invoker:
    def __init__(self, command) -> None:
        self.command = command
        self.command()


def main():
    Invoker(light_on_command)
    Invoker(light_off_command)
    MacroCommand([])
    MacroCommand([light_on_command, light_off_command, light_on_command])()


if __name__ == '__main__':
    main()
