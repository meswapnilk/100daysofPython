
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    return f"{f_name.title()} {l_name.title()}"

print(format_name("Abcd", "DEFG"))
print(format_name("PQRS", ""))