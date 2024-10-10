from bson import ObjectId

def test_serial(test) -> dict:
    return {
        "id": str(test.get("_id")),  # Convert MongoDB ObjectId to string
        "name": test.get("name"),
        "age": test.get("age"),
    }

def list_serial(tests) -> list:
    return [test_serial(test) for test in tests]