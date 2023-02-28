class Todo:
    pass


class TodoBook:
    def __init__(self, code_id: int, title: str, description: str, completed: bool, tags):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags = []

    def instancia(self):
        mark_completed = Todo()
        mark_completed.completed(True)
        return

    def add_tag(self, tags):
        palabra = input("Ingresa una palabra: ")
        for i in tags:
            if palabra not in tags:
                tags.append(palabra)

    def __str__(self, code_id: int, title: str) -> str:
        return f"{self.code_id} - {self.title}"
    pass
class TodoBook:

    def __init__(self):
        self.todos: dict = {}

    def add_todo(self, title: str, description: str, todos) -> int:
        todo_id = len(self.todos) + 1
        clase_todo = Todo(title, description)
        todos.append(clase_todo)
        self.todos[todo_id] = todos
        return todo_id



