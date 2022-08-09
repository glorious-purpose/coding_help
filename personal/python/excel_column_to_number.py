"""Take up to 2 letters and return column number."""
import string

while True:
    target_column = input("Target Column -> ")
    if len(target_column) == 1:
        print(ord(target_column.lower()) - ord("a") + 1)
    elif len(target_column) == 2:
        alphas = [""] + list(string.ascii_lowercase)
        column_no = alphas.index(target_column[0].lower()) * 26 + 1 + ord(target_column[1]) - ord("a")
        print(f"{column_no}")
    else:
        print("Not prepared for that.")
