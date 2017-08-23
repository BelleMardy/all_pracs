GRANTED = "Access granted"
DENIED = "Access denied"

user_names = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_name = input("What is your surname: >>> ").swapcase()
if user_name.swapcase() in user_names:
    print(GRANTED)
elif user_name.lower() in user_names:
    print(GRANTED)
elif user_name.upper() in user_names:
    print(GRANTED)
elif user_name in user_names:
    print(GRANTED)
else:
    print(DENIED)


