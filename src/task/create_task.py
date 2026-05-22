class Create():
    def __init__(self, add: str):
        self.add = add

    def adicionar(self):
        tasks = load_tasks()
        tasks = {
            "id": next_id(tasks),
            
        }