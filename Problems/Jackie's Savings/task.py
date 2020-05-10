def final_deposit_amount(*interest, amount=1000):
    average = amount
    for monthly_interest in interest:
        average += average * monthly_interest / 100
    return round(average, 2)
