"""
name = input("NAME: ")
age = int(input("AGE: "))
address = input("ADDRESS: ")
salary = float(input("SALARY: "))
expenses = float(input("EXPENSES: "))

remaining_salary = round((salary - expenses),1)
is_salary_good = remaining_salary >= 500

print(f"{name}, who is {age} years old, and lives in {address} has {remaining_salary} dollars left from her salary after expenses. It is {is_salary_good} that she has more than $500 left.")

"""

poem = """Some say the world will end in fire,
Some say in ice.
From what I’ve tasted of desire
I hold with those who favor fire.
But if it had to perish twice,
I think I know enough of hate
To say that for destruction ice
Is also great
And would suffice."""

string = "python is awesome!"
poem_no_dots = poem.replace(".", " ") 
poem_no_commas = poem_no_dots.replace(",", " ")
final_string = poem_no_commas.lower()+string
print(len(final_string))
poem_list = final_string.split()
print(poem_list)