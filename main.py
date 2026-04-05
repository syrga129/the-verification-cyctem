import json

class Verification:
    def __init__(self, name, klass, country, old):
        self.name = name
        self.klass = klass
        self.country = country
        self.old = old

    def get_info(self):
        return f"{self.name}, student {self.klass}, from {self.country}, {self.old}"

while True:
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        
        user_data = {}
        
        for field in config["fields"]["text"]:
            user_data[field] = input(f"Введите {field}: ")
            
        for field in config["fields"]["numeric"]:
            user_data[field] = int(input(f"Введите {field}: "))
        
        current_user = Verification(**user_data)
        
        rules = config["rules"]
        is_valid = (
            current_user.old > rules["min_age"] and 
            current_user.country == rules["required_country"]
        )
        
        if is_valid:
            print(f"\n[ДОСТУП РАЗРЕШЕН]\nДанные: {current_user.get_info()}")
        else:
            print(f"\n[ОТКАЗАНО] Вы не соответствуете правилам")

    except FileNotFoundError:
        print("Ошибка: Файл config.json не найден.")
        break
    except ValueError:
        print("Ошибка: Введены некорректные числовые данные.")
        continue
    except TypeError:
        print("Ошибка: Несовпадение аргументов класса и данных JSON.")
        break
    except KeyError as e:
        print(f"Ошибка: В JSON отсутствует ключ {e}")
        break
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        break

    cmd = input("\nВведите '1' для продолжения или '0' для выхода: ")
    if cmd == "0":
        break
