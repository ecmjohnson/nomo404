import math

def recursive_merging(sizes, bin_size):
    import pdb; pdb.set_trace()
    if len(sizes) == 1:
        return sizes
    else:
        arr1 = sizes[:len(sizes)/2]; arr2 = sizes[len(sizes)/2:];
        return merge_func(recursive_merging(arr1, bin_size), recursive_merging(arr2, bin_size), bin_size)

def merge_func(arr1, arr2, bin_size):
    len1 = len(arr1); len2 = len(arr2);
    if len1 == len2 == 1: # trivial merge logic
        ER_curr1 = math.fabs(arr1[0] - bin_size)
        ER_curr2 = math.fabs(arr2[0] - bin_size)
        ER_comb = math.fabs(arr1[0] + arr2[0] - bin_size)
        if ER_comb <= ER_curr1 and ER_comb <= ER_curr2:
            return [arr1, arr2]
    else:
        # we want to combine only the last elem of arr1 and first elem of arr2
        ER_curr1 = sum(arr1[-1]) - bin_size; ER_curr2 = sum(arr2[0]) - bin_size;
        # we only need to consider re-allocating the inside elements of arrs
        # three cases:
        #  1. arr1[-1][-1] -> arr2
        #  2. arr2[0][-1] -> arr1
        #  3. arr1[-1][-1], arr2[0][-1] -> new_arr
        cs_1_1 = ER_curr1 - arr1[-1][-1]; cs_1_2 = ER_curr2 + arr1[-1][-1];
        if cs_1_1 <= ER_curr1 and cs_1_2 <= ER_curr2:
            arr2[0].append(arr1[-1][-1])
            del arr1[-1][-1]
            if len(arr1[-1]) == 0:
                return [arr2]
            else:
                return [arr1, arr2]
        cs_2_1 = ER_curr1 + arr2[0][-1]; cs_2_2 = ER_curr2 - arr2[0][-1];
        if cs_2_1 <= ER_curr1 and cs_2_2 <= ER_curr2:
            arr1[-1].append(arr2[0][-1])
            del arr2[0][-1]
            if len(arr2[0]) == 0:
                return [arr1]
            else:
                return [arr1, arr2]
        cs_3_1 = ER_curr1 - arr1[-1][-1]; cs_3_2 = ER_curr2 - arr2[0][-1];
        cs_3_3 = math.fabs(arr1[-1][-1] + arr2[0][-1] - bin_size)
        if cs_3_1 <= ER_curr1 and cs_3_2 <= ER_curr2 and cs_3_3 <= ER_curr1 and cs_3_3 <= ER_curr2:
            if len(arr1[-1]) == 0 and len(arr2[0]) == 0:
                return [arr1[-1][-1], arr2[0][-1]]
            elif len(arr1[-1]) == 0:
                del arr2[0][-1]
                return [[arr1[-1][-1], arr2[0][-1]], arr2]
            elif len(arr2[0]) == 0:
                del arr1[-1][-1]
                return [arr1, [arr1[-1][-1], arr2[0][-1]]]
            else:
                return [arr1, [arr1[-1][-1], arr2[0][-1]], arr2]


while True:
    # get the definitions for the next test case
    try:
        temp = input("")
        posts_per_page = int(temp.split(" ")[0])
        num_posts = int(temp.split(" ")[1])
    except EOFError:
        break

    # get the test case data
    threads = []
    for i in range(1, num_posts+1):
        link = int(input(""))
        if i == 1: # this is the first post, must be 0
            threads.append([i])
        else:
            if link == 0: # this is the first post in a new thread
                threads.append([i])
            else: # this post links to a previous thread
                for thread in threads:
                    if link in thread:
                        threads[threads.index(thread)].append(i)

    # sum reduce the threads array
    post_sums = list(map(len, threads))
    import ipdb; ipdb.set_trace()

    assignment = recursive_merging(post_sums, posts_per_page)

    print(assignment)

    # accum = 0; badness = [];
    # for post_sum in post_sums:
    #     if accum > posts_per_page:
    #         badness.append(math.fabs(accum - posts_per_page)); accum = 0;
    #     elif post_sum > posts_per_page:
    #         badness.append(post_sum - posts_per_page)
    #     elif post_sum + accum > posts_per_page:
    #         badness.append(math.fabs(accum - posts_per_page)); accum = post_sum;
    #     else:
    #         accum += post_sum

    # print(max(badness))
