def select_actyivity(activity_list):
    # activity_list[[activity,strat_time,finish_time]]

    # step 1: sort the arrays according to the finish time.
    activity_list.sort(key=lambda x: x[2])

    # step 2: select the first activity and print it.
    current_activity = activity_list[0]
    print(current_activity)

    # step 3: for all remaining actoivities :
    # if the start time of this acyivity is grater or equal to the finish time of previously
    # selected activity then select this activity and print it.

    for i in range(1, len(activity_list)):
        if activity_list[i][1] >= current_activity[2]:
            current_activity = activity_list[i]
            print(current_activity)

    # Time complexity o(n)+o(nlogn)= o(nlogn)


activities = [["A1", 0, 6], ["A2", 3, 4], ["A3", 1, 2],
              ["A4", 5, 8], ["A5", 5, 7], ["A6", 8, 9]]
select_actyivity(activities)
