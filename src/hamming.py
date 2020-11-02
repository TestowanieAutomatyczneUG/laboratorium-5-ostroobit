def distance(str1, str2):
    if str1 == "" and str2 == "":
        return 0
    elif str1[0] == str2[0] and len(str1) == 1 and len(str2) == 1:
        return 0
    elif str1[0] != str2[0] and len(str1) == 1 and len(str2) == 1:
        return 1