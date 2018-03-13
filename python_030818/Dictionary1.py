# Q1.1 Print Elizabeth's phone number. Q1.2 Add a entry to the dictionary: Kareem's number is 938-489-1234.
# Q1.3 Delete Alice's phone entry.
# Q1.4 Change Bob's phone number to '968-345-2345'.
# Q1.5 Print all the phone entries.


phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print(phonebook_dict['Elizabeth'])
phonebook_dict['Kareem'] = '938-489-1234'
print(phonebook_dict['Kareem'])
del phonebook_dict['Alice']
phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict['Bob']
print(phonebook_dict.items())