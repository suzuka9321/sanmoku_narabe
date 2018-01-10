# coding:shift-jis



# �O�ڕ��׃N���X
# �v���C���[��CPU

# ��: Player
# �~: CPU

# 0: �󂫃}�X
# 1: ��
# 2: �~

# �ϐ���
# �@���@: left
# �^��: center
# �@�E�@: right

# ��i: over
# ���i: middle
# ���i: under

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
        
        self.table_draw()
        onscreenclick(self.game_start)
        mainloop()
    
    
    
    
    
    def table_draw(self):
        #�Ֆʂ̕`��
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
        
        #���Z�b�g�{�^���̕`��
        self.penup()
        self.goto(120,-50)
        self.pendown()
        num = self.heading()
        self.right(num)
        for i in range(4):
            self.forward(120)
            self.right(90)
    
    
    #���A�~�̏�����
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
        
        config.count = 0
    
    
    #�v���C���[�̑���𖳌���
    def cpu_move(self,x,y):
        pass


    #�Q�[���I����̃��Z�b�g�{�^��
    def game_out(self,x,y):
        if -170 < y and y < -50:
            if 120 < x and x < 240:
            	#�Ֆʂ������āA�ĂєՖʂ̕`��
                self.clear()
                self.table_draw()
                
                #����������������
                self.reset()
                onscreenclick(self.game_start)
    
    
    
    def game_start(self,x,y):
        #���Z�b�g�{�^���B����������������
        if -170 < y and y < -50:
            if 120 < x and x < 240:
                self.clear()
                self.table_draw()
                self.reset()
        config.pass_count = 0
        
        #�v���C���[�̎��
        if 0 < y and y < 120:
            if 0 < x and x < 120:
                if config.left_under == 0:
                    onscreenclick(self.cpu_move)
                    self.whole(60,10)
                    config.left_under = 1
                    config.pass_count = 1
            elif 120 < x and x < 240:
                if config.center_under == 0:
                    onscreenclick(self.cpu_move)
                    self.whole(180,10)
                    config.center_under = 1
                    config.pass_count = 1
            elif 240 < x and x < 360:
                if config.right_under == 0:
                    onscreenclick(self.cpu_move)
                    self.whole(300,10)
                    config.right_under = 1
                    config.pass_count = 1
        elif 120 < y and y < 240:
            if 0 < x and x < 120:
                if config.left_middle == 0:
                    onscreenclick(self.cpu_move)
                    self.whole(60,130)
                    config.left_middle = 1
                    config.pass_count = 1
            elif 120 < x and x < 240:
                if config.center_middle == 0:
                    onscreenclick(self.cpu_move)
                    self.whole(180,130)
                    config.center_middle = 1
                    config.pass_count = 1
            elif 240 < x and x < 360:
                if config.right_middle == 0:
                    onscreenclick(self.cpu_move)
                    self.whole(300,130)
                    config.right_middle = 1
                    config.pass_count = 1
        elif 240 < y and y < 360:
            if 0 < x and x < 120:
                if config.left_over == 0:
                    onscreenclick(self.cpu_move)
                    self.whole(60,250)
                    config.left_over = 1
                    config.pass_count = 1
            elif x < 240:
                if config.center_over == 0:
                    onscreenclick(self.cpu_move)
                    self.whole(180,250)
                    config.center_over = 1
                    config.pass_count = 1
            elif x < 360:
                if config.right_over == 0:
                    onscreenclick(self.cpu_move)
                    self.whole(300,250)
                    config.right_over = 1
                    config.pass_count = 1
        
        
        self.gameset()
        
        #CPU�̎��
        #CPU�����[�`�Ȃ�r���S����P��
        #�v���C���[�����[�`�Ȃ�r���S�����Ȃ��悤�ɂP��
        #�^�񒆂��󂢂Ă�����A�^�񒆁B���Ȃ���Ίp�ȊO�ɂP��
        
        if config.pass_count == 1:
            config.pass_count = 0
            #CPU�����[�`�Ȃ�r���S����P��
            self.cpu_cut_win(2)
            if config.pass_count == 0:
            	#�v���C���[�����[�`�Ȃ�r���S�����Ȃ��悤�ɂP��
                self.cpu_cut_win(1)
                if config.pass_count == 0:
                	#�^�񒆂��󂢂Ă�����A�^�񒆂ɂP��
                	#���Ȃ���Ίp�ɂP��
                    self.cpu_turn()
            self.gameset()
        
        if config.pass_count == 1:
            onscreenclick(self.game_start)
            config.count += 1
            if config.count == 5:
                if self.bingo_judge(1) == False and self.bingo_judge(2) == False:
                    print("��������!!�@���̘g�������čĒ���!!")




    #���s����
    def bingo_judge(self,num):
        if config.left_over == num and config.center_over== num and config.right_over == num or config.left_middle == num and config.center_middle == num and config.right_middle == num or config.left_under == num and config.center_under == num and config.right_under == num or config.left_over == num and config.left_middle == num and config.left_under == num or config.center_over == num and config.center_middle == num and config.center_under == num or config.right_over == num and config.right_middle == num and config.right_under == num or config.left_over == num and config.center_middle == num and config.right_under == num or config.right_over == num and config.center_middle == num and config.left_under == num:
            return True
        else:
            return False



    def gameset(self):
        if self.bingo_judge(1) == True:
            onscreenclick(self.game_out)
            config.pass_count = 0
            print("���̏���!!�@���̘g�������čĒ���!!")
        if self.bingo_judge(2) == True:
            onscreenclick(self.game_out)
            config.pass_count = 0
            print("�~�̏���!!�@���̘g�������čĒ���!!")


    #CPU�̎�ԁB���̒l�ɂ���ăr���S��j�~�ƃr���S���铮��
    def cpu_cut_win(self,num):
        if config.left_over == num and config.center_over == num and config.right_over == 0:
            self.cross(300,250)
            config.right_over = 2
            config.pass_count = 1
        elif config.left_middle == num and config.center_middle == num and config.right_middle == 0:
            self.cross(300,130)
            config.right_middle = 2
            config.pass_count = 1
        elif config.left_under == num and config.center_under == num and config.right_under == 0:
            self.cross(300,10)
            config.right_under = 2
            config.pass_count = 1

        elif config.left_over == num and config.right_over == num and config.center_over == 0:
            self.cross(180,250)
            config.center_over = 2
            config.pass_count = 1
        elif config.left_middle == num and config.right_middle == num and config.center_middle == 0:
            self.cross(180,130)
            config.center_middle = 2
            config.pass_count = 1
        elif config.left_under == num and config.right_under == num and config.center_under == 0:
            self.cross(180,10)
            config.center_under = 2
            config.pass_count = 1

        elif config.center_over == num and config.right_over == num and config.left_over == 0:
            self.cross(60,250)
            config.left_over = 2
            config.pass_count = 1
        elif config.center_middle == num and config.right_middle == num and config.left_middle == 0:
            self.cross(60,130)
            config.left_middle = 2
            config.pass_count = 1
        elif config.center_under == num and config.right_under == num and config.left_under == 0:
            self.cross(60,10)
            config.left_under = 2
            config.pass_count = 1


        elif config.left_over == num and config.left_middle == num and config.left_under == 0:
            self.cross(60,10)
            config.left_under = 2
            config.pass_count = 1
        elif config.center_over == num and config.center_middle == num and config.center_under == 0:
            self.cross(180,10)
            config.center_under = 2
            config.pass_count = 1
        elif config.right_over == num and config.right_middle == num and config.right_under == 0:
            self.cross(300,10)
            config.right_under = 2
            config.pass_count = 1

        elif config.left_over == num and config.left_under == num and config.left_middle == 0:
            self.cross(60,130)
            config.left_middle = 2
            config.pass_count = 1
        elif config.center_over == num and config.center_under == num and config.center_middle == 0:
            self.cross(180,130)
            config.center_middle = 2
            config.pass_count = 1
        elif config.right_over == num and config.right_under == num and config.right_middle == 0:
            self.cross(300,130)
            config.right_middle = 2
            config.pass_count = 1

        elif config.left_middle == num and config.left_under == num and config.left_over == 0:
            self.cross(60,250)
            config.left_over = 2
            config.pass_count = 1
        elif config.center_middle == num and config.center_under == num and config.center_over == 0:
            self.cross(180,250)
            config.center_over = 2
            config.pass_count = 1
        elif config.right_middle == num and config.right_under == num and config.right_over == 0:
            self.cross(300,250)
            config.right_over = 2
            config.pass_count = 1


        elif config.left_over == num and config.center_middle == num and config.right_under == 0:
            self.cross(300,10)
            config.right_under = 2
            config.pass_count = 1
        elif config.right_over == num and config.center_middle == num and config.left_under == 0:
            self.cross(60,10)
            config.left_under = 2
            config.pass_count = 1

        elif config.left_over == num and config.right_under == num and config.center_middle == 0:
            self.cross(180,130)
            config.center_middle = 2
            config.pass_count = 1
        elif config.right_over == num and config.left_under == num and config.center_middle == 0:
            self.cross(180,130)
            config.center_middle = 2
            config.pass_count = 1

        elif config.center_middle== num and config.right_under == num and config.left_over == 0:
            self.cross(60,250)
            config.left_over = 2
            config.pass_count = 1
        elif config.center_middle == num and config.left_under== num and config.right_over == 0:
            self.cross(300,250)
            config.right_over = 2
            config.pass_count = 1



    #CPU�̎��
    def cpu_turn(self):
    	#�^�񒆂��󂢂Ă�����A�^�񒆂Ɂ~
        if config.center_middle == 0:
            self.cross(180,130)
            config.center_middle = 2
        
        #�󂢂Ă��Ȃ���΁A�p�ɂP��
        elif config.left_over == 0:
            self.cross(60,250)
            config.left_over = 2
        
        elif config.right_over == 0:
            self.cross(300,250)
            config.right_over = 2
        
        elif config.right_under == 0:
            self.cross(300,10)
            config.right_under = 2
        
        elif config.left_under == 0:
            self.cross(60,10)
            config.left_under = 2
        
        elif config.center_over == 0:
            self.cross(180,250)
            config.center_over = 2
        
        elif config.right_middle == 0:
            self.cross(300,130)
            config.right_middle = 2
        
        elif config.center_under == 0:
            self.cross(180,10)
            config.center_under = 2
        
        elif config.left_middle == 0:
            self.cross(60,130)
            config.left_middle = 2
        config.pass_count = 1



    #x�ly�l�̉ӏ��ɁZ��`��
    def whole(self,x,y):
        self.penup()
        self.goto(x,y)
        num = self.heading()
        self.right(num)
        self.pendown()
        self.circle(50)



    #x�ly�l�̉ӏ��Ɂ~��`��
    def cross(self,x,y):
        self.penup()
        self.goto(x,y)
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


if __name__ == "__main__":
    san = Sanmoku()
