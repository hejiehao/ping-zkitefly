import requests
headers = {
    'Accept': 'application/json',
    'x-api-key': '$2a$10$nQZas1zYsguFaT4zxAK/UeG0WRETgg.ZDZveqXIO80Nrqrc.KvbB.'
}

r = requests.get('/v1/minecraft/version', params={
    "sortDescending": True
}, headers = headers)

print(r.json())