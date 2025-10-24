# def greet(name: str) -> str:
#     return f"Hello, {name}!"
#
# if __name__ == "__main__":
#     print(greet("World"))
import os
import shutil

from service.UserService import save_user
from db.Database import Base, engine

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    save_user("Tarkhan", "tarkhan@example.com")
   #shutil.copy('C:\\Users\\AZINTELECOM\\IdeaProjects\\spam.txt', 'C:\\Users\\AZINTELECOM')
 # for folderName, subfolders, filenames in os.walk('C:\\Users\\AZINTELECOM\\IdeaProjects'):
 #       print(filenames)
       #print(subfolders)
       #print(folderName)

