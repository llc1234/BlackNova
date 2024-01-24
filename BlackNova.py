import os
import colorama

colorama.init()


class BlackNova:
    def __init__(self):
        self.running = True

        self.use_data = {}

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
            row_txt = pp.find("info.txt")
            if not row == -1 and row_txt == -1:
                st = colorama.Fore.WHITE + pp.replace(command[1], f"{colorama.Back.RED}{command[1]}{colorama.Fore.WHITE}{colorama.Back.RESET}")
                print(st.replace("\\", "/"))
                found = True

        if not found:
            print("")
            print(f"{colorama.Fore.RED}[-]{colorama.Fore.WHITE} No results from search")
            print("")
        print("")

    def set_command(self, command):
        try:
            for i in range(len(command)):
                try:
                    t = self.use_data[command[1].lower()]
                    self.use_data[command[1].lower()] = command[2]
                except:
                    pass
        except:
            pass

    def exploit_run_command(self, dir):
        ad = ""
        for name, inside in self.use_data.items():
            ad += inside + " "

        print(f"python {dir} {ad}")
        # os.system(f"python {dir} {ad}")

    def help_command(self):
        print("")
        print(self.help_command_text)
        print("")

    def show_options_command(self):
        print("")
        for name, inside in self.use_data.items():
            print(f"{name}: {inside}")
        print("")


    def get_info_txt(self, dir):
        path = os.path.dirname(dir)

        print(f"{path}/info.txt")

        r = open(f"{path}/info.txt", "r")
        
        for pp in r.read().split(":"):
            self.use_data[pp] = ""

        r.close()


    def use_BlackNova(self, comm):
        # os.system(f"python {command[1]}")

        self.get_info_txt(comm[1])

        print("")
        print(f"Start {comm[1]}")
        print("")

        while True:
            comman = input(f"m9>").split(" ")
            command = [item for item in comman if item != '']

            if command[0].lower() == "exit":
                self.use_data = {}
                break
            if command[0].lower() == "help":
                self.help_command()
            elif command[0].lower() == "set":
                self.set_command(command)
            elif command[0].lower() == "show" and command[1].lower() == "options":
                self.show_options_command()
            elif command[0].lower() == "run" or command[0].lower() == "exploit":
                self.exploit_run_command(comm[1])

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
