# # 1. Գրել ֆունկցիա որը կվերդարձնի ստացած արգումենտներից թվերի գումարը։

# def sum_nums(*nums):
#     count = 0
#     for el in nums:
#         count += el
#     return count


# print(sum_nums(10,12,14,50))

# # 2. Գրել ֆունկցիա որը կվերդարձնի ստացած արգումենտներից տողերի քանակը։

# def strings_count(*args):
#     count = 0
#     for el in args:
#         if type(el) == str:
#             count += 1
#     return count


# print(strings_count('hello',5,False,40,'beautiful','world'))

# # 3. Գրել ֆունկցիա որը կվերադարձնի ստասած արգումենտների միջին թվաբանականը։

# def arithmetic_average(*nums):
#     count = 0
#     res = 0
#     for el in nums:
#         count += el
#         res += 1
#     return count/res


# print(arithmetic_average(10,20,40,10))

# # 4. Գրել ֆունկցիա որը կստանա արգումենտ և կվերադարձնի այդ արգումենտերի հետ կատարած մաթեմատիկական գործողությունների արդյունքները։

# def math(a, b):
#     return a + b, a - b, a * b, a / b


# print(math(20, 6))

# # 5. Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի այն  դարձված ամբողջությամբ մեծատառ  (upper ֆունկցիան օգտագործել չի կարելի ։)

# def upper_str(string):
#     tmp = ''
#     for el in string:
#         if 97 <= ord(el) <= 122:
#             tmp += chr(ord(el) - 32)
#         else:
#             tmp += el
#     return tmp    


# mstr = input('Enter a sentence: ')
# print(upper_str(mstr))

# # 6. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և կվերադարձնի այն դարձված ամբողջությամբ փոքրատառ (lower ֆունկցիան օգտագործել չի կարելի ։)

# def lower_str(string):
#     tmp = ''
#     for el in string:
#         if 65 <= ord(el) <= 90:
#             tmp += chr(ord(el) + 32)
#         else:
#             tmp += el
#     return tmp    


# mstr = input('Enter a sentence: ')
# print(lower_str(mstr))

# 7. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և կվերադարձնի այն դարձված բոլոր բառերի առաջին տառերը մեծատառ (title ֆունկցիան օգտագործել չի կարելի ։)

# def my_upper_string(string):
#     mstr = string.split()
#     mstr2 = ''
#     for el in mstr:
#         mstr2 += el[0].upper() + el[1:] + ' '
#     return mstr2 

# print(my_upper_string("hello good world"))

# 8. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և կվերադարձնի այն դարձված հակառակ։

# def reverse_str(string):
#     return string[::-1]

# mstr = input('Enter a sentence: ')
# print(reverse_str(mstr))

# 9. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և թիվ։ Այն պետք է վերադարձնի տրված թվերի արանքում եղած ենթատողը։

# def mid_string(string, num1, num2):
#     if num1 > num2:
#         if len(string) < num1:
#             return 'Index out of range'
#         else:
#             return string[num2:num1]
#     elif num2 > num1:
#         if len(string) < num2:
#             return 'Index out of range'
#         else:
#             return string[num1:num2]


# print(mid_string('Hello good and beautiful world', 5, 12))

# 10. Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաերկար բառը։

# def longest_word(string):
#     ml = string.split()
#     max = ''
#     for el in ml:
#         if len(el) > len(max):
#             max = el
#     return max


# mstr = input('Enter a sentence: ')
# print(longest_word(mstr))

# 11. Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաշատ օգտագործված տառը։

# def return_letter(string):
#     md = {}
#     mstr = string.lower()
#     for el in mstr:
#         if el in md:
#             md[el] += 1
#         else:
#             md[el] = 1
#     if not md:
#         return 'String is empty'
#     max = 0
#     for k, v in md.items():
#         if v > max:
#             max = v
#             letter = k
#     return letter


# print(return_letter('hello good and beautiful world'))

# 12. Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաերկար բառում ամենաշատ օգտագործված տառը։

# def max_letter(string):
#     ml = string.split()
#     max_word = ''
#     for el in ml:
#         if len(el) > len(max_word):
#             max_word = el
#     md = {}
#     for el in max_word:
#         if el in md:
#             md[el] += 1
#         else:
#             md[el] = 1
#     print(md)
#     count = 0
#     max_letter = ''
#     for k, v in md.items():
#         if v > count:
#             count = v
#             max_letter = k
#     return max_letter


# mstr = input('Enter a sentence: ')
# print(max_letter(mstr))

# 13. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և թիվ։ Կվերադարձնի այդ թվին համապատասխն ինդեքսում եղած էլէմենտները՝ սկզբից և վերջից։

# num = int(input('Enter a number: '))
# mstr = input('Enter a sentence: ')

# def el_index(str,index):
#     if not str:
#         return 'String is empty'
#     if index == 0:
#         return str[0]
#     if index > len(str):
#         return 'Index out of range'
#     else:
#         return str[index],str[-index]


# print(el_index(mstr, num))

# 14. Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կստուգի պոլինդրոմ է այն թե ոչ։

# def is_polindrome(num):
#     tmp = str(num)
#     flag = True
#     for i in range(1, (len(tmp) // 2) + 1):
#         if tmp[i - 1] != tmp[-i]:
#             flag = False
#     if flag:
#         return 'The number is polindrome'
#     elif not flag:
#         return 'The number is not polindrome'

# print(is_polindrome(616))

# 15. Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կվերադարձնի իրեն ամենամոտ պոլինդրոմ թիվը։

# def nearest_palindrome(number):
#     def is_palindrome(n):
#         return str(n) == str(n)[::-1]

#     if is_palindrome(number):
#         return number

#     nearest_lower = number - 1
#     nearest_upper = number + 1

#     while True:
#         if is_palindrome(nearest_lower):
#             return nearest_lower
#         elif is_palindrome(nearest_upper):
#             return nearest_upper
#         nearest_lower -= 1
#         nearest_upper += 1

# print(nearest_palindrome(652))

# 16. Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կվերադարձնի իր առաջին և վերջին թվանշանների արտադրյալը։

# def multiply(num):
#     if -9 <= num <= 9:
#         return num
#     tmp = str(num)
#     return int(tmp[0]) * int(tmp[-1])


# print(multiply(642))

#  17. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում եղած տողերի քանակությունը։

# def return_str(list):
#     count = 0
#     for el in list:
#         if type(el) == str:
#             count += 1
#     return count


# my_list = ['hi','beautiful','20','world','15']
# print(return_str(my_list))

#  18. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում առկա թվերից առավելագույնը։

# def max_num(nums):
#     max = nums[0]
#     for el in nums:
#         if el > max:
#             max = el
#     return max


# ml = [50,20,0,-24,54,]
# print(max_num(ml))

#  19. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի այդ լիստում առկա երկնիշ զույգ թվերը։

# def is_even(nums):
#     ml1 = []
#     for el in nums:
#         if 10 <= el <= 99 and el % 2 == 0:
#             ml1.append(el)
#     return ml1


# ml = [24,40,20,5,7,1,25]
# print(is_even(ml))

#  20. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի այդ լիստում առկա թվերի միջին թվաբանականը։

# def arithmetic_average(list):
#     res = 0
#     count = 0
#     for el in list:
#         if type(el) == int:
#             res += el
#             count += 1
#     return res/count


# ml = [50,12,52,True,'hi',100,12,25]
# print(arithmetic_average(ml))

#  21. Գրել ֆունկցիա որը որպես արգումենտ կստանա տողերի լիստ և կվերադարձնի այդ տողերի երկարությունները պարունակող լիստ։

# def len_words(list):
#     ml = []
#     for el in list:
#         ml.append(len(el))
#     return ml


# ml1 = ['hello','good','and','beautiful','world']
# print(len_words(ml1))

#  22. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում առկա թվերը դասավորված նվազման կարգով։

# def sorted_nums(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums) - 1 - i):
#             if nums[j] < nums[j + 1]:
#                 nums[j],nums[j + 1] = nums[j + 1],nums[j]
#     return nums

# ml = [5,12,54,25,98]
# print(sorted_nums(ml))

# 23. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում առկա տողերը դասավորված երկարությունների նվազման կարգով։

# def sorted_words(words):
#     for i in range(len(words)):
#         for j in range(len(words) - 1 - i):
#             if len(words[j]) < len(words[j + 1]):
#                 words[j],words[j + 1] = words[j + 1],words[j]
#     return words

# ml = ['hello','my','world','door','school','average']
# print(sorted_words(ml))

#  24. Գրել ֆունկցիա որը որպես արգումենտ կնդունի տողերի լիստ և կվերադարձնի այն բառը որը կպարունակի ամենաշատ ձայնավորները։

# def vowels_word(list):
#     vowels = 'aeiou'
#     md = {}
#     for el in list:
#         count = 0
#         for i in el:
#             if i in vowels:
#                 count += 1
#         md[el] = count
#     count = 0
#     max = ''
#     for k, v in md.items():
#         if v > count:
#             count = v
#             max = k
#     return max


# print(vowels_word(['hello','good','and','beautiful','world']))

#  25. Գրել ֆունկցիա որը որպես արգումենտ կընդունի նախադասությունների լիստ և կվերադարձնի այն նախադասությունը որը կպարունակի ամենաշատ բառերը։

# def longest_sentence(list):
#     max = list[0]
#     for el in list:
#         for i in range(len(list)):
#             if len(el) > len(max):
#                 max = el
#     return max
            

# ml = ['good world','hi','beautiful world']
# print(longest_sentence(ml))

# 26. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող (իրականում նախադասություն և կվերադարձնի այդ նախադասությունում առկա ամենամեծ թիվը ոչ թե թվանշանը ։

# def max_number(str):
#     ml = []
#     for el in str:
#         if el.isdigit():
#             ml.append(int(el))
#     return max(ml)


# print(max_number('hello 4510 45 good  beautiful 545 world 10'))

#  27. Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝ մարդկանց նկարագրող և կվերադարձնի այն բառարանը որում մարդու տարիքն ամենամեծն է։

# def oldest_man(people):
#     max = 0
#     man = ''
#     for el in people:
#         if el['age'] > max:
#             max = el['age']
#             man = el['name']
#     return man, max


# print(oldest_man([{'name': 'john','age': 20},{'name': 'daniel','age': 45},{'name': 'David','age': 10}]))

# 28. Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝ ուսանողների նկարագրող և կվերադարձնի այդ ուսանողների լիստը դասավորված աճման կարգով՝ ըստ միավորների։
### (Դիմել եմ Chat GPT - ին չեմ հասկացել, ու սխալ է լուծել)
# def sort_students(students):
#     for i in range(len(students)):
#         for j in range(i + 1, len(students)):
#             if students[i]['միավորներ'] > students[j]['միավորներ']:
#                 students[i], students[j] = students[j], students[i]

#     return students

# students = [
#     {'անուն': 'Ալիսա', 'միավորներ': 85},
#     {'անուն': 'Բենջամին', 'միավորներ': 92},
#     {'անուն': 'Գարեգին', 'միավորներ': 78},
#     {'անուն': 'Դավիթ', 'միավորներ': 95}
# ]

# print(sort_students(students))


#  29. Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝ համալսարաններին նկարագրող և կվերադարձնի այն համալսարանը, որի անվանումն ամենաերկարն է։

# def max_univer(universities):
#     count = 0
#     univer = ''
#     for el in universities:
#             if len(el['name']) > count:
#                 count = len(el['name'])
#                 univer = el['name']
#     return univer


# print(max_univer([{'name': 'National Polytechnic University of Armenia','est': 1933},
#                 {'name': 'University of Cambridge','est': 1209},
#                 {'name': 'University of Oxford','est': 1096},
# ]))

