def solution(s):
    pairs = {")": "(", "]": "[", "}": "{"}

    if len(s) % 2:
        return 0

    def is_paired(s):
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            elif not stack or stack.pop() != pairs[c]:
                return False

        return not stack

    return sum(is_paired(s[i:] + s[:i]) for i in range(len(s)))
