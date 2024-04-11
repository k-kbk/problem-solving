aeiou = ["a", "e", "i", "o", "u"]


while True:
    isAeiou = False
    isAcceptable = True
    mCnt = 0
    jCnt = 0

    password = input()

    if password == "end":
        break

    for s in aeiou:
        if s in password:
            isAeiou = True
            break

    if not isAeiou:
        print(f"<{password}> is not acceptable.")
        continue

    for i in range(len(password)):
        s = password[i]
        if s in aeiou:
            mCnt += 1
            jCnt = 0
        else:
            jCnt += 1
            mCnt = 0

        if mCnt >= 3 or jCnt >= 3:
            print(f"<{password}> is not acceptable.")
            isAcceptable = False
            break

        if i > 0 and password[i - 1] == s:
            if s != "e" and s != "o":
                print(f"<{password}> is not acceptable.")
                isAcceptable = False
                break

    if isAcceptable:
        print(f"<{password}> is acceptable.")
