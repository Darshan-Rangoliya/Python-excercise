from functools import reduce

class Number:
    def __init__(self,numbers):
        self.numbers = numbers

    def get(self):
        return self.numbers

    def change_original_value(self,func = lambda x:x):
        new_numbers = list(map(func,self.numbers))
        return new_numbers

    def filter_value(self,filter_func = lambda x:x):
        filtered_numbers = list(filter(filter_func,self.numbers))
        return filtered_numbers

    def compount_the_numbers(self,compound_func = lambda compond,d:compond+d):
        compound = reduce(compound_func,self.numbers)
        return compound

    def sort(self):
        return sorted(self.numbers)

if __name__ == '__main__':
    numbers = [2, 5, 1, 66, 22, 11, 10]

n1 = Number(numbers)

print('Numbers: ', n1.get())

print('New Values: ',n1.change_original_value(func=lambda x:x*2))

print('Filtered Values: ',n1.filter_value(filter_func=lambda x:x%2==0))

print('Compounded value: ',n1.compount_the_numbers(compound_func=lambda a,b:a+b))

print('Sorted list: ', n1.sort())
