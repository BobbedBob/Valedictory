import glob

if __name__ == "__main__":
    print("Welcome to Bob's Valedictory Assistant.")
    print("========")
    print("Loading names...")
    try:
        names = open("names.txt")
    except Exception as error:
        print(f"Could not find names.txt: {error.args}")
        exit(1)

    all_students = {}

    for line in names.readlines():
        student_code = line[-9 : len(line) - 2]
        all_students[student_code] = line[0:-11]
        print(f"{student_code} : {all_students[student_code]}")

    print(f"Loaded {len(all_students)} students!")

    print("========")
    year7 = int(input("Enter the photos year corresponding to YEAR 7:\n"))
    year12 = year7 + 5

    print("========")
    print("ACCEPTED FORMATS:")
    print("Exact student code; (e.g. YAN0185)")
    print("Exact student codes seperated by a comma, NO SPACES; (e.g. YI-0009,YAN0185)")
    print("Write * to list for ALL students in the names.txt file;")
    print("Write ** to list for ALL students in the names.txt file while skipping any confirmation prompts.")
    s = ""
    year7_path = rf"Q:\GWSC Photos\{str(year7)} GWSC Photos"
    year12_path = rf"Q:\GWSC Photos\{str(year12)} GWSC Photos"
    while s.lower() != "bye":
        print("========")
        s = input("Enter STUDENT CODE, * or ** to query; Press ENTER key or enter BYE to exit programme:\n")
        if s.lower() == "bye" or str(s) == "":
            break

        if s != "*" and s != "**":
            students_list = s.split(",")
        else:
            students_list = list(all_students.keys())

        print("----RESULTS----")
        for student in students_list:
            year7_photo = glob.glob(
                year7_path + f"/**/{student.upper()}.*", recursive=True
            )
            year12_photo = glob.glob(
                year12_path + f"/**/{student.upper()}.*", recursive=True
            )
            if not year7_photo:
                year7_photo = ["Could not find corresponding photo."]
            if not year12_photo:
                year12_photo = ["Could not find corresponding photo."]

            if all_students.get(student.upper()) is None:
                print(f"    Student {student.upper()} is not a valid student found in names.txt.")
            else:
                print(f"""
    Student {student.upper()} ({all_students.get(student.upper())}):
    Year 7 Photo Location: 
    {year7_photo[0]}
    Year 12 Photo Location: 
    {year12_photo[0]}
                """)

            if len(students_list) > 0 and not s == "**":
                input("Press ENTER to continue; \n Write ** during initial input to skip all confirmation prompts.")

        if s == "*" or s == "**":
            s = ""

    print("See ya!")
    exit(0)
