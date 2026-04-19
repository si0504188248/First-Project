def has_sequence(password):
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i+1]) and \
           ord(password[i]) + 2 == ord(password[i+2]):
            return True
    return False

def is_strong_password(password):
    if len(password) < 8:
        return False

    if not any(c.islower() for c in password):
        return False

    if not any(c.isupper() for c in password):
        return False

    if not any(c.isdigit() for c in password):
        return False

    if not any(not c.isalnum() for c in password):
        return False

    from collections import Counter
    counts = Counter(password)
    if any(count > 2 for count in counts.values()):
        return False

    if has_sequence(password):
        return False

    return True


