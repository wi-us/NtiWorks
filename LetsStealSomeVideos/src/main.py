import requests

file = open('C://Users//1вин//Documents//projs//LetsStealSomeVideos', 'w+')
with file:
    file.write(requests.get("https://player02.getcourse.ru/player/f5575abba73921f23a49c22f88ca1610/1f5a86b9814472f53f862dc613af48b5/media/360.m3u8?sid=&user-cdn=cdnvideo&version=10%3A1%3A1%3A0%3Acdnvideo&user-id=345729533&jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyLWlkIjozNDU3Mjk1MzN9.30rSiRux1u_hta3kZtaxhIL51E2vp-sRuls-O6JX9q0"))
    

