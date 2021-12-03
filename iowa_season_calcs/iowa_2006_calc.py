from carry_lib import bucket_carry_counts

#manually add 7y for young, missing carry in ILL data
#manually move 0 to 3 for young, mislabeled carry for no gain was 3y in OSU


young_2006_carries = [1, 3, 6, 11, 3, 3, 3, 6, 3, 4, 7, 5, 5, 6, 8, 3, 3, 7, 5, 4, -3, 8, 26, 1, -1, 4, 3, -1, 3, -1, -5, 3, 1, -3, 1, 2, 21, 7, 2, 1, 1, -3, 4, 4, 2, 1, 0, 1, 4, 21, 9, 5, -2, 6, 5, 2, 3, 2, 5, 6, 4, 1, 6, 2, 0, 6, 1, 3, 4, 3, 2, 2, 2, 9, 4, 4, 5, 2, 1, 1, 2, 1, 5, 1, -1, 3, 3, 4, 6, 6, 6, 8, 6, -1, 11, 7, 5, 3, -1, -1, 15, 6, 3, 1, 5, 0, 0, 2, -2, 3, 5, 1, 0, 2, 3, 11, 6, 6, 2, 19, 7, 8, -3, -1, 4, 3, 4, 5, 2, 2, 6, -1, 4, 11, 3, 3, 6, 3, 8, 5, 2, 3, 5, 6, 3, 1, 1, 3, 7, 11, 6, 3, 3, -3, 8, 1, 8, 1, 7, 4, 3, 15, 3, 8, -1, 9, 0, 3, 9, 5, 4, 7, 6, 8, 6, 0, 1, 9, 5, 3, 8, 3, 13, 6, 5, 7, 8, 3, 0, 0,7]
sims_2006_carries = [2, 3, 3, 21, 2, 5, 2, 2, 0, 1, 5, 3, 6, 2, 0, -3, -2, 3, 10, 5, 4, 15, 4, 0, 2, 17, 4, -1, 1, 5, 0, 3, 11, 5, 5, 3, 1, 3, 3, 5, 2, -1, 4, 2, 2, 7, 12, 2, 21, 0, 12, 0, 5, 3, 2, 1, 35, 1, 1, 2, 1, 4, 44, 11, 12, 8, 7, 1, 5, 2, -1, 2, 9, 8, 3, 1, 3, 1, 1, 12, 6, -3, 3, 2, -1, 3, 1, 41, 6, -2, 2, 4, 3, 1, -3, 7, -1, 1, 2, 12, 1, 1, -2, 11, 5, 3, 1, 7, 3, 9, 2, 4, 4, 7, 10, 1, 3, 3, 3, 11, 2, 2, 6, 28, 2, 1, 6, 15, 5, 3, 3, 3]

young_sorted_carries = bucket_carry_counts(young_2006_carries)
sims_sorted_carries = bucket_carry_counts(sims_2006_carries)

print(young_sorted_carries)
print(sims_sorted_carries)