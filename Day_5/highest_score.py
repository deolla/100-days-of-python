# # Input a list of student scores
# student_scores = input().split()

# for i in range(0, len(student_scores)):
#     student_scores[i] = int(student_scores[i])


# total = 0
# max_score = student_scores[0]

# # checks for the highest score in a list.
# for i in student_scores:
#     # check if i is greater than max_score
#     if i > max_score:
#         # save it in a variable 
#         max_score = i

# total += max_score
# print(total)

student_scores = [78, 65, 89, 86, 91, 64, 89]

total = 0

min_score = student_scores[0]

# checks for the lowest score in a list.
for m in student_scores:
    # check if m is less that the max score
    if m < min_score:
        min_score = m
# Add the lowest score to the total.
total += min_score
print(total)
