# 03. Podzielność i reszty

**Dlaczego warto:** W każdym arkuszu Alfika jest kilka zadań, w których pomaga podzielność: cechy podzielności przez 3, 4, 5, 9, liczenie wielokrotności, wspólne wielokrotności („kiedy znów razem?”), reszty z dzielenia i ostatnia cyfra wyniku. Kto zna cechy podzielności i sztuczkę „dodaj 1, żeby reszta zniknęła”, rozwiązuje takie zadania w minutę.

- **W pliku:** 47 zadań: 14 nowych i 33 z prawdziwych arkuszy Alfika (18 za 3 pkt, 14 za 4 pkt, 15 za 5 pkt).

**Wskazówki**
- Cechy podzielności: przez 3 i przez 9 — patrz na **sumę cyfr**; przez 4 — na **dwie ostatnie cyfry**; przez 5 — ostatnia cyfra 0 lub 5; przez 6 — parzysta i podzielna przez 3; przez 12 — przez 4 i przez 3.
- Ile wielokrotności liczby 6 jest od 1 do 100? Podziel 100 : 6 i weź wynik bez reszty: 16.
- „Przez 4 lub przez 6”: dodaj obie grupy, a potem odejmij te liczby, które policzyłeś dwa razy (podzielne przez obie).
- „Kiedy znów razem?” — szukasz najmniejszej wspólnej wielokrotności. „Jak najwięcej jednakowych paczek?” — szukasz największego wspólnego dzielnika.
- Gdy przy każdym dzieleniu brakuje 1 do pełnej grupy (reszta 5 z dzielenia przez 6, reszta 7 z dzielenia przez 8…), dodaj 1 — wtedy wszystko dzieli się bez reszty.
- Ostatnia cyfra wyniku mnożenia zależy tylko od ostatnich cyfr mnożonych liczb. Ostatnie cyfry kolejnych potęg powtarzają się co 4.

**Spis treści**

- [A. Cechy podzielności](#a-cechy-podzielności)
- [B. Wielokrotności i wspólne dzielniki](#b-wielokrotności-i-wspólne-dzielniki)
- [C. Dzielenie z resztą](#c-dzielenie-z-resztą)
- [D. Ostatnia cyfra i zera na końcu](#d-ostatnia-cyfra-i-zera-na-końcu)
- [Klucz odpowiedzi](#klucz-odpowiedzi)
- [Ściąga](#ściąga)

---

## A. Cechy podzielności

Cechy podzielności pozwalają sprawdzić, czy liczba dzieli się przez 3, 4, 5, 9…, bez wykonywania dzielenia.

1. W liczbie 52□4 w miejsce □ wpisano cyfrę tak, że powstała liczba podzielna przez 9. Jaka to cyfra? *(3 pkt)*
   - A) 1
   - B) 3
   - C) 7
   - D) 8
   - E) 9
   <details><summary>rozwiązanie</summary>C — 7<br>Liczba dzieli się przez 9, gdy jej suma cyfr dzieli się przez 9. Bez brakującej cyfry suma to 5 + 2 + 4 = 11. Do 18 brakuje 7, a do 27 brakowałoby 16 — za dużo na jedną cyfrę. Więc cyfra to 7: 5274 : 9 = 586.</details><br>
2. Ile jest cyfr, które można wpisać w miejsce □ w liczbie 41□6, żeby otrzymać liczbę podzielną przez 4? *(3 pkt)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5
   <details><summary>rozwiązanie</summary>E — 5<br>Liczba dzieli się przez 4, gdy liczba utworzona z jej dwóch ostatnich cyfr dzieli się przez 4. Sprawdzamy □6: 16, 36, 56, 76, 96 dzielą się przez 4, a 06, 26, 46, 66, 86 — nie. Pasują cyfry 1, 3, 5, 7, 9, czyli 5 cyfr. Pułapka: to, że liczba jest parzysta, jeszcze nie wystarcza do podzielności przez 4.</details><br>
3. Suma 5 liczb dwucyfrowych wynosi 100. Ile najwięcej liczb nieparzystych może być wśród tych pięciu liczb? *(3 pkt)* *(Alfik 2025, zad. 8)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5
   <details><summary>rozwiązanie</summary>D — 4<br>Suma nieparzystej liczby liczb nieparzystych jest nieparzysta, a 100 jest parzyste — więc liczb nieparzystych musi być parzyście wiele: 5 odpada. 4 się da: 11 + 11 + 11 + 11 + 56 = 100.</details><br>
4. Znając cyfrę jedności i cyfrę dziesiątek liczby trzycyfrowej nie można jednoznacznie ustalić, czy liczba ta jest podzielna przez: *(3 pkt)* *(Alfik 2024, zad. 8)*
   - A) 2
   - B) 3
   - C) 4
   - D) 5
   - E) 10
   <details><summary>rozwiązanie</summary>B — 3<br>Podzielność przez 2, 5 i 10 zależy tylko od cyfry jedności, a przez 4 — od dwóch ostatnich cyfr. Podzielność przez 3 zależy od sumy WSZYSTKICH cyfr, więc bez cyfry setek nie da się jej ustalić (np. 112 nie dzieli się przez 3, a 312 — tak).</details><br>
5. Z czterech spośród poniższych cyfr można ułożyć (wykorzystując każdą cyfrę raz) czterocyfrową liczbę podzielną przez 9. Której cyfry nie użyjemy? *(3 pkt)* *(Alfik 2024, zad. 9)*
   - A) 0
   - B) 1
   - C) 2
   - D) 3
   - E) 4
   <details><summary>rozwiązanie</summary>B — 1<br>Liczba dzieli się przez 9, gdy suma jej cyfr dzieli się przez 9. Wszystkie cyfry 0 + 1 + 2 + 3 + 4 dają 10. Żeby zostało 9, musimy pominąć cyfrę 1 — np. 4320 dzieli się przez 9.</details><br>
6. Ile jest takich trzycyfrowych liczb podzielnych przez 9, które można ułożyć z cyfr 2, 3, 4 (wykorzystując każdą cyfrę najwyżej raz)? *(3 pkt)* *(Alfik 2023, zad. 8)*
   - A) 2
   - B) 3
   - C) 4
   - D) 6
   - E) 7
   <details><summary>rozwiązanie</summary>D — 6<br>Liczba trzycyfrowa z różnych cyfr 2, 3, 4 musi zawierać wszystkie trzy. Suma cyfr 2 + 3 + 4 = 9, więc każda taka liczba dzieli się przez 9. Ułożeń jest 3 · 2 · 1 = 6: 234, 243, 324, 342, 423, 432.</details><br>
7. Której z poniższych liczb nie można przedstawić jako sumy dwóch liczb nieparzystych? *(3 pkt)* *(Alfik 2019, zad. 7)*
   - A) 24
   - B) 28
   - C) 32
   - D) 36
   - E) 39
   <details><summary>rozwiązanie</summary>E — 39<br>Nieparzysta + nieparzysta = zawsze liczba parzysta. 39 jest nieparzyste, więc nie da się go tak zapisać. Pozostałe da się, np. 24 = 1 + 23.</details><br>
8. Suma pewnych 13 liczb naturalnych (niekoniecznie różnych) jest równa 100. Ile najwięcej liczb nieparzystych może być wśród tych liczb? *(3 pkt)* *(Alfik 2017, zad. 2)*
   - A) 9
   - B) 10
   - C) 11
   - D) 12
   - E) 13
   <details><summary>rozwiązanie</summary>D — 12<br>Suma nieparzystej liczby liczb nieparzystych jest nieparzysta, a 100 jest parzyste — więc liczb nieparzystych musi być parzyście wiele. Wszystkie 13 odpada, ale 12 się da: dwanaście jedynek i liczba 88 (12 + 88 = 100).</details><br>
9. Suma trzynastu liczb całkowitych jest równa 100. Ile najwięcej spośród tych liczb może być liczbami nieparzystymi? *(3 pkt)* *(Alfik 2016, zad. 4)*
   - A) 9
   - B) 10
   - C) 11
   - D) 12
   - E) 13
   <details><summary>rozwiązanie</summary>D — 12<br>Suma nieparzystej liczby liczb nieparzystych jest nieparzysta, a 100 jest parzyste — więc liczb nieparzystych musi być parzyście wiele, najwyżej 12. Przykład: dwanaście jedynek i liczba 88.</details><br>
10. Ile jest dwucyfrowych liczb nieparzystych (dodatnich)? *(3 pkt)* *(Alfik 2016, zad. 10)*
   - A) 40
   - B) 44
   - C) 45
   - D) 46
   - E) 50
   <details><summary>rozwiązanie</summary>C — 45<br>Liczb dwucyfrowych jest 90 (od 10 do 99), a nieparzysta jest co druga: 90 : 2 = 45.</details><br>
11. Ile jest liczb trzycyfrowych podzielnych przez 5, których suma cyfr wynosi 10? *(4 pkt)*
   - A) 9
   - B) 10
   - C) 13
   - D) 14
   - E) 15
   <details><summary>rozwiązanie</summary>D — 14<br>Ostatnia cyfra to 0 albo 5. Gdy na końcu jest 0, pierwsze dwie cyfry dają sumę 10: 190, 280, 370, 460, 550, 640, 730, 820, 910 — to 9 liczb. Gdy na końcu jest 5, pierwsze dwie cyfry dają sumę 5: 145, 235, 325, 415, 505 — to 5 liczb (055 nie jest trzycyfrowa). Razem 9 + 5 = 14. Pułapka: 9 — gdy zapomnimy o liczbach kończących się na 5.</details><br>
12. Ile jest takich trzycyfrowych liczb podzielnych przez 9, których cyfrą dziesiątek jest 9? *(4 pkt)* *(Alfik 2021, zad. 14)*
   - A) 8
   - B) 9
   - C) 10
   - D) 90
   - E) więcej niż 90
   <details><summary>rozwiązanie</summary>C — 10<br>Suma cyfr musi dzielić się przez 9, więc cyfra setek + cyfra jedności = 9 lub 18. Suma 9: 198, 297, 396, 495, 594, 693, 792, 891, 990 (9 liczb). Suma 18: tylko 999. Razem 10. Pułapka: łatwo zapomnieć o 999 lub o 990.</details><br>
13. W liczbie 7□3□ w miejsca □ wpisano cyfry (mogą być takie same lub różne) tak, że powstała liczba podzielna przez 12. Ile różnych liczb można w ten sposób otrzymać? *(5 pkt)*
   - A) 6
   - B) 7
   - C) 8
   - D) 9
   - E) 10
   <details><summary>rozwiązanie</summary>B — 7<br>Liczba dzieli się przez 12, gdy dzieli się i przez 4, i przez 3. Przez 4: dwie ostatnie cyfry 3□ muszą tworzyć 32 albo 36. Przez 3: suma cyfr musi dzielić się przez 3. Gdy końcówka to 32, suma to 7 + 3 + 2 = 12 plus brakująca cyfra, więc ta cyfra to 0, 3, 6 lub 9 (4 liczby). Gdy końcówka to 36, suma to 16 plus brakująca cyfra, więc cyfra to 2, 5 lub 8 (3 liczby). Razem 4 + 3 = 7.</details><br>
14. Iloczyn 5 liczb (naturalnych) wynosi 120, a ich suma jest liczbą nieparzystą. Ile liczb parzystych jest wśród tych pięciu liczb? *(5 pkt)* *(Alfik 2019, zad. 25)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5
   <details><summary>rozwiązanie</summary>B — 2<br>120 = 2 · 2 · 2 · 15, więc parzystych liczb może być 1, 2 albo 3. Suma pięciu liczb jest nieparzysta, gdy liczb nieparzystych jest nieparzyście wiele. 1 parzysta → 4 nieparzyste (suma parzysta), 3 parzyste → 2 nieparzyste (suma parzysta), 2 parzyste → 3 nieparzyste (suma nieparzysta). Przykład: 2 · 4 · 1 · 3 · 5 = 120, suma 15.</details><br>
15. Suma pewnych pięciu liczb dwucyfrowych jest liczbą nieparzystą, a ich iloczyn jest liczbą parzystą, niepodzielną przez 8. Ile spośród tych pięciu liczb jest liczbami parzystymi? *(5 pkt)* *(Alfik 2018, zad. 28)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5
   <details><summary>rozwiązanie</summary>B — 2<br>Suma jest nieparzysta, więc liczb nieparzystych jest nieparzyście wiele (1, 3 lub 5), czyli parzystych: 4, 2 lub 0. Iloczyn jest parzysty, więc 0 odpada. Cztery liczby parzyste dają iloczyn podzielny przez 2 · 2 · 2 · 2 = 16, a więc i przez 8 — też odpada. Zostają 2 liczby parzyste (np. 10 · 14 · 11 · 13 · 15 — iloczyn dzieli się przez 4, ale nie przez 8).</details><br>

## B. Wielokrotności i wspólne dzielniki

Wielokrotności liczby 6 to 6, 12, 18, … Wspólne wielokrotności dwóch liczb to te liczby, które są na obu listach.

16. Ile liczb od 1 do 100 dzieli się przez 6? *(3 pkt)*
   - A) 16
   - B) 17
   - C) 18
   - D) 20
   - E) 25
   <details><summary>rozwiązanie</summary>A — 16<br>100 : 6 = 16 reszty 4. Wielokrotności szóstki to 6, 12, …, 96 — jest ich 16, bo 16 · 6 = 96, a 17 · 6 = 102 to już więcej niż 100.</details><br>
17. Ile jest takich ułamków nieskracalnych, których licznik i mianownik to liczby jednocyfrowe o sumie 12? *(3 pkt)* *(Alfik 2025, zad. 3)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 6
   <details><summary>rozwiązanie</summary>B — 2<br>Pary cyfr o sumie 12: 3 i 9, 4 i 8, 5 i 7, 6 i 6 (w obu kolejnościach). 3/9, 4/8, 6/6 i odwrotności 9/3, 8/4 da się skrócić. Nieskracalne są tylko 5/7 i 7/5 — dwa ułamki.</details><br>
18. Ile jest nieskracalnych ułamków, których licznik jest dodatnią liczbą jednocyfrową, a mianownik jest o 2 większy od licznika? *(3 pkt)* *(Alfik 2024, zad. 3)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5 lub więcej
   <details><summary>rozwiązanie</summary>E — 5 lub więcej<br>Ułamki to 1/3, 2/4, 3/5, 4/6, 5/7, 6/8, 7/9, 8/10, 9/11. Gdy licznik jest parzysty, mianownik też jest parzysty i ułamek da się skrócić przez 2. Gdy licznik jest nieparzysty, licznik i mianownik różnią się o 2 i nie mają wspólnego dzielnika. Zostaje 1/3, 3/5, 5/7, 7/9, 9/11 — to 5 ułamków.</details><br>
19. Największy wspólny dzielnik dwóch liczb jednocyfrowych wynosi 2, a ich najmniejsza wspólna wielokrotność to 12. Ile wynosi suma tych dwóch liczb? *(3 pkt)* *(Alfik 2023, zad. 2)*
   - A) 10
   - B) 12
   - C) 14
   - D) 16
   - E) 24
   <details><summary>rozwiązanie</summary>A — 10<br>Obie liczby są parzyste i dzielą 12: to mogą być 2, 4, 6. Pasują 4 i 6: NWD = 2, NWW = 12. Suma 4 + 6 = 10. (2 i 6 mają NWW 6, a 2 i 4 mają NWD 2, ale NWW 4.)</details><br>
20. Ile jest dwucyfrowych wielokrotności liczby 11? *(3 pkt)* *(Alfik 2022, zad. 10)*
   - A) 6
   - B) 7
   - C) 8
   - D) 9
   - E) 10
   <details><summary>rozwiązanie</summary>D — 9<br>To liczby 11, 22, 33, …, 99 — od 11 · 1 do 11 · 9, czyli 9 liczb. 110 jest już trzycyfrowe.</details><br>
21. Ile liczb od 1 do 100 dzieli się przez 4 lub przez 6 (czyli przez co najmniej jedną z tych liczb)? *(4 pkt)*
   - A) 25
   - B) 33
   - C) 37
   - D) 41
   - E) 50
   <details><summary>rozwiązanie</summary>B — 33<br>Przez 4 dzieli się 25 liczb (100 : 4 = 25), przez 6 — 16 liczb. Ale niektóre liczby są na obu listach — to te podzielne przez 12: 12, 24, 36, 48, 60, 72, 84, 96, czyli 8 liczb. Policzyliśmy je dwa razy, więc odejmujemy: 25 + 16 − 8 = 33. Pułapka: 41 — gdy nie odejmiemy powtórzeń; 37 — gdy jako wspólne weźmiemy tylko wielokrotności 24, a zapomnimy o 12, 36, 60, 84.</details><br>
22. Autobus linii 3 odjeżdża z przystanku co 12 minut, a autobus linii 8 — co 18 minut. O 7:00 oba odjechały jednocześnie. O której godzinie najbliższy raz znów odjadą razem? *(4 pkt)*
   - A) 7:24
   - B) 7:30
   - C) 7:36
   - D) 8:00
   - E) 10:36
   <details><summary>rozwiązanie</summary>C — 7:36<br>Linia 3 odjeżdża o 7:12, 7:24, 7:36, … Linia 8 odjeżdża o 7:18, 7:36, … Pierwszy wspólny odjazd to 7:36 — bo 36 to najmniejsza liczba, która dzieli się i przez 12, i przez 18. Pułapka: 12 · 18 = 216 minut = 3 h 36 min daje 10:36 — wtedy też odjadą razem, ale to nie jest najbliższy raz.</details><br>
23. Ile jest takich liczb jednocyfrowych, które mają dokładnie trzy dzielniki? *(4 pkt)* *(Alfik 2025, zad. 14)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5
   <details><summary>rozwiązanie</summary>B — 2<br>Sprawdzamy: 4 ma dzielniki 1, 2, 4, a 9 ma dzielniki 1, 3, 9. Pozostałe mają 1, 2 albo 4 dzielniki (np. 6: 1, 2, 3, 6; 8: 1, 2, 4, 8). Są więc 2 takie liczby — kwadraty liczb pierwszych.</details><br>
24. Ile jest takich jednocyfrowych liczb, które są równe iloczynowi wszystkich swoich dzielników? *(4 pkt)* *(Alfik 2023, zad. 14)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) więcej niż 4
   <details><summary>rozwiązanie</summary>E — więcej niż 4<br>Liczba pierwsza p ma dzielniki 1 i p, a ich iloczyn to p — pasują 2, 3, 5, 7. Pasuje też 1 (jedyny dzielnik to 1). Liczby 4, 6, 8, 9 nie pasują (np. 1 · 2 · 4 = 8). Razem 5 liczb, czyli więcej niż 4. ⚠ Uwaga: oficjalny klucz uznaje w tym zadaniu dwie odpowiedzi — D i E. Odpowiedź D (4) wychodzi, jeśli nie liczyć liczby 1; liczymy ją, bo 1 jest równe iloczynowi swoich dzielników.</details><br>
25. Liczbę 1000 chcemy przedstawić w postaci iloczynu liczb parzystych. Ile najwięcej czynników może liczyć taki iloczyn? *(4 pkt)* *(Alfik 2023, zad. 19)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) więcej niż 4
   <details><summary>rozwiązanie</summary>C — 3<br>1000 = 2 · 2 · 2 · 5 · 5 · 5. Każdy czynnik parzysty musi zawierać co najmniej jedną dwójkę, a dwójki są tylko 3. Więc czynników jest najwyżej 3, np. 2 · 2 · 250.</details><br>
26. Iloczyn pięciu liczb (naturalnych) wynosi 360. Ile najwięcej spośród tych pięciu liczb może być parzystych? *(4 pkt)* *(Alfik 2021, zad. 16)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5
   <details><summary>rozwiązanie</summary>C — 3<br>360 = 2 · 2 · 2 · 45, a 45 jest nieparzyste — w iloczynie są tylko trzy dwójki. Każda liczba parzysta „zużywa” co najmniej jedną dwójkę, więc parzystych może być najwyżej 3. Przykład: 2 · 2 · 2 · 9 · 5 = 360.</details><br>
27. Na lekcji plastyki nauczycielka podzieliła dziewczynki na grupy trzyosobowe, a chłopców na grupy czteroosobowe. Ilu uczniów brało udział w tej lekcji, jeśli wiemy, że było ich mniej niż 30, i że dziewczynek było o 3 więcej niż chłopców? *(4 pkt)* *(Alfik 2016, zad. 17)*
   - A) 21
   - B) 24
   - C) 25
   - D) 27
   - E) 28
   <details><summary>rozwiązanie</summary>D — 27<br>Liczba chłopców dzieli się przez 4, a dziewczynek (o 3 więcej) przez 3. Sprawdzamy: 4 i 7 — nie, 8 i 11 — nie, 12 i 15 — tak! Razem 27 uczniów (mniej niż 30). Następna para, 24 i 27, daje już za dużo.</details><br>
28. Ile jest takich parzystych liczb dwucyfrowych, które są podzielne przez 9? *(4 pkt)* *(Alfik 2015, zad. 12)*
   - A) 4
   - B) 5
   - C) 6
   - D) 8
   - E) 9
   <details><summary>rozwiązanie</summary>B — 5<br>Dwucyfrowe wielokrotności 9 to 18, 27, 36, 45, 54, 63, 72, 81, 90, 99. Parzyste z nich: 18, 36, 54, 72, 90 — jest ich 5.</details><br>
29. Pani Ania ma 48 jabłek, 60 gruszek i 84 śliwki. Chce zapakować wszystkie owoce do jak największej liczby jednakowych paczek: w każdej paczce ma być tyle samo jabłek, tyle samo gruszek i tyle samo śliwek, i nic nie może zostać. Ile owoców będzie w jednej paczce? *(5 pkt)*
   - A) 4
   - B) 7
   - C) 12
   - D) 14
   - E) 16
   <details><summary>rozwiązanie</summary>E — 16<br>Liczba paczek musi dzielić bez reszty i 48, i 60, i 84. Największa taka liczba to 12, bo 48 = 12 · 4, 60 = 12 · 5, 84 = 12 · 7. W każdej z 12 paczek są więc 4 jabłka, 5 gruszek i 7 śliwek, razem 4 + 5 + 7 = 16 owoców. Pułapka: 12 to liczba paczek, a nie liczba owoców w paczce.</details><br>
30. Wczoraj, na lekcji matematyki, wszyscy uczniowie byli obecni, zaś dzisiaj nieobecnych było trzech uczniów. Wczoraj nauczyciel podzielił wszystkich obecnych uczniów na 4-osobowe grupy, a dzisiaj – na grupy 7-osobowe. Ilu uczniów liczy ta klasa? *(5 pkt)* *(Alfik 2025, zad. 21)*
   - A) 20
   - B) 21
   - C) 24
   - D) 28
   - E) 31
   <details><summary>rozwiązanie</summary>C — 24<br>Liczba uczniów dzieli się przez 4, a po odjęciu 3 — przez 7. Sprawdzamy odpowiedzi podzielne przez 4: 20 − 3 = 17, 24 − 3 = 21, 28 − 3 = 25. Tylko 21 dzieli się przez 7, więc klasa liczy 24 uczniów.</details><br>
31. Największy wspólny dzielnik pewnych dwóch liczb wynosi 3, a ich najmniejsza wspólna wielokrotność to 30. Ile wynosi suma tych dwóch liczb, jeśli wiemy, że żadna z nich nie jest równa 3? *(5 pkt)* *(Alfik 2024, zad. 22)*
   - A) 15
   - B) 18
   - C) 20
   - D) 21
   - E) 24
   <details><summary>rozwiązanie</summary>D — 21<br>Obie liczby są wielokrotnościami 3 i dzielnikami 30: to 3, 6, 15 lub 30. Pary z NWD 3 i NWW 30 to 3 i 30 albo 6 i 15. Liczba 3 jest wykluczona, więc to 6 i 15, a ich suma to 21.</details><br>
32. Jeśli pomnożymy wszystkie jednocyfrowe liczby pierwsze, to otrzymamy liczbę: *(5 pkt)* *(Alfik 2024, zad. 30)*
   - A) jednocyfrową
   - B) dwucyfrową
   - C) trzycyfrową
   - D) czterocyfrową
   - E) pięciocyfrową
   <details><summary>rozwiązanie</summary>C — trzycyfrową<br>Jednocyfrowe liczby pierwsze to 2, 3, 5 i 7 (1 nie jest liczbą pierwszą, 9 = 3 · 3). 2 · 3 · 5 · 7 = 210 — liczba trzycyfrowa.</details><br>
33. Schronisko oferuje noclegi w pokojach 5-osobowych i 8-osobowych. Łącznie w schronisku jest 47 miejsc noclegowych. Ile pokoi jest w tym schronisku? *(5 pkt)* *(Alfik 2017, zad. 21)*
   - A) 5
   - B) 6
   - C) 7
   - D) 8
   - E) 9
   <details><summary>rozwiązanie</summary>C — 7<br>Miejsca w pokojach 5-osobowych dają liczbę kończącą się na 0 lub 5, więc miejsca w pokojach 8-osobowych muszą kończyć się na 7 lub 2. Z wielokrotności 8 (8, 16, 24, 32, 40) pasuje tylko 32 — to 4 pokoje. Zostaje 15 miejsc, czyli 3 pokoje 5-osobowe. Razem 7 pokoi.</details><br>
34. Agata ma same pięciozłotówki, Beata – same dwuzłotówki, a Dorota – same monety jednozłotowe. Każda z dziewczynek ma taką samą kwotę pieniędzy. Ile monet mają łącznie te dziewczynki, jeśli wiemy, że mają ich mniej niż 20? *(5 pkt)* *(Alfik 2017, zad. 25)*
   - A) 15
   - B) 16
   - C) 17
   - D) 18
   - E) 19
   <details><summary>rozwiązanie</summary>C — 17<br>Kwota musi dać się zapłacić pięciozłotówkami i dwuzłotówkami, więc dzieli się przez 5 i przez 2, czyli przez 10. Dla 10 zł: 2 + 5 + 10 = 17 monet. Dla 20 zł byłoby już 34 monety — za dużo.</details><br>

## C. Dzielenie z resztą

Reszta z dzielenia przez 7 może wynosić tylko 0, 1, 2, 3, 4, 5 albo 6 — zawsze mniej niż dzielnik.

35. Pewna liczba podzielona przez 7 daje resztę 4. Jaką resztę z dzielenia przez 7 da liczba dwa razy większa? *(3 pkt)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 6
   <details><summary>rozwiązanie</summary>A — 1<br>Przykład: 11 : 7 = 1 reszty 4. Liczba dwa razy większa to 22, a 22 : 7 = 3 reszty 1. Tak jest zawsze: podwojona reszta to 4 + 4 = 8, a z 8 da się zrobić jeszcze jedną pełną siódemkę i zostaje 1. Pułapka: 8 nie może być resztą z dzielenia przez 7.</details><br>
36. Klasa Jacka liczy kilkunastu uczniów. Wczoraj, gdy dwóch uczniów było nieobecnych, nauczycielka podzieliła wszystkie obecne dzieci na 6-osobowe grupy. Ilu uczniów liczy klasa Jacka? *(3 pkt)* *(Alfik 2021, zad. 9)*
   - A) 14
   - B) 15
   - C) 16
   - D) 17
   - E) 18
   <details><summary>rozwiązanie</summary>A — 14<br>Klasa ma od 11 do 19 uczniów, więc obecnych było od 9 do 17. Wśród tych liczb jedyna wielokrotność 6 to 12. Zatem w klasie jest 12 + 2 = 14 uczniów.</details><br>
37. Ola ma więcej niż 30, ale mniej niż 60 cukierków. Gdy rozdziela je po 6, zostaje jej 5 cukierków, a gdy rozdziela je po 8 — zostaje jej 7. Ile cukierków ma Ola? *(4 pkt)*
   - A) 35
   - B) 41
   - C) 45
   - D) 47
   - E) 53
   <details><summary>rozwiązanie</summary>D — 47<br>W obu przypadkach brakuje 1 cukierka do pełnej grupy. Gdyby Ola miała o 1 cukierek więcej, podzieliłaby je równo i po 6, i po 8. Liczby podzielne przez 6 i przez 8 to 24, 48, 72, … Między 31 a 60 jest tylko 48, więc Ola ma 47 cukierków. Sprawdzenie: 47 = 7 · 6 + 5 i 47 = 5 · 8 + 7.</details><br>
38. Gdyby uczniów pewnej klasy podzielić na 5-osobowe zespoły, to w jednym zespole zabraknie jednej osoby. Gdyby natomiast uczniów tych podzielić na 4-osobowe zespoły, to jedna osoba zostałaby bez przydziału. Ilu uczniów liczy ta klasa? *(4 pkt)* *(Alfik 2024, zad. 14)*
   - A) 25
   - B) 26
   - C) 27
   - D) 28
   - E) 29
   <details><summary>rozwiązanie</summary>E — 29<br>„Zabraknie jednej osoby” oznacza, że po dodaniu 1 ucznia liczba dzieliłaby się przez 5 — z odpowiedzi pasuje tylko 29 (29 + 1 = 30). Sprawdzamy drugi warunek: 29 = 7 · 4 + 1, czyli jedna osoba zostaje bez zespołu.</details><br>
39. Pewna klasa liczy dwudziestu kilku uczniów. Gdyby tych uczniów podzielić na grupy 9-osobowe, to dla dwóch uczniów zostałoby bez przydziału. Gdyby natomiast uczniów podzielić na grupy 7-osobowe, to jeden uczeń zostałby bez przydziału. Ilu uczniów zostanie bez przydziału, jeśli podzielimy uczniów na grupy 5-osobowe? *(4 pkt)* *(Alfik 2022, zad. 18)*
   - A) 0
   - B) 1
   - C) 2
   - D) 3
   - E) 4
   <details><summary>rozwiązanie</summary>E — 4<br>Między 20 a 29 reszta 2 z dzielenia przez 9 jest dla 20 i 29. Reszta 1 z dzielenia przez 7: 22 i 29. Wspólna liczba to 29. Grupy 5-osobowe: 29 = 5 · 5 + 4, zostaje 4 uczniów.</details><br>
40. Dzieci z obozu jadą na wycieczkę. Gdy ustawiają się czwórkami, w ostatnim rzędzie stoi tylko 3 dzieci. Gdy ustawiają się piątkami — w ostatnim rzędzie jest 4 dzieci, a gdy szóstkami — 5 dzieci. Ile najmniej dzieci może być na tej wycieczce? *(5 pkt)*
   - A) 19
   - B) 29
   - C) 39
   - D) 49
   - E) 59
   <details><summary>rozwiązanie</summary>E — 59<br>Za każdym razem w ostatnim rzędzie brakuje 1 dziecka do pełnego rzędu. Gdyby przyszło jeszcze 1 dziecko, dałoby się je ustawić i czwórkami, i piątkami, i szóstkami. Najmniejsza liczba podzielna przez 4, przez 5 i przez 6 to 60. Więc dzieci jest 59. Pułapka: 29 pasuje do piątek i szóstek, ale czwórkami zostaje 1 dziecko, a nie 3. Liczba 4 · 5 · 6 = 120 daje 119 — to też pasuje, ale nie jest najmniejsze.</details><br>
41. W pudełku jest 20 kamyków. Możemy do tego pudełka dokładać kamyki (za każdym razem dokładając 9 kamyków) lub zabierać kamyki (za każdym razem zabierając 12 kamyków). Ile najmniej kamyków może zostać w pudełku po wykonaniu dowolnej liczby takich ruchów? *(5 pkt)* *(Alfik 2023, zad. 25)*
   - A) 0
   - B) 1
   - C) 2
   - D) 3
   - E) 4
   <details><summary>rozwiązanie</summary>C — 2<br>9 i 12 dzielą się przez 3, więc reszta z dzielenia liczby kamyków przez 3 się nie zmienia: 20 daje resztę 2. Nie da się więc zejść do 0 ani 1. Dwa kamyki osiągniemy: 20 − 12 = 8, 8 + 9 = 17, 17 − 12 = 5, 5 + 9 = 14, 14 − 12 = 2.</details><br>
42. Gdyby uczniów pewnej klasy podzielić na 5-osobowe grupy, to jedna osoba zostałaby bez przydziału. Gdyby natomiast uczniów tej klasy podzielić na 7-osobowe grupy, to dwie osoby zostałyby bez przydziału. Ilu uczniów liczy ta klasa? *(5 pkt)* *(Alfik 2019, zad. 24)*
   - A) 26
   - B) 23
   - C) 22
   - D) 21
   - E) mniej niż 20
   <details><summary>rozwiązanie</summary>E — mniej niż 20<br>Sprawdzamy opcje: 26 : 7 daje resztę 5, 23 : 5 resztę 3, 22 : 5 resztę 2, 21 : 5 resztę 1, ale 21 : 7 resztę 0. Żadna nie pasuje. Pasuje 16: 16 = 3 · 5 + 1 i 16 = 2 · 7 + 2 — a następna pasująca liczba to dopiero 51.</details><br>
43. Pewna liczba naturalna mniejsza od 20 daje resztę 2 przy dzieleniu przez 3 i daje resztę 3 przy dzieleniu przez 4. Co to za liczba? *(5 pkt)* *(Alfik 2017, zad. 23)*
   - A) 10
   - B) 11
   - C) 12
   - D) 13
   - E) 14
   <details><summary>rozwiązanie</summary>B — 11<br>Reszta 3 przy dzieleniu przez 4: 3, 7, 11, 15, 19. Z nich resztę 2 przy dzieleniu przez 3 daje tylko 11 (11 = 3 · 3 + 2).</details><br>
44. Gdyby dzieci z klasy Jacka podzielić na 5-osobowe grupy, to jedno dziecko zostałoby bez przydziału. Gdyby zaś te same dzieci podzielić na 6-osobowe grupy, to dwójka dzieci zostałaby bez przydziału. Ile dzieci liczy klasa Jacka? *(5 pkt)* *(Alfik 2017, zad. 27)*
   - A) mniej niż 10
   - B) 11
   - C) 16
   - D) 21
   - E) więcej niż 25
   <details><summary>rozwiązanie</summary>E — więcej niż 25<br>Reszta 1 przy dzieleniu przez 5: 6, 11, 16, 21, 26, … Reszta 2 przy dzieleniu przez 6: 8, 14, 20, 26, … Najmniejsza wspólna liczba to 26, więc klasa liczy więcej niż 25 dzieci. Pułapka: 11, 16, 21 spełniają tylko pierwszy warunek.</details><br>

## D. Ostatnia cyfra i zera na końcu

Ostatnia cyfra wyniku mnożenia zależy tylko od ostatnich cyfr mnożonych liczb — resztę można pominąć.

45. Jaka jest ostatnia cyfra wyniku mnożenia 11 · 12 · 13 · 14? *(3 pkt)*
   - A) 0
   - B) 2
   - C) 4
   - D) 6
   - E) 8
   <details><summary>rozwiązanie</summary>C — 4<br>Wystarczy pomnożyć ostatnie cyfry: 1 · 2 · 3 · 4 = 24, więc ostatnia cyfra to 4. Rzeczywiście 11 · 12 · 13 · 14 = 24 024.</details><br>
46. Jaka jest ostatnia cyfra liczby 7²⁰²⁷ (czyli wyniku mnożenia 2027 siódemek)? *(4 pkt)*
   - A) 1
   - B) 3
   - C) 7
   - D) 9
   - E) nie da się tego ustalić
   <details><summary>rozwiązanie</summary>B — 3<br>Ostatnie cyfry kolejnych potęg siódemki: 7, 49, 343, 2401, … czyli 7, 9, 3, 1, i potem znów 7, 9, 3, 1 — powtarzają się co 4. 2027 = 4 · 506 + 3, więc po 506 pełnych „czwórkach” jesteśmy na 3. miejscu w cyklu 7, 9, 3, 1 — to cyfra 3.</details><br>
47. Iloma zerami kończy się wynik mnożenia wszystkich liczb od 1 do 30, czyli 1 · 2 · 3 · … · 30? *(5 pkt)*
   - A) 3
   - B) 5
   - C) 6
   - D) 7
   - E) 8
   <details><summary>rozwiązanie</summary>D — 7<br>Każde zero na końcu to jedno mnożenie przez 10 = 2 · 5. Dwójek (liczb parzystych) jest bardzo dużo, więc wystarczy policzyć piątki. Liczby 5, 10, 15, 20, 25, 30 dają po jednej piątce, a 25 = 5 · 5 daje jeszcze jedną dodatkową. Razem 6 + 1 = 7 zer. Pułapka: 3 — gdy liczymy tylko 10, 20, 30; 6 — gdy zapomnimy, że w 25 są dwie piątki.</details><br>

---

## Klucz odpowiedzi

1. C — 7
2. E — 5
3. D — 4 *(Alfik 2025, zad. 8)*
4. B — 3 *(Alfik 2024, zad. 8)*
5. B — 1 *(Alfik 2024, zad. 9)*
6. D — 6 *(Alfik 2023, zad. 8)*
7. E — 39 *(Alfik 2019, zad. 7)*
8. D — 12 *(Alfik 2017, zad. 2)*
9. D — 12 *(Alfik 2016, zad. 4)*
10. C — 45 *(Alfik 2016, zad. 10)*
11. D — 14
12. C — 10 *(Alfik 2021, zad. 14)*
13. B — 7
14. B — 2 *(Alfik 2019, zad. 25)*
15. B — 2 *(Alfik 2018, zad. 28)*
16. A — 16
17. B — 2 *(Alfik 2025, zad. 3)*
18. E — 5 lub więcej *(Alfik 2024, zad. 3)*
19. A — 10 *(Alfik 2023, zad. 2)*
20. D — 9 *(Alfik 2022, zad. 10)*
21. B — 33
22. C — 7:36
23. B — 2 *(Alfik 2025, zad. 14)*
24. E — więcej niż 4 *(Alfik 2023, zad. 14)*
25. C — 3 *(Alfik 2023, zad. 19)*
26. C — 3 *(Alfik 2021, zad. 16)*
27. D — 27 *(Alfik 2016, zad. 17)*
28. B — 5 *(Alfik 2015, zad. 12)*
29. E — 16
30. C — 24 *(Alfik 2025, zad. 21)*
31. D — 21 *(Alfik 2024, zad. 22)*
32. C — trzycyfrową *(Alfik 2024, zad. 30)*
33. C — 7 *(Alfik 2017, zad. 21)*
34. C — 17 *(Alfik 2017, zad. 25)*
35. A — 1
36. A — 14 *(Alfik 2021, zad. 9)*
37. D — 47
38. E — 29 *(Alfik 2024, zad. 14)*
39. E — 4 *(Alfik 2022, zad. 18)*
40. E — 59
41. C — 2 *(Alfik 2023, zad. 25)*
42. E — mniej niż 20 *(Alfik 2019, zad. 24)*
43. B — 11 *(Alfik 2017, zad. 23)*
44. E — więcej niż 25 *(Alfik 2017, zad. 27)*
45. C — 4
46. B — 3
47. D — 7

## Ściąga

| Dzieli się przez… | gdy… |
|---|---|
| 2 | ostatnia cyfra parzysta (0, 2, 4, 6, 8) |
| 3 | suma cyfr dzieli się przez 3 |
| 4 | liczba z dwóch ostatnich cyfr dzieli się przez 4 |
| 5 | ostatnia cyfra 0 lub 5 |
| 6 | dzieli się przez 2 i przez 3 |
| 9 | suma cyfr dzieli się przez 9 |
| 10 | ostatnia cyfra 0 |
| 12 | dzieli się przez 3 i przez 4 |

- **Ile wielokrotności liczby k od 1 do N?** Wynik dzielenia N : k bez reszty (100 : 6 → 16).
- **„Przez a lub przez b”:** (ile przez a) + (ile przez b) − (ile przez obie naraz).
- **Najmniejsza wspólna wielokrotność** — „kiedy znów razem?” (12 i 18 → 36). **Największy wspólny dzielnik** — „jak najwięcej jednakowych paczek” (48, 60, 84 → 12).
- **Sztuczka z resztą:** reszta zawsze o 1 mniejsza od dzielnika → liczba + 1 dzieli się przez wszystkie dzielniki.
- **Ostatnie cyfry potęg (cykl co 4):** 2 → 2, 4, 8, 6; 3 → 3, 9, 7, 1; 7 → 7, 9, 3, 1; 8 → 8, 4, 2, 6. Potęgi liczb kończących się na 0, 1, 5, 6 zawsze kończą się tą samą cyfrą.
- **Zera na końcu iloczynu 1 · 2 · … · N:** policz piątki (25 daje dwie piątki).
