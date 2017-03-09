import string
import File_2

key_words = list(string.ascii_letters)

# creating the required CSV file to store the data
filename = "DETAILS.csv"
f = open(filename, "w")

headers = "School_Name, Affiliation_no, State, District, Postal_address, Phone_no, Email_id, Web_site, Year_of_foundation, Date_of_opening, Name_of_Principal, Status_of_affiliation, Type_of_affiliation, Affiliation_from, Affiliation_to, Name_of_trust_society_managing_committee\n"

f.write(headers)
f.close()

for key in key_words:
    print key
    a = key
    File_2.search_key(a)
