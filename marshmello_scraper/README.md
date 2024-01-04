# Marshmello Scraper

This is a web scraping project built with Scrapy to extract song details of the artist Marshmello from a Chinese website; music.migu.cn . The project allows you to scrape data such as song and artiste names associated with Marshmello.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Scraped Data](#scraped-data)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you can use this web scraper, ensure you have the following installed on your system:

- Python (3.6 or higher)
- Scrapy

You can install Scrapy using pip:

```shell
pip install Scrapy
```

Getting Started
Clone this repository to your local machine:
```shell
git clone https://github.com/MarsIncarnate/Chinese-Marshmello-Scraper.git
```

Navigate to the project directory:
```shell
cd marshmello scraper
```

Set up your Scrapy project by creating a new Scrapy spider. You can modify the spider code to customize the scraping process for your specific needs.

Usage
To run the web scraper, follow these steps:

Ensure you are in the project directory.

Run the Scrapy spider with the following command:

```shell
scrapy crawl marshmello_scraper
```
The spider will start scraping review data and output a json with the required data.

Review the scraped data in the json or process it as needed.

Scraped Data

Contributing
If you would like to contribute to this project, feel free to create a pull request with your changes or open an issue if you have any suggestions or questions.

License
This project is licensed under the MIT License - see the LICENSE file for details.

