from tkinter import *

## 함수 선언 부분 ##
def draw_triangle(x, y, size) :
    if size >= 30 :
        draw_triangle(x, y, size/2)
        draw_triangle(x+size/2, y, size / 2)
        draw_triangle(x + size / 4, int(y-size*(3**0.5)/4), size / 2)
    else :
        canvas.create_polygon (x, y, x + size, y, x + size / 2, y - size*(3 ** 0.5) / 2, fill = 'red', outline = "red")

## 전역 변수 선언 부분 ##
w_size = 1000
radius = 400

## 메인 코드 부분 ##
window = Tk()
window.title("삼각형 모양의 프랙탈")
canvas = Canvas(window, height = w_size, width = w_size, bg = 'white')

draw_triangle(w_size/5, w_size/5*4, w_size*2/3)

canvas.pack()
window.mainloop()
