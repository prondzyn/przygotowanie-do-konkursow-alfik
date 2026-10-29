# 05. Liczenie i kombinatoryka

**Dlaczego warto:** W arkuszu Alfika prawie zawsze są 3–5 zadań typu „ile jest…”: liczb o danych cyfrach, meczów, dróg, prostokątów na rysunku albo strojów. Trudność polega na tym, żeby niczego nie pominąć i niczego nie policzyć dwa razy.

- **W pliku:** 24 zadań: 15 nowych i 9 z prawdziwych arkuszy Alfika (10 za 3 pkt, 7 za 4 pkt, 7 za 5 pkt).

**Wskazówki**
- Gdy wybierasz kolejno kilka rzeczy (cyfrę dziesiątek, potem jedności; bluzkę, potem spódnicę), **mnożysz** liczby możliwości.
- Uważaj na zero: liczba nie może zaczynać się od 0.
- Przy uściskach dłoni i meczach „każdy z każdym” jedno spotkanie łączy dwie osoby — dlatego dzielisz przez 2.
- Drogi w kratce licz „ile dróg prowadzi do tego punktu” — dopisuj liczby przy skrzyżowaniach (każda liczba = suma liczby z lewej i liczby z dołu).
- Gdy liczysz figury na rysunku, rób to po kolei według wielkości albo według boków — nigdy „na oko”.
- Jeśli wypisanie wszystkich przypadków zajmie minutę, wypisz je — to najpewniejsza metoda.

**Spis treści**

- [A. Liczby z danych cyfr](#a-liczby-z-danych-cyfr)
- [B. Uściski dłoni i mecze](#b-uściski-dłoni-i-mecze)
- [C. Drogi i trasy](#c-drogi-i-trasy)
- [D. Figury na rysunku](#d-figury-na-rysunku)
- [E. Stroje i kanapki](#e-stroje-i-kanapki)
- [Klucz odpowiedzi](#klucz-odpowiedzi)
- [Ściąga](#ściąga)

---

## A. Liczby z danych cyfr

Ustalamy cyfry po kolei: najpierw pierwszą, potem drugą itd., i mnożymy liczby możliwości. Czasem lepiej po prostu wypisać wszystkie liczby.

1. Ile liczb dwucyfrowych można zapisać za pomocą cyfr 1, 3 i 5, jeśli cyfry w liczbie nie mogą się powtarzać? *(3 pkt)*
   - A) 3
   - B) 5
   - C) 6
   - D) 8
   - E) 9
   <details><summary>rozwiązanie</summary>C — 6<br>Cyfrę dziesiątek wybieramy na 3 sposoby, a cyfrę jedności już tylko na 2 (bo nie może być taka sama). 3 · 2 = 6. Wypisane: 13, 15, 31, 35, 51, 53. Pułapka: 9 to wynik, gdy cyfry mogą się powtarzać (11, 33, 55 też).</details><br>
2. Ile jest takich liczb trzycyfrowych, które zapisywane są przy użyciu jednej jedynki i dwóch dwójek? *(3 pkt)* *(Alfik 2025, zad. 10)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 6
   <details><summary>rozwiązanie</summary>C — 3<br>Wystarczy wybrać miejsce dla jedynki (setki, dziesiątki albo jedności): 122, 212, 221. Pułapka: 6 wychodzi, gdy traktujemy obie dwójki jako różne cyfry.</details><br>
3. Ile jest takich trzycyfrowych liczb, które można ułożyć z cyfr 2, 3, 5 (wykorzystując każdą cyfrę jeden raz)? *(3 pkt)* *(Alfik 2022, zad. 4)*
   - A) 2
   - B) 3
   - C) 4
   - D) 5
   - E) 6
   <details><summary>rozwiązanie</summary>E — 6<br>Wypisujemy: 235, 253, 325, 352, 523, 532. Na pierwszym miejscu 3 możliwości, na drugim 2, na trzecim 1: 3 · 2 · 1 = 6.</details><br>
4. Ile jest trzycyfrowych liczb podzielnych przez 4, które można ułożyć z cyfr 2, 3, 4 (każdą cyfrę wykorzystując tylko raz)? *(3 pkt)* *(Alfik 2021, zad. 7)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) więcej niż 4
   <details><summary>rozwiązanie</summary>B — 2<br>Liczba dzieli się przez 4, gdy jej dwie ostatnie cyfry tworzą liczbę podzielną przez 4. Możliwe końcówki: 23, 32, 24, 42, 34, 43 — przez 4 dzielą się tylko 32 i 24. Liczby: 432 i 324, czyli 2.</details><br>
5. Ile jest liczb dwucyfrowych, które można ułożyć z cyfr 2, 5, 7 (wykorzystując każdą cyfrę najwyżej raz)? *(3 pkt)* *(Alfik 2016, zad. 7)*
   - A) 3
   - B) 4
   - C) 5
   - D) 6
   - E) więcej niż 6
   <details><summary>rozwiązanie</summary>D — 6<br>Cyfrę dziesiątek wybieramy na 3 sposoby, cyfrę jedności spośród pozostałych dwóch: 3 · 2 = 6. To 25, 27, 52, 57, 72, 75.</details><br>
6. Ile liczb trzycyfrowych można zapisać za pomocą cyfr 0, 2, 4, 6, jeśli cyfry w liczbie nie mogą się powtarzać? *(4 pkt)*
   - A) 12
   - B) 18
   - C) 24
   - D) 27
   - E) 48
   <details><summary>rozwiązanie</summary>B — 18<br>Cyfra setek nie może być zerem, więc mamy na nią 3 możliwości (2, 4 lub 6). Na cyfrę dziesiątek zostają 3 cyfry (teraz już można użyć zera), a na cyfrę jedności 2 cyfry. 3 · 3 · 2 = 18. Pułapka: 4 · 3 · 2 = 24 liczy też „liczby” zaczynające się od 0, np. 024.</details><br>
7. Ile jest liczb trzycyfrowych, w których iloczyn cyfr jest równy 8? *(4 pkt)*
   - A) 6
   - B) 7
   - C) 9
   - D) 10
   - E) 12
   <details><summary>rozwiązanie</summary>D — 10<br>Zera być nie może (iloczyn byłby 0). Trzy cyfry o iloczynie 8 to: {1, 2, 4}, {1, 1, 8} oraz {2, 2, 2}. Trzy różne cyfry 1, 2, 4 można ustawić na 6 sposobów (124, 142, 214, 241, 412, 421). Cyfry 1, 1, 8 dają tylko 3 liczby: 118, 181, 811. Cyfry 2, 2, 2 dają jedną liczbę: 222. Razem 6 + 3 + 1 = 10. Pułapka: 6 — gdy pominiemy zestawy z powtarzającymi się cyframi.</details><br>
8. Bartek nie pamięta numeru PIN do swojego telefonu, ale pamięta, że składał się on z 4 cyfr ustawionych od najmniejszej do największej i ostatnią cyfrą było 4. Ile co najmniej kombinacji musiałby wypróbować, żeby mieć pewność, że jedna z nich będzie prawidłowym numerem PIN? *(4 pkt)* *(Alfik 2024, zad. 19)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5
   <details><summary>rozwiązanie</summary>D — 4<br>Przed czwórką stoją trzy różne cyfry mniejsze od 4, ustawione rosnąco — wybieramy je z 0, 1, 2, 3. Wystarczy wybrać, której z tych czterech cyfr brakuje: 1234, 0234, 0134, 0124. To 4 możliwości.</details><br>
9. Z cyfr 1, 2, 3, 4 (każdej użytej dokładnie raz) tworzymy liczby czterocyfrowe. Ile z nich jest podzielnych przez 4? *(5 pkt)*
   - A) 6
   - B) 8
   - C) 12
   - D) 18
   - E) 24
   <details><summary>rozwiązanie</summary>A — 6<br>Liczba dzieli się przez 4, gdy jej dwie ostatnie cyfry tworzą liczbę podzielną przez 4. Z naszych cyfr (różnych) da się ułożyć takie końcówki: 12, 24, 32 (a 14, 34, 42 się nie dzielą). Przy każdej końcówce dwie pozostałe cyfry ustawiamy z przodu na 2 sposoby, np. 3412 i 4312. Razem 3 · 2 = 6. Pułapka: 12 to liczba wszystkich liczb <i>parzystych</i>, a nie podzielnych przez 4.</details><br>

## B. Uściski dłoni i mecze

„Każdy z każdym” — każda osoba spotyka wszystkie pozostałe, ale jedno spotkanie liczymy raz, a nie dwa razy.

10. Sześcioro przyjaciół spotkało się w parku i każdy podał rękę każdemu innemu dokładnie jeden raz. Ile było uścisków dłoni? *(3 pkt)*
   - A) 12
   - B) 15
   - C) 18
   - D) 30
   - E) 36
   <details><summary>rozwiązanie</summary>B — 15<br>Pierwsza osoba podaje rękę 5 innym, druga — 4 nowym (z pierwszą już się przywitała), trzecia — 3 nowym, i tak dalej: 5 + 4 + 3 + 2 + 1 = 15. Inaczej: każdy z 6 podaje rękę 5 osobom, 6 · 5 = 30, ale każdy uścisk policzyliśmy dwa razy, więc 30 : 2 = 15. Pułapka: 30.</details><br>
11. Między każdymi dwoma wyspami w archipelagu 4 wysp zbudowano jeden most. Ile mostów zbudowano? *(3 pkt)* *(Alfik 2023, zad. 6)*
   - A) 4
   - B) 5
   - C) 6
   - D) 12
   - E) 16
   <details><summary>rozwiązanie</summary>C — 6<br>Każda wyspa łączy się z 3 innymi: 4 · 3 = 12, ale każdy most policzyliśmy dwa razy (z obu końców). 12 : 2 = 6. Pułapka: odpowiedź 12.</details><br>
12. W turnieju piłkarskim każda drużyna zagrała z każdą inną dokładnie jeden mecz. Rozegrano 21 meczów. Ile drużyn wzięło udział w turnieju? *(4 pkt)*
   - A) 7
   - B) 9
   - C) 11
   - D) 14
   - E) 21
   <details><summary>rozwiązanie</summary>A — 7<br>Przy n drużynach meczów jest 1 + 2 + … + (n − 1). Dodajemy po kolei: 1, 3, 6, 10, 15, 21 — suma 21 wychodzi przy dodaniu liczb od 1 do 6, czyli drużyn jest 7. Sprawdzenie: 7 · 6 : 2 = 21. Pułapka: 14 = 2 · 7 albo 21 (jakby każdy mecz to była nowa drużyna).</details><br>
13. W turnieju piłki nożnej każda z 8 drużyn rozegrała jeden mecz z każdą z pozostałych. Ile meczy rozegrano? *(4 pkt)* *(Alfik 2016, zad. 18)*
   - A) 27
   - B) 28
   - C) 30
   - D) 32
   - E) 56
   <details><summary>rozwiązanie</summary>B — 28<br>Każda drużyna gra 7 meczów: 8 · 7 = 56, ale każdy mecz liczymy wtedy dwa razy (dla obu drużyn). Meczów jest 56 : 2 = 28. Pułapka: odpowiedź 56.</details><br>
14. Na zbiórce harcerskiej każdy harcerz podał rękę każdemu innemu dokładnie raz. Tylko dwaj bracia Kowalscy nie podali sobie ręki, bo widzieli się już rano w domu. Razem było 44 uściski dłoni. Ilu harcerzy było na zbiórce? *(5 pkt)*
   - A) 6
   - B) 7
   - C) 8
   - D) 9
   - E) 10
   <details><summary>rozwiązanie</summary>E — 10<br>Gdyby bracia też podali sobie rękę, uścisków byłoby 44 + 1 = 45. Szukamy liczby harcerzy, dla której „każdy z każdym” daje 45: 1 + 2 + 3 + … + 9 = 45, więc harcerzy jest 10. Sprawdzenie: 10 · 9 : 2 = 45, minus uścisk braci = 44. Pułapka: 9 harcerzy daje tylko 9 · 8 : 2 = 36 uścisków.</details><br>
15. W turnieju szachowym każdy szachista miał rozegrać z każdym innym jedną partię. Jeden z uczestników, Jacek, rozchorował się i wycofał się z turnieju po rozegraniu tylko części z zaplanowanych partii. Łącznie rozegrano 20 partii. Ilu szachistów (wliczając Jacka) brało udział w turnieju? *(5 pkt)* *(Alfik 2025, zad. 30)*
   - A) 4
   - B) 5
   - C) 6
   - D) 7
   - E) 8
   <details><summary>rozwiązanie</summary>D — 7<br>Pozostali gracze rozegrali wszystkie partie między sobą. Przy 6 pozostałych to 6 · 5 : 2 = 15 partii, a Jacek zagrał 5 z 6 zaplanowanych — razem 20. Przy 5 pozostałych byłoby 10 + co najwyżej 4 &lt; 20, a przy 7 pozostałych już 21 &gt; 20. Zatem graczy było 6 + 1 = 7.</details><br>
16. W pewnym mieście są 4 linie metra, a na każdej linii są 4 stacje. Jaka jest łączna liczba stacji metra w tym mieście, jeśli każda stacja leży na dokładnie dwóch liniach metra? *(5 pkt)* *(Alfik 2018, zad. 29)*
   - A) 4
   - B) 8
   - C) 12
   - D) 14
   - E) 16
   <details><summary>rozwiązanie</summary>B — 8<br>Gdyby policzyć stacje osobno na każdej linii, wyszłoby 4 · 4 = 16. Ale każdą stację policzyliśmy dwa razy (leży na dwóch liniach), więc stacji jest 16 : 2 = 8.</details><br>

## C. Drogi i trasy

Gdy trasa ma kilka etapów, mnożymy liczby możliwości na każdym etapie. W kratce dopisujemy przy każdym skrzyżowaniu, iloma drogami można do niego dojść.

17. Z domu Zosi do szkoły prowadzą 3 różne ścieżki, a ze szkoły do parku 4 różne ścieżki. Na ile sposobów Zosia może przejść z domu do parku, idąc przez szkołę? *(3 pkt)*
   - A) 7
   - B) 10
   - C) 12
   - D) 14
   - E) 16
   <details><summary>rozwiązanie</summary>C — 12<br>Każdą z 3 ścieżek do szkoły można połączyć z każdą z 4 ścieżek do parku: 3 · 4 = 12 tras. Pułapka: 3 + 4 = 7 — dodawanie zamiast mnożenia.</details><br>
18. Plan osiedla to kwadrat podzielony ulicami na 3 · 3 = 9 jednakowych kwadratowych kwartałów (4 ulice poziome i 4 pionowe). Mrówka idzie ulicami z lewego dolnego rogu do prawego górnego rogu i porusza się tylko w prawo albo w górę. Iloma różnymi drogami może przejść? *(5 pkt)*
   - A) 6
   - B) 9
   - C) 12
   - D) 16
   - E) 20
   <details><summary>rozwiązanie</summary>E — 20<br>Przy każdym skrzyżowaniu wpisujemy, iloma drogami da się do niego dojść. Na dolnej ulicy i lewej ulicy wszędzie jest 1. Każde inne skrzyżowanie = liczba z lewej + liczba z dołu. Rzędy od dołu: 1, 1, 1, 1 → 1, 2, 3, 4 → 1, 3, 6, 10 → 1, 4, 10, 20. W prawym górnym rogu jest 20. Pułapka: 16 to liczba skrzyżowań, a nie dróg.</details><br>

## D. Figury na rysunku

Prostokąt wyznaczają dwie linie pionowe i dwie poziome. Licz figury systematycznie: najpierw złożone z jednej części, potem z dwóch, z trzech…

19. Prostokąt podzielono trzema pionowymi odcinkami na 4 węższe prostokąty ułożone obok siebie w jednym rzędzie. Ile wszystkich prostokątów widać na tym rysunku? *(3 pkt)*
   - A) 4
   - B) 5
   - C) 8
   - D) 10
   - E) 12
   <details><summary>rozwiązanie</summary>D — 10<br>Liczymy według szerokości: z jednego paska — 4 prostokąty, z dwóch sąsiednich pasków — 3, z trzech — 2, z czterech (cały prostokąt) — 1. Razem 4 + 3 + 2 + 1 = 10. Pułapka: 5 to tylko 4 małe paski i cały prostokąt.</details><br>
20. Z wierzchołka trójkąta poprowadzono 3 odcinki do przeciwległego boku, tak jak na rysunku (dolny bok jest podzielony na 4 części). Ile wszystkich trójkątów jest na tym rysunku? <svg width="220" height="120" viewBox="0 0 220 120" fill="none" stroke="currentColor" stroke-width="2" style="display:block"><path d="M110 10 L10 110 L210 110 Z"/><path d="M110 10 L60 110 M110 10 L110 110 M110 10 L160 110"/></svg> *(4 pkt)*
   - A) 4
   - B) 6
   - C) 10
   - D) 12
   - E) 16
   <details><summary>rozwiązanie</summary>C — 10<br>Każdy trójkąt na rysunku ma górny wierzchołek, a jego dolny bok to kawałek dolnej linii między dwoma z 5 zaznaczonych punktów. Liczymy dolne boki: złożone z 1 części — 4, z 2 części — 3, z 3 części — 2, z 4 części — 1. Razem 4 + 3 + 2 + 1 = 10. Pułapka: 4 to tylko najmniejsze trójkąty.</details><br>
21. Prostokąt podzielono na 6 jednakowych kwadratów: 2 rzędy po 3 kwadraty (jak na rysunku). Ile wszystkich prostokątów (licząc także kwadraty) widać na tym rysunku? <svg width="130" height="90" viewBox="0 0 130 90" fill="none" stroke="currentColor" stroke-width="2" style="display:block"><rect x="5" y="5" width="120" height="80"/><path d="M45 5 V85 M85 5 V85 M5 45 H125"/></svg> *(5 pkt)*
   - A) 6
   - B) 8
   - C) 12
   - D) 15
   - E) 18
   <details><summary>rozwiązanie</summary>E — 18<br>Prostokąt wyznaczamy, wybierając 2 z 4 linii pionowych i 2 z 3 linii poziomych. Dwie linie pionowe z czterech można wybrać na 6 sposobów (tak jak w zadaniu 10: 3 + 2 + 1), a dwie poziome z trzech na 3 sposoby. 6 · 3 = 18. Można też policzyć po kształtach: 1×1 — 6, 1×2 — 4, 1×3 — 2, 2×1 — 3, 2×2 — 2, 2×3 — 1; razem 18. Pułapka: zapomnieć o prostokątach „stojących” (2×1) albo o całym prostokącie.</details><br>

## E. Stroje i kanapki

Każdy wybór „jedno z tego i jedno z tamtego” to mnożenie. Gdy są zakazy (np. „nie w tym samym kolorze”), najprościej policzyć wszystko i odjąć zakazane.

22. Kasia ma 3 różne bluzki i 4 różne spódnice. Ile różnych strojów „bluzka + spódnica” może ułożyć? *(3 pkt)*
   - A) 7
   - B) 12
   - C) 14
   - D) 16
   - E) 24
   <details><summary>rozwiązanie</summary>B — 12<br>Do każdej z 3 bluzek można założyć każdą z 4 spódnic: 3 · 4 = 12 strojów. Pułapka: 3 + 4 = 7.</details><br>
23. W szkolnym sklepiku robi się kanapki. Najpierw wybiera się chleb: jasny albo ciemny. Potem wybiera się dodatki: albo jeden dodatek, albo dwa różne dodatki spośród czterech: ser, szynka, jajko, pomidor. Kolejność dodatków nie ma znaczenia. Ile różnych kanapek można zrobić? *(4 pkt)*
   - A) 20
   - B) 24
   - C) 28
   - D) 32
   - E) 36
   <details><summary>rozwiązanie</summary>A — 20<br>Z jednym dodatkiem są 4 możliwości. Z dwoma różnymi dodatkami: ser-szynka, ser-jajko, ser-pomidor, szynka-jajko, szynka-pomidor, jajko-pomidor — 6 możliwości. Razem 4 + 6 = 10 zestawów dodatków, a każdy może być na jasnym lub ciemnym chlebie: 2 · 10 = 20. Pułapka: 32 wychodzi, gdy „ser + szynka” i „szynka + ser” liczy się jako dwie różne kanapki.</details><br>
24. Ola ma 4 bluzki: czerwoną, niebieską, zieloną i żółtą, oraz 3 spódnice: czerwoną, niebieską i białą. Nie chce założyć bluzki i spódnicy w tym samym kolorze. Do każdego stroju może też założyć kapelusz albo pójść bez kapelusza. Ile różnych strojów może ułożyć Ola? *(5 pkt)*
   - A) 10
   - B) 12
   - C) 14
   - D) 20
   - E) 24
   <details><summary>rozwiązanie</summary>D — 20<br>Wszystkich par „bluzka + spódnica” jest 4 · 3 = 12. Zakazane są dwie: czerwona z czerwoną i niebieska z niebieską. Zostaje 12 − 2 = 10 par. Każdą parę można nosić z kapeluszem albo bez, więc strojów jest 10 · 2 = 20. Pułapki: 10 (zapomniany kapelusz) i 24 (zapomniany zakaz).</details><br>

---

## Klucz odpowiedzi

1. C — 6
2. C — 3 *(Alfik 2025, zad. 10)*
3. E — 6 *(Alfik 2022, zad. 4)*
4. B — 2 *(Alfik 2021, zad. 7)*
5. D — 6 *(Alfik 2016, zad. 7)*
6. B — 18
7. D — 10
8. D — 4 *(Alfik 2024, zad. 19)*
9. A — 6
10. B — 15
11. C — 6 *(Alfik 2023, zad. 6)*
12. A — 7
13. B — 28 *(Alfik 2016, zad. 18)*
14. E — 10
15. D — 7 *(Alfik 2025, zad. 30)*
16. B — 8 *(Alfik 2018, zad. 29)*
17. C — 12
18. E — 20
19. D — 10
20. C — 10
21. E — 18
22. B — 12
23. A — 20
24. D — 20

## Ściąga

| Sytuacja | Jak liczyć | Przykład |
|---|---|---|
| Wybieram po kolei (cyfry, bluzka i spódnica) | mnożę liczby możliwości | 3 bluzki, 4 spódnice → 3 · 4 = 12 |
| Cyfry bez powtórzeń | za każdym razem jedna cyfra mniej | z 1, 3, 5: 3 · 2 = 6 |
| Pierwsza cyfra | nie może być 0 | z 0, 2, 4, 6: 3 · 3 · 2 = 18 |
| „Każdy z każdym” (n osób) | n · (n − 1) : 2 = 1 + 2 + … + (n − 1) | 6 osób → 15, 7 drużyn → 21, 10 → 45 |
| Drogi w kratce (tylko w prawo/w górę) | przy skrzyżowaniu: lewa + dolna | kratka 2×2 → 6, 3×3 → 20 |
| Prostokąty w pasku z n części | 1 + 2 + … + n | 4 paski → 10 |
| Prostokąty w kratce | (pary linii pionowych) · (pary linii poziomych) | 2×3 → 6 · 3 = 18 |
| Trójkąty „wachlarz” z n częściami podstawy | 1 + 2 + … + n | 4 części → 10 |
| Są zakazy | policz wszystko, odejmij zakazane | 12 − 2 = 10 |

Liczby „trójkątne” warto znać na pamięć: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55.
