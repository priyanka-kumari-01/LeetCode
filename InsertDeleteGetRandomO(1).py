import random

class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}  # Dictionary to store values as keys and indices as values
        self.values = []  # List to store the values in the set

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False

        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        index = self.val_to_index[val]
        last_value = self.values[-1]

        # Swap the value to be removed with the last value in the list
        self.values[index] = last_value
        self.val_to_index[last_value] = index

        # Remove the last element from the list and the dictionary
        self.values.pop()
        del self.val_to_index[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)

# Create an instance of the RandomizedSet class
randomSet = RandomizedSet()

# Example usage:
randomSet.insert(1)  # Inserts 1 into the set, returns True
randomSet.remove(2)  # Since 2 is not present, returns False
randomSet.insert(2)  # Inserts 2 into the set, returns True
randomSet.getRandom()  # Returns a random element from the set (either 1 or 2)
randomSet.remove(1)  # Removes 1 from the set, returns True
randomSet.insert(2)  # 2 is already present, so returns False
randomSet.getRandom()  # Returns 2, the only remaining element in the set