
# coding: utf-8

# In[713]:


from bs4 import BeautifulSoup #import beautifulsoup and csv library
import csv
filename = "microsoft.txt"
file = open(filename, "r") #open microsoft txt file


# In[714]:


#initalize variable and list
section = 0 
subsections = []

#write for loop to write each line into subsections list
#when string is found, append line into list
for line in file:
   if section == 1:
    subsections.append(line)
   if '1A_RISK_FACTORS' in line: #find '1A_RISK_FACTORS' language
    item_title = line
    section = 1


# In[715]:


#each successive index is the next column for table
item_title = BeautifulSoup(item_title).a['name'].replace('_',' ').title() #convert to lowercase except first letter
introduction = BeautifulSoup(subsections[0]).p.text
section_title = BeautifulSoup(subsections[1]).p.text
subsection_title = BeautifulSoup(subsections[2]).p.text
subsection_text = BeautifulSoup(subsections[3]).p.text
subsection_word_count = len(subsection_text.split())


# In[716]:


#convert specific uppercase letters in 'item_title' to lowercase
indices = set([6, 8, 13])
s = item_title
item_title = ("".join(c.lower() if i in indices else c for i, c in enumerate(s)))


# In[717]:


#initalize list
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("apple.txt"))

subsections = []

for line in soup.find_all('div'):
    subsections.append(line.text)


# In[718]:


# replace non-ASCII tick with apostrophe
def removeNonAscii(s): 
    return "".join(i for i in s if ord(i)<128)


# In[719]:


#item title is found at 85
apple_item_title = subsections[85] + subsections[86]
apple_item_title = apple_item_title.replace(u'\xa0', u' ') #remove unwanted characters

apple_introduction = subsections[87] + subsections[88] + subsections[89]
apple_introduction = removeNonAscii(apple_introduction.replace(u'\xa0', u' ')) 

apple_subsection_title = subsections[90]
apple_subsection_title = removeNonAscii(apple_subsection_title.replace(u'\xa0', u' '))


apple_subsection_text = subsections[91] + " " + subsections[92]
apple_subsection_text = removeNonAscii(apple_subsection_text.replace(u'\xa0', ' '))

apple_subsection_word_count = len(apple_subsection_text.split())


# In[720]:


#convert specific uppercase letters in 'apple_item_title' to lowercase
indices = set([6,9,14])
s = apple_item_title
apple_item_title = ("".join(c.lower() if i in indices else c for i, c in enumerate(s)))

#remove '.'
apple_item_title = apple_item_title.replace(".", "")


# In[721]:


#create table / dictionary, write to csv
with open('test.csv', 'w') as csvfile:
    fieldnames = ['Company','Item title','Introduction','Section title','Subsection title','Subsection text','Subsection word count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Company': 'Microsoft', 'Item title': item_title, 'Introduction': introduction,'Section title':section_title,'Subsection title':subsection_title,'Subsection text':subsection_text,'Subsection word count':subsection_word_count})
    writer.writerow({'Company': 'Apple', 'Item title': apple_item_title, 'Introduction': apple_introduction,'Section title':'','Subsection title':apple_subsection_title,'Subsection text':apple_subsection_text,'Subsection word count':apple_subsection_word_count})

