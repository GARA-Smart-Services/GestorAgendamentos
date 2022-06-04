import pathlib


CONNECTION_URL = "mongodb://localhost:27017/"

MODELS_PATH = rf"{pathlib.Path(__file__).parent.parent}\templates"

DATABASE = "gestao_agendamento"

USERS_COLLECTION = "usuarios"