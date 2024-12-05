import requests
import json

url = "https://raw.githubusercontent.com/ErikThiart/cryptocurrency-icons/refs/heads/master/coin_map.json"
response = requests.get(url)

body_dict = response.json()
# user_id = body_dict['userId'] # 1

# print(body_dict)

coinlist = []

for coin in body_dict:
    if coin['symbol'] not in coinlist:
        coinlist.append(coin['symbol'])

# print(coinlist)


import requests

url = 'https://logos.tradeloop.app/api/getLogos'
myobj = {
      # "symbols": ["BTCUSDT","ETH","1000PEPE"],
      "symbols": coinlist,
      "resolution": "64",
      "mode": "multiple",
      "parser": {
        "enable": True,
        "options": {"removeNumbers": True}
      }
    }

x = requests.post(url, json = myobj)

f = open('coinMarketCapImages.json','w', encoding="utf-8")
print(x.text, file=f) # Python 3.x



 #   final body = ;
#
 #   final response = await _restClient.post(url, body);
#
 #   if (response.statusCode != 200) {
 #     printError(info: 'Failed to load data. Url: $url, body: $body.');
 #     return {};
 #   }
#
 #   final List<dynamic> jsonResponse = response.body;
 #   List<CoinModel> coins =
 #       jsonResponse.map((data) => CoinModel.fromJson(data)).toList();
#
 #   coins.sort((a, b) => a.rank.compareTo(b.rank));
#
 #   // Convert list to map with symbol as key
 #   Map<String, CoinModel> coinMap = {};
 #   for (var coin in coins) {
 #     coinMap.putIfAbsent(coin.symbol, () => coin);