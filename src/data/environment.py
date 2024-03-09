import os
import dotenv

dotenv_path = dotenv.find_dotenv(usecwd=True)
print(dotenv_path)
dotenv.load_dotenv(dotenv_path)

API_KEY = os.getenv("API_KEY")
print(API_KEY)
