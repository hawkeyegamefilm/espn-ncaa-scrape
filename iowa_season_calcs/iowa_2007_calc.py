from carry_lib import bucket_carry_counts

young_2007_carries = [1, 1, 12, 0, 7, 6, 7, 5, 12, 5, 6, 12, 11, 3, 6, 7, 11, 3, 4, 6, 17, -1, 1, 5, 2, -1, 6, 2, 3, 7, -1, 1, 1, 0, -4, 3, 5, 9, 1, 4, 5, 5, 7, 9, 0, 4, 7, 4, 4, 6, 2, 4, 1, 6, -2, 5, 1, 6, 6, 9, 3, 4, 21, 3, 3, 11, 1, 9, 2, 13, 2, 1, 6, 5, 0, 3, 2, 9, 0, 1, 3, 5, 4, 0, 5, 7, 6, 5, 4, 4, 7, 4, 7, 13, -1, 1, 0, 3, 1, 4, 9, 4, 3, 6, 2, 5, 2, -1, 2, 7, 2, 2, -1, 0, 26, 5, 10, 2, 5, 7, 6, 9, 4, 0, 4, 1, 1, 0, 4, 26, 5, 6, 5, 15, 3, 29, 2, 3, 2, 7, 0, 1, 4, 4, -3, 7, 5, 0, 1, 5, 5, 6, 0, 1, 2, 6, 2, 8, 4, 1, -1, 2, 16, 3, 6, 2, 2, 5, 4, 1, 3, 22, 5, 4, 1, 2, 7, 2, 1, 6, 3, 7, -1, 12, 4, 2, 3, 4, 0, 7, 0, 0, -1, 7, 4, 9, 10, 5, 4, 14, 3, 8, 3, 24, 0, -2]
sims_2007_carries = [5, 23, -1, 3, 15, -2, 17, 3, 12, 1, 18, 0, 1, 3, 9, 3, 8, 4, 0, 5, 1, 5, 0, 1, 12, 12, 15, -1, 2, 8, 0, 9, 0, 0, 17, 5, -5, 5, 2, 2, -2, -1, 2, 0, 22, 3, 3, 1, 17, -2, 12, 4, 2, 4, 0, 0, 1, 1, 7, 2, -3, 7, 4, 8, 2, 0, 5, 3, 10, 3, 0, 7, 7, 4, 6, 0, 5, 10, 8, -11, 3, 2, 30, 3, 2, 11, 2, 2, 2, 8, 18, 22, -1, 3, 1, 4, 11, 3, 4, 1]

young_sorted_carries = bucket_carry_counts(young_2007_carries)
sims_sorted_carries = bucket_carry_counts(sims_2007_carries)

print(young_sorted_carries)
print(sims_sorted_carries)