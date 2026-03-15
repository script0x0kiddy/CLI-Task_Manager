# Beta v0.3

from time import sleep

print('=======Добро пожаловать========')

TASKS = []
start_menu = 0

def start():
	# Вывод меню Task Manager'a
	print('1. Вывести список задач')
	print('2. Добавить')
	print('3. Изменить')
	print('4. Удалить')
	print('5. Закрыть <Task Manager>')
	print('==========================')

def list_output(TASKS):
	print()
	print(f'Выбрано: Вывести список задач')

	if len(TASKS) == 0:
		print('--------------------')
		print('Список пуст')
		print('--------------------')
		print()
	else:
		print('--------------------')
		print('Список задач: ')

		for task in TASKS:
			print(f'--> {task}')

		print('--------------------')
		print()

def add_task(TASKS):
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
		TASKS.append(new_task_name.capitalize())
		print('Задача успешно добавлена!')
		print('Чтобы проверить нажмите <1>')
		sleep(1)
		print()

def change_task(TASKS):
	print()
	print(f"Выбрано: Изменить задачу")
	print()

	chg_task_num = str(input("Введите номер изменяемой задачи: "))
	task_isvalid = ''

	# Перебор списка задач с номером chg_task_num
	for i in range(0, len(TASKS)):
		# Если номер введённой задачи найден в списке задач
		if int(chg_task_num) - 1 == i:
			task_isvalid = TASKS[i]

	if task_isvalid == '':
		print()
		print("Нет такой задачи.")
		sleep(1)
		print()
	else:
		print(f"Выбрана: <{task_isvalid}>")
		print('--------------------')
		print("1. Отметить выполненой\n2. Изменить название")
		print('--------------------')

		chg_task = str(input("Выберите действие над задачей: "))

		if int(chg_task) == 1:
			if task_isvalid.endswith(" \u2705"):
				print("⚠️  Задача уже отмечена как выполненная.")
				sleep(1)
				print()
			else:
				TASKS[i] = task_isvalid + " \u2705"
				print(f'Задача <{task_isvalid}> отмечена выполненой \u2705')
				print()
				sleep(1)

		elif int(chg_task) == 2:
			task_isvalid = str(input("Введите новое название задачи: "))
			TASKS[i] = task_isvalid
			print(f'Название задачи изменено на: <{TASKS[i]}>')
			sleep(1)
			print()

def delete_task(TASKS):
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
			for i in range(0, len(TASKS)):
				# Если номер удаляемой задачи и номер существующей задачи совпал
				if int(del_task_num) - 1 == i:
					# Вытаскиваем из цикла удаляемую задачу
					del_task = i

			# Обработка удаляемой задачи
			if del_task == '':
				print()
				print('Нет такой задачи.')
				print()
			else:
				print(f'Будет удалена задача: {TASKS[del_task]}')
				delete = str(input('Удалить? (Y/N): ')).lower()

				if delete == 'y':
					print(f'Задача {TASKS[del_task]} удалена.')
					del TASKS[del_task]
					sleep(1)
					print()
				elif delete == 'n':
					print('Отмена удаления задачи.')

		elif int(del_select) == 2:
			if TASKS != []:
				print(f'Будут удалены следующие задачи: ')

				for task in TASKS:
					print(f"-> {task}")
					
				delete = str(input('Удалить? (Y/N): ')).lower()

				if delete == 'y':
					del TASKS[::]
					TASKS = []
					print(f'Список задач очищен.')
					sleep(1)
					print()

				elif delete == 'n':
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

while start_menu != 5:

	# Выести список
	if start_menu == 1:
		list_output(TASKS)

	# Добавить задачу
	elif start_menu == 2:
		add_task(TASKS)

	# Изменить
	elif start_menu == 3:
		change_task(TASKS)

	# Удалить задачу
	elif start_menu == 4:
		delete_task(TASKS)

	start()

	try:
		print()
		start_menu = int(input("Выберите действие: "))
	except ValueError:
		print('❌ Ошибка. Вы ввели не цифру.')
		start_menu = 0
		print()

print()
print('До скорой встречи.')
print()
