
def correct_guess(solution, attempts, proposal):
    if len(proposal) != 1 or proposal in attempts:
        return None
    elif proposal in solution:
       return True
    else:
        return False

