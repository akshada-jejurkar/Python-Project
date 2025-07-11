# 🔷 Akshada's Student Record Tracker – Core Python Project

student_data_list = []

def add_new_record():
    roll = input("Enter Roll No: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")
    student_data_list.append({"roll": roll, "name": name, "marks": marks})
    print("✅ Record added successfully!\n")

def view_all_records():
    if not student_data_list:
        print("⚠️ No records found.\n")
        return

    print("\n📘 Student Records:")
    total_marks = 0
    for student in student_data_list:
        print(f"🎓 Roll: {student['roll']} | Name: {student['name']} | Marks: {student['marks']}")
        total_marks += int(student['marks'])

    avg_marks = total_marks / len(student_data_list)
    print(f"\n📊 Average Marks of Class: {avg_marks:.2f}\n")

def search_by_roll():
    roll = input("Enter Roll No to Search: ")
    for student in student_data_list:
        if student["roll"] == roll:
            print(f"🔍 Found: Roll: {student['roll']}, Name: {student['name']}, Marks: {student['marks']}\n")
            return
    print("❌ Record not found!\n")

def update_record():
    roll = input("Enter Roll No to Update: ")
    for student in student_data_list:
        if student["roll"] == roll:
            student["name"] = input("Enter New Name: ")
            student["marks"] = input("Enter New Marks: ")
            print("✅ Record updated successfully!\n")
            return
    print("❌ Record not found!\n")

def remove_student_record():
    roll = input("Enter Roll No to Delete: ")
    for student in student_data_list:
        if student["roll"] == roll:
            student_data_list.remove(student)
            print("✅ Record deleted successfully!\n")
            return
    print("❌ Record not found!\n")

def main():
    print("🔷 Welcome to Akshada's Student Tracker")
    print("🔸 Built with ❤️ using Core Python\n")

    while True:
        print("🗂️ Menu:")
        print("1. Add Student Record")
        print("2. View All Records")
        print("3. Search by Roll No")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_new_record()
        elif choice == "2":
            view_all_records()
        elif choice == "3":
            search_by_roll()
        elif choice == "4":
            update_record()
        elif choice == "5":
            remove_student_record()
        elif choice == "6":
            print("👋 Thank you for using Akshada's Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
