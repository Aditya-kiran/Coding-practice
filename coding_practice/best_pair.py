from typing import List


def best_pair(nums: List[int], target: int) -> List[int]:

    store = dict()
    best_pair = []

    for index, item in enumerate(nums):
        if item in store:
            # get pair, sort, check bigger, return
            if nums[index] > nums[store[item]]:
                pair = [store[item], index]
            else:
                pair = [index, store[item]]
            # print(pair)
            if best_pair:
                if nums[best_pair[1]] > nums[pair[1]]:
                    best_pair = best_pair
                else:
                    best_pair = pair
            else:
                best_pair = pair

        else:
            difference = target - 30 - item
            store[difference] = index
    return best_pair


print(best_pair([20, 50, 40, 25, 30, 10], 90))
