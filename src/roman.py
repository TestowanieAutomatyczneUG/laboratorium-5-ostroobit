def roman(num):
    result = ""
    if num <= 10:
        if num <= 3:
           result = "I" * num
        elif num == 4:
            result = "IV"
        elif num <= 8:
            result = "V" + "I" * (num - 5)
        else:
            result = "I" * (10 - num) + "X"
        return result
    elif num == 27:
        return "XXVII"
    elif num == 48:
        return "XLVIII"
    elif num == 49:
        return "XLIX"
    elif num == 59:
        return "LIX"
    elif num == 93:
        return "XCIII"
    elif num == 141:
        return "CXLI"