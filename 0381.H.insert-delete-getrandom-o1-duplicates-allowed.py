# 381. O(1) 时间插入、删除和获取随机元素 - 允许重复
# https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

import collections
import random


class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_list = []
        self.idx_dict = collections.defaultdict(list)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.val_list.append(val)
        self.idx_dict[val].append(len(self.val_list) - 1)
        return len(self.idx_dict[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.val_list:
            return False
        idx = self.idx_dict[val].pop(0)
        lst = self.val_list.pop(-1)
        self.val_list[idx] = lst
        self.idx_dict[lst][self.idx_dict[lst].index(len(self.val_list))] = idx
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.val_list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
    test = RandomizedCollection()
    # print(test.insert(0))
    print(test.insert(1))
    print(test.remove(1))
    print(test.insert(1))
    # print(test.remove(1))
    # print(test.getRandom())
