# Documate: Automated Custom Document Generator
This is a python script for automating the document generation process. This script can be extremely effective for tasks where you need to create custom certificates or 1000 unique ID cards for your organization. I am providing a step-by-step instructions regarding how to use this script, incase you think it can provide you with any utility.

### Step 1: Open in Adobe Illustrator
Start by Opening your Target Document in Adobe Illustrator.

<img src="https://i.imgur.com/hCFSibU.png" width="400" height="300">


### Step 2: Make a List
Make an excel file "NameList'xlsx" with list of names you want to place in the target. Fill it up like in the picture. (or just copy stuff you need to put from your Google Sheets ;) )


<img src="https://i.imgur.com/bRDLLP1.png" width="400" height="300">


### Step 3: Show the script where you want text to be in
Draw a rectangle over the area where you want to place your text. (Area excluding stroke)

<img src="https://i.imgur.com/VOivlfc.png" width="600" height="400">


### Step 4: Adjusting the variables
Open the script with notepad or any other text editor, and set the proper variables from Adobe Illustrator


<img src="https://i.imgur.com/41cu2M1.png" width="800" height="400">

- Set 'name_list' to name of excel file containing list of text you want to write.
- Set 'target_file' to the image name where the text will be written to.
- You need to provide the script with the ttf format of the font you are willing to use. So, donwload and keep the font file in the same directory. Set 'font_file' to the name of font. In my case it is "Montserrat-ExtraBold.ttf"
- Set 'fs' to atlest 2x the font size you normally need to use in where you want to put text in. I needed somewhere around 50, so I put 10 times of that value here.


### Step 5: Run the Script.
Open the script in any IDE like Spyder or Jupyter Notebook/Lab and execute it.

<img src="https://i.imgur.com/ZRLyXE8.png" width="1000" height="600">


*__Credits: AUST Innovation & Design Club & everyone mentioned in this Name List.__*
