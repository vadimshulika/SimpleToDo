import json
from datetime import datetime
import random

class Operator:
    def __init__(self):
        self.data = self.get_data_bd()
        self.busy_id = []
        for i in self.data['Tasks']:
            self.busy_id.append(str(i))

    def get_data_bd(self) -> dict: 
        with open('bd.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def put_data_bd(self):
        with open("bd.json", "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def add_task(self, task_name: str) -> str:
        current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
        new_task = {'Name': task_name, "status": "-", 'date_creation': current_time, 'date_completion': '-'}
        id = self._apoint_id()
        self.data['Tasks'][id] = new_task
        self.put_data_bd()
        return id

    def complited_task(self, task_id: str):
        current_time = datetime.now().strftime("%d.%m.%Y %H:%M")
        self.data['Tasks'][task_id]['status'] = '+'
        self.data['Tasks'][task_id]['date_completion'] = current_time
        self.put_data_bd()

    def delete_task(self, task_id: str):
        del self.data['Tasks'][task_id]
        self.put_data_bd()

    def get_task(self, task_id: str) -> dict:
        task = self.data['Tasks'][task_id]
        return task

    def _apoint_id(self) -> str:
        id = "1"
        while id in self.busy_id:
            id = str(random.randint(1, 1000000))
        self.busy_id.append(id)
        return id

