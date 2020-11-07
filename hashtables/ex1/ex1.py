def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    for i in range(length):
        cache[weights[i]] = i

    for index, weight in enumerate(weights):
        w = limit - weight

        if w in cache:
            i = cache[w]
            return (index, i) if index > i else (i, index)
