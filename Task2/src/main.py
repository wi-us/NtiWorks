from seasons import *


winter = Season("Winter", open('seasons/winter.txt', 'r', encoding = 'utf-8').readlines(), [], "#B0E2FF")
spring = Season("Spring", open('seasons/spring.txt', 'r', encoding = 'utf-8').readlines(), [], "#CAFF70")
summer = Season("Summer", open('seasons/summer.txt', 'r', encoding = 'utf-8').readlines(), [], "#00C957")
autamn = Season("Autamn", open('seasons/autamn.txt', 'r', encoding = 'utf-8').readlines(), [], "#FFD700")

from interface import root
root.mainloop()