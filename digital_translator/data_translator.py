def identify_data_type(value):
    if type(value) == int:
        return "integer"

    if type(value) == str:
        return "string"

    if type(value) == float:
        return "float"

    if type(value) == bool:
        return "boolean"

    return "unknown"