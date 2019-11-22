from typing import List
import collections

# Amazon Echo has lots of competitors
# Web crawler got list of reviews
# Given list of reviews, list of competitors, N, return most frequently mentioned top N competitors in the reviews.


class Solution:
    def top_n_comp(
        self,
        numCompetitors: int,
        topNcompetitors: int,
        competitors: List[str],
        numReviews: int,
        reviews: List[str],
    ) -> List[str]:

        topcompetitors = set(competitors)

        for c in "\"',`.;?*&!":
            reviews = [line.replace(c, "").lstrip().lower() for line in reviews]

        freq = {}
        for word in topcompetitors:
            freq[word] = 0
        for line in reviews:
            used = []
            for word in line.split():
                if word in topcompetitors and word not in used:
                    freq[word] += 1
                    used.append(word)

        # print(freq)

        # count = collections.Counter(word for line in reviews for word in line.split())
        # print(count)
        sort = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        result = [item[0] for item in sort]
        # result = []
        # for index, item in enumerate(sort):
        #     if item[0] in topcompetitors:
        #         result.append(item[0])
        if topNcompetitors <= len(competitors):
            return result[:topNcompetitors]
        else:
            return result


sol = Solution()
result = sol.top_n_comp(
    6,
    2,
    ["newshop", "shopnow", "fashion", "fashionbeats", "random"],
    6,
    [
        "Newshop? is the newshop",
        "newshop' is newshop, newshop",
        "random. statement",
        "I fashion shopnow",
        " random is the best",
        " ,random ",
        "thanks random",
    ],
)
print(result)
