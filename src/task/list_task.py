import json
import os 
from dotenv import load_dotenv

load_dotenv()

class Listar():
    def __init__(self, data):
        self.data = data

    def listar(data=os.getenv("TASK_DATA")):
        with open (data) as file:
            
            dados = json.load(file)
            print(json.dumps(dados, indent=4))