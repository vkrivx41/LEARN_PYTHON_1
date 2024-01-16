
# Logical operators: are operators that are used to compare boolean values to state the Truth

# Let us say that this is a guy who is gonna be passed through different girls with different priorities

black_hair = False
blue_eyes = True
tall = False
big = True
light_skin = False

lisas_favorite = black_hair and tall
naomis_favorites = light_skin or big
sarahs_favorite = not blue_eyes
niks_favorite = not big and light_skin or black_hair
ellas_favorite = not tall and blue_eyes
bellas_favorite = not tall and big or light_skin  # True and True => True

print(lisas_favorite, naomis_favorites, sarahs_favorite, niks_favorite, ellas_favorite, bellas_favorite)


number_1 = 10
number_2 = 10.01
number_3 = 5
number_4 = 25

expression_1 = number_1 >= number_2 and number_3 < number_2
expression_2 = number_4 != number_2 or number_4 < number_2
expression_3 = not number_4 == number_3

print(expression_1, expression_2, expression_3)