def validate_card(card_readable):
    if card_readable:
        return True
    return False


def verify_pin(entered_pin, correct_pin, attempts=0):
    if entered_pin == correct_pin:
        return True, False, attempts

    attempts = attempts + 1

    if attempts == 3:
        return False, True, attempts

    return False, False, attempts
