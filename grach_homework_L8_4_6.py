class Storage:
    def __init__(self, units, prices):
        self.units  = units
        self.prices = prices

class Devices:
    def __init__(self, type, devs, price):
        self.store = {"black": 0, "white": 0}
        self.price = price
        self.type = type
        for k, v in devs.items():
            self.store[k] += v

    def add_dev(self, unt):
        #print("\n===  unt:", unt)
        for k, v in unt.items():
            self.store[k] += v
            print(f"adding\t{self.type}:\t{v}\t{k}")

    def del_dev(self, unt):
        for k, v in unt.items():
            if self.store[k] >= v:
                self.store[k] -= v
                print(f"removing\t{self.type}:\t{v}\t{k}")
            else:
                print(f"\n*** Attempt to remove {v} {self.type}: more then currently in stock, ignored ***")

def status():
    print(f"{Printer.type}s:\t{Printer.store['black']}\tblack,\t{Printer.store['white']}\twhite")
    print(f"{Scanner.type}s:\t{Scanner.store['black']}\tblack,\t{Scanner.store['white']}\twhite")
    print(f"{Xerox.type}es:\t{Xerox.store['black']}\tblack,\t{Xerox.store  ['white']}\twhite")

### stock initialisation
MyStorage = Storage({"printer": 0, "scanner": 0, "xerox": 0},{"printer": 0, "scanner": 0, "xerox": 0} )
Printer = Devices("printer", {"black": 0}, 2000)
Scanner = Devices("scanner", {"white": 0}, 10000)
Xerox   = Devices("xerox",   {"black": 0}, 12000)
print("\nInitial stock status:")
status()
print(f"Prices: printer - {Printer.price}, scanner - {Scanner.price}, xerox - {Xerox.price} RUB per unit\n")

### stock population: adding units
print("\nPopulating stock:")
Printer.add_dev({"black": 1})
Scanner.add_dev({"white": 2})
Xerox.add_dev({"black": 3})


print("\nStock population completed:")
status()

def menu_inp():
    print("\n*** Enter 4 options in one line, split by space  ('q' to quit):")
    print("device type   ('p'rinter, 's'canner,  'x'exrox)")
    print("needed action ('a'dd,     'r'emove)")
    print("device color  ('w'hite,   'b'lack)" )
    print("number of devices")
    req = input("==> ")
    return req

def check_inp(l):
    result = 'ok'
    if l[0] not in ("p", "s", "x") or l[1] not in ("a", "r") or l[2] not in ("w", "b"):
        print('\n*** Incorrect type, action or color, please retry...\n')
        result = 'ko'
    if not l[3].isnumeric():
        print('\n*** Please enter digit for number of devices...\n')
        result = 'ko'
    return result


while True:
    inp = menu_inp()
    if inp == 'q':
        break
    inp = inp.split()
    if len(inp) !=4:
        print(f"\n*** Please retry: enter 4 arguments or 'q' to quit")
        continue
    if check_inp(inp) != 'ok':
        continue
    if    inp[2] == "w": inp[2] = "white"
    else: inp[2] = "black"
    m = inp
    #print("\m ==>",m,"\n")
    if   m[0] == 'p' and m[1] == 'a': Printer.add_dev({m[2]: int(m[3])})
    elif m[0] == 'p' and m[1] == 'd': Printer.del_dev({m[2]: int(m[3])})
    elif m[0] == 's' and m[1] == 'a': Scanner.add_dev({m[2]: int(m[3])})
    elif m[0] == 's' and m[1] == 'r': Scanner.del_dev({m[2]: int(m[3])})
    elif m[0] == 'x' and m[1] == 'a': Xerox.add_dev  ({m[2]: int(m[3])})
    elif m[0] == 'x' and m[1] == 'r': Xerox.del_dev  ({m[2]: int(m[3])})
    status()

print("\nFinal stock status:")
status()
MyStorage.units["printer"] = Printer.store['black'] + Printer.store['white']
MyStorage.units["scanner"] = Scanner.store['black'] + Scanner.store['white']
MyStorage.units["xerox"]   = Xerox.store  ['black'] + Xerox.store  ['white']
p_values = MyStorage.units["printer"]*Printer.price
s_values = MyStorage.units["scanner"]*Scanner.price
x_values = MyStorage.units["xerox"]*Xerox.price
print (f'Total value printers:\t{p_values}\tRUB')
print (f'Total value scanners:\t{s_values}\tRUB')
print (f'Total value xeroxes:\t{x_values}\tRUB')
print (f'Total stock value:\t\t{p_values+s_values+x_values}\tRUB')
print("\nThank you and good luck !")
