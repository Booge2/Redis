from exhibit import Exhibit
from person import Person
from auth import Auth


def main():
    auth = Auth()

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            if auth.register(username, password):
                print("Registration successful")
            else:
                print("User already exists")

        elif choice == '2':
            username = input("Username: ")
            password = input("Password: ")
            if auth.login(username, password):
                print("Login successful")
                museum_menu()
            else:
                print("Invalid credentials")

        elif choice == '3':
            break


def museum_menu():
    while True:
        print("1. Add Exhibit")
        print("2. Delete Exhibit")
        print("3. Edit Exhibit")
        print("4. View Exhibit")
        print("5. View All Exhibits")
        print("6. View Exhibits by Type")
        print("7. Add Related Person to Exhibit")
        print("8. View Related People for Exhibit")
        print("9. View Related Exhibits for Person")
        print("10. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            exhibit_id = input("Exhibit ID: ")
            title = input("Title: ")
            description = input("Description: ")
            type = input("Type: ")
            exhibit = Exhibit(exhibit_id, title, description, type)
            exhibit.save()
            print("Exhibit added")

        elif choice == '2':
            exhibit_id = input("Exhibit ID: ")
            Exhibit.delete(exhibit_id)
            print("Exhibit deleted")

        elif choice == '3':
            exhibit_id = input("Exhibit ID: ")
            title = input("New Title: ")
            description = input("New Description: ")
            type = input("New Type: ")
            exhibit = Exhibit.get(exhibit_id)
            if exhibit:
                exhibit.update(title, description, type)
                print("Exhibit updated")
            else:
                print("Exhibit not found")

        elif choice == '4':
            exhibit_id = input("Exhibit ID: ")
            exhibit = Exhibit.get(exhibit_id)
            if exhibit:
                print(f"Title: {exhibit.title}")
                print(f"Description: {exhibit.description}")
                print(f"Type: {exhibit.type}")
                print(f"Related People: {', '.join(exhibit.get_related_people())}")
            else:
                print("Exhibit not found")

        elif choice == '5':
            exhibits = Exhibit.get_all_exhibits()
            for exhibit in exhibits:
                print(f"ID: {exhibit.exhibit_id}")
                print(f"Title: {exhibit.title}")
                print(f"Description: {exhibit.description}")
                print(f"Type: {exhibit.type}")
                print("----")

        elif choice == '6':
            type = input("Type: ")
            exhibits = Exhibit.get_by_type(type)
            for exhibit in exhibits:
                print(f"ID: {exhibit.exhibit_id}")
                print(f"Title: {exhibit.title}")
                print(f"Description: {exhibit.description}")
                print(f"Type: {exhibit.type}")
                print("----")

        elif choice == '7':
            exhibit_id = input("Exhibit ID: ")
            person_id = input("Person ID: ")
            exhibit = Exhibit.get(exhibit_id)
            if exhibit:
                exhibit.add_related_person(person_id)
                person = Person.get(person_id)
                if person:
                    person.add_related_exhibit(exhibit_id)
                    print("Related person added to exhibit")
                else:
                    print("Person not found")
            else:
                print("Exhibit not found")

        elif choice == '8':
            exhibit_id = input("Exhibit ID: ")
            exhibit = Exhibit.get(exhibit_id)
            if exhibit:
                related_people = exhibit.get_related_people()
                for person_id in related_people:
                    person = Person.get(person_id)
                    if person:
                        print(f"ID: {person.person_id}")
                        print(f"Name: {person.name}")
                        print(f"Bio: {person.bio}")
                        print("----")
            else:
                print("Exhibit not found")

        elif choice == '9':
            person_id = input("Person ID: ")
            person = Person.get(person_id)
            if person:
                related_exhibits = person.get_related_exhibits()
                for exhibit_id in related_exhibits:
                    exhibit = Exhibit.get(exhibit_id)
                    if exhibit:
                        print(f"ID: {exhibit.exhibit_id}")
                        print(f"Title: {exhibit.title}")
                        print(f"Description: {exhibit.description}")
                        print(f"Type: {exhibit.type}")
                        print("----")
            else:
                print("Person not found")

        elif choice == '10':
            break


if __name__ == "__main__":
    main()
