person = ['Энакин Скайуокер',
		  41,
		  ['Татуин', 'Набу', 'Джеонозис', 'Корусант', 'Мустафар', 'Звезда Смерти'],
		  {'световой меч': 'синий', 'ранг': 'лорд ситхов'}
		  ]




def main():

	while True:
		task_number = input("Введите номер задания (1-10) или 'Выход' для выхода: ")

		if task_number.lower() == 'выход':
			print("Выход из программы.")
			break

		if task_number == '1':
			name_parts = person[0]
			print(f"Персона: {name_parts[1]}, {name_parts[0]}")
		elif task_number == '2':
			print(f"Возраст Энакина: {person[1]}")
		elif task_number == '3':
			places = ', '.join(person[2])
			print(f"Места: {places}")
		elif task_number == '4':
			print(f"Количество мест: {len(person[2])}")
		elif task_number == '5':
			serves_empire = 'Звезда Смерти' in person[2]
			print(serves_empire)
		elif task_number == '6':
			lightsaber_color = person[3]['световой меч']
			print(f"Цвет светового меча: {lightsaber_color}")
		elif task_number == '7':
			person[1] = 42
			print(f"Новый возраст Энакина: {person[1]}")
		elif task_number == '8':
			if 'Эндор' not in person[2]:
				person[2].append('Эндор')
			print(f"Обновленный список мест: {person[2]}")
		elif task_number == '9':
			rank = person[3]['ранг']
			if rank == 'лорд ситхов':
				print("Энакин - лорд ситхов")
			else:
				print("Энакин - джедай")
		elif task_number == '10':
			if len(person[2]) > 4:
				print("Энакин побывал во многих местах")
			else:
				print("Энакин не так много путешествовал")
		else:
			print("Некорректный номер задания. Пожалуйста, попробуйте снова.")

main()





