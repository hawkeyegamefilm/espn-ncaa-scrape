# pulled pbp data from API, Miami OH, USC, Penn St
from carry_lib import bucket_carry_counts

# automated data pull from STATS DB, data is clean for Miami, Penn St, & USC, all others wonky & mislabeled
russell_carries = [0,2,16,4,1,6,0,3,13,9,4,6,8,4,6,-1,4,1,7,2,0,1,7,6,9,9,3,3,1,-4,-1,9,1,5,5,0,8,10,15,6,8,3,-2,3,4,7,-1,21,2,0,20,-5,4,5,15,-1,2,16,3,1,7,2,6,6,2,4,0,5,8,1,3,1,4,0,2,2]
lewis_carries = [2,29,12,2,6,3,10,6,1]

# Scraping old PBP
russell_akron_carries = [7,44,6,11,35,19,-2,1,11,3,11,2,2,20]
lewis_akron_carries = [7,5,13,33,2,10,1,15,0,0,0,2,1,-1,0,1,7,23,4]

russell_isu_carries = [4,12,2,6,11,2,-4,11,16,-5,5,9,14,1,15,6,46]
lewis_isu_carries = [10,3,-1,1,6]

russell_utah_st_carries = []
lewis_utah_st_carries = [5,12,-3,3,3,75,2,11,1]

russell_purdue_carries = [9,6,4,9,8,1,-1,14,9,7,4,-1,-3,3,17,10,3,3,11,-5,-2,3]
lewis_purdue_carries = []

russell_mich_st_carries = [3,5,5,2,5,0,6,13,3,9,-1,7,-4,3,1,7,9,2]
lewis_mich_st_carries = [2,2]

russell_ind_carries = [4,4,4,21,2,2,2,5,9,3,-3,8,9,3,0,10,13,1,3]
lewis_ind_carries = [9,4,7,14,9]

russell_mich_carries = [-2,-3,0,7,4,0,-2,3,0,2,-5,2,-3,7,13,-1,4,-1,1,2]
lewis_mich_carries = [4,10,0,24,5,28,-1,9,-2,7,-2,10,-1,0,12,0,3,3]

russell_wisc_carries = []
lewis_wisc_carries = [1,7,0,7,-2,4,3,13,3,4,2,0,2,3,-2,0,6,5,0,7,5,4,1,8,0]

russell_nw_carries = [0,-5,0,4,5,7,6,3,2,1,14,19,13,3,4,3,21]
lewis_nw_carries = [8,7,0,3,2,6,4,2,1,17,-3,3]

russell_minn_carries = [12,13,10,4,5,13,-2,53,4,0,16,20,14,7,3,17,5]
lewis_minn_carries = [6,6,3,9,2,2,1,21,4,7,15,-2,0,5,-8,1,6,9,14]


final_russell = russell_carries + russell_akron_carries + russell_isu_carries + russell_utah_st_carries + russell_purdue_carries + russell_mich_st_carries + russell_ind_carries + russell_mich_carries + russell_wisc_carries + russell_nw_carries + russell_minn_carries
final_lewis = lewis_carries + lewis_akron_carries + lewis_isu_carries + lewis_utah_st_carries + lewis_purdue_carries + lewis_mich_st_carries + lewis_ind_carries + lewis_mich_carries + lewis_wisc_carries + lewis_nw_carries + lewis_minn_carries


lewis_sorted_carries = bucket_carry_counts(final_lewis)
russell_sorted_carries = bucket_carry_counts(final_russell)

print(lewis_sorted_carries)
print(russell_sorted_carries)