def parse_fopc(expression):
    predicate = expression.split("(")[0]
    arguments = expression.split("(")[1].replace(")", "").split(",")
    arguments = [arg.strip() for arg in arguments]
    return predicate, arguments

expr = "Likes(John, Mary)"
pred, args = parse_fopc(expr)

print("Predicate:", pred)
print("Arguments:", args)