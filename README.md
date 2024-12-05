# Coin Market Cap Images

This repository provides a Python script to fetch cryptocurrency images.
It is using different sources and APIs to generate a JSON file. This JSON file can then be used by other applications to display cryptocurrency information and their corresponding images.

Example:
{
  "png": "https://s2.coinmarketcap.com/static/img/coins/64x64/1.png",
  "rank": 1,
  "symbol": "BTC",
  "name": "Bitcoin"
}

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/s-sparber/CoinMarketCapImages.git
   ```
2. **Install dependencies:**
   ```bash
   pip install requests
   ```

## Usage

1. **Run the script:**
   ```bash
   python reloadJsonFile.py
   ```
   This will fetch the data and recreate the `coinMarketCapImages.json` file in the project directory.

## Contributing

Feel free to contribute to this project by:

* **Reporting Issues:** Use the GitHub issue tracker to report bugs or feature requests.
* **Submitting Pull Requests:** Contribute code improvements or new features.

## License

This project is licensed under the MIT License.
