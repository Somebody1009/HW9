from utils import factorial, is_power_of_5

if __name__ == "__main__":
    number = 5
    result = factorial(number)
    print(f"Factorial of {number} is {result}")
    
    # Test power of 5
    test_number = 125  # 5^3
    is_power = is_power_of_5(test_number)
    print(f"Is {test_number} a power of 5? {is_power}") 