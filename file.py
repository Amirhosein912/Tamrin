import os

def create_file():
    filename = input("نام فایل جدید را وارد کنید: ")
    try:
        f = open(filename, "x")
        print(f"فایل {filename} با موفقیت ایجاد شد.")
        content = input("لطفا محتوای دلخواه را وارد کنید")
        print(content, file=f)
        f.close()
    except FileExistsError:
        print(f"فایل {filename} قبلاً وجود دارد.")

def edit_file():
    filename = input("نام فایل مورد نظر را وارد کنید: ")
    lineNumber = int(input("سطر مورد نظر را وارد کنید: "))
    newContent = input("محتوای جدید را وارد کنید: ")
    lineCounter = 1
    try:
        oldfile = open(filename, "r")
        tempfile = open("temp", "w")
        oldFilelineContent = oldfile.readline() # این اولین خط فایل است
        while oldFilelineContent:
            if lineNumber == lineCounter:
                tempfile.write(newContent + "\n")
            else:
                tempfile.write(oldFilelineContent)
            oldFilelineContent = oldfile.readline()
            lineCounter += 1

        oldfile.close()
        tempfile.close()
        os.remove(filename)
        os.rename("temp", filename)

        print(f"محتوای '{newContent}' به فایل {filename} اضافه شد.")

    except FileNotFoundError:
        print(f"فایل {filename} یافت نشد.")

def delete_file():
    filename = input("نام فایل مورد نظر را وارد کنید: ")
    try:
        os.remove(filename)
        print(f"فایل {filename} با موفقیت حذف شد.")
    except FileNotFoundError:
        print(f"فایل {filename} یافت نشد.")

def show_file():
    filename = input("نام فایل مورد نظر را وارد کنید: ")
    try:
        f = open(filename, "r")
        print(f.read())
    except FileNotFoundError:
        print(f"فایل {filename} یافت نشد.")
def main():
    while True:
        print("\nمنو:")
        print("1. ایجاد فایل")
        print("2. ویرایش فایل")
        print("3. حذف فایل")
        print("4. نمایش فایل")
        print("5. خروج")
        choice = input("گزینه مورد نظر را انتخاب کنید: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            edit_file()
        elif choice == "3":
            delete_file()
        elif choice == "4":
            show_file()
        elif choice == "5":
            print("خداحافظ!")
            break
        else:
            print("گزینه نامعتبر است. لطفاً دوباره انتخاب کنید.")

# if __name__ == "__main__":
main()