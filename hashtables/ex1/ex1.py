#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    """
    YOUR CODE HERE
    """
    # weights is a list of ints
    # length is useless
    # limit is the value we are trying to sum and equal to.
    # we are storing the weights then searching through the weights to find the sum

    # insert each value in the weights list
    for i in range(len(weights)):
        # Note: these functions are not methods, the table must be passed in
        # key will be the weight, value will be the index in the weights list
        hash_table_insert(ht, weights[i], i)
    
    # iterate through each value
    for pair in ht.storage:
        # check if index is None
        pair = pair
        if pair:
            hash_table_remove(ht, pair.key)
        # if there is more than one value in the index
            if  pair.next: 
                # check first value
                temp_next = pair
                # check if there is a solution with the first value
                compliment = hash_table_retrieve(ht, limit - pair.key)

                #TODO check if values match to see if repeating values

                # if it exists
                if compliment:
                    # if the iterated value is greater
                    if compliment < pair.value:
                        # return a tuple with the first value in the 0th position
                        return (pair.value, compliment)
                    else:
                        # otherwise return it with the iterated valuein the first index
                        return (compliment, pair.value)
                # if the first is no good we iterate through the rest of the linked list
                while temp_next.next:
                    # move to the next value
                    temp_next = temp_next.next
                    # get this ahead of time to avoid calling twice
                    compliment = hash_table_retrieve(ht, limit - temp_next.key)
                    # same logic as above
                    if compliment:
                        if compliment < temp_next.value:
                            return (temp_next.value, compliment)
                        else:
                            return (compliment, temp_next.value)
            # if it is just one value
            else:
                # same logic as above
                compliment = hash_table_retrieve(ht, limit - pair.key)
                if compliment:
                    if compliment < pair.value:
                        return (pair.value, compliment)
                    else:
                        return (compliment, pair.value)
        # search for if a value limit - iterable exists
        # if no continue
        # if yes add values to a tuple, with the larger of the two coming first
    # if no pairs are found return none
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")



# weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
# answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
# weights_2 = [4, 4]
# answer_2 = get_indices_of_item_weights(weights_2, 2, 8)

# print(answer_2)
# print(answer_4)


'''
I would like to point out that the [4, 4] is an extreme edge case where you are putting the same key into a hash table
and it should be overwritten, but the test expects that both be input. 
This is either a flaw with the tips in README.md or with the implementation of the hash-table
'''