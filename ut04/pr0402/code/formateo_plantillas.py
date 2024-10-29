def replace_str(string: str, dictionary: dict) -> str:
    words = string.split(" ")
    for i in range(len(words)):
        if words[i][0] == "{" and words[i][-1] == "}":
            final_idx = len(words[i]) - 1
            words[i] = dictionary.get(words[i][1:final_idx], "")
    return " ".join(words)
print(replace_str("Hola, {nombre}", {"nombre": "Alba"}))
