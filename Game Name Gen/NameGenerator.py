from random import randint
nome0 = "Artur"
nome1 = "Bogo"
nome2 = "Santos"
pos0 = randint(0, 4)
pos1 = randint(0, 3)
pos2 = randint(0, 5)
print("{}{}{}".format(nome0[0:pos0], nome1[0:pos1], nome2[0:pos2]))