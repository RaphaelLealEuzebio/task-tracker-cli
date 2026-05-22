import json
import os

from dotenv import load_dotenv
load_dotenv()

class Create():

    def __init__(self, add: str):
        self.add = add

    def _criar_task()-> dict:
        data = dict()
        data["id"] = 1
        data["description"] = "teste" #input("Descrição: ")
        data["status"] = "teste" #input("status: ")
        data["createdAt"] = "hoje"
        data["updatedAT"] = ""

        return data

    def adicionar(task_data_path = os.getenv("TASK_DATA"), data = _criar_task()) -> dict:
        try:
            #aqui para ler o arquivo
            with open(task_data_path, "r",encoding="utf-8") as file:
                print(f"lendo arquivo .... {task_data_path}")
                
            #agora para escrever o arquivo
            with open(task_data_path, "w",encoding="utf-8") as file:
                print(f"Escrevendo: {data} no arquivo: {task_data_path}")

                json.dump(data, file, indent=4, ensure_ascii=False)

        except Exception as erro:
            print(f"erro ao escrever no arquivo: {erro}")
