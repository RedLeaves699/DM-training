## 4.1-2:
(a)$\neg P \wedge R \rightarrow Q$\
(b)$R \rightarrow  Q$\
(c)$\neg P$\
(d)$Q \leftrightarrow (R \wedge \neg P)$

---

## 4.1-3a:
$\neg P=P\uparrow T;\\
P \wedge Q=(P \uparrow Q)\uparrow T \\
P\vee Q=(P \uparrow T)\uparrow (Q \uparrow T)\\
P\rightarrow Q=\neg P \vee Q=P \uparrow (Q \uparrow T)\\
P \leftrightarrow Q=(P\rightarrow Q)\wedge(Q \rightarrow P)=((P \uparrow (Q \uparrow T))\uparrow(Q \uparrow (P \uparrow T)))\uparrow T
$

---

## 4.1-3c:
$
P\wedge Q=\neg(\neg P \vee \neg Q)\\
P\rightarrow Q=\neg P \vee Q\\
P\leftrightarrow Q=\neg(\neg(\neg P\vee Q)\vee \neg(\neg Q\vee P))
$

---

## 4.2-2e:
|$P$   |$Q$     |$P\vee \neg Q\rightarrow \neg P \vee \neg Q$|
|------|-------:|:--------------------------------------------:|
|  F   |   F    | F F    T  F      T       T      F    T   T  F |
|  F   |   T    | F F    F  T      T       T      F    T   F  T |
|  T   |   F    | T T    T  F      T       F      T    T   T  F |
|  T   |   T    | T F    F  T      T       F      T    F   F  T |

## 4.2-3:
编程求解，0表示F，1表示T\
(c)(0,0,1),(0,1,1),(1,0,1),(1,1,1)\
(d)(0,0,0),(0,1,0)

---

## 4.2-4:
(a)$
原式可化为 \\ 
\iff\neg (P \wedge(\neg P \vee Q))\vee Q\\
\iff \neg(P\wedge \neg P)\vee (P\wedge Q)\vee Q\\
\iff \neg(P \wedge Q)\vee Q\\
\iff \neg P \vee \neg Q \vee Q\\
\iff \neg P \vee (\neg Q \vee Q)\\
\iff \neg P \vee T\\
\iff T
是一个永真式
$\
(d)$
原式可化为 \\
\iff \neg P \vee Q \wedge (\neg Q \vee P)\\
\iff P \leftrightarrow Q\\
原式是可满足的
$
(e)$
原式可化为 \\
\iff \neg(P \vee \neg P)\vee Q\\
\iff Q\\
原式是可满足的\\
$
(f)$
当P=F,Q=T,原式的值为F\\
当P=T,Q=T,原式的值为T\\
所以,原式是可满足的\\
$
(i)$
原式可化为\\
\iff (P\vee Q)\wedge(\neg P\wedge\neg Q)\wedge R\\
\iff ((P\vee Q)\wedge R)\wedge(\neg P\wedge\neg Q)\\
\iff (P\vee Q)\wedge(\neg P\wedge\neg Q)\wedge...\\
\iff F\wedge...\\
\iff F\\
原式是永假式。
$

---
## 4.2-6:
c是a的代换实例\
e是b的代换实例

---
## 4.3-2b:
$
要证原式，只要证\\
(P\vee \neg Q)\wedge(P\vee Q)\wedge(\neg P\vee \neg Q)\iff\neg(\neg P\vee Q)\\
只要证(P\vee \neg Q)\wedge(P\vee Q)\wedge(\neg P\vee \neg Q)\iff P\wedge \neg Q\\
只要证P\vee(\neg Q\wedge Q)\wedge(\neg P\vee \neg Q)\iff P\wedge \neg Q\\
只要证P\vee F\wedge(\neg P\vee\neg Q)\iff P \wedge\neg Q\\
只要证P\wedge(\neg P\vee \neg Q)\iff P\wedge\neg Q\\
只要证(P\wedge\neg P)\vee(P\wedge\neg Q)\iff P\wedge\neg Q\\
只要证F\vee(P\wedge\neg Q)\iff P\wedge\neg Q\\
P\wedge\neg Q\iff P\wedge\neg Q,结论得证。
$

---
## 4.3-3c:
$
要证原式，只要证(\neg Q\vee P)\wedge(P\vee Q)\iff P\\
只要证P\vee(\neg Q\wedge Q)\iff P\\
只需证P\vee F\Leftrightarrow P\\
结论得证
$

---
## 4.3-4:
(a)$
P\wedge Q\Rightarrow Q\\
Q\Rightarrow P\rightarrow Q\\
由\Rightarrow关系的传递性:P\wedge Q \Rightarrow P\rightarrow Q
$

(e)$
要证原式，只要证:(T\rightarrow Q)\rightarrow (T\rightarrow R)\Leftrightarrow Q\rightarrow R\\
只要证(F\vee Q)\rightarrow (F\vee R)\Leftrightarrow Q\rightarrow R\\
只要证\neg((F\vee Q)\vee (F\vee R))\Leftrightarrow Q\rightarrow R\\
只要证\neg Q\vee R\Leftrightarrow Q\rightarrow R\\
根据等价规则16,结论得证。
$

---

## 4.3-课件题目:
P：今天下午出太阳，Q：去武装泅渡，R：去越野 S:太阳下山时返回营地\
$
P=F......(0) \\
P\leftrightarrow Q......(1)\\
\neg P\leftrightarrow R......(2)\\
R \leftrightarrow S......(3)\\
证明：S=True\\
P=F,则R=T，Q=F,推出S=T,得证
$

---

## 4.4-2a:
$
原式左侧可化为:\\
(\neg P\vee Q)\wedge(\neg P\vee R)\\
原式右侧可化为:\\
\neg P\vee (Q\wedge R)\\
\iff (\neg P\vee Q)\wedge(\neg P\vee R)\\
左侧右侧主合取范式相同，故等价关系成立
$

---
## 4.4-3e:
$
\text原式 \\
\iff \neg P \vee \neg Q \rightarrow ((\neg P \vee \neg Q) \wedge(P\vee Q))
\\
\iff P \wedge Q \vee((\neg P \vee \neg Q) \wedge(P\vee Q))\\
\iff P \wedge Q\vee((\neg P \wedge Q)\vee (\neg Q \wedge P))\\
所以(P \wedge Q)\vee(\neg P \wedge Q)\vee (\neg Q \wedge P) 是 \neg p \vee \neg q \rightarrow (p \Leftrightarrow \neg q) \text的主析取范式 \\
\\
原式 \\
\iff \neg P \vee \neg Q \rightarrow ((\neg P \vee \neg Q) \wedge(P\vee Q))
\\
\iff P \wedge Q \vee((\neg P \vee \neg Q) \wedge(P\vee Q))\\
\iff T \wedge ((P \wedge Q)\vee (P\vee Q))\\
\iff P \vee Q \\
所以P\vee Q 是 \neg p \vee \neg q \rightarrow (p \Leftrightarrow \neg q) 的主合取范式 \\
$

---
## 4.4-3g:
$原式可化为\\
\iff (\neg P \vee Q \wedge R)\vee(P \vee \neg Q \wedge \neg R)\\
\iff (\neg P \vee (Q \wedge R))\vee(P \vee (\neg Q \wedge \neg R))\\
\iff (Q\wedge R)\vee (\neg Q \wedge \neg R)\\
\iff (P \wedge \neg Q \wedge \neg R) \vee (P \wedge Q \wedge R)\vee(\neg P \wedge  Q \wedge  R)\vee(\neg P \wedge \neg Q \wedge \neg R)\\
所以(P \wedge \neg Q \wedge \neg R) \vee (P \wedge Q \wedge R)\vee(\neg P \wedge  Q \wedge  R)\vee(\neg P \wedge \neg Q \wedge \neg R)是原式的主析取范式\\
\\
原式可化为\\
\iff (\neg P \vee Q \wedge R)\vee(P \vee \neg Q \wedge \neg R)\\
\iff ((\neg P \vee Q) \wedge R)\vee((P \vee \neg Q) \wedge \neg R)\\
\iff ((\neg P \vee Q)\vee (P \vee \neg Q))\wedge (R\vee P \vee \neg Q)\vee (\neg P \vee Q \vee \neg R)\\
\iff ((\neg P \vee Q)\vee (P \vee \neg Q))\wedge (R\vee P \vee \neg Q)\vee (\neg P \vee Q \vee \neg R)\\
\iff (R\vee P \vee \neg Q)\vee (\neg P \vee  Q \vee \neg R) \vee (\neg P \vee \neg Q \vee R)\vee(P \vee Q \vee \neg R)\vee(P \vee \neg Q \vee \neg R)\vee(\neg P \vee  Q \vee \neg R)\\
所以(R\vee P \vee \neg Q)\wedge (\neg P \vee  Q \vee \neg R) \wedge (\neg P \vee \neg Q \vee R)\wedge(P \vee Q \vee \neg R)\wedge(P \vee \neg Q \vee \neg R)\wedge(\neg P \vee  Q \vee \neg R)是原式的主合取范式\\
$

---