from time import sleep

print()
print('==========================')
print('1. Вывести список задач')
print('2. Добавить')
print('3. Изменить')
print('4. Удалить задачу')
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
		sleep(1)
		print()

		new_task_name = str(input('Введите название задачи: '))

		# Добавление в список задач
		tasks.append(new_task_name.capitalize())
		sleep(1)
		print('Задача успешно добавлена!')
		sleep(1)
		print('Чтобы проверить нажмите <1>')
		sleep(1)
		print()

	# Изменить
	elif select == 3:
		print()
		print(f"Выбрано: Изменить задачу")
		sleep(1)
		print()

		chg_task_num = int(input("Введите номер изменяемой задачи: "))
		select_task = ''

		# Перебор списка задач с номером chg_task_num
		for i in range(0, len(tasks)):
			# Если номер введённой задачи найден в списке задач
			if chg_task_num - 1 == i:
				select_task = tasks[i]

		if select_task == '':
			print()
			print("Нет такой задачи.")
			sleep(1)
			print()
		else:
			print(f"Выбрана: <{select_task}>")
			sleep(1)
			print('--------------------')
			print("1. Отметить выполненой\n2. Изменить название")
			print('--------------------')

			chg_task = int(input("Выберите действие над задачей: "))
			print()

			if chg_task == 1:
				tasks[i] = select_task
				print(f'Задача отмечена выполненой: {select_task}')
				sleep(1)
				print()
			elif chg_task == 2:
				select_task = str(input("Введите новое название задачи: "))
				tasks[i] = select_task
				print(f'Новое название: {tasks[i]}')

	# Удалить задачу
	elif select == 4:
		print()
		print(f'Выбрано: Удалить задачу')
		sleep(1)
		print()

		del_task_num = int(input("Введите номер удаляемой задачи: "))
		del_task = ''

		for i in range(0, len(tasks)):
			if del_task_num - 1 == i:
				del_task = tasks[i]

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
				print()
			elif delete == 'N' or delete == 'n':
				print('Отмена удаления задачи.')

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
