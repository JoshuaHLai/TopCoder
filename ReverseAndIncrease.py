class ReverseAndIncrease():
    def isPossible(self, s, t):
        if s > 2147483647:
            return "Impossible"
        else:
            if s < t or s == t:
                return "Possible"
            else:
                if (s % 10) == 0:
                    return "Impossible"
                else:
                    ans = 0
                    while s != 0:
                        temp = s % 10
                        ans = ans * 10 + temp
                        s = s / 10
                    if ans < t:
                        return "Possible"
                    else:
                        return "Impossible"
