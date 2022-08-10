from prettytable import PrettyTable

table = PrettyTable()
# Using predefined class methods
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])

# Using / Updating Table attributes
table.align = "r"
print(table)
