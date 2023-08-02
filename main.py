from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, NumericProperty
#import ast

Builder.load_file('home.kv')

#설명하는 주석은 아래쪽에 모으기

class FirstScreen(Screen):
  overview = StringProperty(" 0", font_size=40)
  pass


#global 선언을 통해 모든 곳에서 이용이 가능해집니다.

class CarlApp(App):
  def build(self):
    sm = ScreenManager() #간략화
    sm.add_widget(FirstScreen(name='main'))
    return sm
    #first_screen = self.root.get_screen('main')

  global tool
  tool = ['+', '-', '*', '/']
  
  def add(self, button):
      first_screen = self.root.get_screen('main')
      if first_screen.overview == " 0":  # 추가된 조건
        first_screen.overview = ""
      if first_screen.overview == 'Not divided by 0':
        first_screen.overview = ""
      if first_screen.overview == "Hello World":
        first_screen.overview = ""
      if first_screen.overview != '':
        if CarlApp.can_float(self, button.text) and first_screen.overview == "0":
          first_screen.overview = first_screen.overview[:-1] + button.text
          # 03+3과 같은 입력을 방지
          return
        else:
          pass
      first_screen.overview += button.text
    
  def clear(self):
      first_screen = self.root.get_screen('main')
      first_screen.overview = " 0"
    
  def lastc(self):
      first_screen = self.root.get_screen('main')
      first_screen.overview = first_screen.overview[:-1]
      if first_screen.overview == '':
        first_screen.overview = " 0"
      #리스트의 가장 마지막을 제거함으로써,
      #한 글자만 지워짐(출처: 뤼튼)

  def hello(self):
      first_screen = self.root.get_screen('main')
      first_screen.overview = "Hello World"
  
  def percent(self, button):
      first_screen = self.root.get_screen('main')
      if first_screen.overview == ' 0':
        return
      last = first_screen.overview[-1]
      if last == "%" or last in tool:
        return
      elif last == '(' or last == ')' or last == '.' or last == 'R':
        return
      # 합치면 너무 길다매.. 근데 왜 합치라 해 자
      else:
        CarlApp.add(self, button)

  def namersy(self, button):
      first_screen = self.root.get_screen('main')
      if first_screen.overview == ' 0':
        return
      last = first_screen.overview[-1]
      if last == "R" or last in tool or last == '(' or last == ')' or last == '.':
        return
      else:
        CarlApp.add(self, button)
  def plus(self, button):
      first_screen = self.root.get_screen('main')
      if first_screen.overview == " 0":
        return
      else:
        last = first_screen.overview[-1]
        if last == "+":
           return
        elif last in tool:
          first_screen.overview = first_screen.overview[:-1] + "+"
        elif last == '(' or last == '.':
          return
        else:
          CarlApp.add(self, button)
  
  def double(self, button):
      first_screen = self.root.get_screen('main')
      if first_screen.overview == " 0":
        return
      else:
        last = first_screen.overview[-1]
        if last == "^" or last == '(' or last == '.' or last == '%' or last == 'R':
          return
        else:
          CarlApp.add(self, button)
          #CarlApp.plus_end(self)
      #end_plus =int(first_screen.overview) + int()
      #first_screen.overview = end_plus
    #소수를 위한 덧셈이라 int가 아닌 float를 사용

  def can_float(self, num_str):
    try:
        float(num_str)
        return True
    except ValueError:
        return False
      #GPT 도움. except는 와 대단하긴 함ㅋㅋㅋㅋ

  def zzum(self, button):
      first_screen = self.root.get_screen('main')
      if first_screen.overview == ' 0':
        first_screen.overview = '0.'
      last = first_screen.overview[-1]
      zumspl = first_screen.overview.split('.')
      #마지막, 즉 0.3에서는 0이 유리수가 될 수 있는가?를 확인합니다.
      #만약 0.0.0이라면 될 수 있을 테고,
      #0.3+0 인 상태에서 이 버튼을 눌렀다면 불가능할테니까 말이죠.
      # 이 아이디어는, 제 아이디어입니다. (칭찬해줘!)
      if '.' in first_screen.overview and CarlApp.can_float(self, zumspl[-1]):
          return
      if last == "." or last in tool or last =='(' or last == ')' or last == 'R':
        return
      else:
        CarlApp.add(self, button)
        
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
      else:
          return
  def multi(self, button):
      first_screen = self.root.get_screen('main')
      if first_screen.overview == " 0":
        return
      else:
        last = first_screen.overview[-1]
        if last == "*":
           return
        elif last in tool:
          first_screen.overview = first_screen.overview[:-1] + "*"
        elif last == '(' or last == '.' or last == 'R':
          return
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
    if first_screen.overview == " 0":
        return
    else:
        last = first_screen.overview[-1]
        if last == "-":
            return
        elif last in tool:
            first_screen.overview = first_screen.overview[:-1] + "-"
        elif last == '(' or last == '.' or last == 'R':
          return
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
    if first_screen.overview == " 0":
        return
    else:
        last = first_screen.overview[-1]
        if last == "/":
            return
        elif last in tool:
            first_screen.overview = first_screen.overview[:-1] + "/"
        elif last == '(' or last == '.' or last == 'R':
          return
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

  def gwalh(self):
    first_screen = self.root.get_screen('main')
    if first_screen.overview == ' 0':
      first_screen.overview = ''
    if first_screen.overview == '':
      first_screen.overview += '('
      return
    #first_screen.overview
    last = first_screen.overview[-1]
    if last == '.' or last == '^' :
      return
    elif last == '(':
      first_screen.overview += '('
      return
    elif last == ')':
      first_screen.overview += ')'
      return
    else:
      if last != '(' and '(' in first_screen.overview:
        first_screen.overview += ')'
        return
      else:
        first_screen.overview += '('
      if '+' in last or '-' in last or '*' in last or '/' in last or 'R' in last:
        first_screen.overview += '('
        return
      else:
        #first_screen.overview += ')'
        return
        
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
  
  #기본 계산 함수
  def evla2(self):
    # 퍼센트 계산을 위해서는, 순서를 한번 싹 바꿔야겠군요.
    # 아닌가? 정신이 없어서 잘.. 아무튼 50+5%=52.5와 50-5%-5%=47.125(오류)를 기준으로!
    # 두번째를 위해서는, 50-5%를 먼저 계산해야 합니다. 음
      first_screen = self.root.get_screen('main')
      last = first_screen.overview[-1]
      format0 = first_screen.overview
      if last == '+' or last == '/' or last == 'Hello World' or last == 'R':
        return
      if last== '*' or last == '-' or last == 'Not divided by 0':
        return
      if first_screen.overview.count('(') != first_screen.overview.count(')'):
        return
      #elif '%' in first_screen.overview:
        #format0 = first_screen.overview.replace("%", " / 100")
      format1 = format0.replace("+", " + ")
      format2 = format1.replace("-", " - ")
      format3 = format2.replace("*", " * ")
      format4 = format3.replace("/", " / ")
      format5 = format4.replace("^", " ** ")
      format6 = format5.replace("R", " % ")
      format7 = format6
      if '(' in first_screen.overview and ')' in first_screen.overview:
        screen3 = first_screen.overview.split('(')
        screen4 = screen3[0]
        if screen4 not in tool and screen4 != '':
          format7 = format6.replace('(', ' * ( ')
        else:
          format7 = format6
      global result
      result = eval(format7)
        
      #print(format)
      if result == int(result):  # 결과가 정수인 경우 소수점 제거
          result = int(result)
      if result == 0:
          result = " 0" # 되면 천재임ㅋㅋ
      first_screen.overview = str(result)

if __name__ == '__main__':
  CarlApp().run()

