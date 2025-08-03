import random
import time
import os
import msvcrt
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_screen():
    clear_screen()
    print("Welcome to the Typing Speed Test!")
    print("Press 's' to start, 'q' to quit")
    print()
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 's':
                return True
            elif key == 'q':
                return False

def display_text(target, current, wpm=0):
    clear_screen()
    print(f"WPM: {wpm}")
    print()
    
    # Display target text
    print("Target text:")
    print(target)
    print()
    
    # Display current text with color coding
    print("Your typing:")
    for i, char in enumerate(current):
        if i < len(target):
            if char == target[i]:
                print(char, end='')  # Correct character
            else:
                print(char, end='')  # Incorrect character
        else:
            print(char, end='')
    print()
    print("_" * len(target))

def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
    return random.choice(lines).strip()

def wpm_test():
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    
    print("Get ready! Press any key to start typing...")
    msvcrt.getch()
    
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / time_elapsed) * 60 / 5)
        display_text(target_text, current_text, wpm)
        
        if "".join(current_text) == target_text:
            clear_screen()
            print(f"Test completed! Your WPM: {wpm}")
            print("Press any key to continue...")
            msvcrt.getch()
            break
            
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\x08':  # Backspace
                if current_text:
                    current_text.pop()
            elif key == b'\x1b':  # ESC key
                break
            else:
                try:
                    char = key.decode('utf-8')
                    if char.isprintable():
                        current_text.append(char)
                except:
                    continue

def main():
    while True:
        if not start_screen():
            break
        wpm_test()

if __name__ == "__main__":
    main()

