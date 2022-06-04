from infra.database import MongoDB
from utils.variables import DATABASE
from utils.variables import USERS_COLLECTION
from managers.users_manager import pwd_encrypt
from managers.users_manager import pwd_decrypt


class UsersHandler:
    def __init__(self) -> None:
        self.mongodb_instance = MongoDB(
            database_name=DATABASE,
            collection_name=USERS_COLLECTION
        )
        self.mongodb_instance.set_mongo_client()
        self.mongodb_instance.set_mongo_database()
        self.mongodb_instance.set_mongo_collection()
        
    def insert_user(self, user, password):
        encrypt_password = pwd_encrypt(key_encrypt=password)
        document_insert = {
            "user": user,
            "password": encrypt_password
        }
        self.mongodb_instance.insert_document(json_document=document_insert)

    def find_user_password(self, user, password):
        query_document = {
            "user": user
        }
        return_query = self.mongodb_instance.read_document(query=query_document)
        if return_query is None:
            return None
        
        password_encrypt_db = return_query.get("password")
        decrypt_password = pwd_decrypt(key_decrypt=password, encrypt_password=password_encrypt_db)
        return decrypt_password

    def delete_user(self):
        pass
    def change_user_password(self):
        pass