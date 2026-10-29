# 02. Liczby i cyfry

**Dlaczego warto:** W każdym arkuszu Alfika są 2–4 zadania o cyfrach: suma albo iloczyn cyfr, palindromy, dopisywanie cyfr, „największa liczba, która…” czy numerowanie stron. Nie trzeba w nich dużo liczyć — trzeba za to porządnie wypisać wszystkie możliwości i żadnej nie zgubić.

- **W pliku:** 42 zadań: 14 nowych i 28 z prawdziwych arkuszy Alfika (15 za 3 pkt, 15 za 4 pkt, 12 za 5 pkt).

**Wskazówki**
- Wypisuj możliwości **po kolei** (np. od najmniejszej pierwszej cyfry) — wtedy łatwo zauważyć, czy czegoś nie brakuje.
- Pamiętaj o cyfrze 0: może stać w środku i na końcu liczby, ale nie na początku. A jeśli iloczyn cyfr ma być różny od 0, to zera w liczbie być nie może.
- Najmniejsza liczba: jak najmniej cyfr, a na początku jak najmniejsza cyfra. Największa liczba: jak najwięcej cyfr, a na początku jak największa.
- Dopisanie zera na końcu = pomnożenie liczby przez 10. Dopisanie cyfry na początku liczby dwucyfrowej = dodanie 100, 200, … .
- Przy numerowaniu stron: strony 1–9 zużywają 9 cyfr, strony 10–99 zużywają 180 cyfr, razem 189.
- Przy liczeniu, ile razy pisze się cyfrę, licz osobno miejsce jedności i miejsce dziesiątek.

**Spis treści**

- [A. Suma i iloczyn cyfr](#a-suma-i-iloczyn-cyfr)
- [B. Palindromy i dopisywanie cyfr](#b-palindromy-i-dopisywanie-cyfr)
- [C. Największa i najmniejsza liczba](#c-największa-i-najmniejsza-liczba)
- [D. Liczenie cyfr i numerowanie stron](#d-liczenie-cyfr-i-numerowanie-stron)
- [Klucz odpowiedzi](#klucz-odpowiedzi)
- [Ściąga](#ściąga)

---

## A. Suma i iloczyn cyfr

Tu najważniejsze jest uporządkowane wypisywanie: najpierw ustal, jakie cyfry mogą wystąpić, a potem — na ile sposobów da się je ustawić.

1. Ile jest liczb dwucyfrowych, których suma cyfr wynosi 9? *(3 pkt)*
   - A) 8
   - B) 9
   - C) 10
   - D) 11
   - E) 18
   <details><summary>rozwiązanie</summary>B — 9<br>Są to: 18, 27, 36, 45, 54, 63, 72, 81, 90 — razem 9 liczb. Pułapka: łatwo zapomnieć o 90 (zero też jest cyfrą), a 09 nie jest liczbą dwucyfrową.</details><br>
2. Ile jest parzystych liczb dwucyfrowych o iloczynie cyfr równym 12? *(3 pkt)* *(Alfik 2021, zad. 3)*
   - A) 2
   - B) 3
   - C) 4
   - D) 5
   - E) więcej niż 5
   <details><summary>rozwiązanie</summary>B — 3<br>12 jako iloczyn dwóch cyfr: 2 · 6 lub 3 · 4. Liczby: 26, 62, 34, 43. Parzyste są 26, 62 i 34 — razem 3 (43 jest nieparzysta).</details><br>
3. Ile jest takich liczb trzycyfrowych, w których cyfra setek jest dwa razy większa od cyfry dziesiątek, a cyfra dziesiątek – dwa razy większa od cyfry jedności? *(3 pkt)* *(Alfik 2019, zad. 2)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5
   <details><summary>rozwiązanie</summary>B — 2<br>Cyfra setek jest 4 razy większa od cyfry jedności i musi być cyfrą (najwyżej 9). Jedności = 1 daje 421, jedności = 2 daje 842, a jedności = 3 dałyby setki 12 — za dużo. Jedności = 0 daje 000, a to nie jest liczba trzycyfrowa. Są więc 2 takie liczby.</details><br>
4. Ile jest trzycyfrowych liczb o sumie cyfr równej 4? *(3 pkt)* *(Alfik 2019, zad. 9)*
   - A) 5
   - B) 6
   - C) 7
   - D) 8
   - E) więcej niż 8
   <details><summary>rozwiązanie</summary>E — więcej niż 8<br>Wypisujemy według cyfry setek: 1 → 103, 112, 121, 130 (4 liczby); 2 → 202, 211, 220 (3); 3 → 301, 310 (2); 4 → 400 (1). Razem 4 + 3 + 2 + 1 = 10, czyli więcej niż 8.</details><br>
5. Ile jest takich liczb trzycyfrowych, których iloczyn cyfr jest mniejszy niż 3? *(3 pkt)* *(Alfik 2018, zad. 7)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) więcej niż 4
   <details><summary>rozwiązanie</summary>E — więcej niż 4<br>Każda liczba z cyfrą 0 ma iloczyn cyfr równy 0, np. 100, 101, 102, 103, 110 — już 5 takich liczb. (Wszystkich jest aż 175.) Pułapka: zapomnieć o zerze i liczyć tylko 111, 112, 121, 211.</details><br>
6. Ile jest takich liczb dwucyfrowych, których suma cyfr wynosi 3? *(3 pkt)* *(Alfik 2017, zad. 9)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) więcej niż 4
   <details><summary>rozwiązanie</summary>C — 3<br>Cyfra dziesiątek może być 1, 2 lub 3: to liczby 12, 21 i 30. Pułapka: łatwo zapomnieć o 30 (zero też jest cyfrą).</details><br>
7. Iloczyn cyfr pewnej liczby trzycyfrowej wynosi 12. Ile jest takich liczb trzycyfrowych? *(4 pkt)*
   - A) 9
   - B) 12
   - C) 15
   - D) 18
   - E) 24
   <details><summary>rozwiązanie</summary>C — 15<br>Zera nie może być (iloczyn byłby 0). 12 jako iloczyn trzech cyfr to: 1 · 2 · 6, 1 · 3 · 4 albo 2 · 2 · 3. Cyfry 1, 2, 6 da się ustawić na 6 sposobów (126, 162, 216, 261, 612, 621), cyfry 1, 3, 4 też na 6 sposobów, a cyfry 2, 2, 3 tylko na 3 sposoby (223, 232, 322), bo dwie dwójki są takie same. Razem 6 + 6 + 3 = 15. Pułapka: zapomnienie o 2 · 2 · 3 daje 12.</details><br>
8. Ile jest liczb trzycyfrowych, w których suma cyfr jest równa iloczynowi cyfr? *(4 pkt)*
   - A) 0
   - B) 1
   - C) 2
   - D) 3
   - E) 6
   <details><summary>rozwiązanie</summary>E — 6<br>Zera być nie może (iloczyn byłby 0, a suma nie). Gdy wszystkie cyfry są co najmniej 2, iloczyn jest większy od sumy (2 · 2 · 2 = 8, a 2 + 2 + 2 = 6, a dla większych cyfr różnica jeszcze rośnie). Dwie jedynki też nie pasują: suma 1 + 1 + trzecia cyfra jest zawsze o 2 większa niż iloczyn 1 · 1 · trzecia cyfra. Zostaje jedna jedynka — próbując, znajdujemy 1 + 2 + 3 = 6 = 1 · 2 · 3. Cyfry 1, 2, 3 da się ustawić na 6 sposobów: 123, 132, 213, 231, 312, 321. Pułapka: odpowiedź 1 — zapominamy, że cyfry można przestawiać.</details><br>
9. Ile jest takich liczb dwucyfrowych, które mają sumę cyfr równą 6, a iloczyn cyfr większy niż 6? *(4 pkt)* *(Alfik 2024, zad. 15)*
   - A) 0
   - B) 1
   - C) 2
   - D) 3
   - E) 4
   <details><summary>rozwiązanie</summary>D — 3<br>Liczby o sumie cyfr 6: 15, 24, 33, 42, 51, 60. Iloczyny: 5, 8, 9, 8, 5, 0. Większy niż 6 mają 24, 33 i 42 — to 3 liczby.</details><br>
10. Jeśli liczbę, o której pomyślałem, pomnożę przez sumę jej cyfr, to otrzymam iloczyn 52. Jaka jest suma cyfr liczby, o której pomyślałem? *(4 pkt)* *(Alfik 2022, zad. 16)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5
   <details><summary>rozwiązanie</summary>D — 4<br>Liczba musi być dzielnikiem 52: 1, 2, 4, 13, 26, 52. Sprawdzamy: 13 ma sumę cyfr 4, a 13 · 4 = 52. Pozostałe nie pasują (np. 26 · 8 = 208, 4 · 4 = 16).</details><br>
11. Pewna liczba dwucyfrowa jest dokładnie 5 razy większa od sumy swoich cyfr. Jaka jest cyfra dziesiątek tej liczby? *(4 pkt)* *(Alfik 2018, zad. 18)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) inna odpowiedź
   <details><summary>rozwiązanie</summary>D — 4<br>Liczba jest 5 razy większa od czegoś, więc dzieli się przez 5 — kończy się na 0 lub 5. Sprawdzamy: 45 ma sumę cyfr 9, a 5 · 9 = 45. Pasuje (i to jedyna taka liczba). Cyfra dziesiątek to 4.</details><br>
12. Ile jest takich trzycyfrowych liczb, których iloczyn cyfr wynosi 9? *(4 pkt)* *(Alfik 2017, zad. 18)*
   - A) 1
   - B) 3
   - C) 6
   - D) 9
   - E) 12
   <details><summary>rozwiązanie</summary>C — 6<br>9 jako iloczyn trzech cyfr: 1 · 1 · 9 albo 1 · 3 · 3. Z cyfr 1, 1, 9 są liczby 119, 191, 911, a z cyfr 1, 3, 3 — 133, 313, 331. Razem 6.</details><br>
13. Jacek zapomniał czterocyfrowego PIN-u do swojego telefonu. Pamiętał jedynie, że cyfry były ustawione w kolejności rosnącej (od najmniejszej do największej), iloczyn wszystkich cyfr był równy 70, a suma – 15. Jaka była trzecia cyfra PIN-u? *(4 pkt)* *(Alfik 2016, zad. 15)*
   - A) 2
   - B) 3
   - C) 4
   - D) 5
   - E) 7
   <details><summary>rozwiązanie</summary>D — 5<br>70 = 2 · 5 · 7, a czwarta cyfra musi być 1 (cyfry są różne, bo rosną). PIN to 1257: suma 1 + 2 + 5 + 7 = 15 — zgadza się. Trzecia cyfra to 5.</details><br>
14. Ile jest liczb dwucyfrowych, które są 4 razy większe od sumy swoich cyfr? *(5 pkt)*
   - A) 1
   - B) 2
   - C) 4
   - D) 5
   - E) 6
   <details><summary>rozwiązanie</summary>C — 4<br>Liczba dwucyfrowa to 10 razy cyfra dziesiątek plus cyfra jedności. Cztery razy suma cyfr to 4 razy cyfra dziesiątek plus 4 razy cyfra jedności. Gdy porównamy obie strony i „zabierzemy” to, co wspólne, zostaje: 6 razy cyfra dziesiątek = 3 razy cyfra jedności, czyli cyfra jedności jest 2 razy większa od cyfry dziesiątek. Pasują 12, 24, 36, 48 (przy cyfrze dziesiątek 5 cyfra jedności musiałaby wynosić 10 — a to nie jest cyfra). Sprawdzenie: 36 = 4 · (3 + 6).</details><br>
15. Ile jest takich liczb dwucyfrowych, które są dokładnie 6 razy większe od swojej cyfry jedności? *(5 pkt)* *(Alfik 2025, zad. 23)*
   - A) 0
   - B) 1
   - C) 2
   - D) 3
   - E) 4 lub więcej
   <details><summary>rozwiązanie</summary>E — 4 lub więcej<br>Sprawdzamy: 12 = 6 · 2, 24 = 6 · 4, 36 = 6 · 6, 48 = 6 · 8. Działa, gdy cyfra jedności jest dwa razy większa od cyfry dziesiątek — są 4 takie liczby.</details><br>
16. W każde swoje urodziny Ania porównuje sumę cyfr bieżącego roku z liczbą lat, które kończy. Wielokrotnie obie te liczby były równe, ale w ubiegłym roku równe nie były. Ile lat ma Ania, jeśli wiemy, że jest jeszcze niepełnoletnia? *(5 pkt)* *(Alfik 2023, zad. 29)*
   - A) 7
   - B) 10
   - C) 12
   - D) 15
   - E) 16
   <details><summary>rozwiązanie</summary>E — 16<br>Konkurs był w 2023 roku. W latach 2010–2019 suma cyfr roku rośnie co roku o 1 (od 3 do 12), tak jak wiek. Jeśli w 2010 Ania kończyła 3 lata (urodzona w 2007), to liczby były równe 10 razy, aż do 2019. W 2020 suma cyfr spada do 4, więc w 2022 już nie były równe. W 2023 Ania kończy 16 lat. Inne odpowiedzi nie pasują, np. przy 7 latach (rok 2016) liczby były równe także w 2022.</details><br>
17. Ile jest takich liczb trzycyfrowych, których suma cyfr jest równa iloczynowi cyfr? *(5 pkt)* *(Alfik 2022, zad. 30)*
   - A) 0
   - B) 1
   - C) 2
   - D) 3
   - E) 4 lub więcej
   <details><summary>rozwiązanie</summary>E — 4 lub więcej<br>Cyfry 1, 2, 3: 1 + 2 + 3 = 6 i 1 · 2 · 3 = 6. Z tych cyfr można ułożyć 6 liczb: 123, 132, 213, 231, 312, 321. To już więcej niż 4 (a innych takich liczb trzycyfrowych nie ma).</details><br>
18. Ile cyfr ma najmniejsza taka liczba, której cyfrą jedności jest 4, i której suma cyfr jest równa iloczynowi cyfr? *(5 pkt)* *(Alfik 2016, zad. 22)*
   - A) 3
   - B) 4
   - C) 5
   - D) 6
   - E) nie ma takiej liczby
   <details><summary>rozwiązanie</summary>B — 4<br>Dwucyfrowa: a + 4 = 4 · a nie ma rozwiązania w cyfrach. Trzycyfrowa: sprawdzając cyfry (np. 1, 1, 4: suma 6, iloczyn 4; 1, 2, 4: suma 7, iloczyn 8) — żadna nie pasuje. Czterocyfrowa 1124: suma 1 + 1 + 2 + 4 = 8 i iloczyn 1 · 1 · 2 · 4 = 8. Najmniejsza taka liczba ma 4 cyfry.</details><br>
19. Jaką cyfrę dziesiątek ma liczba dwucyfrowa, której iloczyn cyfr jest równy sumie cyfr? *(5 pkt)* *(Alfik 2015, zad. 23)*
   - A) 4
   - B) 3
   - C) 2
   - D) 1
   - E) nie ma takiej liczby
   <details><summary>rozwiązanie</summary>C — 2<br>To liczba 22: 2 · 2 = 4 i 2 + 2 = 4. Sprawdzając wszystkie liczby dwucyfrowe, innej takiej nie ma (np. dla cyfry 1 iloczyn jest zawsze mniejszy od sumy).</details><br>

## B. Palindromy i dopisywanie cyfr

Palindrom to liczba, która czyta się tak samo od lewej i od prawej, np. 727 albo 4554.

20. Ile jest palindromów trzycyfrowych większych od 500? *(3 pkt)*
   - A) 40
   - B) 44
   - C) 45
   - D) 49
   - E) 50
   <details><summary>rozwiązanie</summary>E — 50<br>Pierwsza cyfra (taka sama jak ostatnia) może być 5, 6, 7, 8 lub 9 — 5 możliwości. Środkowa cyfra dowolna, od 0 do 9 — 10 możliwości. Razem 5 · 10 = 50. Najmniejszy z nich to 505, a on jest większy od 500.</details><br>
21. Do pewnej liczby dwucyfrowej dopisano na końcu cyfrę 0. Nowa liczba jest o 252 większa od początkowej. Jaka była początkowa liczba? *(3 pkt)*
   - A) 25
   - B) 28
   - C) 32
   - D) 36
   - E) 42
   <details><summary>rozwiązanie</summary>B — 28<br>Dopisanie zera na końcu to pomnożenie liczby przez 10. Nowa liczba to 10 takich liczb, stara to 1 taka liczba, więc różnica to 9 takich liczb. 252 : 9 = 28. Sprawdzenie: 280 − 28 = 252.</details><br>
22. Liczba palindromiczna to liczba, która czytana wprzód i wspak wygląda tak samo, np. 3223 lub 15251. Ile jest czterocyfrowych liczb palindromicznych o sumie cyfr równej 6? *(3 pkt)* *(Alfik 2022, zad. 6)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5 lub więcej
   <details><summary>rozwiązanie</summary>C — 3<br>Czterocyfrowy palindrom ma postać abba, więc suma cyfr to 2 · (a + b) = 6, czyli a + b = 3. Cyfra a nie może być zerem: 1221, 2112, 3003. Są 3 takie liczby.</details><br>
23. Liczba palindromiczna, to liczba, która czytana od lewej do prawej jest taka sama jak czytana od prawej do lewej, np. 343. Ile jest trzycyfrowych liczb palindromicznych o sumie cyfr równej 7? *(3 pkt)* *(Alfik 2021, zad. 10)*
   - A) 2
   - B) 3
   - C) 4
   - D) 5
   - E) 6
   <details><summary>rozwiązanie</summary>B — 3<br>Palindrom trzycyfrowy ma postać „a b a”, więc suma cyfr to a + a + b = 7. a = 1 → b = 5 (151), a = 2 → b = 3 (232), a = 3 → b = 1 (313); dla a = 4 już za dużo. Razem 3.</details><br>
24. Liczba palindromiczna to liczba, która czytana wprzód i wspak wygląda jednakowo, np. 2552. Ile lat o numerach palindromicznych wystąpiło w ciągu ostatnich stu lat? *(3 pkt)* *(Alfik 2016, zad. 5)*
   - A) 0
   - B) 1
   - C) 2
   - D) 3
   - E) 4
   <details><summary>rozwiązanie</summary>C — 2<br>W latach 1917–2016 palindromami są tylko 1991 i 2002. Następny będzie dopiero 2112.</details><br>
25. Jaką najmniejszą liczbę trzeba dodać do 2026, aby otrzymać palindrom? *(4 pkt)*
   - A) 76
   - B) 86
   - C) 96
   - D) 106
   - E) 186
   <details><summary>rozwiązanie</summary>B — 86<br>Palindrom czterocyfrowy zaczynający się od 2 musi kończyć się na 2 i mieć dwie jednakowe cyfry w środku: 2002, 2112, 2222, … Liczba 2002 jest mniejsza od 2026, więc najbliższy większy palindrom to 2112. 2112 − 2026 = 86.</details><br>
26. Liczba palindromiczna to liczba, która czytana wprzód wygląda tak samo jak czytana wspak, np. 242 lub 3553. Ile jest trzycyfrowych liczb palindromicznych o sumie cyfr 10? *(4 pkt)* *(Alfik 2024, zad. 18)*
   - A) 4
   - B) 5
   - C) 6
   - D) 9
   - E) 10
   <details><summary>rozwiązanie</summary>B — 5<br>Palindrom trzycyfrowy ma postać aba, a suma cyfr to a + b + a = 10. Pierwsza cyfra a może być 1, 2, 3, 4 lub 5 (dla 6 byłoby już 12 > 10): 181, 262, 343, 424, 505. To 5 liczb.</details><br>
27. Liczbę 12345 chcemy zamienić w liczbę 34512, wykonując ruchy polegające na zamianie miejscami dwóch cyfr. Jaka jest najmniejsza liczba ruchów jaką musimy wykonać? *(4 pkt)* *(Alfik 2018, zad. 13)*
   - A) 4 lub mniej
   - B) 5
   - C) 6
   - D) 7
   - E) 8 lub więcej
   <details><summary>rozwiązanie</summary>A — 4 lub mniej<br>Każdym ruchem możemy postawić jedną cyfrę na właściwym miejscu: 12345 → 32145 → 34125 → 34521 → 34512. Wystarczą 4 ruchy (a ostatni ruch zawsze ustawia od razu dwie cyfry).</details><br>
28. Liczba palindromiczna to taka liczba, która czytana od lewej do prawej i czytana od prawej do lewej wygląda tak samo, np. 3553 lub 727. Ile jest trzycyfrowych liczb palindromicznych o sumie cyfr równej 10? *(4 pkt)* *(Alfik 2017, zad. 11)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) więcej niż 4
   <details><summary>rozwiązanie</summary>E — więcej niż 4<br>Palindrom trzycyfrowy ma postać „aba”, a suma cyfr to a + b + a. Pasują: 181, 262, 343, 424, 505 — to już 5 liczb (dla a = 6 suma przekracza 10).</details><br>
29. Do liczby dwucyfrowej dopisano cyfrę 1 na początku i cyfrę 1 na końcu. Powstała liczba czterocyfrowa jest 23 razy większa od początkowej. Jaka była początkowa liczba? *(5 pkt)*
   - A) 44
   - B) 55
   - C) 66
   - D) 77
   - E) 88
   <details><summary>rozwiązanie</summary>D — 77<br>Liczba 1 _ _ 1 to 1000 + 1 + 10 razy nasza liczba, czyli 1001 + 10 razy nasza liczba. Ma to być 23 razy nasza liczba. Zatem 1001 to 23 − 10 = 13 razy nasza liczba: 1001 : 13 = 77. Sprawdzenie: 77 · 23 = 1771. Można też po prostu sprawdzić odpowiedzi: np. 1441 : 44 nie dzieli się bez reszty.</details><br>
30. Pewna dwucyfrowa liczba zwiększa się 7-krotnie, jeśli między obie jej cyfry wstawimy zero (otrzymując liczbę trzycyfrową). Jaka jest suma cyfr tej liczby? *(5 pkt)* *(Alfik 2022, zad. 22)*
   - A) 3
   - B) 4
   - C) 5
   - D) 6
   - E) 7
   <details><summary>rozwiązanie</summary>D — 6<br>Szukana liczba to 15: po wstawieniu zera mamy 105 = 7 · 15. Suma cyfr: 1 + 5 = 6. (Sprawdzenie wszystkich liczb dwucyfrowych pokazuje, że to jedyna taka liczba.)</details><br>
31. Ile jest takich liczb dwucyfrowych, które zmniejszają się dokładnie 6 razy po usunięciu cyfry dziesiątek? *(5 pkt)* *(Alfik 2021, zad. 26)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) nie ma takich liczb
   <details><summary>rozwiązanie</summary>D — 4<br>Po usunięciu cyfry dziesiątek zostaje cyfra jedności, a liczba ma być 6 razy większa od niej. Liczba = 10 · dziesiątki + jedności = 6 · jedności, więc 10 · dziesiątki = 5 · jedności, czyli jedności = 2 · dziesiątki. Pasują 12, 24, 36, 48 (12 = 6 · 2, 24 = 6 · 4, 36 = 6 · 6, 48 = 6 · 8). Razem 4.</details><br>
32. Pewna liczba dwucyfrowa zwiększa się 5 razy, gdy na jej początku (jako cyfrę setek) dopiszemy cyfrę 1. Jaka jest cyfra jedności tej liczby? *(5 pkt)* *(Alfik 2019, zad. 30)*
   - A) 2
   - B) 3
   - C) 5
   - D) 6
   - E) 8
   <details><summary>rozwiązanie</summary>C — 5<br>Dopisanie jedynki z przodu dodaje 100. Nowa liczba to 5 razy stara, czyli dodaliśmy 4 razy starą liczbę: 4 · liczba = 100, więc liczba to 25 (125 = 5 · 25). Cyfra jedności to 5.</details><br>

## C. Największa i najmniejsza liczba

Najmniejsza liczba: jak najmniej cyfr i jak najmniejsza cyfra na początku. Największa liczba: jak najwięcej cyfr i jak największa cyfra na początku.

33. Jaka jest najmniejsza liczba naturalna, której suma cyfr wynosi 30? *(3 pkt)*
   - A) 3999
   - B) 5799
   - C) 6699
   - D) 9993
   - E) 39999
   <details><summary>rozwiązanie</summary>A — 3999<br>Trzy cyfry dają najwyżej 9 + 9 + 9 = 27, a to za mało, więc potrzeba co najmniej 4 cyfr. Żeby liczba czterocyfrowa była jak najmniejsza, pierwsza cyfra ma być jak najmniejsza, a pozostałe jak największe: trzy dziewiątki dają 27, więc pierwsza cyfra to 30 − 27 = 3. Wynik: 3999.</details><br>
34. Jaka jest największa liczba o różnych cyfrach, której suma cyfr wynosi 20? *(4 pkt)*
   - A) 9821
   - B) 98210
   - C) 863210
   - D) 953210
   - E) 963110
   <details><summary>rozwiązanie</summary>D — 953210<br>Im więcej cyfr, tym większa liczba. Siedem różnych cyfr ma sumę co najmniej 0 + 1 + 2 + 3 + 4 + 5 + 6 = 21, czyli za dużo — więc najwyżej 6 cyfr. Na początku chcemy 9; wtedy pięć pozostałych różnych cyfr musi dać 11, a jedyny sposób to 0, 1, 2, 3, 5. Ustawiamy malejąco: 953210. Pułapka: 963110 jest większa, ale ma dwie jedynki — cyfry się powtarzają.</details><br>
35. Ile jest takich dwucyfrowych liczb, które po pomnożeniu przez 6 dają w wyniku liczbę dwucyfrową? *(4 pkt)* *(Alfik 2018, zad. 20)*
   - A) 5
   - B) 6
   - C) 7
   - D) 8
   - E) więcej niż 8
   <details><summary>rozwiązanie</summary>C — 7<br>Wynik ma być najwyżej 99, a 6 · 16 = 96, 6 · 17 = 102. Pasują liczby od 10 do 16 — jest ich 7.</details><br>
36. Jaka jest najmniejsza liczba naturalna, której iloczyn cyfr wynosi 360? *(5 pkt)*
   - A) 589
   - B) 598
   - C) 2459
   - D) 3358
   - E) 12589
   <details><summary>rozwiązanie</summary>A — 589<br>Dwie cyfry dają iloczyn najwyżej 9 · 9 = 81, więc potrzeba co najmniej trzech. 360 dzieli się przez 5, a jedyna cyfra podzielna przez 5 (oprócz zera) to 5 — więc jedna cyfra to 5. Zostaje 360 : 5 = 72, a 72 jako iloczyn dwóch cyfr to tylko 8 · 9. Cyfry 5, 8, 9 ustawiamy od najmniejszej: 589. Pułapka: 2459 i 3358 też mają iloczyn cyfr 360, ale są czterocyfrowe, więc większe.</details><br>

## D. Liczenie cyfr i numerowanie stron

Licz osobno cyfry na miejscu jedności, dziesiątek i setek. Przy stronach książki dziel strony na jednocyfrowe, dwucyfrowe i trzycyfrowe.

37. Ile razy trzeba napisać cyfrę 7, zapisując wszystkie liczby od 1 do 100? *(3 pkt)*
   - A) 10
   - B) 11
   - C) 19
   - D) 20
   - E) 21
   <details><summary>rozwiązanie</summary>D — 20<br>Siódemka jako cyfra jedności: 7, 17, 27, …, 97 — 10 razy. Siódemka jako cyfra dziesiątek: 70, 71, …, 79 — 10 razy. Razem 20. W liczbie 77 siódemkę piszemy dwa razy i obie są policzone. Pułapka: 19 to liczba <b>liczb</b> zawierających siódemkę, a pytamy o liczbę napisanych <b>cyfr</b>.</details><br>
38. Ile jest wszystkich liczb dwucyfrowych? *(3 pkt)* *(Alfik 2018, zad. 4)*
   - A) 89
   - B) 90
   - C) 91
   - D) 99
   - E) 100
   <details><summary>rozwiązanie</summary>B — 90<br>Liczby od 10 do 99. Od 1 do 99 jest 99 liczb, odejmujemy 9 jednocyfrowych: 99 − 9 = 90.</details><br>
39. Ile jedynek ma w swoim zapisie liczba *sto jedenaście milionów sto jedenaście*? *(3 pkt)* *(Alfik 2016, zad. 3)*
   - A) 3
   - B) 4
   - C) 5
   - D) 6
   - E) 7
   <details><summary>rozwiązanie</summary>D — 6<br>Ta liczba to 111 000 111 — ma sześć jedynek (trzy w milionach i trzy w jednościach).</details><br>
40. Do ponumerowania wszystkich stron książki (zaczynając od 1) zużyto 192 cyfry. Ile stron ma ta książka? *(4 pkt)*
   - A) 96
   - B) 99
   - C) 100
   - D) 101
   - E) 192
   <details><summary>rozwiązanie</summary>C — 100<br>Strony 1–9 to 9 cyfr. Strony 10–99 to 90 stron po 2 cyfry, czyli 180 cyfr. Razem 189 cyfr. Do 192 brakuje jeszcze 3 cyfr — to dokładnie jedna strona trzycyfrowa, strona 100.</details><br>
41. Numerując wszystkie strony pewnej książki kolejnymi liczbami naturalnymi (zaczynając od numeru 1), zapisano łącznie 300 cyfr. Ile stron ma ta książka? *(4 pkt)* *(Alfik 2023, zad. 17)*
   - A) 100
   - B) 124
   - C) 130
   - D) 134
   - E) 136
   <details><summary>rozwiązanie</summary>E — 136<br>Strony 1–9 to 9 cyfr, strony 10–99 to 90 · 2 = 180 cyfr; razem 189. Zostaje 300 − 189 = 111 cyfr, czyli 111 : 3 = 37 stron trzycyfrowych: od 100 do 136.</details><br>
42. Ola numeruje kolejne strony bardzo grubego zeszytu, zaczynając od 1. Na której stronie skończy, jeśli zużyje dokładnie 2026 cyfr? *(5 pkt)*
   - A) 612
   - B) 613
   - C) 711
   - D) 712
   - E) nie da się zużyć dokładnie 2026 cyfr
   <details><summary>rozwiązanie</summary>E — nie da się zużyć dokładnie 2026 cyfr<br>Strony 1–99 zużywają 189 cyfr. Na strony trzycyfrowe zostaje 2026 − 189 = 1837 cyfr. Każda strona trzycyfrowa zużywa 3 cyfry, a 1837 nie dzieli się przez 3 (1837 = 3 · 612 + 1). Po stronie 711 (to 612. strona trzycyfrowa) zużytych jest 2025 cyfr, a po stronie 712 — już 2028. Do stron czterocyfrowych nie dojdziemy, bo strony 1–999 to aż 2889 cyfr. Pułapka: 612 to liczba stron trzycyfrowych, a nie numer ostatniej strony.</details><br>

---

## Klucz odpowiedzi

1. B — 9
2. B — 3 *(Alfik 2021, zad. 3)*
3. B — 2 *(Alfik 2019, zad. 2)*
4. E — więcej niż 8 *(Alfik 2019, zad. 9)*
5. E — więcej niż 4 *(Alfik 2018, zad. 7)*
6. C — 3 *(Alfik 2017, zad. 9)*
7. C — 15
8. E — 6
9. D — 3 *(Alfik 2024, zad. 15)*
10. D — 4 *(Alfik 2022, zad. 16)*
11. D — 4 *(Alfik 2018, zad. 18)*
12. C — 6 *(Alfik 2017, zad. 18)*
13. D — 5 *(Alfik 2016, zad. 15)*
14. C — 4
15. E — 4 lub więcej *(Alfik 2025, zad. 23)*
16. E — 16 *(Alfik 2023, zad. 29)*
17. E — 4 lub więcej *(Alfik 2022, zad. 30)*
18. B — 4 *(Alfik 2016, zad. 22)*
19. C — 2 *(Alfik 2015, zad. 23)*
20. E — 50
21. B — 28
22. C — 3 *(Alfik 2022, zad. 6)*
23. B — 3 *(Alfik 2021, zad. 10)*
24. C — 2 *(Alfik 2016, zad. 5)*
25. B — 86
26. B — 5 *(Alfik 2024, zad. 18)*
27. A — 4 lub mniej *(Alfik 2018, zad. 13)*
28. E — więcej niż 4 *(Alfik 2017, zad. 11)*
29. D — 77
30. D — 6 *(Alfik 2022, zad. 22)*
31. D — 4 *(Alfik 2021, zad. 26)*
32. C — 5 *(Alfik 2019, zad. 30)*
33. A — 3999
34. D — 953210
35. C — 7 *(Alfik 2018, zad. 20)*
36. A — 589
37. D — 20
38. B — 90 *(Alfik 2018, zad. 4)*
39. D — 6 *(Alfik 2016, zad. 3)*
40. C — 100
41. E — 136 *(Alfik 2023, zad. 17)*
42. E — nie da się zużyć dokładnie 2026 cyfr

## Ściąga

| Fakt | Przykład |
|---|---|
| Liczb dwucyfrowych jest 90 (10–99), trzycyfrowych 900 (100–999) | |
| Palindromów trzycyfrowych jest 9 · 10 = 90 | 101, 111, …, 999 |
| Trzy różne cyfry ustawisz na 6 sposobów, trzy cyfry z dwiema takimi samymi — na 3 | 126, 162, 216, 261, 612, 621 / 223, 232, 322 |
| Dopisanie 0 na końcu = mnożenie przez 10 | 28 → 280 |
| Dopisanie cyfry 1 na początku liczby dwucyfrowej = dodanie 100 | 28 → 128 |
| Numerowanie stron: 1–9 → 9 cyfr, 1–99 → 189 cyfr, 1–999 → 2889 cyfr | |
| Od 1 do 100 każda cyfra 1–9 pojawia się 20 razy (cyfra 1 — 21 razy, przez 100) | cyfra 7: 20 razy |
| Najmniejsza liczba o danej sumie cyfr: na końcu same dziewiątki, reszta z przodu | suma 30 → 3999 |
| Najmniejsza liczba o danym iloczynie cyfr: jak najmniej cyfr (duże cyfry 9, 8), ustawione rosnąco | iloczyn 360 → 589 |
