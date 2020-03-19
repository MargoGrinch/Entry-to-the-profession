from PyInquirer import prompt
from uuid import uuid1
from pprint import pprint
from datetime import date
import actions
import utils

# Список для хранения продуктов
products = []

def get_action_index():
	# Используем библиотеку PyInquirer для обеспечения удобного CLI
	# Больше информации: https://github.com/CITGuru/PyInquirer#documentation
    answers = prompt([
        {
            'type': 'list',
            'message': 'Select action',
            'name': 'action_index',
            'choices': [
                {
                    'name': '🏬 Gel all products',
                    'value': 0
                },
                {
                    'name': '🔎 Get product by ID',
                    'value': 1
                },
                {
                    'name': '🔄 Update product',
                    'value': 2
                },
                {
                    'name': '🗑️  Remove product',
                    'value': 3
                },
                {
                    'name': '➕ Add new product',
                    'value': 4
                },
                {
                    'name': '❌ Quit',
                    'value': 5
                }
            ]
        }
    ])

	# Вернуть поле `action_index`
    return answers.get('action_index')

def switch_action(action_index):
    # Получение всех элеменов
    if action_index == 0:
        pprint(actions.get_all_products(products))

    # Получение элемента по ID
    if action_index == 1:
		# Попытатся найти элемент
        result = actions.get_product_by_id(utils.input_product_id(), products)

        if result is not None:
            pprint(result)
        else:
            print('Unable to find product')

    # Обновление продукта
    elif action_index == 2:
		# Ввести ID продукта
        product_id = utils.input_product_id()
		# Ввести данные для обновления
        product_data = utils.input_product_data()
		# Попытатся обновить продукт
        result = actions.update_product_by_id(product_id, products, product_data)

        if result is not None:
            pprint(result)
        else:
            print("Unable to update product")

	# Удалиение продукта
    elif action_index == 3:
		# Ввести ID продукта
        product_id = utils.input_product_id()
		# Попытатся удалить продукт
        result = actions.remove_product_by_id(product_id, products)

        if result is not None:
            pprint(result)
        else:
            print("Unable to remove product")

	# Создать новый продукт
    elif action_index == 4:
		# Ввести данные для продукта
        product_data = utils.input_product_data()
		# Сконструировать новый продукт
        new_product = {
            'id': uuid1(), # сгенерировать ID
            **product_data,
            'created_at': date.today().strftime("%d/%m/%Y") # получить текущую дату и форматировать
        }

		# Добавить новый продукт в список
        product = actions.add_product(new_product, products)

        pprint(product)

	# Повторить если был выбран вариант из меню
    if action_index in range(5):
        switch_action(get_action_index())

# Инициализировать приложение
if __name__ == '__main__':
	switch_action(get_action_index())
