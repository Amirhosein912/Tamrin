import os

def create_file():
    filename = input("نام فایل جدید را وارد کنید: ")
    try:
        f = open(filename, "x")
        print(f"فایل {filename} با موفقیت ایجاد شد.")
        f.close()
    except FileExistsError:
        print(f"فایل {filename} قبلاً وجود دارد.")

def edit_file():
    filename = input("نام فایل مورد نظر را وارد کنید: ")
    try:
        f = open(filename, "a")
        content = input("محتوای جدید را وارد کنید: ")
        f.write(content)
        print(f"محتوای '{content}' به فایل {filename} اضافه شد.")
        f.close()
    except FileNotFoundError:
        print(f"فایل {filename} یافت نشد.")

def delete_file():
    filename = input("نام فایل مورد نظر را وارد کنید: ")
    try:
        os.remove(filename)
        print(f"فایل {filename} با موفقیت حذف شد.")
    except FileNotFoundError:
        print(f"فایل {filename} یافت نشد.")

def main():
    while True:
        print("\nمنو:")
        print("1. ایجاد فایل")
        print("2. ویرایش فایل")
        print("3. حذف فایل")
        print("4. خروج")
        choice = input("گزینه مورد نظر را انتخاب کنید: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            edit_file()
        elif choice == "3":
            delete_file()
        elif choice == "4":
            print("خداحافظ!")
            break
        else:
            print("گزینه نامعتبر است. لطفاً دوباره انتخاب کنید.")

if __name__ == "__main__":
    main()
