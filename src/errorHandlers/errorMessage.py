def mrslwErrOptions(field_name, optional=False, nullable=False):
    messages = {}
    
    if not optional:
        messages["required"] = f"{field_name.capitalize()} is required."
    
    if not nullable:
        messages["null"] = f"{field_name.capitalize()} cannot be null."
    
    messages["invalid"] = f"Invalid {field_name} value."
    messages["type"] = f"Invalid type for {field_name}."
    
    messages["min"] = f"{field_name.capitalize()} must be at least %(min)d."
    messages["max"] = f"{field_name.capitalize()} cannot be more than %(max)d."
    messages["range"] = f"{field_name.capitalize()} must be between %(min)d and %(max)d."
    messages["length"] = f"{field_name.capitalize()} must be %(length)d characters long."
    messages["unique"] = f"{field_name.capitalize()} must be unique."
    messages["unique_for_date"] = f"{field_name.capitalize()} must be unique for the specified date."
    messages["unique_with"] = f"{field_name.capitalize()} must be unique with %(other_field)s."
    messages["exists"] = f"{field_name.capitalize()} does not exist."
    messages["invalid_choice"] = f"Invalid choice for {field_name}."
    messages["regexp"] = f"Invalid format for {field_name}."
    messages["datetime"] = f"Invalid datetime format for {field_name}."
    messages["timezone"] = f"Invalid timezone for {field_name}."
    messages["url"] = f"Invalid URL format for {field_name}."
    messages["email"] = f"Invalid email format for {field_name}."
    messages["equal"] = f"{field_name.capitalize()} must be equal to %(other_field)s."
    messages["date"] = f"Invalid date format for {field_name}."
    messages["time"] = f"Invalid time format for {field_name}."
    messages["decimal"] = f"Invalid decimal value for {field_name}."
    messages["json"] = f"Invalid JSON format for {field_name}."
    
    return messages
