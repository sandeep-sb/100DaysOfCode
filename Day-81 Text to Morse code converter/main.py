# Text to morse code
import time
from morse_code_dict import morse_code
import winsound


def text_to_morse_code(string):
    convert_to_morse_code = ""
    for char in string:
        if char != " ":
            convert_to_morse_code += f"{morse_code[char]} "
        else:
            convert_to_morse_code += "   "
    return convert_to_morse_code


def morse_code_to_sound(string):
    for char in string:
        if char != " ":
            # Space is added to distinguish between different letters
            # so we can provide enough pause between letters of a word.
            convert_to_morse_code = f"{morse_code[char]} "
            for dit_dah in convert_to_morse_code:
                if dit_dah == ".":
                    winsound.Beep(frequency=700, duration=150)
                elif dit_dah == "_":
                    winsound.Beep(frequency=700, duration=450)
                elif dit_dah == " ":
                    # After every dit/dah, we pause for a specific time.
                    time.sleep(0.2)
                # After every letter, we pause for a specific time.
                # It's 3 times the dit/dah pause
                time.sleep(0.6)
        # Space between words means we take longer pauses
        # It's 7 times the dit/dah pause
        elif char == " ":
            time.sleep(1.4)


input_string = input("Enter the string... ").lower()
morse_code_text = text_to_morse_code(input_string)

print("Morse code is", morse_code_text)

choice = input("Do you want to hear the morse code?(Y/N)").upper()
morse_code_to_sound(input_string)
