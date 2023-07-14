def log(text):
    str_text = str(text)
    final_text = "\n" + str_text
    with open("log.txt", "a") as f:
        f.write(final_text)