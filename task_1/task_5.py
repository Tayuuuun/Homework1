

possible_subjects = {"меч", "лук", "топор", "щит", "зелье"}

common_subject = possible_subjects.copy()

def get_subjects_input():
    while True:
        subjects = input("Введите предметы, которые выбрал авантюрист: ").split()
        if all( subject in possible_subjects for subject in subjects):
            if 1 <= len(subjects) <= 3:
                return set(subjects)
            else:
                print("Каждый авантюрист должен выбрать минимум 1 и максимум 3 предмета.")
        else:
            print("Неверный предмет, попробуйте снова.")

for x in range(1, 4):
    print(f"Авантюрист {x}:")
    chosen_subjects = get_subjects_input()
    common_subject &= chosen_subjects

if common_subject:
    print(f"Предметы, включенные в общий набор: {', '.join(common_subject)}")
else:
    print("0")