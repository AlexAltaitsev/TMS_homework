from re import X


def list_of_pc(func):
    """Здесь я создал функцию где при помощи декоратора буду добавлять детали в ПК"""
    def wrapper():
        print("Parts list for building my PC: ")
        func()
        print("End of list with PC parts.")
    return wrapper
 
def peripherals_for_pc(func):
    """Здесь я создал функцию где при помощи декоратора буду добавлять переферию для ПК"""
    def wrapper():
        print("Parts list for my PC peripherals: ")
        func()
        print("End of list with PC peripherals.")
    return wrapper

@list_of_pc
def cpu_var(cpu="AMD Ryzen 5 1600", videocard= "Nvidia GTX 1050 Ti"):
    """Функциия в которую я добавляю детали для ПК"""
    print(cpu, videocard, sep = '\n')


@peripherals_for_pc      
def peripherals_var(mouse="Logitech G500S", keybord = 'SVEN 2400s'):
    """Функциия в которую я добавляю переферию для ПК"""
    print(mouse, keybord, sep = '\n')




def lambda_var(number = int(234)):
    """Здесь я сделал простой калькулятор для деления числа при помощи lambda"""
    var_lambda = (lambda x:x / 5 )(number)
    print(var_lambda)
    




if __name__ == '__main__':
    cpu_var()
    peripherals_var() 
    lambda_var()