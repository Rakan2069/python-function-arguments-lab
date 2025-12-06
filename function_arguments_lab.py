# Python Function Arguments Laboratory Activity

# PART 1 & 2: Basic, Positional, and Keyword Arguments

def describe_pet(animal_type, pet_name):
    """
    Part 1 & 2: Prints a simple description of a pet using two arguments.
    """
    print(f"I have a {animal_type} and its name is {pet_name}.")

print("\n--- PART 1: Basic Function Arguments ---")
# Task: Call the function three times
describe_pet("hamster", "Hamtaro")
describe_pet("snake", "Slinky")
describe_pet("parrot", "Squawk")

print("\n--- PART 2: Positional vs Keyword Arguments ---")
# Task: Call using positional arguments
print("Positional Call:")
describe_pet("dog", "Buddy")

# Task: Call using keyword arguments (reverse order)
print("\nKeyword Call:")
describe_pet(pet_name="Milo", animal_type="cat")


# PART 3: Default Arguments


def describe_pet(pet_name, animal_type="dog"):
    """
    Part 3: Modified function with a default value for animal_type.
    This new definition overrides the previous one.
    """
    print(f"I have a {animal_type} and its name is {pet_name}.")

print("\n--- PART 3: Default Arguments ---")
# Task: Call describe_pet("Brownie") (uses default animal_type="dog")
print("Default Argument Call (animal_type=dog):")
describe_pet("Brownie")

# Task: Call describe_pet("Nugget", "chicken") (overrides default)
print("\nOverriding Default Call (animal_type=chicken):")
describe_pet("Nugget", "chicken")



# PART 4: Create Your Own Function 

def order_drink(drink, size="medium", iced=False):
    """
    Part 4: Creates a drink order using a required argument and two defaults.
    Returns a string describing the order.
    """
    ice_status = "iced " if iced else "hot "
    # Format the output string
    return f"Your order: {size} {ice_status}{drink.lower()}"

print("\n--- PART 4: Create Your Own Function ---")
# Task: Order a default drink (size="medium", iced=False)
print("Default Order:")
print(order_drink("Coffee"))

# Task: Order a large hot chocolate (no ice)
# Note: Using keyword arguments for clarity
print("\nExplicit Size Order (Hot Chocolate):")
print(order_drink("Chocolate", size="large", iced=False))

# Task: Order a small iced milk tea
print("\nAll Arguments Set (Iced Milk Tea):")
print(order_drink("Milk Tea", size="small", iced=True))



# PART 5: Mini Challenge (Calculator)


def compute(operation, num1, num2=1):
    """
    Part 5: Performs a calculation based on the operation string.
    num2 has a default value of 1.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "subtract":
        return num1 - num2
    else:
        return "Invalid operation"

print("\n--- PART 5: Mini Challenge (Calculator) ---")
# Task: compute("add", 5, 10) - Positional
print(f'compute("add", 5, 10): {compute("add", 5, 10)}')

# Task: compute("multiply", num1=3, num2=4) - Keyword
print(f'compute("multiply", num1=3, num2=4): {compute("multiply", num1=3, num2=4)}')

# Task: compute("subtract", 20) - Uses default num2=1
print(f'compute("subtract", 20): {compute("subtract", 20)} (20 - default 1)')

# Task: Try an invalid operation
print(f'compute("divide", 10, 2): {compute("divide", 10, 2)}')
print("-------------------------------------------------\n")