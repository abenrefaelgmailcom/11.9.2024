


# זמן לפי שעות
hours = int(input("movie_time_hours: "))

# זמן לפי דקות
minuts = int(input("movie_time_min: "))

# חילוק ב60
time_by_hours = hours // 60
# חישוב משולשים אקסטרה
time_by_minuts = minuts % 60


print(f"time by hours = {hours} time by minuts = {minuts}")
