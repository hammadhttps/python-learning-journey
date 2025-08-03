import random

operators=["+","-","*","/"]
min_operand=3
max_operand=12


def generate_problem(level):
    left=random.randint(min_operand,max_operand)
    right=random.randint(min_operand,max_operand)
    operator=random.choice(operators)

    match level:
        case "easy":
            right=random.randint(1,10)
            left=random.randint(1,10)
            operators_include=[random.choice(operator),random.choice(operator)]
            return f"{left} {operators_include[0]} {right} {operators_include[1]} {left}"

        case "medium":
            right=random.randint(11,20) 
            left=random.randint(11,20)
            operators_include=[random.choice(operator),random.choice(operator),random.choice(operator)]
            return f"{left} {operators_include[0]} {right} {operators_include[1]} {left} {operators_include[2]} {right}"
        case "hard":
            right=random.randint(21,30)
            left=random.randint(21,30)
            operators_include=[random.choice(operator),random.choice(operator),random.choice(operator),random.choice(operator)]
            return f"{left} {operators_include[0]} {right} {operators_include[1]} {left} {operators_include[2]} {right} {operators_include[3]} {left}"
        case _:
            raise ValueError("Invalid level")

def solve_problem(problem):
    try:
        result=eval(problem)
        return result
    except:
        return "Invalid problem"


level=input("Enter the level of the game: ")
problem=generate_problem(level)

while True:
  user_answer=input(f"Solve the problem: {problem} = ")
  result=int(solve_problem(problem))

  if int(user_answer)==result:
    print("Correct!")
    break
  else:
    print(f"Incorrect! The correct answer is {result}")
    print("Try again!")
  problem=generate_problem(level)


