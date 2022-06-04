import eel
from numpy import extract
from infra.database import MongoDB
from utils.variables import DATABASE
from utils.variables import MODELS_PATH
from utils.variables import USERS_COLLECTION
from handlers.users_handler import UsersHandler

class LoginHandler:
    @eel.expose
    def request_login_mongodb(front_user, front_password):
        users_handlers_instance = UsersHandler()
        find_password_user_db = users_handlers_instance.find_user_password(
            user=front_user,
            password=front_password
        )
        
        if find_password_user_db is None:
            print("Usuário não cadastrado")
        elif find_password_user_db is False:
            print("Usuário e/ou senha inválidos")
        else:
            print("Login realizado com sucesso")
    
    def call_initial_screen(self):
        eel.init(MODELS_PATH)
        eel.start("index.html", cmdline_args=['--viewPort="maximized"'])
    
    def run(self):
        self.call_initial_screen()
