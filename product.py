# pdt_name="Iphone"
# pdt_price=int(input("Enter Price : "))
# pdt_qty=3
# print("The total price of",pdt_name,"is",pdt_price*pdt_qty)

# list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# list2 = ["Piatti", "The Grill at Torrey Pines", "Shogun"]
# def find(list1, list2):
#     min_sum = (len(list1) - 1) + (len(list2) - 1)
#     list3 = []
#     for i in range(len(list1)):
#         for j in range(len(list2)):
#             if list1[i] == list2[j]:
#                 if i + j < min_sum:
#                     min_sum = i + j
#                     list3 = [list1[i]]
#                 elif i + j == min_sum:
#                     list3.append(list1[i])
#     return list3
# print(find(list1, list2))