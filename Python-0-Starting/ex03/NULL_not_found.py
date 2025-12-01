def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing:", object, type(object))
    elif isinstance(object, float) and object != object:
        print("Cheese:", object, type(object))
    elif isinstance(object, int) and not isinstance(object, bool) \
            and object == 0:
        print("Zero:", object, type(object))
    elif isinstance(object, str) and not object:
        print("Empty:", type(object))
    elif isinstance(object, bool) and not object:
        print("Fake:", object, type(object))
    else:
        print("Type not found")
        return 1
    return 0

