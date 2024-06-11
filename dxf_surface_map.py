import math
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
def find_closest_tuple(tuples_list, input_tuple):
    closest_tuple_low = None
    closest_tuple_high = None
    smallest_distance = float('inf')  # Initialize with a large number

    for tup in tuples_list:
        distance = euclidean_distance(tup, input_tuple)
        if distance < smallest_distance and tup[0]<input_tuple[0] and tup[1]<input_tuple[1]:
            smallest_distance = distance
            closest_tuple_low = tup

    smallest_distance = float('inf')  # Initialize with a large number
    for tup in tuples_list:
        distance = euclidean_distance(tup, input_tuple)
        if distance < smallest_distance and tup[0]>input_tuple[0] and tup[1]>input_tuple[1]:
            smallest_distance = distance
            closest_tuple_high = tup

    return closest_tuple_low, closest_tuple_high


# Example usage
tuples_list = [(1, 1), (2, 1), (3, 1), (4, 1),(1,2), (2, 2), (3, 2), (4, 2),(1, 3), (2, 3), (3, 3), (4, 3),(1, 4), (2, 4), (3, 4), (4, 4)]
input_tuple = (3.1647, 3.547)
closest_tuple_low,closest_tuple_high = find_closest_tuple(tuples_list, input_tuple)
print("The closest tuple Low to", input_tuple, "is", closest_tuple_low)
print("The closest tuple High to", input_tuple, "is", closest_tuple_high)
