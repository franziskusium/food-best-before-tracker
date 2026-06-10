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


def add_food(foods):
    answer = input("\nDo you want to add food? (yes/no): ")

    while answer.lower() == "yes":

        name = input("Food name: ")

        date_string = input(
            "Best-before date (YYYY-MM-DD): "
        )

        expiry_date = datetime.strptime(
            date_string,
            "%Y-%m-%d"
        ).date()

        foods.append([name, expiry_date])

        answer = input(
            "\nAdd another food? (yes/no): "
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

def main():
    print("Saving file here:", os.path.abspath(FILE_PATH))
    
    foods = load_foods_from_file(FILE_PATH)
    

    today_string = input("What date is it? (YYYY-MM-DD): ")
    today = datetime.strptime(today_string, "%Y-%m-%d").date()

    show_foods(foods, today)
    add_food(foods)

    print("Foods before saving:", foods)

    foods = remove_expired_foods(foods, today)

    save_foods_to_file(FILE_PATH, foods)


    print("Food list updated.")

    with open(FILE_PATH, "r") as file:

        print("\nContents of foods.txt:")
        print(file.read())


if __name__ == "__main__":
    main()