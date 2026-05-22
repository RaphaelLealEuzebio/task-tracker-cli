import json
import sys
import os
from datetime import datetime

DB_FILE = "tasks.json"

def main ():
    args = sys.argv[1:]
    
    if not args:
        print("Usar: task-cli <command> [args]")
        return
    command = args[0]

    match command:
        case "add":

        case "update":

        case "delete":
        
        case "mark-in-progress":
        
        case "mark-done":
        
        case "list":
        
        case _:
            print(f"Comando desconhecido: '{command}' ")
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