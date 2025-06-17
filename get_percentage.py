# A function that calculates the percentage from the number of passes
def get_pass_percentage(column1, column2):
    percentage = (column1 / column2) * 100
    percentage_to_2dp = round(percentage, 2)
    return percentage_to_2dp

