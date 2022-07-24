def nb_year(p0, percent, aug, p):
    # your code
    population = p0
    years = 0
    while population < p:
        years += 1
        population = population + (population * percent/100) + aug
        print(population )
    return years


print(nb_year(1500000, 2.5, 10000, 2000000))
