def split_string(s, delimeter):
    tokens = s.split(delimeter)
    for token in tokens:
        print(token)

print("Test 1: ")
split_string("Thats my house,\" I said.", " ")