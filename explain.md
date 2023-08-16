안녕하세요.   
코드를 설명하려고 합니다.   
(실제로 앱에서 사용되는 코드만)

각 부분에는 더욱 유용한 참고를 위해, 링크를 달아두었습니다.   
(파란색 글씨)


***
## 전체 코드 확인하기
[main.py](https://github.com/tsyqax/mathmatic-git/blob/main2/main.py)   
[home.kv](https://github.com/tsyqax/mathmatic-git/blob/main2/home.kv)

***
### [파이썬의 문자 타입](https://m.blog.naver.com/youndok/222027341773)
**String(str)** 이라고 하는 건 글자나, 문자 그 자체를 의미합니다. ex/ '안녕하세요', 'Hello World' 등등   
**Integer(int)** 라고 하는 건, 정수인 숫자의 형태를 의미합니다. ex/ 3, 7, -20 등등   
**Float(float)** 소수점까지 포함한 숫자 형태를 의미합니다. ex 20.5와 -31.2 같은 것들

각각의 정의는 다른 형식으로 이루어집니다.
(특히, str과 int)

str은 "큰 따옴표"나 '작은 따옴표'를 이용하여 정의합니다.   
실제로 사용하려면,   
변수 = "문자" 와 같이 정의하는 거죠.

int는 그냥 숫자 그대로 정의합니다.   
변수 = 0 과 같이 정의하면, 변수는 **숫자형 0(숫자 0)** 이 정의됩니다.


그리고 중요한 건,   
- 변수 = "0" 으로 정의한 건 str(문자 타입)  
- 변수 = 0 으로 정의한 건 int(정수 타입)

이와 같이 달라진다는 점입니다.   

우리 코드에서 사용되는 건 저 3가지이고, 나머지가 더 궁금하시면 링크를 참고하세요.

---
### [파이썬 코드 작성](https://namu.wiki/w/Python)
파이썬도 파이썬이지만, 기본적으로 코드를 작성할 때는 **들여쓰기**가 엄청 중요합니다.   
들여쓰기에 따라, 실행될 코드가 달라지기도 하니까 말이에요.    

들여쓰기는 일반적으로 **Tap** 또는 **스페이스 바 4번**으로 합니다.   
(스페이스 바 2번의 들여쓰기를 지원하기도 합니다.)   

**들여쓰기를 하는 경우:**
- 구문 안으로 들어왔다
- 함수 안으로 들어왔다
- 클래스 안으로 들어왔다

(들여쓰기를 하는 더 자세한 경우는 검색하기) 

---
### [파이썬 라이브러리](https://min-zero.tistory.com/entry/Python-%EA%B8%B0%EB%B3%B8-%EA%B3%B5%EB%B6%80%EC%A0%95%EB%A6%AC-13-1-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AClibrary)란?
**다른 사람들이 만들어둔 유용한 코드 모음집** 정도로 생각하시면 될 것 같아요.   

위 링크에 따르면,   
> 라이브러리는 **필요한 코드를 재사용하기 위해   
언제든지 필요한 곳에서 호출할 수 있도록 개발자들에 의해서   
이미 만들어진 클래스나 함수를 모아놓은 것**을 말한다.
>
...라고 하는군요.

***
### 파이썬 --> 앱 설명
기본적으로, 파이썬 코드는 앱으로 만들 수 없습니다.   
그러나 일부 도구를 사용하면, 이를 가능하게 하죠.   
   
그 중, 우리가 사용할 도구는... **[Kivy](https://kivy.org/)**라는 파이썬 라이브러리입니다.
   

**"그냥 이런게 있구나~"** 정도로만 알아도, 파이썬 코딩에는 무방합니다.   
저도 사용할 때마다 필요한 건 검색해보니까 말이죠..
***
### .py? .kv? 이게 뭐죠?
이 녀석들은 [파일 확장자](https://terms.naver.com/entry.naver?docId=3572614&cid=59088&categoryId=59096)입니다.   
대충, 그 파일의 성격을 결정하는 것들이라고 아시면 될 듯합니다.

**.py는 파이썬 파일의 확장자**를,   
.kv는 Kivy 파일의 확장자를 의미합니다.   
   
이 프로젝트에서는 main.py와 home.kv로 존재합니다.
***
## 본격적 코드 설명
자, 우리가 살펴볼 파일은 **main.py**입니다.

---
```(python) from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, NumericProperty
```
이 코드들은 kivy 라이브러리가 상속하고 있는 모듈로부터 **각각의 함수를 불러옵니다.**

모듈이나 함수의 이름들은 자주 변경되기 때문에 이름보다는 구조를 아는 게 더 유용합니다.

`from ㅁㅁㅁ import ㅊㅊㅊ`   
여기에서는, ㅁㅁㅁ**으로부터** ㅊㅊㅊ라는 함수를 **불러옵니다.**

아니면 라이브러리(모듈) 전체를 한번에 불러올 수도 있습니다.
   
`import ㅊㅊㅊ`   
이와 같이 말이죠.   
하지만, 이를 위해서는 'ㅊㅊㅊ'라는 라이브러리(모듈)이 파이썬 패키지로 존재하고 있어야 합니다.

---
`Builder.load_file('home.kv')` 에서는 home.kv라는 파일을 로드합니다.   
*(위와 같은 경우는 builder라는 모듈로 한정됩니다. 실제 사용 코드는 [링크](https://opentutorials.org/module/2980/17643#:~:text=%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%8C%8C%EC%9D%BC%20%EB%B6%88%EB%9F%AC%EC%98%A4%EA%B8%B0%201%20%ED%8C%8C%EC%9D%BC%20%ED%86%B5%EC%A7%B8%EB%A1%9C%20%EB%B6%88%EB%9F%AC%EC%98%A4%EA%B8%B0%201%202,%26%20%EB%B3%91%ED%95%A9%201%202%203%20string%20%3D%27%27%20)를 참고하세요.)*

---
``` (python)
class FirstScreen(Screen):
  overview = StringProperty(" 0", font_size=40)
  pass
```
여기에서는, **FirstScreen**이라는 [클래스](https://ybworld.tistory.com/20)를 정의합니다.   
이 클래스가 가지는 overview라는 것이 " 0"임을 선언하고 있네요.   
*(클래스는 저도 약한 부분이라, 자세한 것은 인터넷과 위 링크를 참고하세요!!)*

---
``` (python)
#global 선언을 통해 모든 곳에서 이용이 가능해집니다.

class CarlApp(App):
  def build(self):
    sm = ScreenManager() #간략화
    sm.add_widget(FirstScreen(name='main'))
    return sm
    #first_screen = self.root.get_screen('main')
```
이 클래스 정의가, 우리 앱의 **전신**이라고 해도 무방합니다.   
(우리가 앱을 만드는 특수한 상황이기 때문에, 이후의 함수를 이 클래스 안에 정의합니다.)


`def build(~~)`는 build라는 함수를 **정의한다**는 것인데,  
이 앱에서의 build 함수는 뼈대가 되긴 하지만 우리가 크게 배울건 없으니 넘어갈게요.

```
그래도 알고싶다고요?
아까 우리가 불러왔던 ScreenManager라는 함수를
sm으로 정의하고, sm에 main이라는 위젯을 추가하는... 대충 뭐 그런거...
(저도 잘 몰라유;;)
```
---
```(python)
global tool
  tool = ['+', '-', '*', '/']
```
이 코드는 변수의 선언과 관련된 코드입니다.   
일반적으로, 함수 내에서 정의되는 변수는 다른 함수에서는 **읽기 전용**과 같은 상태가 됩니다.   
(함수 밖에서 정의하면, 모든 함수에 대해 **읽기 전용**이 됩니다.)

이때, `global (함수 이름)`을 사용하면, [전역 변수](https://code.youngxdev.com/68)로 선언하게 됩니다.   
그리고 전역 변수는, **모든 함수에서 수정할 수 있는 변수**이죠.

---
``` (python)
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
```
버튼의 글자를 화면에 입력하는 add 함수입니다.   
(이와 같이, 앞으로 소개하는 함수들은 직접 이 코드에서 정의된 함수들입니다.)

여기서는 꽤 볼게 많네요.  

**1**
`def 함수(var)`과 같이 정의하면, 이 함수는 함수 내부에서 정의된 **var**라는 값을 필요로 하는 함수가 됩니다.   
이렇게 되면, var를 제공해주어야 제대로 작동하게 되는거죠.   

**2. if-else 구문**   
굉장히 자주 사용하게 될 구문입니다.   
`if (조건문)` 과 같이 if를 사용하여, 조건에 해당하는지를 확인합니다.   
만약 해당하게 된다면, if문 아래에 정의된 코드를 실행하게 되는거죠.

`elif (조건문)` 과 같은 건, '그게 아냐? 만약 ~라면?' 과 같은 내용이죠.   
```
if (조건문)
  코드1
if (조건문)
  코드2
```
위와 같은 경우와,

```
if (조건문)
  코드3
elif (조건문)
  코드4
```
이 두번째 경우는 전혀 다른 경우가 됩니다.   

첫번째는 처음 if문에 해당된다면 코드1을, 아니라면 지나칩니다.   
또한, 두번째 if문에 해당된다면 코드2를, 아니라면 지나칩니다.   
(그러니까, 코드1과 코드2가 모두 실행되거나, 아무것도 실행되지 않을 수 있는겁니다.)   

두번째는 처음 if문에 해당된다면 코드3을 실행하고, elif문은 무시합니다.   
그리고 if문에 해당하지 않으면, elif문을 확인하고, 만약 해당되면 코드4를 실행합니다.   
(그러니까 아무것도 실행되지 않을 망정, 코드3과 코드4가 모두 실행되지는 않는거죠)   

`else:` 는 위에서 제시된 if문들에 **하나도 해당되지 않은 경우** 실행하게 되는 구문입니다.   
그러니까, 위의 if와 elif문들을 다 지나치면, else 아래에 정의된 코드를 실행하게 되는거죠.   
(만약 else문을 작성하지 않았는데, if(elif)문에 하나도 해당하지 않았다면, 아무 코드도 실행하지 않아서, 아무 일도 없게 됩니다.)

---
**first_screen = self.root.get_screen('main')**   
이는 저도 잘 알지는 못하는 코드이나, 모든 함수에 정의되었기 때문에 간략히 설명합니다.   
(아까 우리가 main으로 정의한 화면(스크린)을 가져오는 코드이죠.)   

**first_screen.overview += button.text**   
이건 first_screen.overview라는 변수를, button.text라는 값을 더하여 저장하는 코드입니다.   
만약 두 변수가 str이라면 합쳐진 문자열이,   
int나 float이라면 수학적으로 더해진 값이 저장되게 됩니다.   

아, 그리고 first_screen.overview는 앞으로 **screen**이라고 이야기하겠습니다.   
(왜냐고? 타자 치기 귀찮아요...) 

```                                       ```   
그래서, 이 부분의 코드를 한글로 번역하면 다음과 같습니다.
```
add 함수 정의(button 값 필요)
  만약 screen이 " 0"이라면:
    screen을 ""로 바꾼다

  만약 screen이 "Not divided by 0"이라면:
    screen을 ""로 바꾼다

(중략)

  만약 button.text가 소수가 될 수 있고, screen이 "0"이라면:
    screen의 마지막 문자열을 지우고 button을 더한다.

  아니라면:
    통과한다

(후략)
```
---
``` (python)
  def clear(self):
      first_screen = self.root.get_screen('main')
      first_screen.overview = " 0"
```
이 코드는 **C**의 함수, 즉 전체 지우기 함수입니다.   
전체 지우기는 간단하죠?   
그냥 screen 자체를 초기 상태로 새롭게 정의해버리면 그만입니다.   

---
``` (python)
  def lastc(self):
      first_screen = self.root.get_screen('main')
      first_screen.overview = first_screen.overview[:-1]
      if first_screen.overview == '':
        first_screen.overview = " 0"
      #한 글자만 지워짐(출처: 뤼튼)
```
지우기, Backspace에 해당하는 함수입니다.   
screen의 문자열 중에서, [-1]의 위치에 해당하는 문자열을 제거합니다.   
(자세한 건 검색 plz)   

---
``` (python)
  def hello(self):
      first_screen = self.root.get_screen('main')
      first_screen.overview = "Hello World"
```
이 함수는 Hello World를 출력하는 hello 함수입니다.   
위의 clear 함수에서 초기 상태로 정의했다면,   
이거는 "Hello World"로 정의하여, Hello world를 출력하게 만듭니다.   

---
``` (python)
  def namersy(self, button):
      first_screen = self.root.get_screen('main')
      if first_screen.overview == ' 0':
        return
      last = first_screen.overview[-1]
      if last == "R" or last in tool or last == '(' or last == ')' or last == '.':
        return
      else:
        CarlApp.add(self, button)
```
이 함수는 나머지 기호 R을 입력하는 함수인 **namersy 함수**입니다.
마지막 글자([-1]의 위치)가 어떤 문자인지 확인하는 if문이 있고, 그에 따른 실행 코드가 있습니다.
(tool은 아까 우리가 정의한 리스트를 가리킵니다.)   

여기서는 R이나 사칙연산 기호, 괄호와 점인 경우는 Return하고   
아닌 경우는 add 함수를 호출합니다.   
*(원래는 그냥 호출해도 되는 거지만, Class 내부에 함수를 정의하기 때문에, "클래스 이름.함수(~~)"로 불러와야 합니다.)*   

---
``` (python)
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
```
(덧셈, 곱셈, 뺄셈, 나눗셈, 거듭제의 입력 함수는 같은 패턴이므로 덧셈만 설명합니다.)   
여기도 우리가 알아왔던 **if-else**구문이 주로 사용됩니다.   

`first_screen.overview = first_screen.overview[:-1] + "+"`   
여기서는 만약 마지막 글자가 사칙연산 기호 중 하나인 경우, 마지막 글자를 지우고 +를 입력합니다.   
(만약 +인 경우는 이 이전의 if문에 해당되어 이 elif문은 무시됩니다.)

---
``` (python)
  def can_float(self, num_str):
    try:
        float(num_str)
        return True
    except ValueError:
        return False
      #GPT 도움. except는 와 대단하긴 함ㅋㅋㅋㅋ
```
이 코드는 앞서 add 함수의 if 구문에 사용되었던 함수입니다.   

float(num_str)이 가능한 경우(즉, 소수에 해당하는 경우)는 True를...
만약 오류(valueError-값 오류)가 발생한다면 False를 반환합니다.

※참고로 if문이 해당된다는 건, 조건문이 True가 된다는 것을 의미합니다.
```
예를 들어,
if (조건문) 에서
조건문이 True라면 if 구문 내부의 코드가 실행될 테고,
또한 조건에 해당하는 거겠죠?
```

---
``` (Python)
  def zzum(self, button):
      first_screen = self.root.get_screen('main')
      if first_screen.overview == ' 0':
        first_screen.overview = '0.'
      last = first_screen.overview[-1]
      zumspl = first_screen.overview.split('.')
      if '.' in first_screen.overview and CarlApp.can_float(self, zumspl[-1]):
          return
      if last == "." or last in tool or last =='(' or last == ')' or last == 'R':
        return
      else:
        CarlApp.add(self, button)
```
소수점을 입력하는 zzum 함수입니다.   
개인적으로 가장 만족하는 부분이기도 하죠.   

소수점이 연속으로 입력되는(0....과 같은) 경우를 막는 건 간단합니다.   
앞에서 봐왔던 **마지막 글자가 ~~라면**을 이용하면 충분하죠.

그러나, 간헐적으로 중복되어 입력되는(0.0.0.3과 같은) 경우를 막는 건 다른 조치가 필요했어요.   
아래는 이를 위해 작성해둔 구현 방식입니다.

```
기본적으로 초기 화면에서 점을 입력하는 경우는, "0."으로 반환합니다.

그리고 예를 들어보면,
"3.0+3"인 상태와
"3.0"인 상태를 예로 들겠습니다.

screen의 문자열을 점을 기준으로 분할하고, 그 분할된 것들 중 가장 마지막 문자열이
소수가 될 수 있는지 확인합니다.

만약 기호가 들어가서 점으로 나눈 마지막 부분이 "0+3"과 같았다면, 소수가 될 수 없을테니 말이죠.
그런데 기호가 들어가 있지 않다면, 즉 점으로 분할한 마지막 부분이 "0"이 된다면, 소수가 될 수 있으니까요.

그렇게 소수가 될 수 없다면, 점을 입력하고,
소수가 될 수 있을 때는 점을 입력하지 않습니다.
(이때 점을 입력하면 3.0.과 같은 형태가 되어버리니까요.)
```
챗 GPT에게 도움을 요청해도 유용한 답변이 없었기 때문에,   
고민하고 고민해서 생각해낸 방법입니다.   
(칭찬해줘!)

---
``` (python)
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
```
이게 그 괄호 함수입니다.   
뭔가 더 복잡한 코드를 쓰기보다는,   
사람들이 자주 사용하는 경우를 if-else로 구분해서, 간단하게 만들었습니다.   

막고자 했던 경우는 아래와 같습니다.
```
)와 같이 빈 공간에 괄호를 먼저 닫아버리는 경우
())))와 같이 괄호만 닫아버리는 경우
232)))와 같이 열지도 않고 괄호를 닫는 경우
232+)와 같이 기호 바로 다음에 입력되는 경우
괄호 열기와 닫기의 개수가 맞춰지지 않는 경우---새로운
```

---
``` (python)
  def evla2(self):
      first_screen = self.root.get_screen('main')
      last = first_screen.overview[-1]
      format0 = first_screen.overview
      if last == '+' or last == '/' or last == 'Hello World' or last == 'R':
        return
      if last== '*' or last == '-' or last == 'Not divided by 0':
        return
      if first_screen.overview.count('(') != first_screen.overview.count(')'):
        return
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
      if result == int(result)
          result = int(result)
      if result == 0:
          result = " 0"
      first_screen.overview = str(result)
```
그리고 대망의 계산 함수입니다.   
지금까지는 기호, 숫자의 입력만 구현해왔다면, 여기서는 실질적 기능을 구현해야죠.   

이 부분이 코드가 길기 때문에, 나누어서 설명하겠습니다.

---

``` (python)
      first_screen = self.root.get_screen('main')
      last = first_screen.overview[-1]
      format0 = first_screen.overview
      if last == '+' or last == '/' or last == 'Hello World' or last == 'R':
        return
      if last== '*' or last == '-' or last == 'Not divided by 0':
        return
      if first_screen.overview.count('(') != first_screen.overview.count(')'):
        return
```
이 부분은 evla2 함수의 기본 변수의 정의가 있습니다.   
또한, 그냥 계산해버리면 오류가 발생하는 상황에는 **[return(함수를 즉시 종료함)](https://velog.io/@cha-suyeon/Python-%ED%95%A8%EC%88%98%EC%97%90%EC%84%9C-return%EC%9D%98-%EC%93%B0%EC%9E%84)** 하는 if문이 있죠.

---
``` (python)
      format1 = format0.replace("+", " + ")
      format2 = format1.replace("-", " - ")
      format3 = format2.replace("*", " * ")
      format4 = format3.replace("/", " / ")
      format5 = format4.replace("^", " ** ")
      format6 = format5.replace("R", " % ")
      format7 = format6
```
이 부분은 문자열에서 특정 글자를 [교환(replace)](https://codechacha.com/ko/python-replace-string-in-string/)하는 코드입니다.   
이 교환은 str만 가능합니다.   

사용법은 아주 간단합니다.
``` (python)
input = "hello world"
output = input.replace("hello", "world")

print(output) # 콘솔에 출력하는 print... 결과: world world
```
위와 같이 `str.replace("원래 문자", "바뀌고 난 글자")`로 사용할 수 있습니다.   
*(더 자세한 사용법은 링크를 참고하세요...)*

---
``` (python)
      if '(' in first_screen.overview and ')' in first_screen.overview:
        screen3 = first_screen.overview.split('(')
        screen4 = screen3[0]
        if screen4 not in tool and screen4 != '':
          format7 = format6.replace('(', ' * ( ')
        else:
          format7 = format6
```
그리고 **현재 오류가 있는 괄호 처리** 부분....   

오류가 있는 괄호 부분의 핵심 내용은 아래와 같습니다.
- 만약 ( 앞에 기호가 없다면, " * ("와 같이 곱셈을 포함하도록
- 만약 ( 앞에 기호가 있다면, 그대로 유지하도록

근데, 오류가 있는 부분은 바로 앞의 부분을 찾아야 한다는 겁니다.   
지금 코드 상으로는 바로 앞을 알아낼 수 없죠   
(괄호가 많아지면 일일이 지정할 수 없어서...)    
~~더 찾아보면 해결할 수 있을지 몰라도...~~

---
``` (python)
      global result
      result = eval(format7)
      if result == int(result):  # 결과가 정수인 경우 소수점 제거
          result = int(result)
      if result == 0:
          result = " 0"
      first_screen.overview = str(result)
```
그리고 결과를 출력하는 부분입니다.    
result를 global로 선언한 것은, 현재 코드로는 필요없는 부분입니다.   
(다른 함수에서 result를 사용하지 않기 때문)

result의 값이 정수의 result와 같다면 정수의 result로,   
아니라면 if문에 해당하지 않아 지나칩니다.

만약 결과가 0이라면, " 0"으로(초기 화면의 0으로) 변경해서 반환합니다.

---
``` (python)
if __name__ == '__main__':
  CarlApp().run()
```
앱을 구동하는 부분인 것 같아요.   
[저도 모르는 부분](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)이라 설명은 지나갑니다.

---
## 마치며
솔직히 이 글이 도움되리라고는 생각하지 않습니다.   
제가 설명을 엄청 못하기 때문이죠.   

또한 정식으로 파이썬을 배운 적이 없기 때문에,   
완벽하고 깔끔하게 알려드릴수가 없네요...

그래도 조금이나마, 무언가 알 수 있게 되었으면 좋겠습니다!   
감사합니다!
