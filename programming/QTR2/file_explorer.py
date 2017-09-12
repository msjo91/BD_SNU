import os
import glob
import shutil


def show_sub():
    """Show every items in current directory"""
    print("\nCurrent DIR: {}\n".format(os.getcwd()))
    glob.iglob('*')
    for i in glob.iglob('*'):
        print(i)


def sel_menu():
    """Call select menu"""
    print("\nSelect Menu\n\t1) Change directory\n\t2) Search file\n\t3) Delete directory or file\n\t0) Quit")
    sel = input("Enter: ")
    if sel == '1':
        change_dir()
    elif sel == '2':
        search_dir()
    elif sel == '3':
        del_dir()
    elif sel == '0':
        exit()
    else:
        print("\nWrong input! Input is between 0 ~ 3.")
        sel_menu()


def change_dir():
    """Change directory"""
    idir = input("\nEnter a directory or path\n(Enter .. for the parent dir. and q to exit): ")
    if idir == 'q' or idir == 'Q' or idir == 'quit' or idir == 'QUIT' or idir == 'Quit':
        sel_menu()
    elif os.path.exists(os.path.join(os.getcwd(), idir)):
        try:
            os.chdir(idir)
        except PermissionError:
            print("\nPermissionError. Return to previous directory.")
        show_sub()
        change_dir()
    else:
        print("\nNo such directory.")
        show_sub()
        change_dir()


def search_dir():
    """Search file or directory in every subdirectory"""
    idir = input("\nEnter a keyword to search file or directory (Enter q to exit): ")
    if idir == 'q' or idir == 'Q' or idir == 'quit' or idir == 'QUIT' or idir == 'Quit':
        sel_menu()
    else:
        path = os.path.join(os.getcwd(), "**", "*{}*".format(idir))
        files = list(glob.iglob(path, recursive=True))
        if files:
            for f in files:
                print(f)
        else:
            print("\nNo such file or directory.")
        search_dir()


def del_dir():
    """Delete directory or file"""
    idir = input("\nEnter a directory or file (Enter q to exit): ")
    if idir == 'q' or idir == 'Q' or idir == 'quit' or idir == 'QUIT' or idir == 'Quit':
        sel_menu()
    else:
        if os.path.exists(idir):
            if os.path.isdir(idir):
                try:
                    os.rmdir(idir)
                    print("\nSuccessfully removed {}!".format(idir))
                except OSError:
                    choice = input(
                        "\nThis directory is not empty.\nDo you really want to delete this directory?\nEnter (y/n): ")
                    if choice == 'y' or choice == 'Y' or choice == 'yes' or choice == 'YES' or choice == 'Yes':
                        shutil.rmtree(idir)
                        print("\nSuccessfully removed {}!".format(idir))
                    elif choice == 'n' or choice == 'N' or choice == 'no' or choice == 'NO' or choice == 'No':
                        pass
                    else:
                        print("\nPlease answer accordingly.")
            else:
                os.remove(idir)
                print("\nSuccessfully removed {}!".format(idir))
        else:
            print("\n{} does not exist.".format(idir))
        show_sub()
        del_dir()


# Figure OS
if os.path.exists(os.environ['HOME']):
    # Check if the working directory is HOME or HOMEPATH
    if os.getcwd() != os.environ['HOME']:
        # Change directory to HOME or HOMEPATH
        os.chdir(os.environ['HOME'])
elif os.path.exists(os.environ['HOMEPATH']):
    if os.getcwd() != os.environ['HOMEPATH']:
        os.chdir(os.environ['HOMEPATH'])
show_sub()
sel_menu()
