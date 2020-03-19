from uuid import UUID
import utils


def get_all_products(products):
    return products


def get_product_by_id(product_id, products):
    try:
        # Отфильтровать список, чтобы остался лишь продукт с нужным ID
        result = list(filter(lambda product: product.get('id') == UUID(product_id), products))

        # Вернуть первый элемент списка, если его длина больше 0, иначе None
        return result[0] if len(result) > 0 else None
    except:
        # Вернуть None при ошибке
        return None


def update_product_by_id(product_id, products, data):
    # Попытатся найти продукт
    product = get_product_by_id(product_id, products)

    if product is not None:
        # Объединить два словаря
        updated_product = {**product, **data}

        # Обратится по индексу продукта и обновить элемент
        product_index = products.index(product)
        products[product_index] = updated_product

        return product

    # Вернуть None если произошла проблема при поиске продукта
    return None


def remove_product_by_id(product_id, products):
    # Попытатся найти продукт
    product = get_product_by_id(product_id, products)

    if product is not None:
        # Удалить продукт по индексу
        product_index = products.index(product)
        products.pop(product_index)

    # Вернуть список
    return products


def add_product(product, products):
    # Добавить новый продукт в конец списка
    products.append(product)
    product_index = products.index(product)

    # Вернуть продукт из списка по ID
    return products[product_index]
