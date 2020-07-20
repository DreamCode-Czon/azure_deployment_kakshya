str = "Season"

new_str = str.replace('Season', 'programmer')
center_str = str.center(25, '*')
substring_str = str.count('a')
swaped_case = str.swapcase()
split_str = str.split('-')

website = ' wwww.socialmediawebsite.com '
stripped = website.lstrip(' w.')
print(stripped)

lst = ['season', 1, 2, 3, 'programmer']
lst[1:4] = [6, 6, 6]
lst.append('appended')
# print(lst)
#
# # print(3 in lst)
# for x in lst:
#     print(x)

lst_1 = [2, 8, 9, 10]
lst_2 = [2, 7, 8, 9]

print(cmp(lst_1, lst_2))
