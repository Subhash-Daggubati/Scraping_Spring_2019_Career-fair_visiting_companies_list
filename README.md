# Scraping_Spring_2019_Career-fair_visiting_companies_list
Problem: 

Before every career fair the list of registered companies will be available on the university career services website. But in-order to see
more details (like "available positions", "Description of company", "Work-Authorization Requirements" etc) you have to click on each of the 
company's link and the details will be opened in a new browser window or tab. To short-list the companies it usually takes alot of time. 

Solution: 

If we can extract all these details to Excel sheet, it is really easy to filter the companies based on any individual's criteria. 
Ex: Being an international student I need to target the companies which are accepting "All Work Authorization" students. This can be done 
simply in Excel by adding filter to the Work Authorization column. 

Implementation: 

So, I have decided to put my selenium automation skills and python skills together to extract all this information into a excel sheet and distributed it to all my fellow MIS students. 

This script takes approximately 2-3 minutes to extract the details of 250 + comapnies. Before this solution has been implemented it usually takes 2-3 minutes to open a company details, note down the details if they match your requirements. 

Limitations:

1)This solution has been implemented to re-use the same script for upcoming career fairs. But like any other selenium script, the script will not work with any updates to the website structure. 
2) For Fall 2019 career fair, the university has updated it's website structre and they have provided a feature to extract all these details into an excel sheet just with a button click. 
