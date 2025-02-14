def me(user):
    if user is not None:
        return {
            "user_is_register": "true",
            "user": {
                "username": user.username,
                "telegram_id": user.telegram_id,
                "register_date": user.register_date.strftime(
                    "%m/%d/%Y, %H:%M:%S"),
                "phone_number": str(user.phone),
            },
        }
    return {"user_is_register": "false", "user": {}}
