print("""________                               __    ___________               __    
\______ \   ____   _____  ____________/  |   \__    ___/______   ____ |  | __
 |  | |  \_/ __ \ / ___// __ \_  __ \   __\    |    |  \_  __ \_/ __ \|  |/ /
 |  |_|   \  ___/ \___ \\\ ___/|  | \/|  |      |    |   |  | \/\  ___/|    < 
/_______  /\___ \\ /____/ \\__ \\|__|   |__|      |____|   |__|    \___ \|__|_ \\
        \/     \/                                                   \/     \/""")


print("""        _
    .--' |
   /___^ |     .--.
       ) |    /    \\
      /  |  /`      '.
     |   '-'    /     \\
     \         |      |\\
      \    /   \      /\|
       \  /'----`\   /
       |||       \\ |
       ((|        ((|
       |||        |||
      //_(       //_(
""")

import time



def delay_print(s):
    for c in s:
        print(c, end="", flush=True)
        time.sleep(0.01)
def main():
    delay_print("""Welcome to Desert Trek!
You have stolen a camel to make your way across the great Mojave desert.
The natives want their camel back and are chasing you down! Survive your
journey and out run the natives.""")
    print()
    done = False
    while done == False:
        print()
        print("""OPTIONS:
    A. Drink from your canteen.
    B. Ahead moderate speed.
    C. Ahead full speed.
    D. Stop for the night.
    E. Status check.
    Q. Quit.""")
        print()
        input("What would you like to do? ")
main()
