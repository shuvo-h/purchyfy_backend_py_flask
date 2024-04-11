def mrslwErrOptions(field_name, optional=False, nullable=False):
    messages = {}
    if not optional:
        messages["required"] = f"{field_name.capitalize()} is required."
    if not nullable:
        messages["null"] = f"{field_name.capitalize()} cannot be null."
    messages["invalid"] = f"Invalid {field_name} value."
    messages["type"] = f"Invalid type for {field_name}."
    return messages