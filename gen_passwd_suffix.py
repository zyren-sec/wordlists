def generate_suffixes():
    # KEYWORD-BASE
    keywords = [
        "123", "123123", "456", "456456", "789", "789789", 
        "777", "7777", "888", "8888", "999", "9999", "000", "0000",
        "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027",
        "zxc", "zxczxc", "qwe", "qweqwe", "asd", "asdasd"
    ]
    
    suffixes = []
    
    # THÊM CÁC WORD ĐỘC LẬP (mỗi WORD cũng là một suffix)
    suffixes.extend(keywords)
    
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
    
    # Loại bỏ duplicates và trả về
    return list(set(suffixes))

def main():
    suffixes = generate_suffixes()
    
    # Sắp xếp để dễ nhìn (tùy chọn)
    suffixes.sort()
    
    print(f"Total unique suffixes generated: {len(suffixes)}")
    print("\n=== CATEGORY SAMPLES ===")
    
    # Hiển thị theo nhóm để dễ kiểm tra
    print("\n1. Pure WORD suffixes (26 items):")
    for word in [
        "123", "123123", "456", "456456", "789", "789789", 
        "777", "7777", "888", "8888", "999", "9999", "000", "0000",
        "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027",
        "zxc", "zxczxc", "qwe", "qweqwe", "asd", "asdasd"
    ]:
        print(f"   {word}")
    
    print("\n2. PATTERN-0 (Special chars only - 28 items):")
    for i, suffix in enumerate([
        "`", "!", "@", "#", "$", 
        "``", "!!", "!!!", "@@", "@@@", "##", "###", "$$", "$$$",
        "`!", "!`", "!@", "@!", "@#", "#@", "#$", "$#",
        "`!@", "@!`", "!@#", "#@!", "@#$", "$#@"
    ], 1):
        print(f"   {i:2}. {suffix}")
    
    print("\n3. PATTERN-1 samples (WORD with single special char prefix/suffix):")
    sample_word = "123"
    samples = [
        f"`{sample_word}", f"!{sample_word}", f"@{sample_word}", f"#{sample_word}", f"${sample_word}",
        f"{sample_word}`", f"{sample_word}!", f"{sample_word}@", f"{sample_word}#", f"{sample_word}$"
    ]
    for i, suffix in enumerate(samples, 1):
        print(f"   {i:2}. {suffix}")
    
    print("\n4. PATTERN-2 samples (WORD wrapped with prefix and ` suffix):")
    samples = [
        f"`{sample_word}`", f"!{sample_word}`", f"@{sample_word}`", 
        f"#{sample_word}`", f"${sample_word}`"
    ]
    for i, suffix in enumerate(samples, 1):
        print(f"   {i:2}. {suffix}")
    
    print("\n5. PATTERN-9 samples (Repeated special chars with WORD):")
    samples = [
        f"``{sample_word}", f"```{sample_word}", f"!!{sample_word}", 
        f"{sample_word}``", f"{sample_word}```", f"{sample_word}!!",
        f"{sample_word}`!@", f"{sample_word}!@#"
    ]
    for i, suffix in enumerate(samples, 1):
        print(f"   {i:2}. {suffix}")
    
    # Lưu toàn bộ ra file
    with open("passwd_suffixes.txt", "w", encoding="utf-8") as f:
        for suffix in suffixes:
            f.write(suffix + "\n")
    
    print(f"\n✓ Saved {len(suffixes)} unique suffixes to 'passwd_suffixes.txt'")

if __name__ == "__main__":
    main()
