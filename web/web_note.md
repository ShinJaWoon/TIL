```html
HTML

<input type="text" id="username" name="username" placeholder="아이디를 입력해주세요">
placeholder는 회색으로 입력창에 띄워줌

<input type="password" id="pwd" name="password" autofocus>
autofocus는 새 창에서 자동으로 커서가 들어가게 해줌
여러군데 넣으면 제일 처음 넣은곳에 커서가 간다.

표 빨리 만들기
table>(thead>tr>td*열개수)+(tbody>tr*행개수>td*열개수)+(tfoot>tr*행개수>td*열개수)
rowspan: 행병합 속성
colsapn: 열병합 속성
ex) <td rowspan="2">내용</td>
병합한 곳은 <td></td>를 적지 않는다.

이미지가 너무 클 때
.img-fluid

카드 자체에 링크걸기
<a href="#" class="stretched-link"></a>

```

```css
CSS

font-family: Arial ; : 폰트 종류 설정
font-size: 폰트 크기
font-weight: bold; 	폰트 서식

text-align: center; 가운데 정렬
text-decoration: none; 꾸미기 없애기

글자 세로 가운데 정렬법
line-height: box 높이 / 행 개수 px;


이미지 여백 없애기
display: block; 또는
font-size = 0; 또는
line-height = 0;

원으로 만들기
border-radius: 50%
조절하면 부드러운 사각형을 만든다.

.classname:hover{
    호버되었을때만 적용
}


폰트 적용법
import url(폰트url)
font-family: a, b, c




```

