# Produces a sorted list of weighted ratings from a dictionary of
# user ratings and a user id.
# You can choose the function of similarity between users.
def weightedRating(dict_user, dict_group, user, similarity):
    # In the first place a dictionary is generated with the similarities
    # of our user with all other users.
    # This dictionary could be stored to avoid recomputing it.
    simils = {x: similarity(dict_user[user], dict_group[x])
              for x in dict_group if x != user}

    # Auxiliary dictionaries {movieId: [rating*users similarity]}
    # and {movieId: [users similarity]} (numerator and denominator
    # of the weighted rating)
    numerator   = {}
    denominator = {}

    # The ratings dictionary is traversed, while filling the auxiliary
    # dictionaries with the values found.
    for userId in simils:
        s = simils[userId]
        for movieId in dict_group[userId]:
            if not dict_user[user].has_key(movieId):
                if not numerator.has_key(movieId):
                    numerator  [movieId] = []
                    denominator[movieId] = []
                numerator[movieId].append(dict_group[userId][movieId]*s)
                denominator[movieId].append(s)
        
    # Compute and sort weighted ratings    
    result = []
    for movieId in numerator:
        s1 = sum(numerator[movieId])
        s2 = sum(denominator[movieId])
        if s2 == 0:
            mean = 0.0
        else:
            mean = (s1/s2)
        result.append((movieId,mean))

    result.sort(key = lambda x: x[1], reverse=True)
    return {result[i][0]: 5-i for i in range(len(result))}
