from wiki import article_metadata, ask_search, ask_advanced_search
import datetime
import time

# FOR ALL OF THESE FUNCTIONS, READ THE FULL INSTRUCTIONS.

# 1) 
#
# Function: keyword_to_titles
#
# Parameters:
#   metadata - 2D list of article metadata containing 
#              [title, author, timestamp, article length, keywords]
#              for each article
#
# Return: dictionary mapping keyword to list of article titles in which the
#         articles contain keyword
#
# Example return value:
# {
#   'keyword': ['article title', 'article title 2']
#   'another_keyword': ['article title 2', 'article title 3']
# }
def keyword_to_titles(metadata):
    new_metadata = {}
    for i in range(len(metadata)):
        new_list = []
        for keyword in metadata[i][4]:
            if keyword in new_metadata and metadata[i][0] not in new_metadata[keyword]:
                new_list = new_metadata[keyword] + [metadata[i][0]]
            else:
                new_list = [] + [metadata[i][0]]
            new_metadata[keyword] = new_list
    return new_metadata
 
# 2)
#
# Function: title_to_info
#
# Parameters:
#   metadata - 2D list of article metadata containing 
#              [title, author, timestamp, article length, keywords]
#              for each article
#
# Return: dictionary mapping article title to a dictionary with the following
#         keys: author, timestamp, length of article. It may be assumed that
#         the input data has unique article titles.
#
# Example return value:
# {
#   'article title': {'author': 'some author', 'timestamp': 1234567890, 'length': 2491}
#   'article title 2': {'author': 'another author', 'timestamp': 9876543210, 'length': 85761}
# }
def title_to_info(metadata):
    new_metadata = {}
    for i in range(len(metadata)):
        sort = {}
        sort['author'] = metadata[i][1]
        sort['timestamp'] = metadata[i][2]
        sort['length'] = metadata[i][3]
        new_metadata[metadata[i][0]] = sort
    return new_metadata

# 3) 
#
# Function: search
#
# Parameters:
#   keyword - search word to look for
#   keyword_to_titles - dictionary mapping keyword to a list of all article
#                       titles containing that keyword
#
# Return: list of titles with articles containing the keyword, case-sensitive
#         or an empty list if none are found
def search(keyword, keyword_to_titles):
    for key in keyword_to_titles:
        if key == keyword:
            return keyword_to_titles[key]
    return []
    
'''
Functions 4-8 are called after searching for a list of articles containing the user's keyword.
'''
# 4) 
#
# Function: article_length
#
# Parameters:
#   max_length - max character length of articles
#   article_titles - list of article titles resulting from basic search
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: list of article titles from given titles for articles that do not
#         exceed max_length number of characters
def article_length(max_length, article_titles, title_to_info):
    new_list = []
    for article in article_titles:
        if title_to_info[article]['length'] <= max_length:
            new_list.append(article)
    return new_list

# 5) 
#
# Function: key_by_author
#
# Parameters:
#   article_titles - list of article titles resulting from basic search
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: dictionary that maps author to a list of all articles titles written
#         by that author
#
# Example return value:
# {
#   'author': ['article title', 'article title 2'],
#   'another author': ['article title 3']
# }
def key_by_author(article_titles, title_to_info):
    sort_authors = {}
    for i in range(len(article_titles)):
        new_list = []
        if title_to_info[article_titles[i]]['author'] in sort_authors and article_titles[i] not in sort_authors[title_to_info[article_titles[i]]['author']]:
            new_list = sort_authors[title_to_info[article_titles[i]]['author']] + [article_titles[i]]
        else:
            new_list = [] + [article_titles[i]]
        sort_authors[title_to_info[article_titles[i]]['author']] = new_list
    return sort_authors

# 6) 
#
# Function: filter_to_author
#
# Parameters:
#   author - author name to filter results to
#   article_titles - list of article titles resulting from basic search
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: list of article titles from the initial search written by the author
#         or an empty list if none.
def filter_to_author(author, article_titles, title_to_info):
    new_results = []
    for article in article_titles:
        if title_to_info[article]['author'] == author:
            new_results = new_results + [article]
    return new_results

# 7) 
#
# Function: filter_out
#
# Parameters:
#   keyword - a second keyword to use to filter out results
#   article_titles - list of article titles resulting from basic search
#   keyword_to_titles - dictionary mapping keyword to a list of all article
#                       titles containing that keyword
#
# Return: list of articles from the basic search that do not include the
#         new keyword
def filter_out(keyword, article_titles, keyword_to_titles):
    new_results = []
    if keyword not in keyword_to_titles:
        return article_titles
    for article in article_titles:
        if article not in keyword_to_titles[keyword]:
            new_results.append(article)
    return new_results

# 8) 
#
# Function: articles_from_year
#
# Parameters:
#   year - year (ex: 2009) to filter articles to
#   article_titles - list of article titles resulting from basic search
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: list of article titles from the basic search that were published
#         during the provided year.
def articles_from_year(year, article_titles, title_to_info):
    new_results = []
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    unix_timestamp1 = time.mktime(start_date.timetuple())
    unix_timestamp2 = time.mktime(end_date.timetuple())
    for article in article_titles: 
        if title_to_info[article]['timestamp'] >= int(unix_timestamp1) and title_to_info[article]['timestamp'] <= int(unix_timestamp2):
            new_results = new_results + [article]
    return new_results

# Prints out articles based on searched keyword and advanced options
def display_result():
    # Preprocess all metadata to dictionaries
    keyword_to_titles_dict = keyword_to_titles(article_metadata())
    title_to_info_dict = title_to_info(article_metadata())
    
    # Stores list of articles returned from searching user's keyword
    articles = search(ask_search(), keyword_to_titles_dict)

    # advanced stores user's chosen advanced option (1-7)
    # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
        # value stores max length of articles
        # Update articles to contain only ones not exceeding the maximum length
        articles = article_length(value, articles, title_to_info_dict)
    if advanced == 2:
        # Update articles to be a dictionary keyed by author
        articles = key_by_author(articles, title_to_info_dict)
    elif advanced == 3:
        # value stores author name
        # Update article metadata to only contain titles and timestamps
        articles = filter_to_author(value, articles, title_to_info_dict)
    elif advanced == 4:
        # value stores a second keyword
        # Filter articles to exclude those containing the new keyword.
        articles = filter_out(value, articles, keyword_to_titles_dict)
    elif advanced == 5:
        # value stores year as an int
        # Update article metadata to contain only articles from that year
        articles = articles_from_year(value, articles, title_to_info_dict)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

if __name__ == "__main__":
    display_result()
