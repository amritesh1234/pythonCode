class Solution:
    def solve(self, s1, s2):
        if len(s1) > len(s2):
            return False
        dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        def getLcs(s1, s2):
            for i in range(1, len(s1)+1):
                for j in range(1, len(s2)+1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])
            return dp[len(s1)][len(s2)]
        lcs = getLcs(s1, s2)
        return lcs == len(s1)

s1 = "eenslqbknazecfysadnovvmkoofaqyfgvqluyfrsfyensxhbswfrpfsfblmuihcnpsbpjzscvgmpugadvjwptgbmkvoiobqmaisgyyuigtkqvaygffrehjctx"
s2 = "ekaoensryydlqbiuqknozxazevicfyhysetylefhadegnuovcbvjonrmkmoorfaqyfgolkvqkqsplnzuyfbrvvgsfkuybensxhcvoebswffpcrpdfmusstrdflmbbtlmnuihqcnpsqbpvcjxzkscvzgnmbpiugaovxpwidvjopwnptogfbcbmkvmoiobqmaaaisglzygfqbyjulynigagtkdkqlcqvalycbersjgfwfrmderhjpzqcnitx"
res = Solution().solve(s1, s2)
print(res)