# Phone Number Validator

Write a function that will accept a string and return a formatted phone number string.

EX:
```bash
input: 123-123-1234
output: (123) 123-1234

input: [123]/12--31234
output: (123) 123-1234
```

The main function you write should be decorated with a function called `input_validator`.  `input_validator` should be a decorator whose purpose is to:
1. Check if the input could possibly produce correct output.  If it can't (ex: "12apple6"), then an exception should be raised.
2. If the input makes it through the first check, it should be normalized such that it only contains a string of 10 digits.


Bonus: Write another function that is also decorated with `input_validator`.  Instead of returning a formatted phone number, it extracts the area code, and returns the corresponding state.  You can try to read in the .json file, or simply copy it over and use it as a dictionary.
