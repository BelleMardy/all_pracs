"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""

from prac_07.programming_language import ProgrammingLanguage
INTRO = """The dynamically typed languages are:"""

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)

my_list = [python, visual_basic, ruby]
print(INTRO)
for list in my_list:
    if list.is_dynamic() == True:
        print (list.name)












#     def __str__(self):
#         """Return string representation of a ProgrammingLanguage."""
#         return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)
#
# # class ProgrammingLanguage:
#     """Represent information about a programming language."""
#
#     def __init__(self, name, typing, reflection, year):
#         """Construct a ProgrammingLanguage from the given values."""
#         self.name = name
#         self.typing = typing
#         self.reflection = reflection
#         self.year = year
#
#     def __str__(self):
#         """Return string representation of a ProgrammingLanguage."""
#         return "{}, {} Typing, Reflection={}, First appeared in {}".format(
#             self.name, self.typing, self.reflection, self.year)
#
#     def is_dynamic(self):
#         """Determine if language is dynamically typed."""
#         return self.typing == "Dynamic"
#
# #
# # def run_tests():
# #     """Run simple tests/demos on ProgrammingLanguage class."""
# #     ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
# #     python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
# #     visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
# #
# #     languages = [ruby, python, visual_basic]
# #     print(python)
# #
# #     print("The dynamically typed languages are:")
# #     for language in languages:
# #         if language.is_dynamic():
# #             print(language.name)
