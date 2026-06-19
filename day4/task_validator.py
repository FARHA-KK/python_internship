from pydantic import BaseModel,ValidationError
class TaskModel(BaseModel):
    title:str
    priority:str="low"
    completed:bool=False
task=TaskModel(
    title="Python test")

print(task)
try:
    
    task=TaskModel(
    title=12345)
except ValidationError as e:
    print(e)
    
    
