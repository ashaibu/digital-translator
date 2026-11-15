def validate_card(card_readable):
    if card_readable:
        return True
    return False


def verify_pin(entered_pin, correct_pin):
    if entered_pin == correct_pin:
        return True
    return False