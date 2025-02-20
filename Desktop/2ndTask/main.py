<<<<<<< Updated upstream
from utils import factorial
=======
from utils import factorial, is_power_of_5, is_power_of_2
>>>>>>> Stashed changes

if __name__ == "__main__":
    number = 5
    result = factorial(number)
<<<<<<< Updated upstream
    print(f"Factorial of {number} is {result}") 
=======
    print(f"Factorial of {number} is {result}")
    
    # Test power of 5
    test_number = 125  # 5^3
    is_power = is_power_of_5(test_number)
    print(f"Is {test_number} a power of 5? {is_power}")
    
    # Test power of 2
    test_number_2 = 16  # 2^4
    is_power_2 = is_power_of_2(test_number_2)
    print(f"Is {test_number_2} a power of 2? {is_power_2}") 
>>>>>>> Stashed changes
