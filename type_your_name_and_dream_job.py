# program that you can input your name and dream job

def main():
    # asking user to input their name 
    print("\033[1;32mWhat is your name:\033[0m", end=" ")
    name = input()

    # asking user to input their dream job
    dream_job = input("\033[1mEnter your dream job:\033[0m ")

    # Displaying the input back to the user with font styles and colors
    print("\n\033[1mHello {}, your dream job is to become a {}.\033[0m".format(name, "\033[34;4m{}\033[0m".format(dream_job)))

if __name__ == "__main__":
    main()


