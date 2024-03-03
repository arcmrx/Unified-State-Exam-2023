from turtle import *

color("black", "red")
m = 100
begin_fill()
# left (90)
# for i in range(3):
#   forward (111*m)
#   right (120)
end_fill()
canvas = getcanvas()
cnt = 0
for y in range(-100 * m, 100 * m, m):
    for x in range(-100 * m, 100 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            cnt += 1
print(cnt)
done()
exit()
