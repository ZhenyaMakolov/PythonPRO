from main import logger

def test_3():

    @logger
    def calculate_salary(x, y):
        if x > y:
            print('большее число', x)
        elif x < y:
            print('большее число', y)
        else:
            print('числа равны')


    result = calculate_salary(9,8)


if __name__ == '__main__':
    test_3()