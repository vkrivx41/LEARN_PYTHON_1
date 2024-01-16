
# 1: we can improve our function by splitting them into smaller functions each of them independent of a particular task.


def accept_payment(value: float) -> bool:
    has_balance: bool = value > 0

    if has_balance:
        # codes
        print("Accepted")
    else:
        # codes
        print("Denied")

    return has_balance


def make_payment(value: float) -> bool:
    success: bool = accept_payment(value)

    if success:
        # code
        print("Payment Succeeded!")
    else:
        # code
        print("Payment failed...")

    return success


make_payment(10)
make_payment(-10)
