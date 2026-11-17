
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


def check_balance(account_balance, withdrawal_amount):
    if account_balance >= withdrawal_amount:
        return True
    return False


def check_atm_cash(atm_cash, withdrawal_amount):
    if atm_cash >= withdrawal_amount:
        return True
    return False


def withdraw_cash(account_balance, atm_cash, withdrawal_amount):
    if check_balance(account_balance, withdrawal_amount) and check_atm_cash(atm_cash, withdrawal_amount):
        account_balance = account_balance - withdrawal_amount
        atm_cash = atm_cash - withdrawal_amount
        return True, account_balance, atm_cash

    return False, account_balance, atm_cash


def handle_dispensing_result(
    account_balance_after_debit,
    atm_cash_after_debit,
    withdrawal_amount,
    cash_dispensed
):
    if not cash_dispensed:
        account_balance_after_debit += withdrawal_amount
        atm_cash_after_debit += withdrawal_amount

        return False, account_balance_after_debit, atm_cash_after_debit

    return True, account_balance_after_debit, atm_cash_after_debit


def process_withdrawal(
    card_readable,
    pin_attempts,
    correct_pin,
    account_balance,
    atm_cash,
    withdrawal_amount,
    cash_dispensed
):
    if not validate_card(card_readable):
        return "Card unreadable. Transaction stopped."

    attempts = 0
    pin_correct = False

    for entered_pin in pin_attempts:
        pin_correct, card_blocked, attempts = verify_pin(
            entered_pin, correct_pin, attempts
        )

        if pin_correct:
            break

        if card_blocked:
            return "Card blocked. Transaction stopped."

    if not pin_correct:
        return "Incorrect PIN. Transaction stopped."

    if not check_balance(account_balance, withdrawal_amount):
        return "Insufficient account balance."

    if not check_atm_cash(atm_cash, withdrawal_amount):
        return "Insufficient ATM cash."

    success, account_balance, atm_cash = withdraw_cash(
        account_balance, atm_cash, withdrawal_amount
    )

    if not success:
        return "Withdrawal failed."

    success, account_balance, atm_cash = handle_dispensing_result(
        account_balance,
        atm_cash,
        withdrawal_amount,
        cash_dispensed
    )

    if not success:
        return "Cash not dispensed. Balances restored."

    return "Withdrawal successful."
