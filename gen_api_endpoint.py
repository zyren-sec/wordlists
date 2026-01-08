#!/usr/bin/env python3
#This script will generate the api-endpoint based on api_actions.txt & api_objects.txt by creating a pattern as follow
#1. /{action}{Object}              <=> /getUserProfile (camel case)
#2. /{action}-{object}             <=> /get-user-profile (kebab case)
#3. /{action}/{object}             <=> /get/userProfile
#4. /{object}/{action}             <=> /userProfile/get
#5. /{action}_{object}             <=> /get_user_profile
#6. /{action}/{object_snake}       <=> /get/user_profile
#7. /{object_snake}/{action}       <=> /user_profile/get


ACTIONS_FILE = "api_actions.txt"
OBJECTS_FILE = "api_objects.txt"
OUTPUT_FILE = "api_wordlist.txt"


def load_wordlist(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.strip().startswith("#")
        ]


def to_camel_case(s: str) -> str:
    """
    Normalize an object name to camelCase.
    Accepts:
      user -> user
      user_profile -> userProfile
      user-profile -> userProfile
      user profile -> userProfile
      UserProfile -> userProfile
      userProfile -> userProfile
    """
    s = s.strip()
    if not s:
        return s

    # Treat separators as word breaks
    s2 = s.replace("-", " ").replace("_", " ")
    parts = s2.split()

    # If it's already one token (e.g., userProfile / UserProfile), just lower first char
    if len(parts) == 1:
        token = parts[0]
        return token[0].lower() + token[1:] if token else token

    first = parts[0].lower()
    rest = "".join(p[:1].upper() + p[1:].lower() if p else "" for p in parts[1:])
    return first + rest


def capitalize_first(s: str) -> str:
    """Capitalize first character only for action+Object pattern."""
    return s[0].upper() + s[1:] if s else s


def camel_to_kebab(s: str) -> str:
    """camelCase/PascalCase -> kebab-case (lowercase + hyphens)."""
    if not s:
        return s

    out = []
    for i, ch in enumerate(s):
        if ch.isupper():
            if i != 0 and out and out[-1] != "-":
                out.append("-")
            out.append(ch.lower())
        else:
            out.append(ch)

    kebab = "".join(out)
    while "--" in kebab:
        kebab = kebab.replace("--", "-")
    return kebab.strip("-")


def camel_to_snake(s: str) -> str:
    """camelCase/PascalCase -> snake_case (lowercase + underscores)."""
    if not s:
        return s

    out = []
    for i, ch in enumerate(s):
        if ch.isupper():
            if i != 0 and out and out[-1] != "_":
                out.append("_")
            out.append(ch.lower())
        else:
            out.append(ch)

    snake = "".join(out)
    while "__" in snake:
        snake = snake.replace("__", "_")
    return snake.strip("_")


def main():
    actions = load_wordlist(ACTIONS_FILE)
    objects = load_wordlist(OBJECTS_FILE)

    results: set[str] = set()

    for action in actions:
        action_lc = action.lower()

        for obj_raw in objects:
            obj_camel = to_camel_case(obj_raw)            # userProfile
            obj_cap = capitalize_first(obj_camel)         # UserProfile
            obj_kebab = camel_to_kebab(obj_camel)         # user-profile
            obj_snake = camel_to_snake(obj_camel)         # user_profile

            # 1) /{action}{Object}  (camelCase RPC)
            results.add(f"/{action_lc}{obj_cap}")

            # 2) /{action}-{object} (kebab-case RPC)
            results.add(f"/{action_lc}-{obj_kebab}")

            # 3) /{action}/{object} (camelCase object)
            results.add(f"/{action_lc}/{obj_camel}")

            # 4) /{object}/{action} (camelCase object)
            results.add(f"/{obj_camel}/{action_lc}")

            # 5) /{action}_{object} (snake_case RPC)
            results.add(f"/{action_lc}_{obj_snake}")

            # 6) /{action}/{object} (snake_case object)
            results.add(f"/{action_lc}/{obj_snake}")

            # 7) /{object}/{action} (snake_case object)
            results.add(f"/{obj_snake}/{action_lc}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for line in sorted(results):
            f.write(line + "\n")

    print(f"[+] Generated {len(results)} unique endpoints")
    print(f"[+] Output written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()
