# Running the solutions for each problem


from problem_1 import problem_1
from problem_2 import problem_2
from problem_3 import problem_3
from problem_4 import problem_4
from problem_5 import problem_5
from problem_6 import problem_6
from problem_7 import problem_7


functions = [problem_1(), problem_2(), problem_3(), problem_4(), problem_5(),
             problem_6(), problem_7()]

if __name__ == '__main__':
    for index, func in enumerate(functions):
        print(f'Problem {index+1}: \n',
              func, '\n', '-'*80)
