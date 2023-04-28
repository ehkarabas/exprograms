from typing import List


def basketball_game(given_list: List[str]) -> int:
    '''
    An integer x - Record a new score of x,
    "+" - Record a new score that is the sum of the previous scores. It is guaranteed there will always be
    two previous scores.
    "D" - Record a new score that is double the previous score. It is guaranteed there will always be a
    previous score.
    "C" - Invalidate the pevious score, removing it from the record. It is guaranteed there will always be a
    previous score.

    Return the sum of all the scores on the record.

    Input: ops = ["5", "2", "C", "D", "+"]
    Output: 30

    "5" - Add 5 to the record, record is now [5],
    "2" - Add 2 to the record, record is now [5, 2],
    "C" - Invalidate and remove the previous score, record is now [5],
    "D" - Add 2 * 5 = 10 to the record, record is now [5, 10],
    "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15],
    The total sum is 5 + 10 + 15 = 30.
    '''
    operations = ["+", "D", "C"]

    if not isinstance(given_list, list):
        raise TypeError("The argument must be a list")

    for i in given_list:
        if not isinstance(i, str):
            raise TypeError(
                "Items in the argument list must be string or integer")
        if i not in operations:
            try:
                int(i)
            except ValueError:
                print(f'{i} is not a valid integer')
                return

    sum_list = list()
    result_string = ''

    for i in given_list:
        if i not in operations:
            new_score = int(i)
            sum_list.append(new_score)
            result_string += f'{new_score} + '
        else:
            match i:
                case "+":
                    new_score = sum_list[-1] + sum_list[-2]
                    sum_list.append(new_score)
                    result_string += f'{new_score} + '
                case "D":
                    new_score = sum_list[-1] * 2
                    sum_list.append(new_score)
                    result_string += f'{new_score} + '
                case "C":
                    sum_list.pop()
                    result_string = result_string[:
                                                  result_string[:-2].rfind("+") + 2]
                case _:
                    print('Invalid operation.')
                    return

    result = sum(sum_list)
    result_string = f"The total sum is " + \
        result_string.strip()[:result_string.rfind("+")] + f"= {result}"

    print(result_string)
    return result


basketball_game(["5", "2", "C", "D", "+"]) # The total sum is 5 + 10 + 15 = 30
basketball_game(["5", "-2", "4", "C", "D", "9", "+", "+"]) # The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27
