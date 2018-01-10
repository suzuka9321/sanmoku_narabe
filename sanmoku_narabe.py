# coding:shift-jis



# 三目並べクラス
# プレイヤー対CPU

# ○: Player
# ×: CPU

# 0: 空きマス
# 1: ○
# 2: ×

# 変数名
# 　左　: left
# 真ん中: center
# 　右　: right

# 上段: over
# 中段: middle
# 下段: under

# left_over   | center_over   | right_over
#-------------+---------------+--------------
# left_middle | center_middle | right_middle
#-------------+---------------+--------------
# left_under  | center_under  | right_under




from turtle import *
import config

class Sanmoku(Turtle):
    def __init__(self):
        super(Sanmoku,self).__init__()
        
        self.table_drow()
        onscreenclick(self.mark_whole)
        mainloop()
    
    
    
    #盤面の描画
    def table_drow(self):
        y = 360
        for i in range(4):
            self.penup()
            self.goto(0,y)
            self.pendown()
            self.goto(360,y)
            y -= 120
        x = 360
        for u in range(4):
            self.penup()
            self.goto(x,0)
            self.pendown()
            self.goto(x,360)
            x -= 120
        
        self.penup()
        self.goto(120,-50)
        self.pendown()
        num = self.heading()
        self.right(num)
        for i in range(4):
            self.forward(120)
            self.right(90)
    
    
    #○、×の初期化
    def reset(self):
        config.left_under = 0
        config.center_under = 0
        config.right_under = 0

        config.left_middle = 0
        config.center_middle = 0
        config.right_middle = 0

        config.left_over = 0
        config.center_over = 0
        config.right_over = 0
    
    
    #プレイヤーの操作を無効化
    def cpu_move(self,x,y):
        pass


    #ゲーム終了後のリセットボタン
    def game_out(self,x,y):
        if -170 < y and y < -50:
            if 120 < x and x < 240:
            	#盤面を消して、再び盤面の描画
                self.clear()
                self.table_draw()
                
                #履歴を初期化する
                self.reset()
    
    
    
    def mark_whole(self,x,y):
    	#リセットボタン。履歴を初期化する
        if -170 < y and y < -50:
            if 120 < x and x < 240:
                self.clear()
                self.table_drow()
                self.reset()
        config.pass_count = 0
        
        #プレイヤーの手番
        if 0 < y and y < 120:
            if 0 < x and x < 120:
                if config.left_under == 0:
                    self.getscreen().onclick(self.cpu_move)
                    self.whole_left_under()
                    config.left_under = 1
                    config.pass_count = 1
            elif 120 < x and x < 240:
                if config.center_under == 0:
                    self.getscreen().onclick(self.cpu_move)
                    self.whole_center_under()
                    config.center_under = 1
                    config.pass_count = 1
            elif 240 < x and x < 360:
                if config.right_under == 0:
                    self.getscreen().onclick(self.cpu_move)
                    self.whole_right_under()
                    config.right_under = 1
                    config.pass_count = 1
        elif 120 < y and y < 240:
            if 0 < x and x < 120:
                if config.left_middle == 0:
                    self.getscreen().onclick(self.cpu_move)
                    self.whole_left_middle()
                    config.left_middle = 1
                    config.pass_count = 1
            elif 120 < x and x < 240:
                if config.center_middle == 0:
                    self.getscreen().onclick(self.cpu_move)
                    self.whole_center_middle()
                    config.center_middle = 1
                    config.pass_count = 1
            elif 240 < x and x < 360:
                if config.right_middle == 0:
                    self.getscreen().onclick(self.cpu_move)
                    self.whole_right_middle()
                    config.right_middle = 1
                    config.pass_count = 1
        elif 240 < y and y < 360:
            if 0 < x and x < 120:
                if config.left_over == 0:
                    self.getscreen().onclick(self.cpu_move)
                    self.whole_left_over()
                    config.left_over = 1
                    config.pass_count = 1
            elif x < 240:
                if config.center_over == 0:
                    self.getscreen().onclick(self.cpu_move)
                    self.whole_center_over()
                    config.center_over = 1
                    config.pass_count = 1
            elif x < 360:
                if config.right_over == 0:
                    self.getscreen().onclick(self.cpu_move)
                    self.whole_right_over()
                    config.right_over = 1
                    config.pass_count = 1
        
        
        self.gameset()
        
        #CPUの手番
        #CPUがリーチならビンゴする１手
        #プレイヤーがリーチならビンゴさせないように１手
        #真ん中が空いていたら、真ん中。いなければ角以外に１手
        
        if config.pass_count == 1:
            config.pass_count = 0
            #CPUがリーチならビンゴする１手
            self.cpu_cut_win(2,2)
            if config.pass_count == 0:
            	#プレイヤーがリーチならビンゴさせないように１手
                self.cpu_cut_win(1,2)
                if config.pass_count == 0:
                	#真ん中が空いていたら、真ん中に１手
                	#いなければ角以外に１手
                    self.cpu_turn()
        
        self.gameset()
        self.getscreen().onclick(self.mark_whole)
    
    
    
    
    #勝敗判定
    def gameset(self):
        if config.left_over == 1 and config.center_over== 1 and config.right_over == 1 or config.left_middle == 1 and config.center_middle == 1 and config.right_middle == 1 or config.left_under == 1 and config.center_under == 1 and config.right_under == 1 or config.left_over == 1 and config.left_middle == 1 and config.left_under == 1 or config.center_over == 1 and config.center_middle == 1 and config.center_under == 1 or config.right_over == 1 and config.right_middle == 1 and config.right_under == 1 or config.left_over == 1 and config.center_middle == 1 and config.right_under == 1 or config.right_over == 1 and config.center_middle == 1 and config.left_under == 1:
            self.getscreen().onclick(self.game_out)
            config.pass_count = 0
            print("○の勝ち!!")
        elif config.left_over == 2 and config.center_over== 2 and config.right_over == 2 or config.left_middle == 2 and config.center_middle == 2 and config.right_middle == 2 or config.left_under == 2 and config.center_under == 2 and config.right_under == 2 or config.left_over == 2 and config.left_middle == 2 and config.left_under == 2 or config.center_over == 2 and config.center_middle == 2 and config.center_under == 2 or config.right_over == 2 and config.right_middle == 2 and config.right_under == 2 or config.left_over == 2 and config.center_middle == 2 and config.right_under == 2 or config.right_over == 2 and config.center_middle == 2 and config.left_under == 2:
            self.getscreen().onclick(self.game_out)
            config.pass_count = 0
            print("×の勝ち!!")
    
    
    #CPUの手番。ｘの値によってビンゴを阻止とビンゴする動き。ｙでCPUの手番を記録
    def cpu_cut_win(self,x,y):
        if config.left_over == x and config.center_over == x and config.right_over == 0:
            self.cross_right_over()
            config.right_over = y
            config.pass_count = 1
        elif config.left_middle == x and config.center_middle == x and config.right_middle == 0:
            self.cross_right_middle()
            config.right_middle = y
            config.pass_count = 1
        elif config.left_under == x and config.center_under == x and config.right_under == 0:
            self.cross_right_under()
            config.right_under = y
            config.pass_count = 1

        elif config.left_over == x and config.right_over == x and config.center_over == 0:
            self.cross_center_over()
            config.center_over = y
            config.pass_count = 1
        elif config.left_middle == x and config.right_middle == x and config.center_middle == 0:
            self.cross_center_middle()
            config.center_middle = y
            config.pass_count = 1
        elif config.left_under == x and config.right_under == x and config.center_under == 0:
            self.cross_center_under()
            config.center_under = y
            config.pass_count = 1

        elif config.center_over == x and config.right_over == x and config.left_over == 0:
            self.cross_left_over()
            config.left_over = y
            config.pass_count = 1
        elif config.center_middle == x and config.right_middle == x and config.left_middle == 0:
            self.cross_left_middle()
            config.left_middle = y
            config.pass_count = 1
        elif config.center_under == x and config.right_under == x and config.left_under == 0:
            self.cross_left_under()
            config.left_under = y
            config.pass_count = 1


        elif config.left_over == x and config.left_middle == x and config.left_under == 0:
            self.cross_left_under()
            config.left_under = y
            config.pass_count = 1
        elif config.center_over == x and config.center_middle == x and config.center_under == 0:
            self.cross_center_under()
            config.center_under = y
            config.pass_count = 1
        elif config.right_over == x and config.right_middle == x and config.right_under == 0:
            self.cross_right_under()
            config.right_under = y
            config.pass_count = 1

        elif config.left_over == x and config.left_under == x and config.left_middle == 0:
            self.cross_left_middle()
            config.left_middle = y
            config.pass_count = 1
        elif config.center_over == x and config.center_under == x and config.center_middle == 0:
            self.cross_center_middle()
            config.center_middle = y
            config.pass_count = 1
        elif config.right_over == x and config.right_under == x and config.right_middle == 0:
            self.cross_right_middle()
            config.right_middle = y
            config.pass_count = 1

        elif config.left_middle == x and config.left_under == x and config.left_over == 0:
            self.cross_left_over()
            config.left_over = y
            config.pass_count = 1
        elif config.center_middle == x and config.center_under == x and config.center_over == 0:
            self.cross_center_over()
            config.center_over = y
            config.pass_count = 1
        elif config.right_middle == x and config.right_under == x and config.right_over == 0:
            self.cross_right_over()
            config.right_over = y
            config.pass_count = 1


        elif config.left_over == x and config.center_middle == x and config.right_under == 0:
            self.cross_right_under()
            config.right_under = y
            config.pass_count = 1
        elif config.right_over == x and config.center_middle == x and config.left_under == 0:
            self.cross_left_under()
            config.left_under = y
            config.pass_count = 1

        elif config.left_over == x and config.right_under == x and config.center_middle == 0:
            self.cross_center_middle()
            config.center_middle = y
            config.pass_count = 1
        elif config.right_over == x and config.left_under == x and config.center_middle == 0:
            self.cross_center_middle()
            config.center_middle = y
            config.pass_count = 1

        elif config.center_middle== x and config.right_under == x and config.left_over == 0:
            self.cross_left_over()
            config.left_over = y
            config.pass_count = 1
        elif config.center_middle == x and config.left_under== x and config.right_over == 0:
            self.cross_right_over()
            config.right_over = y
            config.pass_count = 1



    #CPUの手番
    def cpu_turn(self):
    	#真ん中が空いていたら、真ん中に×
        if config.center_middle == 0:
            self.cross_center_middle()
            config.center_middle = 2
        
        #空いていなければ、角以外に１手
        elif config.center_over == 0:
            self.cross_center_over()
            config.center_over = 2
        
        elif config.right_middle == 0:
            self.cross_right_middle()
            config.right_middle = 2
        
        elif config.center_under == 0:
            self.cross_center_under()
            config.center_under = 2
        
        elif config.left_middle == 0:
            self.cross_left_middle()
            config.left_middle = 2
        
        elif config.left_over == 0:
            self.cross_left_over()
            config.left_over = 2
        
        elif config.right_over == 0:
            self.cross_right_over()
            config.right_over = 2
        
        elif config.right_under == 0:
            self.cross_right_under()
            config.right_under = 2
        
        elif config.left_under == 0:
            self.cross_left_under()
            config.left_under = 2
        



    #〇を描く
    def whole(self):
        num = self.heading()
        self.right(num)
        self.pendown()
        self.circle(50)



    #×を描く
    def cross(self):
        num = self.heading()
        self.right(num)
        self.penup()
        self.forward(50)
        self.pendown()
        self.left(135)
        self.forward(141)
        self.right(135)
        self.penup()
        self.forward(100)
        self.pendown()
        self.right(135)
        self.forward(141)


    #左上に○を描く
    def whole_left_over(self):
        self.penup()
        self.goto(60,250)
        self.whole()
    
    
    #左中に○を描く
    def whole_left_middle(self):
        self.penup()
        self.goto(60,130)
        self.whole()
    
    
    #左下に○を描く
    def whole_left_under(self):
        self.penup()
        self.goto(60,10)
        self.whole()
    
    
    #中上に○を描く
    def whole_center_over(self):
        self.penup()
        self.goto(180,250)
        self.whole()
    
    
    #中中に○を描く
    def whole_center_middle(self):
        self.penup()
        self.goto(180,130)
        self.whole()
    
    
    #中下に○を描く
    def whole_center_under(self):
        self.penup()
        self.goto(180,10)
        self.whole()
    
    
    #右上に○を描く
    def whole_right_over(self):
        self.penup()
        self.goto(300,250)
        self.whole()
    
    
    #右中に○を描く
    def whole_right_middle(self):
        self.penup()
        self.goto(300,130)
        self.whole()
    
    
    #右下に○を描く
    def whole_right_under(self):
        self.penup()
        self.goto(300,10)
        self.whole()
    
    
    
    #左上に×を描く
    def cross_left_over(self):
        self.penup()
        self.goto(60,250)
        self.cross()
    
    
    #左中に×を描く
    def cross_left_middle(self):
        self.penup()
        self.goto(60,130)
        self.cross()
    
    
    #左下に×を描く
    def cross_left_under(self):
        self.penup()
        self.goto(60,10)
        self.cross()
    
    
    #中上に×を描く
    def cross_center_over(self):
        self.penup()
        self.goto(180,250)
        self.cross()
    
    
    #中中に×を描く
    def cross_center_middle(self):
        self.penup()
        self.goto(180,130)
        self.cross()
    
    
    #中下に×を描く
    def cross_center_under(self):
        self.penup()
        self.goto(180,10)
        self.cross()
    
    
    #右上に×を描く
    def cross_right_over(self):
        self.penup()
        self.goto(300,250)
        self.cross()
    
    
    #右中に×を描く
    def cross_right_middle(self):
        self.penup()
        self.goto(300,130)
        self.cross()
    
    
    #右下に×を描く
    def cross_right_under(self):
        self.penup()
        self.goto(300,10)
        self.cross()
