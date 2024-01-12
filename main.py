# create a product and price for three items
p1_name, p1_price = 'Item 1', 49.95
p2_name, p2_price = 'Item 2', 579.99
p3_name, p3_price = 'Item 3', 124.89

# create a company name and information
company_name = 'Company Name, inc.'
company_address = 'XXX Roadname St.'
company_city = 'Areaname, XX'

# declare ending message
message = 'Thanks for shopping with us today!'

# create a top border
print('*' * 50)

# print company information first using format
print('*\t\t{}\t\t *'.format(company_name.title()))
print('*\t\t{}\t\t *'.format(company_address.title()))
print('*\t\t{}\t\t\t *'.format(company_city.title()))

# print a line between sections
print('*' + '=' * 48 + '*')

# print out header for section of items
print('*\tProduct Name\tProduct Price\t\t *')

# create a print statement for each item
print('*\t{}\t\t${}\t\t\t *'.format(p1_name.title(), p1_price))
print('*\t{}\t\t${}\t\t\t *'.format(p2_name.title(), p2_price))
print('*\t{}\t\t${}\t\t\t *'.format(p3_name.title(), p3_price))

# print a line between sections
print('*' + '=' * 48 + '*')

# print out header for section of total
print('*\t\t\tTotal\t\t\t *')

# calculate total price and print out
total = p1_price + p2_price + p3_price
print('*\t\t\t${}\t\t\t *'.format(total))

# print a line between sections
print('*' + '=' * 48 + '*')

# output thank you message
print('*\t\t\t\t\t\t *\n*\t{}\t *\n*\t\t\t\t\t\t *'.format(message))

# create a bottom border
print('*' * 50)