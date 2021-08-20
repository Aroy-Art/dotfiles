import os, sys

# Print logo
Logo = '''
    My auto config setup script

                  __..--''``---....___   _..._    __
        /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // /
       ///_.-' _..--.'_    \                    `( ) ) // //
       / (_..-' // (< _     ;_..__               ; `' / ///
        / // // //  `-._,_)' // / ``--...____..-' /// / //
                                                            By Aroy    
    '''
print(Logo)

def query_yes_no(question, default):
#    Ask a yes/no question via input() and return their answer.
#
#    "question" is a string that is presented to the user.
#    "default" is the presumed answer if the user just hits <Enter>.
#            It must be "yes" (the default), "no" or None (meaning
#            an answer is required of the user).
#
#    The "answer" return value is True for "yes" or False for "no".

    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")


def install_missing_packages():

    awnser = query_yes_no("Install missing packages:", "yes")
    
    if awnser == True:

        if os.path.exists("/usr/bin/yay"):
            print("Found Yay")
            os.system("yay -Sy --needed \
                zsh \
                zsh-autosuggestions \
                zsh-completions \
                zsh-history-substring-search \
                zsh-theme-powerlevel10k-git\
                ttf-meslo-nerd-font-powerlevel10k \
                lscolors-git \
                nano-syntax-highlighting")

        else:
            print("Did not find Yay installing yay")
            os.system("sudo pacman -Sy --needed \
                zsh \
                zsh-autosuggestions \
                zsh-completions \
                zsh-history-substring-search \
                ttf-meslo-nerd-font-powerlevel10k \
                nano-syntax-highlighting \
                yay")
                
            os.system("yay -Sy --needed \
                zsh-theme-powerlevel10k-git \
                lscolors-git ")

                

if __name__ =='__main__':
    install_missing_packages()
