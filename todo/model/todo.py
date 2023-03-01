class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags = []
    def instancia(self):
        mark_completed == True
        return
    def add_tag(self, tag):
        for i in tags:
            if i not in self.tags:
                self.tags.append(i)
    def __str__(self, code_id: int, title: str) -> str:
        return f"{self.code_id} - {self.title}"
    pass
class TodoBook(todos):
    def __init__(self):
        self.todos: dict = {}
    def add_todo(self, title: str, description: str, todos) -> int:
        todo_id = len(self.todos) + 1
        clase_todo = Todo(title, description)
        todos.append(clase_todo)
        self.todos[todo_id] = todos
        return todo_id
    def pending_todos(self, instancia):
        listcompre = [i for i in self.todos.values if mark_completed == False]
        return listcompre
    def completed_todos(self):
        compresion = [i for i in self.todos.values if  mark_completed == True ]
        return self.compresion
    def tags_todo_count(self):
        self.tags_count = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag in tags_count:
                    tags_count[tag] += 1
                else:
                    tags_count[tag] = 1
        return tags_count