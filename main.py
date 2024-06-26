import redis


# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#
# class Cart:
#     def __init__(self, user):
#         self.user = user
#         self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
#         self.cart_key = f"cart:{self.user.username}"
#
#     def add_item(self, item, quantity):
#         self.redis_client.hset(self.cart_key, item, quantity)
#         print(f"Added {quantity} of {item} to the cart.")
#
#     def remove_item(self, item):
#         self.redis_client.hdel(self.cart_key, item)
#         print(f"Removed {item} from the cart.")
#
#     def update_item(self, item, quantity):
#         if self.redis_client.hexists(self.cart_key, item):
#             self.redis_client.hset(self.cart_key, item, quantity)
#             print(f"Updated {item} quantity to {quantity}.")
#         else:
#             print(f"{item} does not exist in the cart.")
#
#     def clear_cart(self):
#         self.redis_client.delete(self.cart_key)
#         print("Cart has been cleared.")
#
#     def search_item(self, item):
#         quantity = self.redis_client.hget(self.cart_key, item)
#         if quantity:
#             print(f"{item}: {quantity.decode('utf-8')}")
#         else:
#             print(f"{item} not found in the cart.")
#
#     def view_cart(self):
#         items = self.redis_client.hgetall(self.cart_key)
#         if items:
#             for item, quantity in items.items():
#                 print(f"{item.decode('utf-8')}: {quantity.decode('utf-8')}")
#         else:
#             print("Cart is empty.")
#
#
# def login(users_db):
#     username = input("Enter username: ")
#     print(f"Entered username: {username}")
#     password = input("Enter password: ")
#     print(f"Entered password: {password}")
#     if username in users_db and users_db[username] == password:
#         print("Login successful!")
#         return User(username, password)
#     else:
#         print("Invalid username or password.")
#         return None
#
#
# def main():
#     users_db = {
#         "Vlad": "12345",
#         "user2": "password2",
#     }
#
#     user = None
#     while not user:
#         user = login(users_db)
#
#     cart = Cart(user)
#
#     while True:
#         print("\nMenu:")
#         print("1. Add item to cart")
#         print("2. Remove item from cart")
#         print("3. Update item quantity in cart")
#         print("4. Clear cart")
#         print("5. Search for item in cart")
#         print("6. View cart")
#         print("0. Exit")
#
#         choice = input("Choose an option: ")
#
#         if choice == '1':
#             item = input("Enter item name: ")
#             quantity = input("Enter item quantity: ")
#             cart.add_item(item, quantity)
#         elif choice == '2':
#             item = input("Enter item name: ")
#             cart.remove_item(item)
#         elif choice == '3':
#             item = input("Enter item name: ")
#             quantity = input("Enter item quantity: ")
#             cart.update_item(item, quantity)
#         elif choice == '4':
#             cart.clear_cart()
#         elif choice == '5':
#             item = input("Enter item name: ")
#             cart.search_item(item)
#         elif choice == '6':
#             cart.view_cart()
#         elif choice == '0':
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
#
# if __name__ == "__main__":
#     main()
# Завдання 2


# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#
# class RecordTable:
#     def __init__(self, user):
#         self.user = user
#         self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
#         self.table_key = "game_records"
#
#     def add_result(self, username, score):
#         self.redis_client.zadd(self.table_key, {username: score})
#         print(f"Added result for {username}: {score}")
#
#     def remove_result(self, username):
#         self.redis_client.zrem(self.table_key, username)
#         print(f"Removed result for {username}")
#
#     def update_result(self, username, score):
#         if self.redis_client.zscore(self.table_key, username) is not None:
#             self.redis_client.zadd(self.table_key, {username: score})
#             print(f"Updated result for {username}: {score}")
#         else:
#             print(f"Result for {username} does not exist")
#
#     def clear_table(self):
#         self.redis_client.delete(self.table_key)
#         print("Table has been cleared")
#
#     def search_result(self, username):
#         score = self.redis_client.zscore(self.table_key, username)
#         if score is not None:
#             print(f"{username}: {score}")
#         else:
#             print(f"{username} not found in the table")
#
#     def view_table(self):
#         results = self.redis_client.zrange(self.table_key, 0, -1, withscores=True)
#         if results:
#             for username, score in results:
#                 print(f"{username.decode('utf-8')}: {score}")
#         else:
#             print("Table is empty")
#
#     def view_top_ten(self):
#         results = self.redis_client.zrevrange(self.table_key, 0, 9, withscores=True)
#         if results:
#             for username, score in results:
#                 print(f"{username.decode('utf-8')}: {score}")
#         else:
#             print("No records found")
#
#
# def login(users_db):
#     username = input("Enter username: ")
#     print(f"Entered username: {username}")
#     password = input("Enter password: ")
#     print(f"Entered password: {password}")
#     if username in users_db and users_db[username] == password:
#         print("Login successful!")
#         return User(username, password)
#     else:
#         print("Invalid username or password.")
#         return None
#
# def main():
#     users_db = {
#         "vlad": "1234",
#         "user2": "password2",
#     }
#
#     user = None
#     while not user:
#         user = login(users_db)
#
#     record_table = RecordTable(user)
#
#     while True:
#         print("\nMenu:")
#         print("1. Add result to table")
#         print("2. Remove result from table")
#         print("3. Update result in table")
#         print("4. Clear table")
#         print("5. Search for result in table")
#         print("6. View table")
#         print("7. View top ten results")
#         print("0. Exit")
#
#         choice = input("Choose an option: ")
#
#         if choice == '1':
#             username = input("Enter username: ")
#             score = float(input("Enter score: "))
#             record_table.add_result(username, score)
#         elif choice == '2':
#             username = input("Enter username: ")
#             record_table.remove_result(username)
#         elif choice == '3':
#             username = input("Enter username: ")
#             score = float(input("Enter new score: "))
#             record_table.update_result(username, score)
#         elif choice == '4':
#             record_table.clear_table()
#         elif choice == '5':
#             username = input("Enter username: ")
#             record_table.search_result(username)
#         elif choice == '6':
#             record_table.view_table()
#         elif choice == '7':
#             record_table.view_top_ten()
#         elif choice == '0':
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
#
# if __name__ == "__main__":
#     main()
# Завдання 3

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class NewsFeed:
    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=0):
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True)
        self.news_key = "news_feed"
        self.current_user = None

    def login(self, users_db):
        username = input("Enter username: ")
        print(f"Entered username: {username}")
        password = input("Enter password: ")
        print(f"Entered password: {password}")
        if username in users_db and users_db[username] == password:
            print("Login successful!")
            self.current_user = User(username, password)
        else:
            print("Invalid username or password.")
            return None

    def add_news(self):
        if self.current_user:
            title = input("Введіть заголовок новини: ")
            content = input("Введіть зміст новини: ")
            self.redis_client.lpush(self.news_key, f"{title}: {content}")
            self.redis_client.ltrim(self.news_key, 0, 9)
        else:
            print("Please log in first.")

    def delete_news(self):
        if self.current_user:
            index = int(input("Введіть індекс новини для видалення: "))
            total_news = self.redis_client.llen(self.news_key)
            if 0 <= index < total_news:
                self.redis_client.lset(self.news_key, index, "__DELETE__")
                self.redis_client.lrem(self.news_key, 1, "__DELETE__")
            else:
                print("Invalid index.")
        else:
            print("Please log in first.")
    def edit_news(self):
        if self.current_user:
            index = int(input("Введіть індекс новини для зміни: "))
            total_news = self.redis_client.llen(self.news_key)
            if 0 <= index < total_news:
                new_title = input("Введіть новий заголовок: ")
                new_content = input("Введіть новий зміст: ")
                self.redis_client.lset(self.news_key, index, f"{new_title}: {new_content}")
            else:
                print("Invalid index.")
        else:
            print("Please log in first.")

    def clear_news_feed(self):
        if self.current_user:
            self.redis_client.delete(self.news_key)
        else:
            print("Please log in first.")

    def view_news_feed(self):
        if self.current_user:
            news_feed = self.redis_client.lrange(self.news_key, 0, -1)
            for idx, news in enumerate(news_feed):
                print(f"{idx}. {news}")
        else:
            print("Please log in first.")

    def view_latest_news(self):
        if self.current_user:
            latest_news = self.redis_client.lindex(self.news_key, 0)
            if latest_news:
                print(f"Найсвіжіша новина: {latest_news}")
            else:
                print("Немає новин.")
        else:
            print("Please log in first.")

    def print_menu(self):
        print("\nМеню:")
        print("1. Додати новину")
        print("2. Видалити новину")
        print("3. Змінити новину")
        print("4. Повне очищення стрічки новин")
        print("5. Перегляд стрічки новин")
        print("6. Відображення найсвіжішої новини")
        print("0. Вихід")

    def main(self):
        users_db = {
            "vlad": "1234",
            "user2": "password2",
        }

        self.login(users_db)

        while self.current_user:
            self.print_menu()
            choice = input("Виберіть опцію: ")

            if choice == '1':
                self.add_news()
            elif choice == '2':
                self.delete_news()
            elif choice == '3':
                self.edit_news()
            elif choice == '4':
                self.clear_news_feed()
            elif choice == '5':
                self.view_news_feed()
            elif choice == '6':
                self.view_latest_news()
            elif choice == '0':
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    news_feed_app = NewsFeed()
    news_feed_app.main()