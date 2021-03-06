from distance import euclidean_distance

if __name__ == '__main__':
    pairs_of_points = [((0,0), (0,1)),
                       ((0,0), (1.5,0)),
                       ((0,3), (4,0)),
                       ((0,0), (1,1)),
                       ((-1,0), (1,1)),
                       ((0,0), (1,3))
                       ]
    distances = []

    print 'The distances are:'
    for pair in pairs_of_points:
        distances.append(euclidean_distance(pair[0], pair[1]))
    print distances

    print 'The distances in ascending order are:'
    distances.sort()
    print distances

    print 'The miminal distance in the list is:'
    print distances[0]

    print 'The two largest distances in the list are:'
    print distances[-2], distances[-1]

    print 'The distances whose round value is even are:'
    print filter(lambda distance: distance % 2 == 0, [round(distance) for distance in distances])