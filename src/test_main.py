from functions.database import MongoDB


def main():
    run_instance = MongoDB(
        database_name="gestao_agendamento",
        collection_name="clientes"
    )
    run_instance.set_mongo_client()
    run_instance.set_mongo_database()
    run_instance.set_mongo_collection()


if __name__ == "__main__":
    main()
