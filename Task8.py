# Программа для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.
# ¬ - отрицание, ⋁- логическое или, ⋀ - логическое И

xe = [True, False]
ye = [True, False]
ze = [True, False]
for x in xe:
    for y in ye:
        for z in ze:
            print(x, y, z)
            result1 = not (x or y or z)
            result2 = not x and not y and not z
            print(result1 == result2)



#Программа для проверки утверждения (W ⋀ Z) V ¬Y V (¬X = ¬W)
for w in range(2):
    for z in range(2):
        for y in range(2):
            for x in range(2):
                if not(w and z or not y or (not x==(not w))):
                    print(w, z, y, x)
