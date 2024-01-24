import os
import colorama

colorama.init()

class BlackNova:
    def __init__(self):
        self.running = True

        self.start()

    def help_BlackNova(self):
        print("")
        print("search <name off exploit>")
        print("")
        print("use <name off exploit/the path of exploit>")
        print("")
        print("exit")
        print("")
        print("help")
        print("")

    def exit_BlackNova(self):
        self.running = False

    def Unknown_command_BlackNova(self, command):
        print("")
        print(f"{colorama.Fore.RED}[-]{colorama.Fore.WHITE} Unknown command: ", end="")
        for pp in command: 
            print(pp, end=" ")
        print("")
        print("")
        
    def search_BlackNova(self, command):
        directory = "exploit/"
        extension = None

        file_list = []

        try:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if extension is None or file.endswith(extension):
                        file_list.append(os.path.join(root, file).lower())
        except Exception as e:
            pass
        
        print("")
        found = False
        for pp in file_list:
            row = pp.find(command[1])
            if not row == -1:
                st = colorama.Fore.WHITE + pp.replace(command[1], f"{colorama.Back.RED}{command[1]}{colorama.Fore.WHITE}{colorama.Back.RESET}")
                print(st.replace("\\", "/"))
                found = True

        if not found:
            print("")
            print(f"{colorama.Fore.RED}[-]{colorama.Fore.WHITE} No results from search")
            print("")
        print("")

    def use_BlackNova(self, command):
        os.system(f"python {command[1]}")

    def start(self):
        while self.running:
            comman = input(f"{colorama.Fore.RED}BlackNova>{colorama.Fore.LIGHTBLUE_EX}").lower().split(" ")
            command = [item for item in comman if item != '']

            if command[0] == "exit":
                self.exit_BlackNova()
            elif command[0] == "help":
                self.help_BlackNova()
            elif command[0] == "search":
                self.search_BlackNova(command)
            elif command[0] == "use":
                self.use_BlackNova(command)
            else:
                self.Unknown_command_BlackNova(command)

BlackNova()