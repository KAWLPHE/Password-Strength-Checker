"""
Password Strength Checker
Author: Isomiddin

Description:
A CLI tool that analyzes password strength based on
length, character diversity, and common security rules.
"""

import string


def analyze_password(password: str) -> dict:
    """Analyze password and return strength details."""
    length = len(password)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_lower, has_upper, has_digit, has_symbol])

    return {
        "length": length,
        "lowercase": has_lower,
        "uppercase": has_upper,
        "digits": has_digit,
        "symbols": has_symbol,
        "score": score,
    }


def get_strength_label(score: int, length: int) -> str:
    """Return human-readable strength label."""
    if length < 8:
        return "Very Weak"
    if score == 4 and length >= 12:
        return "Strong"
    if score >= 3:
        return "Medium"
    return "Weak"


def main():
    print("=" * 40)
    print("🔐 PASSWORD STRENGTH CHECKER")
    print("by Isomiddin")
    print("=" * 40)

    password = input("Enter password to analyze: ").strip()

    if not password:
        print("❌ Password cannot be empty.")
        return

    result = analyze_password(password)
    strength = get_strength_label(result["score"], result["length"])

    print("\n📊 Analysis Result:")
    print(f"- Length: {result['length']}")
    print(f"- Lowercase letters: {result['lowercase']}")
    print(f"- Uppercase letters: {result['uppercase']}")
    print(f"- Digits: {result['digits']}")
    print(f"- Symbols: {result['symbols']}")
    print(f"\n🔒 Password Strength: {strength}")


if __name__ == "__main__":
    main()
