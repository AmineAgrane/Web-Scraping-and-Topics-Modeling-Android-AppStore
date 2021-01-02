# Introduction
Monitoring and responding to customer feedback is an essential first step, yet companies don't always take the time to analyze these valuable elements. Indeed, who better than a person who has had a positive or negative experience with a product or service to give their opinion? Today, with the explosion of the Internet, social networks and smartphones, the totality of user opinions represents an important mass of information.

 In the case of mobile applications, every day millions of users share their thoughts and criticisms on Google Play and the Apple Store. Users then express their feelings and feedback after using the application. Faced with this mass of data, traditional marketing studies and techniques are now outdated. New techniques must be adopted to automate and optimize the analysis of user feedback...

Users reviews allow a better understanding of the consumption habits and uses of the products offered by the company. They also highlight the positive and negative points of the customer journey. They are therefore very valuable data that enriches the company with knowledge about its current and future customers.

This project consist in 3 distinct parts : 
- Web Scrapping 
- Sentiment Analysis
- Topics Modeling


## Web Scrapping :
The first step in our project was extraction of user data from the Google Play Store. This will be done using Web Scrapping. The objective is to extract the content of a page from a site in a structured way. The main interest of Web Scrapping is to be able to harvest content from a website, which cannot be copied and pasted without distorting the very structure of the document. For this project, I wrote a Python script to perform Scrapping of user data and storage of these data in a structured form, which is a csv file.

<p align="center">
   <img src="https://github.com/AmineAgrane/Web-Scraping-and-Topics-Modeling-Android-AppStore/blob/main/doc/webscrapping.png" height="300" align="center"/>
</p>

The web scraping script was achieved using the [BeautifulSoup ](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Selenium ](https://selenium-python.readthedocs.io/) modules.
The extracted data are stored in the "scraped_reviews" folder. For example, I scraped ***10.000***  reviews from Android applications like **Instagram**, **Facebook**, **Netflix**, etc

<p align="center">
   <img src="https://github.com/AmineAgrane/Web-Scraping-and-Topics-Modeling-Android-AppStore/blob/main/doc/scrapped_reviews.png" height="200" align="center"/>
</p>

There is 7 columns
## Topics Modeling with Latent Dirichlet Allocation :
Topîc modeling is a text mining model, using unsupervised and supervised statistical machine learning techniques to identify themes in a corpus or large amount of unstructured text. From a collection of documents, the model will group words into word clusters, identifying topics, through a process based on similarity.

Latent Dirichlet allocation is a popular model for fitting a subject model. It treats each document as a mixture of topics and each topic as a mixture of words. This allows documents to "overlap" in terms of content, rather than being separated into distinct groups, in a way that reflects typical natural language usage.

<p align="center">
   <img src="https://github.com/AmineAgrane/Web-Scraping-and-Topics-Modeling-Android-AppStore/blob/main/doc/lda.jpg" height="400" align="center"/>
</p>

## 2-dimensional visualization of the Topics Modeling model :
We can perform a two-dimensional visualization of the topics extracted from the scrapped dataset. To do so, we use the  library which is available on Python. [pyLDAvis ](https://github.com/bmabey/pyLDAvis) is a Python library for interactive LDA visualization. Below,we can see a figure which is a screenshot of the 2D visualization of the LDA model I implemented:

<p align="center">
   <img src="https://github.com/AmineAgrane/Web-Scraping-and-Topics-Modeling-Android-AppStore/blob/main/doc/visualize_topics.PNG" height="600" align="center"/>
</p>

The size of the circle represents the importance of each topic on the whole corpus, the distance between the center of the circles indicates the similarity between the topics. For each topic, the histogram on the right side lists the 30 most relevant terms. LDA helped me to extract 7 main topics.
om/questions/4823468/store-comments-in-markdown-syntax)
