class Solution:

    def encode(self, strs: List[str]) -> str:
        def asc(s):
            return str([ord(c) for c in s])
        if not strs:
            return "EMPTY"
        res = ""
        for i in range(len(strs)):
            res += asc(strs[i]) + "-"
        return res[:-1]
    def decode(self, s: str) -> List[str]:
        if s == "EMPTY":
            return []
        def nasc(s):
            res = []
            if s == "":
                return []
            for c in s.split(","):
                res.append(chr(int(c.strip())))
            return res

        res = []
        for w in s.split("-"):
            w = w[1:-1]
            res.append("".join(nasc(w)))
        return res