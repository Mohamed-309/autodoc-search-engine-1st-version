#Get symptoms from user
#loop through all the anchor links of the website
#compare between symptoms and links
#get the most disease that has common symptoms
#print the best medicine for this disease
#save the report on the PC
#https://www.nhsinform.scot/illnesses-and-conditions/a-to-z/

from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date
import urllib.parse
import urllib.error
import urllib.request
import ssl
import re
import time

Hello_message = '''Welcome to our search engine, our search engine has 3 main
research types, you can search with your symptoms and see if it's match any of most world diseases's symptoms,
 also you can search for treatment of any symptom you have like headache or you can search for any disease and
 get information about it, after finishing this test you csn also save the report as text file '''

instructions = '''Try to follow this instructions to get the best results:
1-Try to put more than one symptom to get more accurate results
2-Try to use medical name for each of your symptoms
3-Make sure you are connected to the network while searching
4-if you did not got results, make sure that you are connected to the network or try to change
the name of symptoms'''




class Main:
    #####################################################################################
    #####################################################################################
    def __init__(self):
        print(Hello_message)
        time.sleep(1)
        print()
        print(instructions)
        time.sleep(1)
        print()
        self.choice()

    #####################################################################################
    #####################################################################################
    def choice(self):
        while True:
            search_type = input("1-Match my symptoms to disease\n"
                                 "2-Search for medicine to my symptoms\n"
                                "3-search with the name of disease\n\n"
                                "Enter the number of your choice: ")
            time.sleep(1)

            try:
                if int(search_type) == 1:
                    self.Match_disease()
                elif int(search_type) == 2:
                    self.medicine_symptom()
                elif int(search_type) == 3:
                    self.disease_name()
                else:
                    print("Enter number between 1 and 3")
                    time.sleep(1)
            except ValueError:
                print("Invalid input, choose number from the above")
                print()
                time.sleep(1)
    #####################################################################################
    #####################################################################################
    def Match_disease(self):
        while True:
            lst_1 = list()
            lst_2 = list()
            lst_3 = list()
            lst_4 = list()
            lst_5 = list()
            url = 'https://www.nhsinform.scot/illnesses-and-conditions/a-to-z/'
            try:
                num_symp = int(input("Enter number of symptoms you will search with:"))
                time.sleep(1)
                for i in range(num_symp):
                    symptom = input("Enter symptom:")
                    lst_1.append(symptom)
                print("please wait few minutes.......")
                    ###################################################################
                    ###################################################################
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                # enter and open url
                html = urllib.request.urlopen(url, context=ctx).read()
                soup = BeautifulSoup(html, 'html.parser')
                tags = soup('a')

                # loop through all <a> tags and
                #get the link and append all of them in a list
                for tag in tags:
                    link = tag.get('href', None)
                    lst_2.append(link)
                for l in lst_2:
                    sub_link = re.findall('^/illnesses-and-conditions/a-to-z/(\S+)', l)
                    for i in sub_link:
                        if len(i) > 1:
                            lst_3.append(i)
                        else:
                            continue
                lst_3.__delitem__(115)
                lst_3.__delitem__(254)
                for li in lst_3[:10]:
                    title = re.findall('.*/(.*)/', li)
                    sub_url = url+li
                    html_2 = urllib.request.urlopen(sub_url, context=ctx).read().decode()
                    soup_1 = BeautifulSoup(html_2,'html.parser')
                    soup_2 = soup_1.text
                    for symp in lst_1:
                        if symp in soup_2:
                            lst_5.append(title[0])
                            lst_4.append(soup_2)
                            print(title[0])
                            print("=================================================================================")
                            print(soup_2)
                            print("=================================================================================")
                            continue
                        else:
                            continue

                choice_save = input("Do you want to save the results in a file in the same directory of the program\n"
                                            "Y: yes please\n"
                                            "N: no i just want to close\n"
                                            "Enter your choice:")
                if choice_save == "Y" or "y":
                    fh = open("autodoc result.txt", 'w+')
                    for l in range(len(lst_5) - 1):
                        fh.write(lst_5[l])
                        fh.writelines("==============================================================================================")
                        fh.writelines("==============================================================================================")
                        fh.writelines("==============================================================================================")
                    for i in range(len(lst_4)-1):
                        fh.write(lst_4[i])

                    fh.close()
                elif choice_save =="N" or "n":
                    print("Thanks for using autodoc, you can read your report now")
                    print("====================================START============================================")
                    break
                else:
                    print("wrong choice")


            except ValueError:
                print("something went error, check if you inserted the values in good shape and try again\n\n")
                print("====================================START============================================")
                time.sleep(2)

    #####################################################################################
    #####################################################################################
    def medicine_symptom(self):
        while True:
            lst_2 = list()
            lst_3 = list()
            lst_4 = list()
            lst_5 = list()
            symp_names = dict()
            try:
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                symptom = input("enter symptom you want to search for: ")
                url = 'https://www.nhsinform.scot/symptoms-and-self-help/a-to-z/'
                html = urllib.request.urlopen(url, context=ctx)
                soup = BeautifulSoup(html, 'html.parser')
                tags = soup('a')
                for tag in tags:
                    link = tag.get('href', None)
                    lst_2.append(link)
                for li in lst_2:
                    symptoms_links = re.findall('^/symptoms-and-self-help/a-to-z/(\S+)', li)
                    for i in symptoms_links:
                        if len(i) > 1:
                            lst_3.append(i)
                        else:
                            continue
                for sub_link in lst_3:
                    title = re.findall('.*/(.*)/', sub_link)
                    title_text = title[0]
                    symp_names[title_text] = sub_link
                for it in symp_names:
                    if symptom == it or symptom in it:
                        add_link = symp_names[it]
                        lst_4.append(add_link)
                        break
                    else:
                         continue
                if len(lst_4) == 1:
                    sub_url = url + lst_4[0]
                    html_2 = urllib.request.urlopen(sub_url, context=ctx)
                    soup_1 = BeautifulSoup(html_2, 'html.parser')
                    soup_2 = soup_1.text
                    today = date.today()
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print("Today's date in Egypt:", today)
                    print("Current Egyptian Time:", current_time)
                    print("result for searching for", symptom)
                    print(soup_2)
                else:continue
                choice_save = input("Do you want to save the results in a file in the same directory of the program\n"
                                            "Y: yes please\n"
                                            "N: no i just want to close\n"
                                    "Enter choice: ")
                if choice_save == "Y" or "y":
                    fh = open("autodoc result.txt", 'w+')
                    fh.write(str(today))
                    fh.write(str(current_time))
                    fh.write(soup_2)
                    fh.close()
                    print("==================START===================")
                elif choice_save == "N" or "n":
                    print("Thanks for using autodoc, you can read you results now")
                else:
                    pass

            except ValueError:
                print("error occurred, please try again")
                print("==================START===================")
    #####################################################################################
    #####################################################################################
    def disease_name(self):
        while True:
            try:
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                url = "https://en.wikipedia.org/wiki/"
                disease_name = input("enter name of disease you want to search for")
                sub_url = url + disease_name
                html = urllib.request.urlopen(sub_url, context=ctx)
                soup = BeautifulSoup(html, 'html.parser')
                soup_2 = soup.text
                print(soup_2)
            except urllib.error.URLError as e:
                print(str(e))
                print("==================START===================")
if __name__ == '__main__':
    Main()
