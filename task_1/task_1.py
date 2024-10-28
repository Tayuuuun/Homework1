
def fix_user_input(variable_name):

    variable_name = ''.join('_' if not char.isalnum() else char for char in variable_name)

    new_name = []
    for char in variable_name:
        if char.isupper():
            if new_name:
                new_name.append('_')
            new_name.append(char.lower())
        else:
            new_name.append(char)

    variable_name = ''.join(new_name).strip()

    parts = variable_name.split('_')
    variable_name = '_'.join(part for part in parts if part)

    while variable_name and variable_name[0].isdigit():
        variable_name = variable_name[1:]

    if any(not (char.isalnum() or char == '_') for char in variable_name):
        print("Введено некорректное имя переменной")
        return None

    return variable_name


user_input = input("Введите имя переменной: ")
result = fix_user_input(user_input)
if result is not None:
    print(result)

