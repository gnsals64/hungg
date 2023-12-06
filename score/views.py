from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import requests

request_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-2272600d-09f9-4408-aa33-fb7dcdc87268"
}

def score_view(request):
    return render(request, 'score/score_view.html')

def search_res(request):
    summoner_result = {}
    summoner_tier = {}
    
    summoner_name = request.GET.get('search_text')
    summoner_response = requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str(summoner_name), headers=request_headers)
    summoner_response = summoner_response.json()
    
    summoner_info = requests.get("https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + str(summoner_response['id']), headers=request_headers)
    summoner_info = summoner_info.json()

    summoner_result['name'] = summoner_response['name']
    summoner_result['level'] = summoner_response['summonerLevel']
    summoner_tier['tier'] = summoner_info[0]['tier']
    summoner_tier['rank'] = summoner_info[0]['rank']
    summoner_tier['wins'] =  summoner_info[0]['wins']
    summoner_tier['losses'] = summoner_info[0]['losses']
    
    # sum_result['profileIconId'] = summoners_response['profileIconId']
    return render(request, 'score/search_res.html', {'res': summoner_result, 'tier': summoner_tier})