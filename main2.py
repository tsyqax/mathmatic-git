from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, NumericProperty
#import ast


'''
<개발 진행도>
사칙연산: 75%
괄호: 11%
유리수: 40%
기호?: 6%

<누적 업데이트 내역>
-기본적인 앱 구성(7/12)
-버튼 추가 및 기본 인터페이스(7/12)
-'입력' 구현(7/12)
-%, + 등의 기호 입력 중복 방지(7/13)
-덧셈, 뺄셈, 나눗셈, 곱셈 구현(7/13)
-버튼에 색을 입혀 가시성 향상(7/13)
-높이에 따라 버튼의 글자 크기 조절(7/13)
-나눗셈 0 기능 추가 & 문제 해결(7/14)
-원시적인 사칙연산 추가(7/20)
'''
Builder.load_file('home.kv')

#설명하는 주석은 아래쪽에 모으기

class FirstScreen(Screen):
  overview = StringProperty("0", font_size=40)
  pass

global tool
tool = ['+', '-', '*', '/']
#global 선언을 통해 모든 곳에서 이용이 가능해집니다.

class CarlApp(App):
  def build(self):
    sm = ScreenManager() #간략화
    sm.add_widget(FirstScreen(name='main'))
    return sm
    #first_screen = self.root.get_screen('main')
  
  def add(self, button):
      first_screen = self.root.get_screen('main')
      if first_screen.overview == "0":  # 추가된 조건
        first_screen.overview = ""
      if first_screen.overview == 'Not divided by 0':
        first_screen.overview = ""
      first_screen.overview += button.text
    
  def clear(self):
      first_screen = self.root.get_screen('main')
      first_screen.overview = "0"
    
  def lastc(self):
      first_screen = self.root.get_screen('main')
      first_screen.overview = first_screen.overview[:-1]
      if first_screen.overview == '':
        first_screen.overview = "0"
      #리스트의 가장 마지막을 제거함으로써,
      #한 글자만 지워짐(출처: 뤼튼)
  
  def percent(self, button):
      first_screen = self.root.get_screen('main')
      last = first_screen.overview[-1]
      if last == "%":
           return
      else:
        CarlApp.add(self, button)
  def plus(self, button):
      first_screen = self.root.get_screen('main')
      if first_screen.overview == "":
        return
      else:
        last = first_screen.overview[-1]
        if last == "+":
           return
        elif last in tool:
          first_screen.overview = first_screen.overview[:-1] + "+"
        else:
          CarlApp.add(self, button)
          #CarlApp.plus_end(self)
      #end_plus =int(first_screen.overview) + int()
      #first_screen.overview = end_plus
    #소수를 위한 덧셈이라 int가 아닌 float를 사용
  def plus_end(self, parts):
      first_screen = self.root.get_screen('main')
      if '+' in first_screen.overview:
        last = first_screen.overview[-1]
        if last == "+":
           return
        #parts = first_screen.overview.split('+')
        if len(parts) >= 2: # '+' 기호 개수가 3개 이상인 경우
          #if parts[0] == '':
            #end_multi2 = float('0') #덧셈은 필요 없는 코드
          end_plus2 = sum(float(num) for num in parts)# 모든 숫자를 더함
          #if end_plus2.is_integer():
            #is_integer는 literal 타입에서는 사용 불가이므로 변경
          if end_plus2 == int(end_plus2):
            end_plus2 = int(end_plus2)
          return end_plus2
          '''else:
          num1 = parts[0]
            #
          num2 = parts[1]
          if '*' in num2 or num1:
            return
          if num2 == '':
            return'''
          #end_plus = float(num1) + float(num2)
        #if '+' in first_screen.overview:
          #first_screen.overview = 
          #if end_plus.is_integer():
            #end_plus = int(end_plus)
          #first_screen.overview = str(end_plus)
      else:
          return
  def multi(self, button):
      first_screen = self.root.get_screen('main')
      if first_screen.overview == "":
        return
      else:
        last = first_screen.overview[-1]
        if last == "*":
           return
        elif last in tool:
          first_screen.overview = first_screen.overview[:-1] + "*"
        else:
          CarlApp.add(self, button)
          if '*' not in first_screen.overview:
            return
  def multi_end(self, parts):
    first_screen = self.root.get_screen('main')
    if '*' in first_screen.overview:
      last = first_screen.overview[-1]
      if last == "+":
          return
      else:
        #parts = first_screen.overview.split('*')
        if len(parts) >= 2:
            end_multi2 = 1
            if parts[0] == '':
              end_multi2 = float('0')
            for num in parts:
                if num != '':
                    end_multi2 *= float(num)
            if end_multi2 == int(end_multi2):  # 결과가 정수인 경우 소수점 제거
                end_multi2 = int(end_multi2)
            return end_multi2
          # 곱셈 쪽은 완전히 AI에게 도움받았습니다.
          # 추후에 다시 공부해 올게요ㅠ
    else:
      return
  def minus(self, button):
    first_screen = self.root.get_screen('main')
    if first_screen.overview == "":
        return
    else:
        last = first_screen.overview[-1]
        if last == "-":
            return
        elif last in tool:
            first_screen.overview = first_screen.overview[:-1] + "-"
        else:
            CarlApp.add(self, button)
  def minus_end(self, parts):
      first_screen = self.root.get_screen('main')
      if '-' in first_screen.overview:
        last = first_screen.overview[-1]
        if last == "-":
           return
        #parts = first_screen.overview.split('-')
        if len(parts) >= 2:
          if parts[0] == '':
            end_minus2 = float('0')
          end_minus2 = float(parts[0]) #초기 값으로 설정해주어야 함
          for num in parts[1:]:
            if num != '':
                end_minus2 -= float(num)
            if end_minus2 == int(end_minus2):
              end_minus2 = int(end_minus2)
            return end_minus2
          
  def divide(self, button):
    first_screen = self.root.get_screen('main')
    if first_screen.overview == "":
        return
    else:
        last = first_screen.overview[-1]
        if last == "/":
            return
        elif last in tool:
            first_screen.overview = first_screen.overview[:-1] + "/"
        else:
            CarlApp.add(self, button)
  def divide_end(self, parts):
      first_screen = self.root.get_screen('main')
      if '/' in first_screen.overview:
        last = first_screen.overview[-1]
        if last == "/":
           return
        #parts = first_screen.overview.split('/')
        if len(parts) >= 2:
          if parts[0] == '':
            end_divide2 = float('0')
            #first_screen.overview = '0으로는 나눌 수 없습니다.'
          end_divide2 = float(parts[0]) #초기 값으로 설정해주어야 함
          for num in parts[1:]:
            if num == '':
              return
            elif num == '0':
              first_screen.overview = 'Not divided by 0'
              return
            else:
              end_divide2 /= float(num)
            if end_divide2 == int(end_divide2):
              end_divide2 = int(end_divide2)
            return end_divide2
  def action(self):
    first_screen = self.root.get_screen('main')
    if '+' in first_screen.overview and '*' in first_screen.overview:
        # 덧셈과 곱셈이 모두 포함된 경우
        parts = first_screen.overview.split('+')
        result = 0
        for part in parts:
            if '*' in part:
                # 곱셈 수행
                multiply_parts = part.split('*')
                multiply_result = 1
                for num in multiply_parts:
                    if num != '':
                        multiply_result *= float(num)
                result += multiply_result
            else:
                # 덧셈 수행
                if part != '':
                    result += float(part)

  def action2(self):
    first_screen = self.root.get_screen('main')
    screen = first_screen.overview
    app = CarlApp
    #precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    #oper = []
    #floats = []
    #계산 주의사항, 일단 나누고, 그 기호로 계산하는 것임
    if '+' in screen: #일단 덧셈 기호가 있고
      parts1 = screen.split('+')
      for parts2 in parts1:
        if '-' in parts2:
          parts3 = parts2.split('-')
          for parts4 in parts3:
            if '*' in parts4: #덧셈 뺄셈 곱셈
              parts5 = parts4.split('*')
              for parts6 in parts5:
                if '/' in parts6: #덧셈 뺄셈 곱셈 나눗셈
                  parts7 = parts6.split('/')
                  parts7 = app.divide_end(self, parts7) #새로운 7번
                  parts67 = parts6 + parts7
                  parts6 = app.multi_end(self, parts67)
                  parts56 = parts5 + parts6
                  parts5 = app.minus_end(self, parts56)
                  parts45 = parts4 + parts5
                  parts4 = app.plus_end(self, parts45)
                  screen = str(parts4)
                  return
                else:  #덧셈 뺄셈 곱셈
                  parts6 = app.multi_end(self, parts6)
                  parts56 = parts5 + parts6
                  parts5 = app.minus_end(self, parts56)
                  parts45 = parts4 + parts5
                  parts4 = app.plus_end(self, parts45)
                  screen = str(parts4)
                  return
            if '/' in parts4: #덧셈 뺄셈 나눗셈(곱셈 없음)
              parts5 = parts4.split('/')
              parts5 = app.divide_end(self, parts5) #새롭게 정의
              parts45 = parts4 + parts5
              parts4 = app.minus_end(self, parts45)
              parts34 = parts3 + parts4
              parts3 = app.plus_end(self, parts34)
              screen = str(parts3)
              return
          #merged_list = list1 + list2 + list3 #리스트 합체
          ''' else: #덧셈 뺄셈 (나눗셈 뺄셈 없음)
          parts2 = app.minus_end(self, parts2)
          parts12 = parts1 + parts2
          parts1 = app.plus_end(self, parts12)
          screen = str(parts1)
          return'''
        if '*' in parts2:  #덧셈 곱셈(뺄셈 없음)
          parts3 = parts2.split('*')
          for parts4 in parts3:
            if '/' in parts4: #덧셈 곱셈 나눗셈(뺄셈 없음)
              parts5 = parts4.split('/')
              parts5 = app.divide_end(self, parts5)
              parts45 = parts4 + parts5
              parts4 = app.multi_end(self, parts45)
              parts34 = parts3 + parts4
              parts3 = app.plus_end(self, parts34)
              screen = str(parts3)
              return
            else: #덧셈 곱셈(뺄셈 없음)
              parts4 = app.multi_end(self, parts4)
              parts34 = parts3 + parts4
              parts3 = app.plus_ennd(self, parts34)
              screen = str(parts3)
              return
        if '/' in parts2: #덧셈 나눗셈
          parts3 = parts2.split('/')
          parts3 = app.divide_end(self, parts3)
          parts23 = parts2 + parts3
          parts2 = app.plus_end(self, parts23)
          screen = str(parts2)
          return
        else: #덧셈만
          parts2 = app.plus_end(self, parts2)
          screen = str(parts2)
          return
        #if문이 안 된다면은 분할을 for 구문으로 돌리셈
        #ㅇㅇ 그러는 중

    
    if '-' in screen: #뺄셈 포함
      parts1 = screen.split('-')
      for parts2 in parts1:
        if '+' in parts2: #뺄셈 덧셈
          parts3 = parts2.split('+')
          for parts4 in parts3:
            if '*' in parts4: #뺄셈 덧셈 곱셈
              parts5 = parts4.split('*')
              for parts6 in parts5:
                if '/' in parts6: #뺄셈 덧셈 곱셈 나눗셈
                  parts7 = parts6.split('/')
                  parts7 = app.divide_end(self, parts7)
                  parts67 = parts6 + parts7
                  parts6 = app.multi_end(self, parts67)
                  parts56 = parts5 + parts6
                  parts5 = app.plus_end(self, parts56)
                  parts45 = parts4 + parts5
                  parts4 = app.minus_end(self, parts45)
                  screen = str(parts4)
                  return
                else: #뺄셈 덧셈 곱셈
                  parts6 = app.multi_end(self, parts6)
                  #이거 이상하면 함수의 6을 5로 바꾸세요.
                  parts56 = parts5 + parts6
                  parts5 = app.plus_end(self, parts56)
                  parts45 = parts4 + parts5
                  parts4 = app.minus_end(self, parts45)
                  screen = str(parts4)
                  return
            if '/' in parts4: #뺄셈 덧셈 나눗셈(곱셈 없음)
              parts5 = parts4.split('/')
              parts5 = app.divide_end(self, parts5)
              parts45 = parts4 + parts5
              parts4 = app.plus_end(self, parts45)
              parts34 = parts3 + parts4
              parts3 = app.minus_end(self, parts34)
              screen = str(parts3)
              return
            else: #뺄셈 덧셈
              #4에 있지 않다면, 쪼개지 않고 바로 대입
              parts4 = app.plus_end(self, parts4)
              parts34 = parts3 + parts4
              parts3 = app.minus_end(self, parts34)
              screen = str(parts3)
              return
        if '*' in parts2: #뺄셈 곱셈
          parts3 = parts2.split('*')
          for parts4 in parts3:
            if '/' in parts4: #뺄셈 곱셈 나눗셈
              parts5 = parts4.split('/')
              parts5 = app.divide_end(self, parts5)
              parts45 = parts4 + parts5
              parts4 = app.multi_end(self, parts45)
              parts34 = parts3 + parts4
              parts3 = app.minus_end(self, parts34)
              screen = str(parts3)
              return
            else: #뺄셈 곱셈
              parts4 = app.multi_end(self, parts4)
              parts34 = parts3 + parts4
              parts3 = app.minus_end(self, parts34)
              screen = str(parts3)
              return
        if '/' in parts2: #뺄셈 나눗셈
          parts3 = parts2.split('/')
          parts3 = app.divide_end(self, parts3)
          parts23 = parts2 + parts3
          parts2 = app.minus_end(self, parts23)
          screen = str(parts2)
          return
        else: #뺄셈만
          parts2 = app.minus_end(self, parts2)
          screen = str(parts2)
          return
    if '*' in screen and '-' not in screen and '+' not in screen:
      parts1 = screen.split('*') #곱셈
      for parts2 in parts1:
        if '/' in parts2: #곱셈 나눗셈만
          parts3 = parts2.split('/')
          parts3 = app.divide_end(self, parts3)
          parts23 = parts2 + parts3
          parts2 = app.multi_end(self, parts23)
          screen = str(parts2)
          return
        else: #곱셈만
          parts2 = app.multi_end(self, parts2)
          screen = str(parts2)
          return
    if '/' in screen and '-' not in screen and '+' not in screen:
      parts1 = screen.split('/') #나눗셈
      for parts2 in parts1:
        if '*' in parts2: #나눗셈 곱셈만
          parts3 = parts2.split('*')
          parts3 = app.multi_end(self, parts3)
          parts23 = parts2 + parts3
          parts2 = app.divide_end(self, parts23)
          screen = str(parts2)
          return
        else: #나눗셈만
          #값이 오류가 있을 때는 else 구문의 숫자를 조정해보세요.
          #왜냐면 헷갈려.. 2일까 1일까
          parts2 = app.divide_end(self, parts2)
          screen = str(parts2)
          return
    else:
      return

#값이 오류가 있을 때는 else 구문의 숫자를 조정해보세요.
#이래도 안되면 ㅈㅅ..이 아니라 eval 쓰러 튈거임 ㅅㄱ
  
  '''
  def megaction(self):
      first_screen = self.root.get_screen('main')
      overview = first_screen.overview
      parsed_expression = ast.parse(overview, mode='eval')
      result1 = eval(compile(parsed_expression, filename='<ast>', mode='eval'))
      overview = result1
      '''
if __name__ == '__main__':
  CarlApp().run()

#아, 참고로 overview라는 게 현재 띄우는 숫자이고
#add는 숫자 누를 때, clear는 CE, lastc는 <-에 해당하는 기능들

#button값이 함수에서 사용되는 경우,
#kv파일에서 app.add(self)와 같이 self를 추가해주어야 합니다.
#버튼의 self값이 여기 함수에서는 button 값

#first_screen = self.root.get_screen('main')은
#main의 스크린을 가져온다는 거 같은데, 나도 모름

#app.add()와 같은 건 app의 add 함수를 불러오는 겁니다.
#또한 초기 화면은 home.kv랍니다.
