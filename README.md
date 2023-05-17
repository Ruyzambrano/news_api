# News API Program README

This program allows you to retrieve and read news articles using the News API. It prompts you to enter your News API key and the topic you are interested in. It then retrieves the top 20 articles related to that topic and displays them with their corresponding numbers. You can choose an article by entering its number and the program will open the article in your default web browser.

## Prerequisites

Before running this program, make sure you have the following:

- Python: Ensure you have Python installed on your machine. You can download Python from the official website: https://www.python.org/downloads/

- Requests Library: This program requires the `requests` library to make HTTP requests. You can install it using pip:
```
pip install requests
```

- Tabulate Library: The program also utilizes the `tabulate` library to format and display the article titles in a table. You can install it using pip:
```
pip install tabulate
```

- News API Key: To use this program, you need an API key from News API. If you don't have an API key, you can sign up for one at https://newsapi.org/register. Once you have the key, keep it handy for running the program.

## Running the Program

1. Download the program file containing the code.

2. Open a terminal or command prompt and navigate to the directory where you saved the program file.

3. Run the program using the following command:
```
python news_api_program.py
```

4. The program will prompt you to enter your News API key. Provide your API key and press Enter.

5. Next, you will be asked to enter the topic you are interested in. If you don't specify a topic and press Enter, it will default to "e".

6. The program will make a request to the News API and retrieve the top 20 articles related to the specified topic. If any articles are found, they will be displayed with their corresponding numbers in a table.

7. Enter the number of the article you want to read or type "0" to exit the program.

8. If you choose an article, the program will open the article's URL in your default web browser.

## Troubleshooting

- If you encounter any errors while running the program, ensure that you have correctly installed the required libraries (`requests` and `tabulate`) and that you have entered a valid News API key.

- Make sure you have an active internet connection to fetch the articles from the News API.

- If you receive an error from the News API, the program will display the error message returned by the API along with the corresponding error code.

## Limitations

- The program currently retrieves the top 20 articles related to the specified topic. If you want to retrieve more articles or customize the query parameters, you can modify the API request URL in the code accordingly.

- The program only opens the URL of the selected article. If you want to perform additional actions or extract more information from the articles, you can extend the code as per your requirements.

## License

This program is open source and distributed under the MIT License. You can find the full license text in the LICENSE file.

## Acknowledgments

This program utilizes the News API to fetch and display news articles. Special thanks to the News API team for providing this service.

For more information about the News API and its usage, please refer to the official documentation: https://newsapi.org/docs
