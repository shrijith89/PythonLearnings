import prettytable

prettytable.PrettyTable

table = prettytable.PrettyTable()
table.add_column("name",["test01","test02","test03"])
table.add_column("place",["UK","US","Russia"])

print(table)