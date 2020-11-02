def distance(str1, str2):
    if str1 == "" and str2 == "":
        return 0
    elif len(str1) > len(str2):
        raise ValueError("Strands' length must be equal!")
    else:
        result = 0
        for x in range(len(str1)):
            if str1[x] != str2[x]:
                result += 1
        return result
