# Running the solutions for each problem


from problem_1 import problem_1
from problem_2 import problem_2
from problem_3 import problem_3
from problem_4 import problem_4
from problem_5 import problem_5


functions = [problem_1(), problem_2(), problem_3(), problem_4(), problem_5()]

if __name__ == '__main__':
    for index, func in enumerate(functions):
        print(f'Problem {index+1}: \n',
              func, '\n', '-'*80)
