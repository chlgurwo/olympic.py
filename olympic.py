import turtle as t

t.speed(30)
t.pensize(20)

t.circle(100)

t.up()
t.forward(240) # 앞으로 240만큼 옮겨서 원 출력
t.down()
t.pencolor('red') # 원색깔 빨간색
t.circle(100) # 원크기 100

t.up()
t.backward(480) # 뒤로 480 만큼 옮겨서 원 출력
t.down()
t.pencolor('blue') #원 색깔 파란색
t.circle(100) # 원크기 100

t.up()
t.forward(240) #다시 앞으로 240만큼 옮겨서 원 출력
t.down()
t.pencolor('black') # 원색깔 검정색
t.circle(100) #원크기 100

t.up()
t.backward(120)
t.goto(-110,-100) # 좌표 -110,-100 만큼 이동하여 원 출력
t.down()
t.pencolor('yellow')
t.circle(100)

t.up()
t.forward(240)
t.goto(120,-100) # 좌표 120,-100 만큼 이동하여 원 출력
t.down()
t.pencolor('green')
t.circle(100)






t.done()