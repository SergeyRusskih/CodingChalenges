import sys

class Commands(object):
    DEPEND = "DEPEND"
    INSTALL = "INSTALL"
    REMOVE = "REMOVE"
    LIST = "LIST"
    END = "END"

def process(input):

    # We need both dependencies list and consumers listkv gh jv
    # to lookup quickly
    # Assume the runtime complexity is more important
    # than memory consumption
    dependencies = dict()  
    used_by = dict()

    # We have to maintain order - need to produce the same input to pass the tests
    installed = []
    installed_explicilty = []

    for line in input:
        line = line.strip() # Not nice (new string is created) but have to validate and compare commands
        if line == Commands.END:
            print(line)
            
            # Assume we can stop the program execution at this point
            return
        elif line.startswith(Commands.DEPEND):
            print(line)
            add_dependencies(line.split()[1:], dependencies, used_by)
        elif line.startswith(Commands.INSTALL):
            print(line)
            program = line.split()[1]
            install(program, dependencies, installed)
            installed_explicilty.append(program)
        elif line.startswith(Commands.REMOVE):
            print(line)

            program = line.split()[1]
            if program not in installed:
                print(program + " is not installed")
                continue

            if not can_remove(program, used_by, installed):
                print(program + " is still needed")
                continue

            remove(program, installed, dependencies, used_by, installed_explicilty)
            installed_explicilty.remove(program)
        elif line == Commands.LIST:
            print(line)
            list_components(installed)
        else:
            # Assume it's safe to skip invalid lines
            continue

def add_dependencies(software, dependencies, used_by):
    root = software.pop(0)

    # We exclude the entire command if it countains
    # circular dependency
    for item in software:
        if item in dependencies:
            if root in dependencies[item]:
                print(item + " depends on " + root + ", ignoring command")
                return             

    if root in dependencies:
        dependants = dependencies[root]
        for item in software:
            if item not in dependants:
                dependants.append(item)
        dependencies[root] = dependants
    else:
        dependencies[root] = software

    for item in software:
        if item in used_by:
            users = used_by[item]
            if root not in users:
                users.append(root)
                used_by[item] = users
        else:
            used_by[item] = [root]


def install(program, dependencies, installed):
    if program in installed:
        print(program + " is already installed")
        return

    if program in dependencies:
        for dependency in dependencies[program]:
            if dependency not in installed:
                install(dependency, dependencies, installed)

    print("Installing " + program)
    installed.append(program)

def can_remove(program, used_by, installed):
    if program in used_by and len(used_by[program]) > 0:
        for item in used_by[program]:
            if item in installed:
                return False

    return True

def remove(program, installed, dependencies, used_by, installed_explicilty):

    print("Removing " + program)
    installed.remove(program)

    if program not in dependencies:
        return

    used_dependencies = dependencies[program]
    for item in used_dependencies:
        if can_remove(item, used_by, installed) and item not in installed_explicilty:
            remove(item, installed, dependencies, used_by, installed_explicilty)


def list_components(installed):
    for item in installed:
        print(item)
    
#process(sys.stdin)

def test_is_sum_of_three():
    process("""
22
DEPEND TELNET TCPIP NETCARD
DEPEND TCPIP NETCARD
DEPEND NETCARD TCPIP
DEPEND DNS TCPIP NETCARD
DEPEND BROWSER TCPIP HTML
INSTALL NETCARD
INSTALL TELNET
INSTALL foo
REMOVE NETCARD
INSTALL BROWSER
INSTALL DNS
LIST
REMOVE TELNET
REMOVE NETCARD
REMOVE DNS
REMOVE NETCARD
INSTALL NETCARD
REMOVE TCPIP
REMOVE BROWSER
REMOVE TCPIP
LIST
END
    """.splitlines())