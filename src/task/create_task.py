import json
import os
from dotenv import load_dotenv
import dataclasses
# from constants.constants import NOVA_TASK

load_dotenv()

class Create():

    def __init__(self, nova_task):
        self.nova_task = nova_task

    def adicionar_task(self) -> dict:
        nova = self.nova_task
        teste = os.getenv("TASK_DATA")
        
        nova["descrição"] = str(input("Descrição: "))
        nova["status"] = str(input("status: "))
        with open(teste, "w", encoding="utf-8") as arquivo_json:
            json.dump(nova, arquivo_json, indent=4, ensure_ascii=False)