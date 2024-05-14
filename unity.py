def unify(st1, st2):
    w1=st1.split()
    w2=st2.split()
    substitution={}
    for w1w,w2w in zip(w1,w2):
        if w2w.isalpha() and w2w[0].isupper():
            substitution[w2w]=w1w
        elif w1w!=w2w:
            return None
    return substitution

statement1 = "Moksha and Vineela are sisters"
statement2 = "X and Y are sisters"

result = unify(statement1, statement2)

if result:
    print("The unification is successful. Substitution =", result)
else:
    print("Unification failed.")