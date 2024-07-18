import random
import time

def generate_random_words(length):
    words_list = ["and", "or", "the", "flower", "house", "tree", "sun", "moon", "star", 
                  "river", "lake", "ocean", "mountain", "cloud", "rain", "snow", 
                  "wind", "fire", "earth", "sky", "bird", "fish", "dog", "cat", 
                  "rabbit", "lion", "elephant", "turtle", "snake", "apple", "banana", 
                  "orange", "grape", "strawberry", "melon", "potato", "carrot", 
                  "tomato", "onion", "pepper"]
    words = random.sample(words_list, length)
    return ' '.join(words)

def calculate_wpm(text, elapsed_time):
    words = text.split()
    num_words = len(words)
    minutes = elapsed_time / 60.0
    wpm = num_words / minutes if minutes > 0 else 0
    return wpm

def main():
    passage_length = 40
    passage = generate_random_words(passage_length)
    
    print("Here is your passage:")
    print(passage)
    
    print("\nChoose timer option:")
    print("1. 30 seconds")
    print("2. 1 minute")
    timer_option = int(input("Enter your choice (1 or 2): "))

    if timer_option == 1:
        timer_seconds = 30
    elif timer_option == 2:
        timer_seconds = 60
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"You have {timer_seconds} seconds to type the passage.")
    time.sleep(1)
    print("Start typing in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("GO!")
    
    start_time = time.time()
    input_text = input()
    end_time = time.time()

    elapsed_time = end_time - start_time
    wpm = calculate_wpm(input_text, elapsed_time)

    print(f"\nTime elapsed: {elapsed_time:.2f} seconds")
    print(f"Your typing speed: {wpm:.2f} WPM")

if __name__ == "__main__":
    main()
