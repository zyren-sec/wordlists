import itertools

# KEYWORD-BASE
WORD_LIST = [
    "123", "123123", "456", "456456", "789", "789789",
    "444", "4444", "777", "7777", "888", "8888", "999", "9999", "000", "0000",
    "100", "1000", "500", "5000", "900", "9000",
    "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027",
    "zxc", "zxczxc", "qwe", "qweqwe", "asd", "asdasd"
]

# PATTERNS đã được định nghĩa dưới dạng string templates
PATTERNS = [
    # PATTERN-1
    "`", "!", "@", "#", "$",
    "`{WORD}", "!{WORD}", "@{WORD}", "#{WORD}", "${WORD}",
    "{WORD}`", "{WORD}!", "{WORD}@", "{WORD}#", "{WORD}$",
    
    # PATTERN-2
    "`{WORD}`", "!{WORD}`", "@{WORD}`", "#{WORD}`", "${WORD}`",
    
    # PATTERN-3
    "`{WORD}!", "!{WORD}!", "@{WORD}!", "#{WORD}!", "${WORD}!",
    
    # PATTERN-4
    "`{WORD}@", "!{WORD}@", "@{WORD}@", "#{WORD}@", "${WORD}@",
    
    # PATTERN-5
    "`{WORD}#", "!{WORD}#", "@{WORD}#", "#{WORD}#", "${WORD}#",
    
    # PATTERN-6
    "`{WORD}$", "!{WORD}$", "@{WORD}$", "#{WORD}$", "${WORD}$",
    
    # PATTERN-7
    "!@", "@!", "@#", "#@", "#$", "$#",
    "!@{WORD}", "@!{WORD}", "@#{WORD}", "#@{WORD}", "#${WORD}", "$#{WORD}",
    "!@{WORD}!@", "@!{WORD}@!", "@#{WORD}@#", "#@{WORD}#@", "#${WORD}#$", "$#{WORD}$#",
    
    # PATTERN-8
    "`!@", "!@#", "@#$", "$#@", "#@!", "@!`",
    "`!@{WORD}", "!@#{WORD}", "@#${WORD}", "$#@{WORD}", "#@!{WORD}", "@!`{WORD}",
    "{WORD}`!@", "{WORD}!@#", "{WORD}@#$", "{WORD}$#@", "{WORD}#@!", "{WORD}@!`",
    
    # PATTERN-9
    "``", "```", "!!", "!!!", "@@", "@@@", "##", "###", "$$", "$$$",
    "`!@", "@!`", "!@#", "#@!", "@#$", "$#@",
    "``{WORD}", "```{WORD}", "!!{WORD}", "!!!{WORD}", "@@{WORD}", "@@@{WORD}",
    "##{WORD}", "###{WORD}", "$${WORD}", "$$${WORD}",
    "`!@{WORD}", "@!`{WORD}", "!@#{WORD}", "#@!{WORD}", "@#${WORD}", "$#@{WORD}",
    "{WORD}``", "{WORD}```", "{WORD}!!", "{WORD}!!!", "{WORD}@@", "{WORD}@@@",
    "{WORD}##", "{WORD}###", "{WORD}$$", "{WORD}$$$",
    "{WORD}`!@", "{WORD}@!`", "{WORD}!@#", "{WORD}#@!", "{WORD}@#$", "{WORD}$#@"
]

def generate_suffixes():
    """
    Tạo tất cả các suffix dựa trên WORD_LIST và PATTERNS
    """
    suffixes = set()  # Dùng set để tránh trùng lặp
    
    for pattern in PATTERNS:
        if "{WORD}" in pattern:
            # Pattern có chứa {WORD} - thay thế bằng mỗi từ trong WORD_LIST
            for word in WORD_LIST:
                suffixes.add(pattern.replace("{WORD}", word))
        else:
            # Pattern không chứa {WORD} - thêm trực tiếp
            suffixes.add(pattern)
    
    return sorted(suffixes)

def save_to_file(suffixes, filename="suffix_list.txt"):
    """
    Lưu danh sách suffix vào file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for suffix in suffixes:
            f.write(f"{suffix}\n")
    print(f"Đã lưu {len(suffixes)} suffix vào file: {filename}")

def generate_username_combinations(username, suffixes, filename="username_password_list.txt"):
    """
    Tạo danh sách username + suffix cho brute force
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for suffix in suffixes:
            f.write(f"{username}{suffix}\n")
    print(f"Đã lưu {len(suffixes)} combination vào file: {filename}")

def main():
    # 1. Tạo tất cả các suffix
    print("Đang tạo suffixes...")
    suffixes = generate_suffixes()
    
    # 2. Hiển thị số lượng và một vài ví dụ
    print(f"Tổng số suffixes: {len(suffixes)}")
    print("\n20 suffixes đầu tiên:")
    for i, suffix in enumerate(suffixes[:20]):
        print(f"  {i+1:3}. {suffix}")
    
    # 3. Lưu toàn bộ suffixes vào file
    save_to_file(suffixes, "suffixes.txt")
    
    # 4. Tạo username combinations (ví dụ với username "admin")
    username = "admin"
    generate_username_combinations(username, suffixes, "admin_combinations.txt")
    
    # 5. Tạo thêm file với các username khác
    common_usernames = ["admin", "root", "user", "test", "administrator"]
    all_combinations = []
    
    for user in common_usernames:
        for suffix in suffixes:
            all_combinations.append(f"{user}{suffix}")
    
    with open("common_users_combinations.txt", 'w', encoding='utf-8') as f:
        for combo in all_combinations:
            f.write(f"{combo}\n")
    
    print(f"\nĐã tạo {len(all_combinations)} combinations cho {len(common_usernames)} usernames phổ biến")

if __name__ == "__main__":
    main()
