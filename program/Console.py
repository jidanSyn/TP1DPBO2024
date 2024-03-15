import os
import sys
# helper to just clear the console
class Console:

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def clear_lines(num_lines):
        for _ in range(num_lines):
            sys.stdout.write("\033[F")  # Move cursor up one line
            sys.stdout.write("\033[K")  # Clear line