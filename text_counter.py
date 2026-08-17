def analyze_text(text):
    words = len(text.split())
    characters = len(text)
    lines = len(text.splitlines())

    return words, characters, lines


def main():
    print("=== Text Counter ===")

    text = input("Enter your text: ")

    words, characters, lines = analyze_text(text)

    print("\n=== Results ===")
    print(f"Words: {words}")
    print(f"Characters: {characters}")
    print(f"Lines: {lines}")


if name == "main":
    main()