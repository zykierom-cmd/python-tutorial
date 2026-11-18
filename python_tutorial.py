import os
import time

def clear_screen():
    # Clears the console screen for a clean UI experience
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    print("=" * 60)
    print("        PYTHON TUTORIAL: FROM ZERO TO CODING HERO")
    print("               LEARN  |  CODE  |  CONQUER")
    print("=" * 60)

def lesson_1():
    clear_screen()
    header()
    print("\n[ LESSON 1: INTRODUCTION TO PROGRAMMING ]\n")
    print("What is Programming?")
    print("- Programming is the process of giving instructions to a computer")
    print("  to perform specific tasks.")
    print("- Python is a popular, high-level, interpreted programming language")
    print("  known for its readability and beginner-friendly syntax.\n")
    print("Why Python?")
    print("1. Easy to read and write (looks like plain English).")
    print("2. Used in Web Development, Data Science, AI, and Automation.")
    print("3. Huge community support and libraries.\n")
    
    print("-" * 60)
    print("QUICK QUIZ:")
    ans = input("Is Python a high-level programming language? (yes/no): ").strip().lower()
    if ans == "yes":
        print("Correct! Python is a high-level, beginner-friendly language.")
    else:
        print("Incorrect. Python IS a high-level programming language!")
    input("\nPress ENTER to return to the main menu...")

def lesson_2():
    clear_screen()
    header()
    print("\n[ LESSON 2: PYTHON BASIC SYNTAX ]\n")
    print("1. Print Statement:")
    print("   Used to display output on the screen.")
    print("   Example: print('Hello, World!')\n")
    print("2. Comments:")
    print("   Used to explain code. Python ignores lines starting with '#'.")
    print("   Example: # This is a comment\n")
    print("3. Variables & Data Types:")
    print("   Variables store data values without needing explicit type declaration.")
    print("   - String (str): text -> name = 'Juan'")
    print("   - Integer (int): whole number -> age = 19")
    print("   - Float (float): decimal -> grade = 1.25")
    print("   - Boolean (bool): True or False -> is_student = True\n")

    print("-" * 60)
    print("QUICK QUIZ:")
    ans = input("What symbol is used to write a single-line comment in Python? : ").strip()
    if ans == "#":
        print("Correct! The '#' symbol starts a comment in Python.")
    else:
        print("Incorrect. The correct symbol is '#'.")
    input("\nPress ENTER to return to the main menu...")

def lesson_3():
    clear_screen()
    header()
    print("\n[ LESSON 3: ARITHMETIC OPERATORS AND EXPRESSIONS ]\n")
    print("Arithmetic operators are used with numeric values to perform math:\n")
    print("  Operator | Name           | Example  | Result")
    print("  ---------+----------------+----------+-------")
    print("     +     | Addition       | 10 + 5   |   15")
    print("     -     | Subtraction    | 10 - 5   |    5")
    print("     *     | Multiplication | 10 * 5   |   50")
    print("     /     | Division       | 10 / 5   |  2.0")
    print("     %     | Modulus        | 10 % 3   |    1 (Remainder)")
    print("     **    | Exponentiation | 2 ** 3   |    8 (2 raised to 3)")
    print("     //    | Floor Division | 10 // 3  |    3 (Whole number)\n")

    print("-" * 60)
    print("QUICK QUIZ:")
    ans = input("What is the output of 10 % 3 in Python? : ").strip()
    if ans == "1":
        print("Correct! 10 divided by 3 has a remainder of 1.")
    else:
        print("Incorrect. The remainder (modulus) of 10 % 3 is 1.")
    input("\nPress ENTER to return to the main menu...")

def lesson_4():
    clear_screen()
    header()
    print("\n[ LESSON 4: BASIC INPUT AND OUTPUT IN PYTHON ]\n")
    print("1. Output using print():")
    print("   Displays text or variables to the user.")
    print("   Example: print('Welcome to Python!')\n")
    print("2. Input using input():")
    print("   Allows the user to type data into the program.")
    print("   Note: input() ALWAYS returns a String (str).")
    print("   Example: user_name = input('Enter your name: ')\n")
    print("3. Type Casting (Converting Input):")
    print("   To do math with input, convert it using int() or float().")
    print("   Example: age = int(input('Enter your age: '))\n")

    print("-" * 60)
    print("INTERACTIVE TRY-IT:")
    sample_num = input("Enter any number to double it: ").strip()
    try:
        num = float(sample_num)
        # Format as int if it's a whole number, otherwise keep decimal
        if num.is_integer():
            num = int(num)
        print(f"Result: {num} * 2 = {num * 2}")
    except ValueError:
        print("That wasn't a valid number, but notice how input() captured your text!")
    input("\nPress ENTER to return to the main menu...")

def lesson_5():
    clear_screen()
    header()
    print("\n[ LESSON 5: CONDITIONAL STATEMENTS IN PYTHON ]\n")
    print("Conditional statements let your program make decisions using:")
    print("  - if   : runs code if the condition is True")
    print("  - elif : checks another condition if previous ones were False")
    print("  - else : runs code if all conditions are False\n")
    print("Example:")
    print("  grade = 85")
    print("  if grade >= 75:")
    print("      print('Passed!')")
    print("  else:")
    print("      print('Failed!')\n")

    print("-" * 60)
    print("QUICK QUIZ:")
    ans = input("Which keyword is short for 'else if' in Python? : ").strip().lower()
    if ans == "elif":
        print("Correct! 'elif' is used for multiple conditions in Python.")
    else:
        print("Incorrect. Python uses 'elif' instead of 'else if'.")
    input("\nPress ENTER to return to the main menu...")

def lesson_6():
    clear_screen()
    header()
    print("\n[ LESSON 6: LOGICAL OPERATORS ]\n")
    print("Logical operators are used to combine conditional statements:\n")
    print("  1. and : Returns True if BOTH statements are true.")
    print("           Example: (5 > 3 and 10 > 5) -> True\n")
    print("  2. or  : Returns True if AT LEAST ONE statement is true.")
    print("           Example: (5 > 3 or 10 < 5)  -> True\n")
    print("  3. not : Reverses the result (True becomes False).")
    print("           Example: not(5 > 3)           -> False\n")

    print("-" * 60)
    print("QUICK QUIZ:")
    ans = input("What does (True and False) evaluate to? (True/False): ").strip().capitalize()
    if ans == "False":
        print("Correct! Both sides must be True for 'and' to return True.")
    else:
        print("Incorrect. (True and False) evaluates to False.")
    input("\nPress ENTER to return to the main menu...")

def lesson_7():
    clear_screen()
    header()
    print("\n[ LESSON 7: INTRODUCTION TO ITERATION AND LOOPS ]\n")
    print("Loops are used to repeat a block of code multiple times.\n")
    print("1. while Loop:")
    print("   Repeats as long as a condition is True.")
    print("   Example:")
    print("     count = 1")
    print("     while count <= 3:")
    print("         print(count)")
    print("         count += 1\n")
    print("2. for Loop:")
    print("   Iterates over a sequence (like a list or range of numbers).")
    print("   Example:")
    print("     for i in range(3):")
    print("         print('Hello!')\n")

    print("-" * 60)
    print("QUICK QUIZ:")
    ans = input("How many times will 'for i in range(5):' repeat? : ").strip()
    if ans == "5":
        print("Correct! range(5) loops 5 times (0, 1, 2, 3, 4).")
    else:
        print("Incorrect. It repeats 5 times.")
    input("\nPress ENTER to return to the main menu...")

def main():
    clear_screen()
    header()
    print("\nYour gateway to Python mastery begins here!")
    input("\n[ PRESS ENTER TO BEGIN ]")

    clear_screen()
    header()
    print("\nWELCOME TO PYTHON TUTORIAL!")
    print("In this knowledge hub, you will learn the fundamentals of Python programming.")
    user_name = input("\nBefore we begin, please enter your name: ").strip()
    if not user_name:
        user_name = "Student"

    while True:
        clear_screen()
        header()
        print(f"\nGreat to have you, {user_name}! Let's get started.\n")
        print("==== PYTHON TUTORIAL ====")
        print("In this course, we will cover the following topics:")
        print("1. Introduction to Programming")
        print("2. Basic Syntax")
        print("3. Arithmetic Operators")
        print("4. Basic Input and Output in Python")
        print("5. Conditional Statements in Python")
        print("6. Logical Operators")
        print("7. Introduction to Iteration and Loops")
        print("8. Exit")
        print("-" * 60)

        choice = input("Choose a lesson (1-8): ").strip()

        if choice == "1":
            lesson_1()
        elif choice == "2":
            lesson_2()
        elif choice == "3":
            lesson_3()
        elif choice == "4":
            lesson_4()
        elif choice == "5":
            lesson_5()
        elif choice == "6":
            lesson_6()
        elif choice == "7":
            lesson_7()
        elif choice == "8":
            clear_screen()
            header()
            print(f"\nThank you for using Python Tutorial, {user_name}!")
            print("Good luck on your Final Exam Defense!\n")
            break
        else:
            print("\nInvalid choice! Please select a number from 1 to 8.")
            time.sleep(1.5)

if __name__ == "__main__":
    main()