def euclidean_distance(point1, point2):
    import math
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
def find_closest_tuple(tuples_list, input_tuple):
    closest_tuple_low = None
    closest_tuple_high = None
    idx_low=None
    idx_high=None

    smallest_distance = float('inf')  # Initialize with a large number
    i=0
    for tup in tuples_list:
        distance = euclidean_distance(tup, input_tuple)
        if distance < smallest_distance and tup[0]<input_tuple[0] and tup[1]<input_tuple[1]:
            smallest_distance = distance
            closest_tuple_low = tup
            idx_low=i
        i=i+1

    smallest_distance = float('inf')  # Initialize with a large number
    i=0
    for tup in tuples_list:
        distance = euclidean_distance(tup, input_tuple)
        if distance < smallest_distance and tup[0]>input_tuple[0] and tup[1]>input_tuple[1]:
            smallest_distance = distance
            closest_tuple_high = tup
            idx_high=i
        i=i+1

    return closest_tuple_low, closest_tuple_high, idx_low, idx_high

def find_closest_tupleV1(tuples_list_real,tuples_list_autocad, input_tuple):
    closest_tuple_low = None
    closest_tuple_high = None
    idx_low=None
    idx_high=None

    smallest_distance = float('inf')  # Initialize with a large number
    i=0
    for tup in tuples_list_real:
        distance = euclidean_distance(tup, input_tuple)
        if distance < smallest_distance and tup[0]<input_tuple[0] and tup[1]<input_tuple[1]:
            smallest_distance = distance
            closest_tuple_low = tup
            idx_low=i
        i=i+1

    smallest_distance = float('inf')  # Initialize with a large number
    i=0
    for tup in tuples_list_real:
        distance = euclidean_distance(tup, input_tuple)
        if distance < smallest_distance and tup[0]>input_tuple[0] and tup[1]>input_tuple[1]:
            smallest_distance = distance
            closest_tuple_high = tup
            idx_high=i
        i=i+1

    ### interpolate X value from real to autocad
    target_value=input_tuple[0]
    a_prev = tuples_list_real[idx_low][0]
    a_next = tuples_list_real[idx_high][0]
    b_prev = tuples_list_autocad[idx_low][0]
    b_next = tuples_list_autocad[idx_high][0]
    # Perform linear interpolation
    interpolated_value = b_prev + ((target_value - a_prev) / (a_next - a_prev)) * (b_next - b_prev)
    x_interp=interpolated_value


    ### interpolate Y value from real to autocad
    target_value =input_tuple[1]
    a_prev = tuples_list_real[idx_low][1]
    a_next = tuples_list_real[idx_high][1]
    b_prev = tuples_list_autocad[idx_low][1]
    b_next = tuples_list_autocad[idx_high][1]
    # Perform linear interpolation
    interpolated_value = b_prev + ((target_value - a_prev) / (a_next - a_prev)) * (b_next - b_prev)
    y_interp=interpolated_value

    xy_tup=(x_interp,y_interp)


    return closest_tuple_low, closest_tuple_high, idx_low, idx_high,xy_tup

# Example usage
tuples_list_real = [(1, 1), (2, 1), (3, 1), (4, 1),(1,2), (2, 2), (3, 2), (4, 2),(1, 3), (2, 3), (3, 3), (4, 3),(1, 4), (2, 4), (3, 4), (4, 4)]
tuples_list_autocad= [(1.5, 1.5), (2.5, 1.5), (3.5, 1.5), (4.5, 1.5),(1.5,2.5), (2.5, 2.5), (3.5, 2.5), (4.5, 2.5),(1.5, 3.5), (2.5, 3.5), (3.5, 3.5), (4.5, 3.5),(1.5, 4.5), (2.5, 4.5), (3.5, 4.5), (4.5, 4.5)]
input_tuple = (2.35, 1.74)
closest_tuple_low,closest_tuple_high,idx_low,idx_high,xy_tup = find_closest_tupleV1(tuples_list_real,tuples_list_autocad, input_tuple)
print("The closest tuple Low to", input_tuple, "is", closest_tuple_low," idx=",idx_low)
print("The closest tuple High to", input_tuple, "is", closest_tuple_high," idx=",idx_high)
print("Interpolated autocad is ", xy_tup)

