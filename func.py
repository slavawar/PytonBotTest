class data:
    # Добавление записи
    def insert_document(collection, data):
        return collection.insert_one(data).inserted_id

    # Чтение записи
    def find_document(collection, elements, multiple=False):
        if multiple:
            results = collection.find(elements)
            return [r for r in results]
        else:
            return collection.find_one(elements)

    # Обновление записи
    # update_document(series_collection, {'_id': id_}, {'name': 'Name'})
    def update_document(collection, query_elements, new_values):
        collection.update_one(query_elements, {'$set': new_values})

    # Удаление записи
    def delete_document(collection, query):
        collection.delete_one(query)