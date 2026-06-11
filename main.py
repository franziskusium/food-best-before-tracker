import os


from datetime import datetime, timedelta
FILE_PATH = "foods.txt"
print("Current folder:", os.getcwd())
print("File path:", os.path.abspath(FILE_PATH))

print("File size:", os.path.getsize(FILE_PATH))

def load_foods_from_file(filepath):
    foods = []

    with open(filepath, "r") as file_reader:
        for line in file_reader:
            cleaned_line = line.strip()

            if cleaned_line != "":
                name, date_string = cleaned_line.split(",")

                expiry_date = datetime.strptime(
                    date_string,
                    "%Y-%m-%d"
                ).date()

                
                foods.append([name, expiry_date])

    return foods


def show_foods(foods, today):
    print("\nExpired foods:")

    found = False

    for food in foods:
        if food[1] < today:
            print(f"- {food[0]} ({food[1]})")
            found = True

    if not found:
        print("None")

    print("\nFoods expiring within 7 days:")

    found = False

    for food in foods:
        if today <= food[1] <= today + timedelta(days=7):
            print(f"- {food[0]} ({food[1]})")
            found = True

    if not found:
        print("None")


def add_food(foods, today):
    answer = input("\nDo you want to add food? (yes/no): ")

    while answer.lower() == "yes":
        name = input("Food name: ")

        while True:
            date_string = input(
                "Best-before date (YYYY-MM-DD): "
            )

            try:
                expiry_date = datetime.strptime(
                    date_string,
                    "%Y-%m-%d"
                ).date()
                break

            except ValueError:
                print(
                    "Wrong format. :( Try YYYY-MM-DD."
                )

        if expiry_date < today:
            print(
                "Attention: expired food. Think before you eat!"
            )

        foods.append([name, expiry_date])

        answer = input(
            "\nDo you want to add another food? (yes/no): "
        )

def remove_expired_foods(foods, today):
    updated_foods = []

    for food in foods:
        if food[1] >= today:
            updated_foods.append(food)

    return updated_foods



def save_foods_to_file(filepath, foods):
    with open(filepath, "w") as file_writer:
        for food in foods:
            line = f"{food[0]},{food[1]}\n"
            print("Writing:", line)
            file_writer.write(line)
def show_foods_to_remove(foods, today):
    print("\nFoods that will be removed:")

    found = False

    for food in foods:
        if food[1] < today:
            print(f"- {food[0]} ({food[1]})")
            found = True

    if not found:
        print("None")

def main():
    print("Saving file here:", os.path.abspath(FILE_PATH))
    
    foods = load_foods_from_file(FILE_PATH)
    

    while True:
        today_string = input(
            "What date is it? (YYYY-MM-DD): "
        )

        try:
            today = datetime.strptime(
                today_string,
                "%Y-%m-%d"
            ).date()
        except ValueError:
            print("Wrong format. :( Try YYYY-MM-DD.")
            continue

        confirm = input(
            f"You entered {today_string}. Press Enter to confirm or 'n' to change: "
        ).strip().lower()

        if confirm == "":
            break

        elif confirm == "n":
            continue

        else:
            print("You had exactly two options! Enter or 'n'! Try again.")
            continue
        
    show_foods(foods, today)    
    add_food(foods,today)

    print("\nFoods before saving:")

    for food in foods: 
        print(f"- {food[0]} ({food[1]})")
    
    show_foods_to_remove(foods, today)

    confirm = input(
    "\nPress Enter to remove expired foods or type 'n' to cancel: "
)   .strip().lower()

    if confirm != "n":
        foods = remove_expired_foods(foods, today)
    

    save_foods_to_file(FILE_PATH, foods)


    print("Food list updated.")

    with open(FILE_PATH, "r") as file:

        print("\nContents of foods.txt:")
        print(file.read())
    


if __name__ == "__main__":
    main()