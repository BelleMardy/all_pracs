"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""
R = "Reflection"
T = "Typing"
F = "First appeared in"

class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return "{}, {} {}, {} = {}, {} {}.".format(self.name, self.typing, T, R, F, self.reflection, self.year)

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


# def run_tests():
#         """Run simple tests/demos on ProgrammingLanguage class."""
#         java = ProgrammingLanguage("Java", "Static", True, 1995)
#         c_plus_plus = ProgrammingLanguage("C++", "Static", False, 1983)
#         python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
#         visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
#         ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
#
#
#         languages = [java, c_plus_plus, python, visual_basic, ruby]
#         print(languages)
#
#         print("The dynamically typed languages are:")
#         for language in languages:
#             if language.is_dynamic():
#                 print("Dynamic {}.".format(language.name))
#             else:
#                 print("Not dynamic {}.".format(language.name))
#
#
# if __name__ == "__main__":
#     run_tests()