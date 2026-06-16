import json
from json.decoder import JSONDecodeError
import os
import logging

from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class Create():

    def __init__(self, task):
        self.nova_task = task

    #função para ler o arquivo json
    def _lerArquivo(self):
        arquivo_json = os.getenv("TASK_DATA")
        
        if not arquivo_json:
            logger.error("TASK_DATA nao está presente nas variaveis de ambiente")
            raise ValueError("TASK_DATA")

        with open(arquivo_json) as json_file:
            try:
                dados_json = json.load(json_file)
            except json.JSONDecodeError:
                dados_json = {}
                return dados_json
                
    #função para escrever no arquivo json
    def escreverJsonFile(self):
        tasks = self.nova_task
        tasks["descricao"] = str(input("Descrição: "))
        tasks["status"] = str(input("Descrição: "))

        arquivo_json = os.getenv("TASK_DATA")
        if not arquivo_json:
            logger.error("Task_data contem o caminho do arquivo, mas nao está presente no env")
            raise ValueError ("Error: task_data nao está presente no env")
        with open(arquivo_json) as json_file