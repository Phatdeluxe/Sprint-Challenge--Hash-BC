#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    # route = [None] * length
    route = []

    """
    YOUR CODE HERE
    """

    '''
    One thing I do not like about this is that they provide a list to populate, but they make it 1 too large.
    It seems like a waste of memory for me to use it at all over using a nice python list.
    Very silly.
    '''


    # add the tickets to the hash table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # find the ticket with source == none
    # location = 0
    # add first tickets destination to route
    ticket = hash_table_retrieve(hashtable, 'NONE')
    # route[location] = ticket
    route.append(ticket)
    # location += 1
    # find ticket with source == first tickets destination
    while True:
        ticket = hash_table_retrieve(hashtable, ticket)
        if ticket == 'NONE' or ticket == None:
            break
        # route[location] = ticket
        route.append(ticket)
        # location += 1
    # repeat until destination == None
    return route
