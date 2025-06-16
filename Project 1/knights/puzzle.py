from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."

statement = And(AKnight, AKnave)

knowledge0 = And(
    # A is a Knight or a Knave
    Or(
        AKnight,
        AKnave
    ),
    # A can't be both
    Not(And(
        AKnight,
        AKnave
    )),
    # "A is only a Knight if (A is a Knight and A is a Knave) is true"
    Biconditional(AKnight, statement)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.

statement = And(AKnave, BKnave)

knowledge1 = And(
    # A is a Knight or a Knave
    Or(AKnight, AKnave),

    # A can't be both
    Not(And(AKnight, AKnave)),

    # B is a Knight or a Knave
    Or(BKnight, BKnave),

    # B can't be both
    Not(And(BKnight, BKnave)),

    # "A is only a Knight if (A is a Knave and B is a Knave) is true"
    Biconditional(AKnight, statement)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

statementA = Or(And(AKnight, BKnight), And(AKnave, BKnave))
statementB = Or(And(AKnight, BKnave), And(AKnave, BKnight))

knowledge2 = And(
    # A is a Knight or a Knave
    Or(AKnight, AKnave),

    # A can't be both
    Not(And(AKnight, AKnave)),

    # B is a Knight or a Knave
    Or(BKnight, BKnave),

    # B can't be both
    Not(And(BKnight, BKnave)),

    Biconditional(AKnight ,statementA),
    Biconditional(BKnight ,statementB)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

statementA = Or(AKnight, AKnave)
A_said_knave  = Biconditional(AKnight, AKnave) # A said 'I am a knave'
statementB1 = Biconditional(BKnight, A_said_knave)
statementB2 = CKnave
statementC = AKnight

knowledge3 = And(
    # A is a Knight or a Knave
    Or(AKnight, AKnave),

    # A can't be both
    Not(And(AKnight, AKnave)),

    # B is a Knight or a Knave
    Or(BKnight, BKnave),

    # B can't be both
    Not(And(BKnight, BKnave)),

    # C is a Knight or a Knave
    Or(CKnight, CKnave),

    # C can't be both
    Not(And(CKnight, CKnave)),

    # Person is only a Knight if their statements are true
    Biconditional(AKnight, statementA),
    Biconditional(BKnight, And(statementB1, statementB2)),
    Biconditional(CKnight, statementC)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
