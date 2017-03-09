from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup


def school_details(new_url):
    my_url = new_url

    # opening up the connection, grabbing the page
    newClient = uReq(my_url)
    new_page_html = newClient.read()
    newClient.close()

    # html parsing
    new_page_soup = soup(new_page_html, "html.parser")

    new_container = new_page_soup.findAll('td', {"width": "494"})

    # getting school_name, Afilliation_no, Addresss, Phone_no, email_id

    school_name = new_container[0].text.strip()
    affiliation_no = new_container[1].text.strip()
    state = new_container[2].text.strip()
    district = new_container[3].text.strip()
    postal_address = new_container[4].text.strip()
    phone_no = new_container[7].text.strip()
    email_id = new_container[10].text.strip()
    web_site = new_container[11].text.strip()
    year_of_foundation = new_container[12].text.strip()
    date_of_opening = new_container[13].text.strip()
    name_of_principal = new_container[14].text.strip()
    status_of_school = new_container[20].text.strip()
    type_of_affiliation = new_container[21].text.strip()
    affiliation_period_from = new_container[22].text.strip()
    affiliation_period_to = new_container[23].text.strip()
    name_of_trust_society_managing_committee = new_container[24].text.strip()

    # printing the data

    print '------------------------------------------------------------------------------------------------------------'
    print 'school_name    : ' + school_name
    print 'affiliation_no : ' + affiliation_no
    print 'Address        : ' + postal_address + ',' + district + ',' + state
    print 'phone_no       : ' + phone_no
    print 'email_id       : ' + email_id
    print 'web_site       : ' + web_site
    print 'year_of_foundation : ' + year_of_foundation
    print 'date_of_opening : ' + date_of_opening
    print 'name_of_principal : ' + name_of_principal
    print 'status_of_school  : ' + status_of_school
    print 'type_of_affiliation : ' + type_of_affiliation
    print 'affiliation_period_from : ' + affiliation_period_from
    print 'affiliation_period_to : ' + affiliation_period_to
    print 'name_of_trust_society_managing_committee : ' + name_of_trust_society_managing_committee
    print '------------------------------------------------------------------------------------------------------------'

    filename = "DETAILS.csv"
    f = open(filename, "a")
    f.write(
        school_name + "," + affiliation_no + "," + state + "," + district + "," + postal_address + "," + phone_no + "," + email_id + "," + web_site + "," + year_of_foundation + "," + date_of_opening + "," + name_of_principal + "," + status_of_school + "," + type_of_affiliation + "," + affiliation_period_from + "," + affiliation_period_to + "," + name_of_trust_society_managing_committee + "\n")

    f.close()
