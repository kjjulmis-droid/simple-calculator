# ============================================================
# Project: Simple Calculator
# Description: A console-based calculator that can add,
#              subtract, multiply, and divide two numbers.
# ============================================================

# --- Calculator Class ---
# A class is a way to organize code. Think of it like a blueprint.
class Calculator:

      def __init__(self):
                # This list keeps track of all past calculations
                self.history = []

      def add(self, a, b):
                return a + b

      def subtract(self, a, b):
                return a - b

      def multiply(self, a, b):
                return a * b

      def divide(self, a, b):
                # We check for division by zero to avoid a crash
                if b == 0:
                              return "Error: You cannot divide by zero!"
                          return a / b

      def calculate(self, a, operator, b):
                # A dictionary maps each symbol to the right function
                operations = {
                              '+': self.add,
                              '-': self.subtract,
                              '*': self.multiply,
                              '/': self.divide
                }

          # Check if the operator typed is valid
                if operator not in operations:
                              return "Error: Please use +, -, *, or /"

                # Run the correct math function and get the result
                result = operations[operator](a, b)

          # Save the calculation to history (as a string)
                self.history.append(f"{a} {operator} {b} = {result}")

          return result

    def show_history(self):
              # Show all past calculations
              if len(self.history) == 0:
                            print("No calculations done yet.")
else:
            print("\n--- Your Calculation History ---")
              for entry in self.history:
                                print(entry)
                            print("--------------------------------")


# --- Main Program ---
# This is where the program starts running

def main():
      print("========================================")
    print("       Welcome to Simple Calculator     ")
    print("====
