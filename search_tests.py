from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)

    def test_keyword_to_titles(self):
        metadata = [['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']], ['Black dog (ghost)', 'Pegship', 1220471117, 14746, ['black', 'dog', 'found', 'the', 'folklore', 'some', 'and', 'often', 'said', 'with', 'devil', 'described', 'its', 'was', 'death', 'has', 'large', 'eyes', 'sometimes', 'such', 'shuck', 'also', 'are', 'dogs', 'have', 'been', 'this', 'were', 'way', 'that', 'barghest', 'they', 'may', 'for', 'known', 'night', 'them', 'from', 'other', 'padfoot', 'skriker', 'church', 'grim', 'not', 'can', 'form', 'england', 'being', 'who', 'his', 'when', 'hounds', 'appeared', 'around', 'ghostly', 'story', 'hound', 'near', 'haunted', 'named', 'which', 'area', 'haunt', 'heard', 'omen', 'seen', 'haunts', 'had', 'name', 'but', 'man', 'village', 'would', 'one', 'there', 'home', 'any', 'where', 'through', 'old', 'legend', 'before', 'their', 'people', 'another', 'like', 'then', 'usually', 'local', 'will']]]
        expected_keyword_to_titles_results = {'edogawa': ['Edogawa, Tokyo'], 'the': ['Edogawa, Tokyo', 'Black dog (ghost)'], 'with': ['Edogawa, Tokyo', 'Black dog (ghost)'], 'and': ['Edogawa, Tokyo', 'Black dog (ghost)'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo'], 'black': ['Black dog (ghost)'], 'dog': ['Black dog (ghost)'], 'found': ['Black dog (ghost)'], 'folklore': ['Black dog (ghost)'], 'some': ['Black dog (ghost)'], 'often': ['Black dog (ghost)'], 'said': ['Black dog (ghost)'], 'devil': ['Black dog (ghost)'], 'described': ['Black dog (ghost)'], 'its': ['Black dog (ghost)'], 'was': ['Black dog (ghost)'], 'death': ['Black dog (ghost)'], 'has': ['Black dog (ghost)'], 'large': ['Black dog (ghost)'], 'eyes': ['Black dog (ghost)'], 'sometimes': ['Black dog (ghost)'], 'such': ['Black dog (ghost)'], 'shuck': ['Black dog (ghost)'], 'also': ['Black dog (ghost)'], 'are': ['Black dog (ghost)'], 'dogs': ['Black dog (ghost)'], 'have': ['Black dog (ghost)'], 'been': ['Black dog (ghost)'], 'this': ['Black dog (ghost)'], 'were': ['Black dog (ghost)'], 'way': ['Black dog (ghost)'], 'that': ['Black dog (ghost)'], 'barghest': ['Black dog (ghost)'], 'they': ['Black dog (ghost)'], 'may': ['Black dog (ghost)'], 'for': ['Black dog (ghost)'], 'known': ['Black dog (ghost)'], 'night': ['Black dog (ghost)'], 'them': ['Black dog (ghost)'], 'from': ['Black dog (ghost)'], 'other': ['Black dog (ghost)'], 'padfoot': ['Black dog (ghost)'], 'skriker': ['Black dog (ghost)'], 'church': ['Black dog (ghost)'], 'grim': ['Black dog (ghost)'], 'not': ['Black dog (ghost)'], 'can': ['Black dog (ghost)'], 'form': ['Black dog (ghost)'], 'england': ['Black dog (ghost)'], 'being': ['Black dog (ghost)'], 'who': ['Black dog (ghost)'], 'his': ['Black dog (ghost)'], 'when': ['Black dog (ghost)'], 'hounds': ['Black dog (ghost)'], 'appeared': ['Black dog (ghost)'], 'around': ['Black dog (ghost)'], 'ghostly': ['Black dog (ghost)'], 'story': ['Black dog (ghost)'], 'hound': ['Black dog (ghost)'], 'near': ['Black dog (ghost)'], 'haunted': ['Black dog (ghost)'], 'named': ['Black dog (ghost)'], 'which': ['Black dog (ghost)'], 'area': ['Black dog (ghost)'], 'haunt': ['Black dog (ghost)'], 'heard': ['Black dog (ghost)'], 'omen': ['Black dog (ghost)'], 'seen': ['Black dog (ghost)'], 'haunts': ['Black dog (ghost)'], 'had': ['Black dog (ghost)'], 'name': ['Black dog (ghost)'], 'but': ['Black dog (ghost)'], 'man': ['Black dog (ghost)'], 'village': ['Black dog (ghost)'], 'would': ['Black dog (ghost)'], 'one': ['Black dog (ghost)'], 'there': ['Black dog (ghost)'], 'home': ['Black dog (ghost)'], 'any': ['Black dog (ghost)'], 'where': ['Black dog (ghost)'], 'through': ['Black dog (ghost)'], 'old': ['Black dog (ghost)'], 'legend': ['Black dog (ghost)'], 'before': ['Black dog (ghost)'], 'their': ['Black dog (ghost)'], 'people': ['Black dog (ghost)'], 'another': ['Black dog (ghost)'], 'like': ['Black dog (ghost)'], 'then': ['Black dog (ghost)'], 'usually': ['Black dog (ghost)'], 'local': ['Black dog (ghost)'], 'will': ['Black dog (ghost)']}
        metadata2 = [['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']]]
        expected_keyword_to_titles_results2 = {'edogawa': ['Edogawa, Tokyo'], 'the': ['Edogawa, Tokyo'], 'with': ['Edogawa, Tokyo'], 'and': ['Edogawa, Tokyo'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo']}

        self.assertEqual(keyword_to_titles(metadata), expected_keyword_to_titles_results)
        self.assertEqual(keyword_to_titles([]), {})
        self.assertEqual(keyword_to_titles(metadata2), expected_keyword_to_titles_results2)

    def test_title_to_info(self):
        metadata = [['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']], ['Black dog (ghost)', 'Pegship', 1220471117, 14746, ['black', 'dog', 'found', 'the', 'folklore', 'some', 'and', 'often', 'said', 'with', 'devil', 'described', 'its', 'was', 'death', 'has', 'large', 'eyes', 'sometimes', 'such', 'shuck', 'also', 'are', 'dogs', 'have', 'been', 'this', 'were', 'way', 'that', 'barghest', 'they', 'may', 'for', 'known', 'night', 'them', 'from', 'other', 'padfoot', 'skriker', 'church', 'grim', 'not', 'can', 'form', 'england', 'being', 'who', 'his', 'when', 'hounds', 'appeared', 'around', 'ghostly', 'story', 'hound', 'near', 'haunted', 'named', 'which', 'area', 'haunt', 'heard', 'omen', 'seen', 'haunts', 'had', 'name', 'but', 'man', 'village', 'would', 'one', 'there', 'home', 'any', 'where', 'through', 'old', 'legend', 'before', 'their', 'people', 'another', 'like', 'then', 'usually', 'local', 'will']]]
        expected_title_to_info_results = {'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}, 'Black dog (ghost)': {'author': 'Pegship', 'timestamp': 1220471117, 'length': 14746}}
        metadata2 = [['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']]]
        expected_title_to_info_results2 = {'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}
        self.assertEqual(title_to_info(metadata), expected_title_to_info_results)
        self.assertEqual(title_to_info([]), {})
        self.assertEqual(title_to_info(metadata2), expected_title_to_info_results2)

    def test_search(self):
        sorted_metadata = {'edogawa': ['Edogawa, Tokyo'], 'the': ['Edogawa, Tokyo', 'Black dog (ghost)'], 'with': ['Edogawa, Tokyo', 'Black dog (ghost)'], 'and': ['Edogawa, Tokyo', 'Black dog (ghost)'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo'], 'black': ['Black dog (ghost)'], 'dog': ['Black dog (ghost)'], 'found': ['Black dog (ghost)'], 'folklore': ['Black dog (ghost)'], 'some': ['Black dog (ghost)'], 'often': ['Black dog (ghost)'], 'said': ['Black dog (ghost)'], 'devil': ['Black dog (ghost)'], 'described': ['Black dog (ghost)'], 'its': ['Black dog (ghost)'], 'was': ['Black dog (ghost)'], 'death': ['Black dog (ghost)'], 'has': ['Black dog (ghost)'], 'large': ['Black dog (ghost)'], 'eyes': ['Black dog (ghost)'], 'sometimes': ['Black dog (ghost)'], 'such': ['Black dog (ghost)'], 'shuck': ['Black dog (ghost)'], 'also': ['Black dog (ghost)'], 'are': ['Black dog (ghost)'], 'dogs': ['Black dog (ghost)'], 'have': ['Black dog (ghost)'], 'been': ['Black dog (ghost)'], 'this': ['Black dog (ghost)'], 'were': ['Black dog (ghost)'], 'way': ['Black dog (ghost)'], 'that': ['Black dog (ghost)'], 'barghest': ['Black dog (ghost)'], 'they': ['Black dog (ghost)'], 'may': ['Black dog (ghost)'], 'for': ['Black dog (ghost)'], 'known': ['Black dog (ghost)'], 'night': ['Black dog (ghost)'], 'them': ['Black dog (ghost)'], 'from': ['Black dog (ghost)'], 'other': ['Black dog (ghost)'], 'padfoot': ['Black dog (ghost)'], 'skriker': ['Black dog (ghost)'], 'church': ['Black dog (ghost)'], 'grim': ['Black dog (ghost)'], 'not': ['Black dog (ghost)'], 'can': ['Black dog (ghost)'], 'form': ['Black dog (ghost)'], 'england': ['Black dog (ghost)'], 'being': ['Black dog (ghost)'], 'who': ['Black dog (ghost)'], 'his': ['Black dog (ghost)'], 'when': ['Black dog (ghost)'], 'hounds': ['Black dog (ghost)'], 'appeared': ['Black dog (ghost)'], 'around': ['Black dog (ghost)'], 'ghostly': ['Black dog (ghost)'], 'story': ['Black dog (ghost)'], 'hound': ['Black dog (ghost)'], 'near': ['Black dog (ghost)'], 'haunted': ['Black dog (ghost)'], 'named': ['Black dog (ghost)'], 'which': ['Black dog (ghost)'], 'area': ['Black dog (ghost)'], 'haunt': ['Black dog (ghost)'], 'heard': ['Black dog (ghost)'], 'omen': ['Black dog (ghost)'], 'seen': ['Black dog (ghost)'], 'haunts': ['Black dog (ghost)'], 'had': ['Black dog (ghost)'], 'name': ['Black dog (ghost)'], 'but': ['Black dog (ghost)'], 'man': ['Black dog (ghost)'], 'village': ['Black dog (ghost)'], 'would': ['Black dog (ghost)'], 'one': ['Black dog (ghost)'], 'there': ['Black dog (ghost)'], 'home': ['Black dog (ghost)'], 'any': ['Black dog (ghost)'], 'where': ['Black dog (ghost)'], 'through': ['Black dog (ghost)'], 'old': ['Black dog (ghost)'], 'legend': ['Black dog (ghost)'], 'before': ['Black dog (ghost)'], 'their': ['Black dog (ghost)'], 'people': ['Black dog (ghost)'], 'another': ['Black dog (ghost)'], 'like': ['Black dog (ghost)'], 'then': ['Black dog (ghost)'], 'usually': ['Black dog (ghost)'], 'local': ['Black dog (ghost)'], 'will': ['Black dog (ghost)']}
        expected_search_results = ['Edogawa, Tokyo', 'Black dog (ghost)']
        self.assertEqual(search('the', sorted_metadata), expected_search_results)
        self.assertEqual(search('The', sorted_metadata), [])
        self.assertEqual(search('', sorted_metadata), [])
        self.assertEqual(search('the', {}), [])
        self.assertEqual(search('', {}), [])
        self.assertEqual(search('great', sorted_metadata), [])
        self.assertEqual(search('story', sorted_metadata), ['Black dog (ghost)'])

    def test_article_length(self):
        title_to_info = {'Black dog (ghost)': {'author': 'Pegship', 'timestamp': 1220471117, 'length': 14746}, 'Mexican dog-faced bat': {'author': 'Mack Johnson', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'Mr Jake', 'timestamp': 1207793294, 'length': 26582}, '1936 in music': {'author': 'RussBot', 'timestamp': 1243745950, 'length': 23417}, 'Guide dog': {'author': 'Jack Johnson', 'timestamp': 1165601603, 'length': 7339}, 'Sun dog': {'author': 'Mr Jake', 'timestamp': 1208969289, 'length': 18050}}
        article_titles = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']
        self.assertEqual(article_length(1500, article_titles, title_to_info), ['Mexican dog-faced bat'])
        self.assertEqual(article_length(500000, article_titles, title_to_info), ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog'])
        self.assertEqual(article_length(-40000, article_titles, title_to_info), [])
        self.assertEqual(article_length(0, article_titles, title_to_info), [])
        self.assertEqual(article_length(2000, [], title_to_info), [])
        self.assertEqual(article_length(0, [], {}), [])

    def test_key_by_author(self):
        title_to_info = {'Black dog (ghost)': {'author': 'Pegship', 'timestamp': 1220471117, 'length': 14746}, 'Mexican dog-faced bat': {'author': 'Mack Johnson', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'Mr Jake', 'timestamp': 1207793294, 'length': 26582}, '1936 in music': {'author': 'RussBot', 'timestamp': 1243745950, 'length': 23417}, 'Guide dog': {'author': 'Jack Johnson', 'timestamp': 1165601603, 'length': 7339}, 'Sun dog': {'author': 'Mr Jake', 'timestamp': 1208969289, 'length': 18050}, 'Steven Cohen (soccer)': {'author': 'Mack Johnson', 'timestamp': 1237669593, 'length': 2117}, 'Will Johnson (soccer)': {'author': 'Burna Boy', 'timestamp': 1218489712, 'length': 3562}, 'Spain national beach soccer team': {'author': 'jack johnson', 'timestamp': 1233458894, 'length': 1526}}
        article_titles = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Sun dog', 'Guide dog']
        article_titles_1 = ['Spain national beach soccer team', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
        self.assertEqual(key_by_author(article_titles, title_to_info), {'Pegship': ['Black dog (ghost)'], 'Mack Johnson': ['Mexican dog-faced bat'], 'Mr Jake': ['Dalmatian (dog)', 'Sun dog'], 'Jack Johnson': ['Guide dog']})
        self.assertEqual(key_by_author(article_titles_1, title_to_info), {'jack johnson': ['Spain national beach soccer team'], 'Burna Boy': ['Will Johnson (soccer)'], 'Mack Johnson': ['Steven Cohen (soccer)']})
        self.assertEqual(key_by_author([], title_to_info), {})
        self.assertEqual(key_by_author([], {}), {})

    def test_filter_to_author(self):
        title_to_info = {'Black dog (ghost)': {'author': 'Pegship', 'timestamp': 1220471117, 'length': 14746}, 'Mexican dog-faced bat': {'author': 'Mack Johnson', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'Mr Jake', 'timestamp': 1207793294, 'length': 26582}, '1936 in music': {'author': 'RussBot', 'timestamp': 1243745950, 'length': 23417}, 'Guide dog': {'author': 'Jack Johnson', 'timestamp': 1165601603, 'length': 7339}, 'Sun dog': {'author': 'Mr Jake', 'timestamp': 1208969289, 'length': 18050}, 'Steven Cohen (soccer)': {'author': 'Mack Johnson', 'timestamp': 1237669593, 'length': 2117}, 'Will Johnson (soccer)': {'author': 'Burna Boy', 'timestamp': 1218489712, 'length': 3562}, 'Spain national beach soccer team': {'author': 'jack johnson', 'timestamp': 1233458894, 'length': 1526}}
        article_titles = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Sun dog', 'Guide dog']
        article_titles_2 = ['Spain national beach soccer team', 'Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']
        self.assertEqual(filter_to_author('Jack Johnson', article_titles, title_to_info), ['Guide dog'])
        self.assertEqual(filter_to_author('jack johnson', article_titles, title_to_info), [])
        self.assertEqual(filter_to_author('', article_titles, title_to_info), [])
        self.assertEqual(filter_to_author('Mr Jake', [], title_to_info), [])
        self.assertEqual(filter_to_author('', [], title_to_info), [])  
        self.assertEqual(filter_to_author('Mr Jake', article_titles, title_to_info), ['Dalmatian (dog)', 'Sun dog'])
             
    def test_filter_out(self):
        article_titles = ['Edogawa, Tokyo', 'Black dog (ghost)']
        expected_keyword_to_titles_results = {'edogawa': ['Edogawa, Tokyo'], 'the': ['Edogawa, Tokyo', 'Black dog (ghost)'], 'with': ['Edogawa, Tokyo', 'Black dog (ghost)'], 'and': ['Edogawa, Tokyo', 'Black dog (ghost)'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo'], 'black': ['Black dog (ghost)'], 'dog': ['Black dog (ghost)'], 'found': ['Black dog (ghost)'], 'folklore': ['Black dog (ghost)'], 'some': ['Black dog (ghost)'], 'often': ['Black dog (ghost)'], 'said': ['Black dog (ghost)'], 'devil': ['Black dog (ghost)'], 'described': ['Black dog (ghost)'], 'its': ['Black dog (ghost)'], 'was': ['Black dog (ghost)'], 'death': ['Black dog (ghost)'], 'has': ['Black dog (ghost)'], 'large': ['Black dog (ghost)'], 'eyes': ['Black dog (ghost)'], 'sometimes': ['Black dog (ghost)'], 'such': ['Black dog (ghost)'], 'shuck': ['Black dog (ghost)'], 'also': ['Black dog (ghost)'], 'are': ['Black dog (ghost)'], 'dogs': ['Black dog (ghost)'], 'have': ['Black dog (ghost)'], 'been': ['Black dog (ghost)'], 'this': ['Black dog (ghost)'], 'were': ['Black dog (ghost)'], 'way': ['Black dog (ghost)'], 'that': ['Black dog (ghost)'], 'barghest': ['Black dog (ghost)'], 'they': ['Black dog (ghost)'], 'may': ['Black dog (ghost)'], 'for': ['Black dog (ghost)'], 'known': ['Black dog (ghost)'], 'night': ['Black dog (ghost)'], 'them': ['Black dog (ghost)'], 'from': ['Black dog (ghost)'], 'other': ['Black dog (ghost)'], 'padfoot': ['Black dog (ghost)'], 'skriker': ['Black dog (ghost)'], 'church': ['Black dog (ghost)'], 'grim': ['Black dog (ghost)'], 'not': ['Black dog (ghost)'], 'can': ['Black dog (ghost)'], 'form': ['Black dog (ghost)'], 'england': ['Black dog (ghost)'], 'being': ['Black dog (ghost)'], 'who': ['Black dog (ghost)'], 'his': ['Black dog (ghost)'], 'when': ['Black dog (ghost)'], 'hounds': ['Black dog (ghost)'], 'appeared': ['Black dog (ghost)'], 'around': ['Black dog (ghost)'], 'ghostly': ['Black dog (ghost)'], 'story': ['Black dog (ghost)'], 'hound': ['Black dog (ghost)'], 'near': ['Black dog (ghost)'], 'haunted': ['Black dog (ghost)'], 'named': ['Black dog (ghost)'], 'which': ['Black dog (ghost)'], 'area': ['Black dog (ghost)'], 'haunt': ['Black dog (ghost)'], 'heard': ['Black dog (ghost)'], 'omen': ['Black dog (ghost)'], 'seen': ['Black dog (ghost)'], 'haunts': ['Black dog (ghost)'], 'had': ['Black dog (ghost)'], 'name': ['Black dog (ghost)'], 'but': ['Black dog (ghost)'], 'man': ['Black dog (ghost)'], 'village': ['Black dog (ghost)'], 'would': ['Black dog (ghost)'], 'one': ['Black dog (ghost)'], 'there': ['Black dog (ghost)'], 'home': ['Black dog (ghost)'], 'any': ['Black dog (ghost)'], 'where': ['Black dog (ghost)'], 'through': ['Black dog (ghost)'], 'old': ['Black dog (ghost)'], 'legend': ['Black dog (ghost)'], 'before': ['Black dog (ghost)'], 'their': ['Black dog (ghost)'], 'people': ['Black dog (ghost)'], 'another': ['Black dog (ghost)'], 'like': ['Black dog (ghost)'], 'then': ['Black dog (ghost)'], 'usually': ['Black dog (ghost)'], 'local': ['Black dog (ghost)'], 'will': ['Black dog (ghost)']}
        self.assertEqual(filter_out('music', article_titles, expected_keyword_to_titles_results), ['Edogawa, Tokyo', 'Black dog (ghost)'])
        self.assertEqual(filter_out('the', article_titles, expected_keyword_to_titles_results), [])
        self.assertEqual(filter_out('', article_titles, expected_keyword_to_titles_results), ['Edogawa, Tokyo', 'Black dog (ghost)'])
        self.assertEqual(filter_out('edogawa', article_titles, expected_keyword_to_titles_results), ['Black dog (ghost)'])

    def test_articles_from_year(self):
        title_to_info = {'Black dog (ghost)': {'author': 'Pegship', 'timestamp': 1220471117, 'length': 14746}, 'Mexican dog-faced bat': {'author': 'Mack Johnson', 'timestamp': 1255316429, 'length': 1138}, 'Dalmatian (dog)': {'author': 'Mr Jake', 'timestamp': 1207793294, 'length': 26582}, '1936 in music': {'author': 'RussBot', 'timestamp': 1243745950, 'length': 23417}, 'Guide dog': {'author': 'Jack Johnson', 'timestamp': 1165601603, 'length': 7339}, 'Sun dog': {'author': 'Mr Jake', 'timestamp': 1208969289, 'length': 18050}, 'Steven Cohen (soccer)': {'author': 'Mack Johnson', 'timestamp': 1237669593, 'length': 2117}, 'Will Johnson (soccer)': {'author': 'Burna Boy', 'timestamp': 1218489712, 'length': 3562}, 'Spain national beach soccer team': {'author': 'jack johnson', 'timestamp': 1233458894, 'length': 1526}}
        article_titles = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']
        self.assertEqual(articles_from_year(2009, article_titles, title_to_info), ['Mexican dog-faced bat'])
        self.assertEqual(articles_from_year(2023, article_titles, title_to_info), [])
        self.assertEqual(articles_from_year(2009, [], title_to_info), [])

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

    #     self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_search_engine_1(self, input_mock):
        keyword = 'dog'
        advanced_option = 1
        advanced_response = 5000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Mexican dog-faced bat']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_search_engine_2(self, input_mock):
        keyword = 'dog'
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: {'Pegship': ['Black dog (ghost)'], 'Mack Johnson': ['Mexican dog-faced bat'], 'Mr Jake': ['Dalmatian (dog)', 'Sun dog'], 'Jack Johnson': ['Guide dog']}\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_search_engine_3(self, input_mock):
        keyword = 'dog'
        advanced_option = 3
        advanced_response = 'Jack Johnson'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Guide dog']\n"

    @patch('builtins.input')
    def test_search_engine_4(self, input_mock):
        keyword = 'dog'
        advanced_option = 4
        advanced_response = 'Mr Jake'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles:  ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']\n"

    @patch('builtins.input')
    def test_search_engine_5(self, input_mock):
        keyword = 'dog'
        advanced_option = 5
        advanced_response = 2008

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles:  ['Black dog (ghost)', 'Dalmatian (dog)', 'Sun dog']\n" 

    @patch('builtins.input')
    def test_search_engine_6(self, input_mock):
        keyword = 'dog'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles:  ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']\n"     

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
