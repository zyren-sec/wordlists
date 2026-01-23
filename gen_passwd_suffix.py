def generate_suffixes():
    # KEYWORD-BASE
    keywords = [
        "123", "123123", "456", "456456", "789", "789789", 
        "777", "7777", "888", "8888", "999", "9999", "000", "0000",
        "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027",
        "zxc", "zxczxc", "qwe", "qweqwe", "asd", "asdasd"
    ]
    
    suffixes = []
    
    # PATTERN-0 (standalone special chars)
    pattern0 = [
        "`", "!", "@", "#", "$", 
        "``", "!!", "!!!", "@@", "@@@", "##", "###", "$$", "$$$",
        "`!", "!`", "!@", "@!", "@#", "#@", "#$", "$#",
        "`!@", "@!`", "!@#", "#@!", "@#$", "$#@"
    ]
    suffixes.extend(pattern0)
    
    # PATTERN-1
    for word in keywords:
        suffixes.extend([
            f"`{word}",
            f"!{word}",
            f"@{word}",
            f"#{word}",
            f"${word}",
            f"{word}`",
            f"{word}!",
            f"{word}@",
            f"{word}#",
            f"{word}$"
        ])
    
    # PATTERN-2
    for word in keywords:
        suffixes.extend([
            f"`{word}`",
            f"!{word}`",
            f"@{word}`",
            f"#{word}`",
            f"${word}`"
        ])
    
    # PATTERN-3
    for word in keywords:
        suffixes.extend([
            f"`{word}!",
            f"!{word}!",
            f"@{word}!",
            f"#{word}!",
            f"${word}!"
        ])
    
    # PATTERN-4
    for word in keywords:
        suffixes.extend([
            f"`{word}@",
            f"!{word}@",
            f"@{word}@",
            f"#{word}@",
            f"${word}@"
        ])
    
    # PATTERN-5
    for word in keywords:
        suffixes.extend([
            f"`{word}#",
            f"!{word}#",
            f"@{word}#",
            f"#{word}#",
            f"${word}#"
        ])
    
    # PATTERN-6
    for word in keywords:
        suffixes.extend([
            f"`{word}$",
            f"!{word}$",
            f"@{word}$",
            f"#{word}$",
            f"${word}$"
        ])
    
    # PATTERN-7
    for word in keywords:
        suffixes.extend([
            f"!@{word}",
            f"@!{word}",
            f"@#{word}",
            f"#@{word}",
            f"#${word}",
            f"$#{word}",
            f"!@{word}!@",
            f"@!{word}@!",
            f"@#{word}@#",
            f"#@{word}#@",
            f"#${word}#$",
            f"$#{word}$#"
        ])
    
    # PATTERN-8
    for word in keywords:
        suffixes.extend([
            f"`!@{word}",
            f"!@#{word}",
            f"@#${word}",
            f"$#@{word}",
            f"#@!{word}",
            f"@!`{word}",
            f"{word}`!@",
            f"{word}!@#",
            f"{word}@#$",
            f"{word}$#@",
            f"{word}#@!",
            f"{word}@!`"
        ])
    
    # PATTERN-9
    for word in keywords:
        suffixes.extend([
            f"``{word}",
            f"```{word}",
            f"!!{word}",
            f"!!!{word}",
            f"@@{word}",
            f"@@@{word}",
            f"##{word}",
            f"###{word}",
            f"$${word}",
            f"$$${word}",
            f"`!@{word}",
            f"@!`{word}",
            f"!@#{word}",
            f"#@!{word}",
            f"@#${word}",
            f"$#@{word}",
            f"{word}``",
            f"{word}```",
            f"{word}!!",
            f"{word}!!!",
            f"{word}@@",
            f"{word}@@@",
            f"{word}##",
            f"{word}###",
            f"{word}$$",
            f"{word}$$$",
            f"{word}`!@",
            f"{word}@!`",
            f"{word}!@#",
            f"{word}#@!",
            f"{word}@#$",
            f"{word}$#@"
        ])
    
    return list(set(suffixes))  # Remove duplicates

def main():
    suffixes = generate_suffixes()
    
    print(f"Total unique suffixes generated: {len(suffixes)}")
    print("\nFirst 50 suffixes:")
    for i, suffix in enumerate(suffixes[:50], 1):
        print(f"{i:3}. {suffix}")
    
    print("\nLast 50 suffixes:")
    for i, suffix in enumerate(suffixes[-50:], len(suffixes)-49):
        print(f"{i:3}. {suffix}")
    
    # Optionally save to file
    with open("suffixes_list.txt", "w", encoding="utf-8") as f:
        for suffix in suffixes:
            f.write(suffix + "\n")
    print(f"\nSaved all suffixes to 'suffixes_list.txt'")

if __name__ == "__main__":
    main()
