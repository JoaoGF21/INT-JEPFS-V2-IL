# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Functions Lab
# MAGIC 
# MAGIC Building on the previous lab, the FizzBuzz Test, we are going to refactor that code into a function.
# MAGIC 0. Declare a fucntion.
# MAGIC   0. The name of the function should be **`fizzBuzz`**
# MAGIC   0. The function has one parameter, presumably an integer (**`int`**).
# MAGIC   0. The function should return a string (**`str`**)
# MAGIC 0. Add a guard, or pre-condition, that asserts that the one specified parameter is of type **`int`**.
# MAGIC 0. Using your solution from the previous lab (one example solution is included below):
# MAGIC   0. Discard the for loop.
# MAGIC   0. Alter the print statements so that they return the corresponding value instead (e.g. return "Fizz" instead of printing "Fizz")
# MAGIC   0. Ensure that the return value is always a string (**`str`**).</br>
# MAGIC   Hint: See the built-in functions to convert numbers to string or employ an f-string.
# MAGIC 
# MAGIC Bonus: Update your function to use type hints.

# COMMAND ----------

# MAGIC %md To help you get started, we have included one possible solution to the Fizz Buzz Test here:

# COMMAND ----------

for num in range(1, 101):
    if (num % 5 == 0) and (num % 3 == 0):
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

# COMMAND ----------

# TODO
def fizz_buzz(number: int) -> str:
    """Function to return Fizz when the number
    is multiple of 3, Buzz when the number is multiple of 5,
    FizzBuzz when the number is multiple of 3 and 5. If the number
    is not multiple of 3 or 5, the function returns the number.

    Parameters
    ----------
    number : int
        Number to be checked.

    Returns
    -------
    str
        Return Fizz, Buzz, FizzBuzz or the number depending on conditions of number multiple.
    """
    assert type(number) == int, f"""Expected number as int, but found "{type(number)}"."""
    
    if (number % 5 == 0) and (number % 3 == 0):
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return str(number)

# COMMAND ----------

# MAGIC %md Use the code below to test your function.

# COMMAND ----------

expected = "Fizz"
result = fizz_buzz(3)
assert type(result) == str, f"Expected actual to be of type str, but found {type(result)}."
assert result == expected, f"""Expected "{expected}", but found "{result}"."""

expected = "Buzz"
result = fizz_buzz(5)
assert type(result) == str, f"Expected actual to be of type str, but found {type(actresultual)}."
assert result == expected, f"""Expected "{expected}", but found "{result}"."""

expected = "FizzBuzz"
result = fizz_buzz(15)
assert type(result) == str, f"Expected actual to be of type str, but found {type(result)}."
assert result == expected, f"""Expected "{expected}", but found "{result}"."""

expected = "7"
result = fizz_buzz(7)
assert type(result) == str, f"Expected actual to be of type str, but found {type(result)}."
assert result == expected, f"""Expected "{expected}", but found "{result}"."""

# COMMAND ----------

# MAGIC %md Using the asserts in the previous command as a template, create a test function that calls **`fizz_buzz()`** for the following sequence of numbers: 0, 1, 2, 3, 5, and 15
# MAGIC 0. Implement the method **`test_fizz_buzz()`**
# MAGIC 0. Iterate over the list **`test_numbers`** and **`expectations`**</br>
# MAGIC Hint: Without introducing any new constructs, you can employ a **`range`**
# MAGIC 0. Call **`fizz_buzz()`** with the specified value
# MAGIC 0. Assert that the result is of type **`str`**, as seen above
# MAGIC 0. Assert that the result matches the expected value, as seen above

# COMMAND ----------

#TODO
def test_fizz_buzz(number: int, expected: str):
    """Function to test function fizz_buzz.
    
    Parameters
    ----------
    number : int
        Number to be checked.
    expected : str
        Result expected from running function fizz_buzz
        with the number specified.
    
    Returns
    -------
        Prints if the test passed or raise an error in case of failure.
    """
    result = fizz_buzz(number)
    
    assert type(result) == str, \
        f"""The fizz_buzz output is expected as string, but it was found "{type(result)}"."""
    assert result == expected, \
        f"""Result expected is "{expected}", but the obtained is "{result}" """
    
    print("Test passed!")

test_numbers = [0, 1, 2, 3, 5, 15]
expectations = ["FizzBuzz", "1", "2", "Fizz", "Buzz", "FizzBuzz"]

for i in range(len(test_numbers)):
    num = test_numbers[i]
    expected = expectations[i]
    
    test_fizz_buzz(number=num, expected=expected)


# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>
