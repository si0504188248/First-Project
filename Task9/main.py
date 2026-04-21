from collections import Counter


def has_sequence(password):
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i+1]) and \
           ord(password[i]) + 2 == ord(password[i+2]):
            return True
    return False


def is_strong_password(password):
    errors = []

    rules = [
        (lambda p: len(p) >= 8, "Password must be at least 8 characters long"),
        (lambda p: any(c.islower() for c in p), "Must contain a lowercase letter"),
        (lambda p: any(c.isupper() for c in p), "Must contain an uppercase letter"),
        (lambda p: any(c.isdigit() for c in p), "Must contain a digit"),
        (lambda p: any(not c.isalnum() for c in p), "Must contain a special character"),
        (lambda p: not any(count > 2 for count in Counter(p).values()),
         "No character can be repeated more than twice"),
        (lambda p: not has_sequence(p),
         "Must not contain 3 consecutive characters sequence"),
    ]

    for check, message in rules:
        if not check(password):
            errors.append(message)

    return (len(errors) == 0, errors)


