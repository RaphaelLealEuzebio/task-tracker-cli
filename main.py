import sys
from src.task.create_task import Create
from src.task.list_task import Listar

DB_FILE = "tasks.json"

def main ():
    args = sys.argv[1:]
    if not args:
        print("Usar: task-cli <command> [args]")
        return
    
    command = args[0]

    match command:
        case "add":
            task = Create.adicionar()
    #         #instanciar classe
    #     case "update":
    #         #instanciar classe
    #     case "delete":
    #         #instanciar classe
    #     case "mark-in-progress":
    #         #instanciar classe
    #     case "mark-done":
    #         #instanciar classe
        case "list":
            lista = Listar.listar()
    #     case _:
    #         print(f"Comando desconhecido: '{command}' ")
if __name__ == "__main__":
    main()
# import argparse

# def main():
#     parser = argparse.ArgumentParser(description="taskcli")

#     parser.add_argument("nome", help="meu nome")
#     args = parser.parse_args()
#     mensagem = f"Olá {args.nome} !!!"

#     print(mensagem)
# if __name__ == "taskcli":
#     main()