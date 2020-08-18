from selenium import webdriver
import time

##PhantomJS ayni klasore konulacak
browser = webdriver.Chrome()

sites = [] #linkler buraya
ctgs = [] # kategoriler buraya

doc = open("urllist" , "r")
content = doc.readlines()

for url in content:
	sites.append(url)
sites = [line.rstrip('\r\n') for line in content]

control = "https://fortiguard.com/webfilter?q="

j = int(0)
i = int(0)

##Ana Kategoriler ve Sub Kategoriler
adult = ["Abortion" , "Advocacy Organizations" , "Alcohol" , "Alternative Beliefs" , "Dating" , "Gambling" , "Lingerie and Swimsuit" , "Marijuana" , "Nudity and Risque" , "Other Adult Materials" , "Pornography" , "Sex Education" , "Sports Hunting and War Games" , "Tobacco" , "Weapons (Sales)"]
bandwith_consuming = ["File Sharing and Storage" , "Freeware and Software Downloads" , "Internet Radio and TV" , "Internet Telephony" , "Peer-to-peer File Sharing" , "Streaming Media and Download"]
gi_business = ["Armed Forces" , "Business" , "Charitable Organizations" , "Finance and Banking" , "General Organizations" , "Government and Legal Organizations" , "Information Technology" , "Information and Computer Security" , "Online Meeting" , "Remote Access" , "Search Engines and Portals" , "Secure Websites" , "Web Analytics" , "Web Hosting" , "Web-based Applications"]
gi_personal = ["Advertising" , "Arts and Culture" , "Auction" , "Brokerage and Trading" , "Child Education" , "Content Servers" , "Digital Postcards" , "Domain Parking" , "Dynamic Content" , "Education" , "Entertainment" , "Folklore" , "Games" , "Global Religion" , "Health and Wellness" , "Instant Messaging" , "Job Search" , "Meaningless Content" , "Medicine" , "News and Media" , "Newsgroups and Message Boards" , "Personal Privacy" , "Personal Vehicles" , "Personal Websites and Blogs" , "Political Organizations" , "Real Estate" , "Reference" , "Restaurant and Dining" , "Shopping" , "Social Networking" , "Society and Lifestyles" , "Sports" , "Travel" , "Web Chat" , "Web-based Email"]
pot_liable = ["Child Abuse" , "Discrimination" , "Drug Abuse" , "Explicit Violence" , "Extremist Groups" , "Hacking" , "Illegal , Unethical" , "Plagiarism" , "Proxy Avoidance"]
sec_risk = ["Dynamic DNS" , "Malicious Websites" , "Newly Observed Domain" , "Newly Registered Domain" , "Phishing" , "Spam URLs"]
unrated = ["Not Rated"]


with open("urllist","r+",encoding = "UTF-8") as file:
	for list_item in sites:
		if(len(list_item.split('|')) == 1):
			browser.get(control + str(list_item))
			time.sleep(3)
			getctg = browser.find_elements_by_xpath("/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/section/div[3]/div/div/h4")#kategori al
			for element in getctg:
				ctgs.append(element.text[10:])
				if(ctgs[j] in adult):
					print("{}|Adult-Mature|{}".format(list_item,ctgs[j]))
					file.write("{}|Adult-Mature|{}\n".format(list_item,ctgs[j]))
				elif(ctgs[j] in bandwith_consuming):
					print("{}|Bandwidth Consuming|{}".format(list_item,ctgs[j]))
					file.write("{}|Bandwidth Consuming|{}\n".format(list_item,ctgs[j]))
				elif(ctgs[j] in gi_business):
					print("{}|General Interest - Business|{}".format(list_item,ctgs[j]))
					file.write("{}|General Interest - Business|{}\n".format(list_item,ctgs[j]))
				elif(ctgs[j] in gi_personal):
					print("{}|General Interest - Personal|{}".format(list_item,ctgs[j]))
					file.write("{}|General Interest - Personal|{}\n".format(list_item,ctgs[j]))
				elif(ctgs[j] in pot_liable):
					print("{}|Potentially Liable|{}".format(list_item,ctgs[j]))
					file.write("{}|Potentially Liable|{}\n".format(list_item,ctgs[j]))
				elif(ctgs[j] in sec_risk):
					print("{}|Security Risk|{}".format(list_item,ctgs[j]))
					file.write("{}|Security Risk|{}\n".format(list_item,ctgs[j]))
				elif(ctgs[j] in unrated):
					print("{}|Unrated|{}".format(list_item,ctgs[j]))
					file.write("{}|Unrated|{}\n".format(list_item,ctgs[j]))
				j+=1
		else:
			print(list_item)
			file.write(list_item + "\n")

browser.close()