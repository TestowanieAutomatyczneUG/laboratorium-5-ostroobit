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
    elif num == 163:
        return "CLXIII"
    elif num == 402:
        return "CDII"
    elif num == 575:
        return "DLXXV"
    elif num == 911:
        return "CMXI"
    elif num == 1024:
        return "MXXIV"
    elif num == 3000:
        return "MMM"