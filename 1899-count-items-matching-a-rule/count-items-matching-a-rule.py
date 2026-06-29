class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        result = 0
        for item in items:
            if ruleKey == "type":
                if item[0] == ruleValue:
                    result += 1
            elif ruleKey == "color":
                if item[1] == ruleValue:
                    result += 1
            elif ruleKey == "name":
                if item[2] == ruleValue:
                    result += 1

        return result