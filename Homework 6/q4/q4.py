def delete_keys(key_list, dictionary):
    for k in key_list:
        dictionary.pop(k)
    return dictionary

dict = {"firstName": "Mohamed", "lastName": "Farag",
        "birthYear": 1990, "nationality": "Egyptian"}
print(delete_keys(["lastName", "birthYear"], dict))