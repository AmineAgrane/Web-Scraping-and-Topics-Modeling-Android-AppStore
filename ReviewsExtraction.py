import csv
from tqdm import tqdm
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException




def ExtractReviews(url, number_of_reviews):
    """
    Take the android app link and the number of reviews to scrape
    """
    i = 0
    num_loop = int(number_of_reviews / 300) 
    browser = webdriver.Chrome(executable_path="./web_driver/chromedriver.exe")
    browser.maximize_window()
    browser.get(url)
    ancre = browser.find_element_by_xpath('/html/body/div[1]/div[4]/div/c-wiz/div/div[2]/div/a[1]')

    pbar = tqdm(total = num_loop)

    while i <= num_loop:
        try:
            plus = browser.find_element_by_xpath('/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div[2]/div/span/span')
            plus.click()
            i+=1
            pbar.update(1)
        except Exception as e:
            browser.execute_script("arguments[0].scrollIntoView();", ancre) 

    try:
        bs= BeautifulSoup(browser.page_source, 'html.parser')
        liste_test = get_reviews(bs, number_of_reviews); 
        liste = liste_test
    except Exception as e:
        exit(-1)
    else:
        liste = liste_test.copy()

    browser.close()
    return liste


def export_csv(file_name, tuples_list):
    """
    Export a list of tuples data into a csv_file 
    """
    with open('scraped_reviews/'+file_name, 'w', encoding='utf-8') as file:
        output_csv = csv.writer(file)
        output_csv.writerow(['user_name','date', 'num_stars', 'review', 'num_likes', 'user_name_answer', 'date_answer', 'answer'])
        for review in tuples_list:
            output_csv.writerow(review)



def get_reviews(bs, number_of_reviews):
    """ 
    Parse raw data and store reviews in an organised way (list of tuples) 
    """
    print("Starting data parsing")
    liste = []
    all_reviews = bs.find_all(jscontroller="H6eOGe")
    for review in all_reviews:
        T = ()
        user_review, date, stars, user_name, num_likes = '', '', '', '', ''
        user_review = full_reviews(review)
        date = review.find(class_='p2TkOb').get_text()
        stars = review.find(class_='pf5lIe').div['aria-label'][6]
        user_name = review.find(class_='X43Kjb').get_text()
        num_likes = review.find(class_='jUL89d y92BAb').get_text()
        user_name_answer, date_answer, answer = infos_answer(review)
        T = (user_name, date, stars, user_review, num_likes, user_name_answer, date_answer, answer)
        liste.append(T)
    return liste[:number_of_reviews]



def infos_answer(review):
    """
    Return all the element of ansewer : the user_name, the date, and the answer itself.
    """
    tag = review.find(class_="LVQB0b")
    user_name_answer, date_answer, answer = '', '', ''
    if tag is not None:
        user_name_answer = tag.find(class_="X43Kjb").get_text()
        date_answer = tag.find(class_="p2TkOb").get_text()
        answer = str(tag.contents[2])
    return (user_name_answer, date_answer, answer)



def full_reviews(review):
    """
    Return the full review of a user.
    In the case of a long review, we click on the button "show more" to get the user's complete review 
    """
    review1 = review.find(jsname='bN97Pc').get_text()
    review2 = review.find(jsname='fbQN7e').get_text()
    len1, len2 = len(review1)-11, len(review2)
    return review1 if len1>len2 else review2



if __name__ == "__main__" :

    # HTML link of the android application. 
    android_app_html_link = "https://play.google.com/store/apps/details?id=com.whatsapp"

    # language of the reviews : en, fr, etc
    lang ="en"

    # compute the final link we're going to use to scrape the reviews.
    final_link = '{}&hl={}{}'.format(android_app_html_link, lang, '&showAllReviews=true')
    print(final_link)


    # name of the output csv to store the scrapped data.
    csv_name = "whatsapp.csv"

    export_csv(csv_name, ExtractReviews(final_link, 10000))

