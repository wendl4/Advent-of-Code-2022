class folder:
    def __init__(self, parent, name, folders={}):
        self.level = 0
        self.parent = parent
        self.name = name
        self.folders = folders
        self.files = []
        self.size = 0
        self.visited = False

    def __str__(self):
        foldes = ""
        space = "  " * self.level
        for fold in self.folders.values():
            foldes+=space+str(fold)
        files = ""
        for file in self.files:
            files+=space+str(file)
        return f"dir {self.name} {self.size} \n{foldes}{files}"

    def get_sum(self):
        acc = 0
        if self.level > 1:
            for file in self.files:
                acc+=file.size
        for fold in self.folders.values():
            fold_sum = fold.get_sum()
            acc+=fold_sum
        self.size = acc
        return acc

    def get_all_sizes(self):
        self.visited = True
        acc = []
        for fold in self.folders.values():
            if fold.visited == False:
                acc = acc + fold.get_all_sizes()
        if self.size <= 100000 and self.level > 1:
            acc.append(self.size)
        return acc


    def get_all_sizes2(self):
        self.visited = True
        acc = []
        for fold in self.folders.values():
            if fold.visited == False:
                acc = acc + fold.get_all_sizes2()
        if self.level > 1:
            acc.append(self.size)
        return acc


class file:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def __str__(self):
        return f"{self.name} {self.size} \n"



def part1():
    with open('input7.txt', 'r') as input:
        root_folder = folder('root', '', {'/':folder(None,'/')})
        root_folder.folders['/'].parent = root_folder
        root_folder.folders['/'].level = 1
        pwd = root_folder
        command = None
        for line in input:
            params = line.rstrip().split(' ')
            if params[0] == "$":
                command = None
                if params[1] == "cd":
                    if params[2] != "..":
                        pwd = pwd.folders[params[2]]
                    elif params[2] == "..":
                        pwd = pwd.parent
                if params[1] == "ls":
                    command = "ls"
            elif command == "ls":
                if params[0] == "dir":
                    pwd.folders[params[1]] = folder(pwd, params[1], {})
                    pwd.folders[params[1]].level = pwd.level+1
                else:
                    pwd.files.append(file(params[1],params[0]))
        
        root_folder.folders['/'].get_sum()


        return sum(root_folder.folders['/'].get_all_sizes())

def part2():
    with open('input7.txt', 'r') as input:
        root_folder = folder('root', '', {'/':folder(None,'/')})
        root_folder.folders['/'].parent = root_folder
        root_folder.folders['/'].level = 1
        pwd = root_folder
        command = None
        for line in input:
            params = line.rstrip().split(' ')
            if params[0] == "$":
                command = None
                if params[1] == "cd":
                    if params[2] != "..":
                        pwd = pwd.folders[params[2]]
                    elif params[2] == "..":
                        pwd = pwd.parent
                if params[1] == "ls":
                    command = "ls"
            elif command == "ls":
                if params[0] == "dir":
                    pwd.folders[params[1]] = folder(pwd, params[1], {})
                    pwd.folders[params[1]].level = pwd.level+1
                else:
                    pwd.files.append(file(params[1],params[0]))
        
    size_sum = root_folder.folders['/'].get_sum()

    sizes = root_folder.folders['/'].get_all_sizes2()
    sizes.sort()

    diff = 30000000 - (70000000 - size_sum)

    return list(filter(lambda x: (x > diff), sizes))[0]
