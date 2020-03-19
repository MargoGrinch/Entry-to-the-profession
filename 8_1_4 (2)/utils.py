from PyInquirer import prompt

# Используем библиотеку PyInquirer для обеспечения удобного CLI
# Больше информации: https://github.com/CITGuru/PyInquirer#documentation

# Ввод ID продукта

def input_product_id():
    answer = prompt({
        'type': 'input',
        'message': 'Enter product ID',
        'name': 'product_id'
    })

    return answer.get('product_id')

# Ввод данных для продукта

def input_product_data():
    answers = prompt([
        {
            'type': 'input',
            'message': 'Enter product name',
            'name': 'name'
        },
        {
            'type': 'input',
            'message': 'Enter product size',
            'name': 'size'
        },
        {
            'type': 'input',
            'message': 'Enter product color',
            'name': 'color'
        }
    ])

    return answers
