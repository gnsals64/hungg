import requests

request_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-2272600d-09f9-4408-aa33-fb7dcdc87268"
}

def check_members():
    print("시작")
    summoner_response = requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/hideonbush", headers=request_headers)
    summoner_response = summoner_response.json()
    print(summoner_response)

check_members()