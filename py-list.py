#using lambda
squares = list(map(lambda x: x**2, range(10) ) )
print(squares)

simpleSquares = [x**2 for x in range(10)]
print(simpleSquares)
