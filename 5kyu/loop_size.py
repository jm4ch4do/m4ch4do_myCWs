def loop_size(node):
    # initialize fast and slow pointers
    fast = node
    slow = node
    
    # fast moves two nodes and slow moves one node
    fast = fast.next.next
    slow = slow.next
    
    # keep moving until they meet (which indicates there is a loop)
    while slow != fast:
        fast = fast.next.next
        slow = slow.next
    
    # fast stays and slow keep moving until it get's back
    count = 1
    slow = slow.next
    while slow != fast:
        count += 1
        slow = slow.next
    
    # the number of times it had slow had to move it's the loop length
    return count
    
