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

home_folder = os.getenv('HOME')

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


def backup_old_user_configs():

    awnser = query_yes_no("\nBackup old user config files(Recommended):", "yes")

    user_backup_files = [
        '.zshrc',
        '.zhistory',
        '.zprofile',
        '.zcompdump',
        '.zshrc'
    ]
    
    if awnser == True:
        
        if not os.path.exists(home_folder + "/Config-Backup"):
            os.mkdir(home_folder + "/Config-Backup")
        elif os.path.exists(home_folder + "/Config-Backup"):
            print("Found old config backup folder")
            os.system("mv -v -i" + home_folder + "/Config-Backup " + home_folder + "/Config-Backup~")
            os.mkdir(home_folder + "/Config-Backup")

        for f in user_backup_files:
            if os.path.exists(home_folder + "/" + f):
                print("Exists (Backing up)   :", home_folder + "/" + f)
                os.system("mv -v -i " + home_folder + "/" + f + " " + home_folder + "/Backup/")
            else:
                print("Doesn't exists skiping:", home_folder + "/" + f)


def copy_new_user_configs():

    if query_yes_no("\nCopy new user config files:", "yes") == True:

        cwd = os.getcwd()

        user_new_configs = [
                '/zsh/.p10k.zsh',
                '/zsh/.zprofile',
                '/zsh/.zshrc',

                '/git/.gitconfig',

                '/nano/.nanorc'
            ]
        
        for f in user_new_configs:
            os.system("cp -v -i " + cwd + f + " " + home_folder)


if __name__ =='__main__':
    install_missing_packages()

    backup_old_user_configs()
    
    copy_new_user_configs()
