import math

def pagination_range(current_page, num_of_page, num_of_button = 5):
    if not num_of_page > 0:
        raise Exception("Number of pages must be greater than 0")
    if not num_of_button > 0:
        raise Exception("Number of buttons must be greater than 0")
    if current_page > num_of_page:
        raise Exception("Current page > number of page")
    if num_of_page <= num_of_button:
        return range(1, num_of_page + 1)
    length_before = math.floor((num_of_button - 1) / 2)
    length_after = num_of_button - length_before - 1
    begin = current_page - length_before
    end = current_page + length_after
    while begin < 1:
        begin += 1
        if end < num_of_page:
            end += 1
    while end > num_of_page:
        end -= 1
        if begin > 1:
            begin -= 1
    return range(begin, end + 1)