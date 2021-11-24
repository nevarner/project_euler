# Running the solutions for each problem


from problem_1 import problem_1


functions = [problem_1()]

if __name__ == '__main__':
    for index, func in enumerate(functions):
        print(f'Problem {index+1}: \n',
              func, '\n', '-'*80)
