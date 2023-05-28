def summa(*sonlar):
    num = 0
    for son in sonlar:
        num += son
    return num


# print(summa(9, 1, 2, 3, 4, 5, ))


def summa(*sonlar):
    return sum(sonlar)


# print(summa(9, 1, 2, 3, 4, 5, 2))


def summa1(x, y, *sonlar):
    return x + y + sum(sonlar)


# print(summa(9, 1, 2, 3, 4, 5, 2))
# print(summa(9, 2))

def avto_info(kompaniya, model, **malumotlar):
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar


avto1 = avto_info('GM', 'nexia', rang='qora', narxi=2000)
print(avto1)
