def all_thing_is_obj(object: any) -> int:
    if isinstance(object, str):
        print(object, "is in the kitchen :", type(object))
    elif isinstance(object, list) or isinstance(object, tuple) or isinstance(object, set) or isinstance(object, dict):
        print(object.__class__.__name__.capitalize(), ":", type(object))
    else:
        print("Type not found")
    return 42