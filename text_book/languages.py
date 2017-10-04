from prac_07.programming_language import ProgrammingLanguage


def language_test():
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    cplusplus = ProgrammingLanguage("C++", "Static", True, 1983)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    languages = [java, cplusplus, python, visual_basic, ruby]
    print(python)
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

language_test()
