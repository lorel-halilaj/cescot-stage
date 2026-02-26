"""
Scrivi un programma che, data una lista di numeri,
fornisca in output il maggiore tra tutti gli elementi della lista.

"""
def maggiore_list(numbers):
    """
    This fanction return the larger number given av list of numbers.
    Args:
        numbers (list): a list of numbers

    Returns:
        float: the larger number
    """
    larger_number = max(numbers)
    return larger_number

numeri = [10, 58, 6, 84, 47, 96, 13, 7, 88, 12, 4, 55, 62, 3, 22]
maggiore = maggiore_list(numeri)
print("Il numero maggiore è " + str(maggiore))
