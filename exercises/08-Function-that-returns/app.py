def dollar_to_euro(dollar_value):
	return dollar_value * 0.89

def euro_to_yen(euro_value):
	return euro_value * 124.15

new_value_eu = dollar_to_euro(137)
new_value_yen = euro_to_yen(new_value_eu)

print("137 dollars are equal to " + str(new_value_yen) + " yenes.")