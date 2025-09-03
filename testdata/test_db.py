import random

# Sample names to rotate through
names = ["Collins Natala", "Amina Wanjiku", "Brian Otieno", "Faith Mwangi", "Kevin Kiptoo", "Lilian Njeri"]

# Function to generate random ID and phone number
def generate_entry(index):
    return {
        "name": names[index % len(names)],
        "id_number": str(random.randint(10000000, 99999999)),
        "phone_number": "07" + str(random.randint(10000000, 99999999))
    }

# Generate list with 6 unique entries
records = [generate_entry(i) for i in range(6)]
print(records)
# Print result
#for entry in data:
# records = []
# for i in range(6):
#     print(i)
#     records.append(generate_entry(i))
# print(records)
