# Инициализация данных
products = [
    {"name": "Акварельные краски", "category": "Рисование", "price": 500, "description": "Набор из 12 цветов"},
    {"name": "Мольберт", "category": "Рисование", "price": 1500, "description": "Деревянный мольберт для художников"},
    {"name": "Гитара", "category": "Музыка", "price": 7000, "description": "Акустическая гитара для начинающих"},
    {"name": "Набор для вышивания", "category": "Рукоделие", "price": 800, "description": "Набор для вышивания крестиком"},
    {"name": "Синтезатор", "category": "Музыка", "price": 12000, "description": "Электронный синтезатор с 61 клавишей"},
]

categories = {"Рисование", "Музыка", "Рукоделие"}
history = []

recommendations = {
    "Рисование": [
        {"name": "Бумага для акварели", "price": 300, "description": "Плотная бумага для акварели"},
        {"name": "Набор кистей", "price": 400, "description": "Набор из 5 кистей разных размеров"},
        {"name": "Палитра для красок", "price": 200, "description": "Пластиковая палитра для смешивания красок"},
    ],
    "Музыка": [
        {"name": "Камертон", "price": 150, "description": "Металлический камертон для настройки инструментов"},
        {"name": "Чехол для гитары", "price": 1000, "description": "Чехол для акустической гитары"},
        {"name": "Метроном", "price": 500, "description": "Электронный метроном для тренировки ритма"},
    ],
    "Рукоделие": [
        {"name": "Набор ниток", "price": 250, "description": "Набор ниток для вышивания"},
        {"name": "Пяльцы", "price": 300, "description": "Деревянные пяльцы для вышивания"},
        {"name": "Ножницы для ткани", "price": 400, "description": "Острые ножницы для работы с тканью"},
    ],
}

# Функция для отображения товаров по категории
def show_products_by_category(category):
    print(f"\nТовары в категории '{category}':")
    for product in products:
        if product["category"] == category:
            print(f"{product['name']} - {product['price']} руб. ({product['description']})")

# Функция для вывода рекомендаций
def show_recommendations(category):
    if category in recommendations:
        print(f"\nРекомендуемые товары для хобби '{category}':")
        for product in recommendations[category]:
            print(f"{product['name']} - {product['price']} руб. ({product['description']})")
    else:
        print("Рекомендации для этой категории отсутствуют.")

# Основной цикл программы
while True:
    print("\nМеню:")
    print("1. Просмотреть категории")
    print("2. Поиск товара")
    print("3. История запросов")
    print("4. Выход")
    choice = input("Выберите действие: ")

    if choice == "1":
        print("\nДоступные категории:")
        for category in categories:
            print(f"- {category}")
        selected_category = input("Введите название категории: ")
        if selected_category in categories:
            show_products_by_category(selected_category)
            ask_recommendations = input("Хотите получить рекомендации по товарам для этого хобби? (да/нет): ")
            if ask_recommendations.lower() == "да":
                show_recommendations(selected_category)
            history.append(f"Просмотр категории: {selected_category}")
        else:
            print("Категория не найдена.")
    elif choice == "2":
        search_query = input("Введите название товара: ")
        found_products = [product for product in products if search_query.lower() in product["name"].lower()]
        if found_products:
            print("\nРезультаты поиска:")
            for product in found_products:
                print(f"{product['name']} - {product['price']} руб. ({product['description']})")
            history.append(f"Поиск товара: {search_query}")
        else:
            print("Товары не найдены.")
    elif choice == "3":
        print("\nИстория запросов:")
        for entry in history:
            print(f"- {entry}")
    elif choice == "4":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")