# [Gold III] 가희와 총선거 5 - 30795 

[문제 링크](https://www.acmicpc.net/problem/30795) 

### 성능 요약

메모리: 31120 KB, 시간: 44 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 파싱, 문자열

### 제출 일자

2024년 2월 15일 20:48:19

### 문제 설명

<p>선거할 때마다 반드시 나타나는 신데렐라를 아시나요? 신데렐라는 예상과 다르게 경악할 정도로 뛰어난 결과를 보여준 캐릭터를 의미합니다. 신데렐라 수치는 티어와 예상 결과, 최종 결과와 같은 요소로 계산됩니다. 해당 수치에 따라 신데렐라가 결정됩니다.</p>

<p>선거가 시작되기 3주 전에 한 언론이 캐릭터 예상 순위를 발표합니다. 개표가 끝난 후 나오는 순위가 최종 결과가 됩니다. 예상 결과와 최종 결과 모두 티어가 있으며, 결과에 따른 티어는 아래 [표 1]과 같습니다.</p>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 400px;">
	<tbody>
		<tr>
			<td style="text-align: center;">티어</td>
			<td style="text-align: center;">순위 범위</td>
		</tr>
		<tr>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">1 ~ 16</td>
		</tr>
		<tr>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;">17 ~ 32</td>
		</tr>
		<tr>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;">33 ~ 48</td>
		</tr>
		<tr>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">49 ~ 64</td>
		</tr>
		<tr>
			<td style="text-align: center;">5</td>
			<td style="text-align: center;">65 ~ 80</td>
		</tr>
		<tr>
			<td style="text-align: center;">6</td>
			<td style="text-align: center;">그 외</td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 1]</strong> 티어와 순위</p>

<p>결과에 나타나지 않은 캐릭터들은 순위 범위가 그 외에 속합니다. <strong>티어 6을 제외하고 각 티어에서 순위가 가장 높으면</strong> <strong>해당 티어에서 센터</strong>가 됩니다. 예를 들어, 17위를 획득한 캐릭터는 티어 2에서 순위가 가장 높습니다. 따라서 <strong>이 캐릭터는 티어 2에서의 센터</strong>가 됩니다.</p>

<p>캐릭터 <code>c</code>의 신데렐라 수치는 최종 티어가 6인 경우 0이고, 그렇지 않으면 아래와 같이 계산됩니다. 캐릭터 <code>c</code>의 예상 결과가 티어 <code>x</code>에 속하고, 최종 결과가 티어 <code>y</code>에 속할 때</p>

<ol>
	<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3E"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D466 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi><mo>></mo><mi>y</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$x > y$</span></mjx-container> 경우
	<ul>
		<li><mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c22C5"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D466 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo>⋅</mo><mo stretchy="false">(</mo><mi>x</mi><mo>−</mo><mi>y</mi><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10\,000 \cdot (x-y)$</span></mjx-container>입니다.</li>
	</ul>
	</li>
	<li>최종 결과가 각 티어에서의 센터인 경우
	<ul>
		<li>조건 <code>1</code>을 만족하는 경우 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$20\,000$</span></mjx-container>입니다.</li>
		<li>그렇지 않은 경우 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10\,000$</span></mjx-container>입니다.</li>
	</ul>
	</li>
	<li><code>x</code>가 <code>1</code>이 아니지만, <code>y</code>가 <code>1</code>인 경우
	<ul>
		<li><strong>아래 조건을 모두 만족하는 캐릭터의 수</strong>를 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$p$</span></mjx-container>라고 할 때 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c22C5"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>30</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mo>⋅</mo><mi>p</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$30\,000 \cdot p$</span></mjx-container>입니다.
		<ul>
			<li>예상 결과가 캐릭터 <code>c</code>보다 좋았지만 최종 결과가 <code>c</code>보다 좋지 않습니다.</li>
			<li>예상 결과가 티어 1에 속했지만 최종 결과가 티어 1에 속하지 않습니다.</li>
		</ul>
		</li>
	</ul>
	</li>
</ol>

<p>조건 <code>1</code>, <code>2</code>, <code>3</code> 중 <strong>만족하는 조건만 합산하여 계산</strong>됩니다. 예를 들어, 캐릭터 <code>c</code>의 예상 결과가 63위였지만 최종 결과가 20위였다면, 캐릭터 <code>c</code>의 신데렐라 수치는 아래와 같이 계산할 수 있습니다.</p>

<ol>
	<li>예상 결과가 티어 4에 속하지만 최종 결과는 티어 2에 속합니다.</li>
	<li>최종 결과가 센터가 아닙니다.</li>
	<li>최종 결과가 티어 1에 속하지 않습니다.</li>
</ol>

<p>따라서, 캐릭터 <code>c</code>의 신데렐라 수치는 조건 <code>1</code>만 합산되어 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>20</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$20\,000$</span></mjx-container>이 됩니다. 최종 결과가 80위 이내에 든 캐릭터 중 신데렐라 수치가 가장 높은 캐릭터들을 '신데렐라 후보'라고 하겠습니다. 이 후보들 중 순위가 가장 높은 캐릭터가 신데렐라가 됩니다. 신데렐라를 구해주세요.</p>

### 입력 

 <p>첫 줄에 예상 결과가 주어집니다. 이때, 1위부터 80위까지 순위가 높은 순서대로 {<code>character_info</code>}가 공백으로 구분되어 주어집니다.</p>

<p>두 번째 줄에 최종 결과가 주어집니다. 이때, 1위부터 80위까지 순위가 높은 순서대로 {<code>character_info</code>}가 공백으로 구분되어 주어집니다.</p>

<p>{<code>character_info</code>}는 아래와 같이 주어집니다.</p>

<p style="text-align: center;">{<code>character_name</code>} {<code>group</code>} {<code>team</code>}</p>

<p>{<code>character_name</code>}, {<code>group</code>}, {<code>team</code>}은 공백으로 구분되어 주어집니다. {<code>group</code>}은 아래와 같이 주어집니다.</p>

<p style="text-align: center;"><code>Group</code> {<code>group_name</code>}</p>

<p><code>Group</code>과 {<code>group_name</code>}은 공백으로 구분되어 주어집니다. {<code>team</code>}은 아래와 같이 주어집니다.</p>

<p style="text-align: center;"><code>Team</code> {<code>team_name</code>}</p>

<p><code>Team</code>과 {<code>team_name</code>}은 공백으로 구분되어 주어집니다.</p>

<ul>
	<li>{<code>character_name</code>}은 공백과 알파벳 대소문자와 숫자로만 주어지며 공백으로 시작하거나 끝나지 않습니다.</li>
	<li>{<code>character_name</code>}에 연속으로 공백이 나오지 않습니다.</li>
	<li>{<code>group_name</code>}과 {<code>team_name</code>}은 알파벳 대소문자와 숫자로만 주어집니다.</li>
</ul>

### 출력 

 <p>첫 번째 줄에 신데렐라의 그룹명을, 두 번째 줄에 신데렐라의 팀 이름을, 세 번째 줄에 신데렐라의 캐릭터 이름을 출력해 주세요.</p>

