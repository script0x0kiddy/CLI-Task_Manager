from time import sleep

print()
print('=======Добро пожаловать========')
print('1. Вывести список задач')
print('2. Добавить')
print('3. Изменить')
print('4. Удалить')
print('5. Закрыть <Task Manager>')
print('==========================')

tasks = []
select = 0

try:
	select = int(input("Выберите действие: "))
except ValueError:
	print('❌ Неверно. Вводите только цифры.')
	select = 0

while select != 5:

	# Выести список
	if select == 1:
		print()
		print(f'Выбрано: Вывести список задач')

		if len(tasks) == 0:
			print('--------------------')
			print('Список пуст')
			print('--------------------')
			print()
		else:
			print('--------------------')
			print('Список задач: ')

			for i in tasks:
				print(f'--> {i}')

			print('--------------------')
			print()

	# Добавить задачу
	elif select == 2:
		print()
		print(f'Выбрано: Добавить задачу')
		print()
		
		new_task_name = str(input('Введите название задачи: '))

		# Обработка имени новой задачи
		while new_task_name == '':
			print("❌ Заполните пустое поле!")
			new_task_name = str(input('Введите название задачи: '))
		else:
			# Добавление в список задач
			tasks.append(new_task_name.capitalize())
			print('Задача успешно добавлена!')
			print('Чтобы проверить нажмите <1>')
			sleep(1)
			print()

	# Изменить
	elif select == 3:
		print()
		print(f"Выбрано: Изменить задачу")
		print()

		chg_task_num = str(input("Введите номер изменяемой задачи: "))
		select_task = ''

		# Перебор списка задач с номером chg_task_num
		for i in range(0, len(tasks)):
			# Если номер введённой задачи найден в списке задач
			if int(chg_task_num) - 1 == i:
				select_task = tasks[i]

		if select_task == '':
			print()
			print("Нет такой задачи.")
			sleep(1)
			print()
		else:
			print(f"Выбрана: <{select_task}>")
			print('--------------------')
			print("1. Отметить выполненой\n2. Изменить название")
			print('--------------------')

			chg_task = str(input("Выберите действие над задачей: "))

			if int(chg_task) == 1:
				if tasks[i] != (select_task + " \u2705"):
					print("⚠️ Задача уже выполнена!")
					chg_task = str(input("Выберите действие над задачей: "))
				else:
					tasks[i] = select_task + " \u2705"
					print(f'Задача <{select_task}> отмечена выполненой')
					print()

			elif int(chg_task) == 2:
				select_task = str(input("Введите новое название задачи: "))
				tasks[i] = select_task
				print(f'Название задачи изменено на: <{tasks[i]}>')
				sleep(1)
				print()

	# Удалить задачу
	elif select == 4:
		print(f'Выбрано: Удалить задачу')
		print()
		print('--------------------')
		print("1. Удалить конкретную задачу\n2. Удалить все задачи")
		print('--------------------')

		del_select = str(input("Выберите действие: "))

		if del_select != '':
			if int(del_select) == 1:
				del_task_num = str(input("Введите номер удаляемой задачи: "))
				del_task = ''

				# Перебор списка задач с номером del_task
				for i in range(0, len(tasks)):
					# Если номер удаляемой задачи и номер существующей задачи совпал
					if int(del_task_num) - 1 == i:
						# Вытаскиваем из цикла удаляемую задачу
						del_task = tasks[i]

				# Обработка удаляемой задачи
				if del_task == '':
					print()
					print('Нет такой задачи.')
					print()
				else:
					print(f'Будет удалена задача: {del_task}')
					delete = str(input('Удалить? (Y/N): '))

					if delete == 'Y' or delete == 'y':
						tasks.remove(del_task)
						print(f'Задача {del_task} удалена.')
						sleep(1)
						print()
					elif delete == 'N' or delete == 'n':
						print('Отмена удаления задачи.')

			elif int(del_select) == 2:
				if tasks != []:
					print(f'Будут удалены следующие задачи: ')

					for task in tasks:
						print(f"--> {task}")
					
					delete = str(input('Удалить? (Y/N): '))

					if delete == 'Y' or delete == 'y':
						tasks = []
						print(f'Список задач очищен.')
						sleep(1)
						print()
					elif delete == 'N' or delete == 'n':
						print('Отмена очистки списка.')
					else:
						print("⚠️  Введите символ Y/y или N/n")
						print()
				else:
					print()
					print('ℹ️  Пустой список нельзя очистить.')
					sleep(1)
		else:
			while del_select == '':
				print("❌ Ошибка. Вы ввели не цифру.")
				del_select = str(input("Выберите действие: "))

	# Вывод меню Task Manager'a
	print('==========================')
	print('1. Вывести список задач')
	print('2. Добавить')
	print('3. Изменить')
	print('4. Удалить')
	print('5. Закрыть <Task Manager>')
	print('==========================')

	try:
		print()
		select = int(input("Выберите действие: "))
	except ValueError:
		print('❌ Ошибка. Вы ввели не цифру.')
		select = 0
		print()

print()
print('До скорой встречи.')
print()