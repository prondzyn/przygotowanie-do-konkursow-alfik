# 08. Kratki, szachownice i cięcie

**Dlaczego warto:** W prawie każdym arkuszu Alfika pojawia się szachownica, kratka do policzenia, cięcie figury albo kostka do gry. Te zadania wymagają mało rachunków, za to porządnego liczenia „po kolei” i jednego sprytnego spostrzeżenia (np. kolorowania).

- **W pliku:** 53 zadań: 14 nowych i 39 z prawdziwych arkuszy Alfika (20 za 3 pkt, 22 za 4 pkt, 11 za 5 pkt).

**Wskazówki**
- Na szachownicy sąsiednie pola mają różne kolory. Jeśli liczba pól jest nieparzysta, pól w kolorze narożnika jest o 1 więcej.
- Kwadraty na kratce licz według wielkości: najpierw 1×1, potem 2×2, 3×3… Na kratce n×n kwadratów k×k jest (n − k + 1) · (n − k + 1).
- Kostka domino zawsze zakrywa jedno pole białe i jedno czarne — to pozwala szybko wykazać, że coś jest niemożliwe.
- Cięcia równoległe: 3 cięcia wzdłuż dają 4 paski, a 4 cięcia w poprzek dzielą każdy pasek na 5 części.
- Na kostce do gry przeciwległe ściany sumują się do 7: 1 i 6, 2 i 5, 3 i 4. Suma wszystkich oczek to 21.
- Na siatce sześcianu w kształcie krzyża co druga ściana w „długim” pasku jest przeciwległa.

**Spis treści**

- [A. Szachownice i kolorowanie](#a-szachownice-i-kolorowanie)
- [B. Ile kwadratów na kratce](#b-ile-kwadratów-na-kratce)
- [C. Cięcie i układanie](#c-cięcie-i-układanie)
- [D. Kostka do gry i siatki sześcianu](#d-kostka-do-gry-i-siatki-sześcianu)
- [Klucz odpowiedzi](#klucz-odpowiedzi)
- [Ściąga](#ściąga)

---

## A. Szachownice i kolorowanie

Pola szachownicy, przemalowywanie wierszy i kolumn, malowanie tak, żeby spełnić warunek.

1. Szachownica ma wymiary 11 × 11, a jej narożne pola są czarne. O ile więcej jest na niej pól czarnych niż białych? *(3 pkt)*
   - A) 0
   - B) 1
   - C) 2
   - D) 11
   - E) 22
   <details><summary>rozwiązanie</summary>B — 1<br>Szachownica ma 11 · 11 = 121 pól. Kolory się przeplatają, więc pól jest prawie po równo, a „nadmiarowe” pole ma kolor narożnika. Czarnych jest 61, białych 60 — różnica 1. Pułapka: 11 — myślenie, że w każdym wierszu czarnych jest o jedno więcej (a w co drugim wierszu jest odwrotnie).</details><br>
2. Pole w prawym górnym rogu kwadratowej szachownicy złożonej z 25 pól jest czarne. Ile jest takich czarnych pól na tej szachownicy, które sąsiadują z czterema białymi polami? *(3 pkt)* *(Alfik 2023, zad. 3)*
   - A) 4
   - B) 5
   - C) 6
   - D) 8
   - E) 9
   <details><summary>rozwiązanie</summary>B — 5<br>Szachownica ma 5×5 pól, a wszystkie 4 rogi są czarne. Cztery sąsiadów (z każdej strony) mają tylko pola wewnętrzne — środkowy kwadrat 3×3. Jego rogi i środek są czarne: to 5 pól, a każde czarne pole ma dookoła tylko białe.</details><br>
3. Narożne pola szachownicy rozmiaru 9×9 są białe. Jeśli szachownicę tę rozetniemy na kwadratowe szachownice rozmiaru 3×3, to ile z otrzymanych szachownic będzie miało narożne pola białe? *(3 pkt)* *(Alfik 2022, zad. 9)*
   - A) 4
   - B) 5
   - C) 6
   - D) 8
   - E) 9
   <details><summary>rozwiązanie</summary>B — 5<br>Powstaje 9 małych szachownic ułożonych też jak 3×3. Sąsiednie małe szachownice mają narożniki w przeciwnych kolorach (przesunięcie o 3 pola, czyli o liczbę nieparzystą). Więc małe szachownice też ułożą się „w szachownicę”: białe narożniki mają te w rogach i w środku — 5 sztuk.</details><br>
4. Na każdym białym polu biało-czarnej szachownicy o wymiarach 4×4 ustawiono 1 czarny pionek, a na każdym czarnym polu ustawiono 2 białe pionki. Ile łącznie pionków obu kolorów ustawiono na całej szachownicy? *(3 pkt)* *(Alfik 2019, zad. 10)*
   - A) 16
   - B) 18
   - C) 20
   - D) 24
   - E) 32
   <details><summary>rozwiązanie</summary>D — 24<br>Szachownica 4×4 ma 16 pól: 8 białych i 8 czarnych. Na białych stoi 8 · 1 = 8 pionków, na czarnych 8 · 2 = 16. Razem 24.</details><br>
5. Ile białych pól jest na szachownicy o wymiarach 7×7, której pole w lewym górnym rogu jest czarne? *(3 pkt)* *(Alfik 2017, zad. 5)*
   - A) 21
   - B) 22
   - C) 23
   - D) 24
   - E) 25
   <details><summary>rozwiązanie</summary>D — 24<br>Pól jest 49 — liczba nieparzysta, więc jednego koloru jest o 1 więcej. Wszystkie rogi mają kolor lewego górnego, czyli czarny, i to czarnych jest więcej: 25 czarnych i 24 białe.</details><br>
6. Ile białych pól ma szachownica o wymiarach 8×8? *(3 pkt)* *(Alfik 2015, zad. 4)*
   - A) 24
   - B) 30
   - C) 32
   - D) 36
   - E) 48
   <details><summary>rozwiązanie</summary>C — 32<br>Szachownica ma 8 · 8 = 64 pola, a białych i czarnych jest po równo: 64 : 2 = 32.</details><br>
7. Wszystkie pola tablicy 5 × 5 są białe. Jeden ruch to zmiana koloru wszystkich pól w jednym wierszu albo w jednej kolumnie (białe stają się czarne, czarne — białe). Kuba przemalował kolejno pierwszy wiersz, drugi wiersz i pierwszą kolumnę. Ile czarnych pól jest teraz na tablicy? *(4 pkt)*
   - A) 9
   - B) 10
   - C) 11
   - D) 13
   - E) 15
   <details><summary>rozwiązanie</summary>C — 11<br>Po przemalowaniu dwóch wierszy czarnych jest 5 + 5 = 10 pól. Pierwsza kolumna ma 5 pól: 2 z nich (w dwóch pierwszych wierszach) były czarne i stają się białe, a 3 były białe i stają się czarne. 10 − 2 + 3 = 11. Pułapka: 15 = 10 + 5 — zapomniane, że czarne pola zmieniają się z powrotem na białe.</details><br>
8. Chcemy pokolorować wszystkie wierzchołki pięciokąta, malując każdy wierzchołek jednym z dostępnych kolorów. Ile co najmniej kolorów musimy użyć, żeby każdy bok miał końce różnego koloru? *(4 pkt)* *(Alfik 2023, zad. 13)*
   - A) 2
   - B) 3
   - C) 4
   - D) 5
   - E) 6
   <details><summary>rozwiązanie</summary>B — 3<br>Dwoma kolorami musielibyśmy malować na przemian: biały, czarny, biały, czarny, biały — ale piąty wierzchołek sąsiaduje z pierwszym, a oba byłyby białe. Pięć to liczba nieparzysta, więc 2 kolory nie wystarczą. Trzy wystarczą: B, C, B, C, Z.</details><br>
9. Na biało-czarnej szachownicy o rozmiarach 4×4 niektóre z czarnych pól chcemy przemalować na czerwono tak, by każde białe pole szachownicy sąsiadowało z przynajmniej jednym polem czerwonym. Ile co najmniej pól musimy przemalować? *(4 pkt)* *(Alfik 2021, zad. 17)*
   - A) 2
   - B) 3
   - C) 4
   - D) 5
   - E) 6
   <details><summary>rozwiązanie</summary>B — 3<br>Białych pól jest 8, a czarne pole sąsiaduje (bokiem) najwyżej z 4 białymi. Biały narożnik sąsiaduje tylko z czarnymi polami brzegowymi, a te mają najwyżej 3 białych sąsiadów — więc 2 czerwone pola obejmą najwyżej 3 + 4 = 7 białych, za mało. 3 wystarczą: np. gdy lewy górny róg jest biały, czerwone pola to (rząd 1, kolumna 2), (rząd 3, kolumna 2) i (rząd 3, kolumna 4) — sprawdziliśmy też programem.</details><br>
10. Niektóre pola biało-czarnej szachownicy o wymiarach 8×8 pomalowano na czerwono tak, aby w każdym rzędzie tej szachownicy i w każdej kolumnie tej szachownicy było dokładnie jedno czerwone pole. Ile pól pomalowano na czerwono? *(4 pkt)* *(Alfik 2019, zad. 13)*
   - A) 6
   - B) 8
   - C) 10
   - D) 12
   - E) 16
   <details><summary>rozwiązanie</summary>B — 8<br>Rzędów jest 8 i w każdym jest dokładnie jedno czerwone pole, więc czerwonych pól jest 8 (i wtedy w każdej kolumnie też jest po jednym, np. na przekątnej).</details><br>
11. Jakie wymiary może mieć biało-czarna prostokątna szachownica złożona z 36 pól, której wszystkie 4 narożne pola są białe? *(4 pkt)* *(Alfik 2019, zad. 15)*
   - A) 6×6
   - B) 4×9
   - C) 3×12
   - D) 2×18
   - E) taka szachownica nie istnieje
   <details><summary>rozwiązanie</summary>E — taka szachownica nie istnieje<br>Idąc wzdłuż rzędu kolory się zmieniają. Żeby oba końce rzędu były tego samego koloru, rząd musi mieć nieparzystą liczbę pól; tak samo kolumna. Wtedy liczba wszystkich pól = nieparzysta · nieparzysta = nieparzysta. A 36 jest parzyste, więc takiej szachownicy nie ma.</details><br>
12. W każde pole szachownicy o wymiarach 8×8 wpisujemy iloczyn numeru kolumny i numeru rzędu, w których znajduje się to pole (zarówno kolumny jak i rzędy numerujemy kolejnymi liczbami od 1 do 8). Jaka jest największa możliwa różnica dwóch liczb wpisanych w sąsiadujące pola (tzn. pola mające wspólny bok)? *(4 pkt)* *(Alfik 2018, zad. 16)*
   - A) 5
   - B) 6
   - C) 7
   - D) 8
   - E) 9 lub więcej
   <details><summary>rozwiązanie</summary>D — 8<br>Sąsiednie pola różnią się numerem kolumny (albo rzędu) o 1, przy tym samym drugim numerze. Różnica liczb jest więc równa temu drugiemu numerowi, czyli najwyżej 8 — np. 8 · 8 = 64 i 8 · 7 = 56.</details><br>
13. Na szachownicy o wymiarach 6×6 ustawiono 18 pionków białych i 18 pionków czarnych, ustawiając po jednym pionku na każdym polu. Jeśli na białych polach ustawiono 7 białych pionków, to ile czarnych pionków ustawiono na czarnych polach? *(4 pkt)* *(Alfik 2018, zad. 17)*
   - A) 7
   - B) 8
   - C) 9
   - D) 11
   - E) zależy od ustawienia pionków
   <details><summary>rozwiązanie</summary>A — 7<br>Białych pionków jest 18; 7 stoi na białych polach, więc 11 na czarnych. Czarnych pól jest 18, zajętych przez 11 białych pionków — na pozostałych 7 czarnych polach stoją czarne pionki.</details><br>
14. Na szachownicy o wymiarach 8×8 ustawiamy pionki – każdy na innym polu. Ile najwięcej pionków możemy ustawić, jeśli chcemy, by w każdej kolumnie był najwyżej jeden pionek i w każdym wierszu były najwyżej dwa pionki? *(4 pkt)* *(Alfik 2017, zad. 17)*
   - A) 8
   - B) 9
   - C) 12
   - D) 15
   - E) 16
   <details><summary>rozwiązanie</summary>A — 8<br>Kolumn jest 8, a w każdej może stać najwyżej jeden pionek — więc więcej niż 8 się nie da. 8 łatwo ustawić, np. wszystkie na przekątnej. Warunek o wierszach nic tu nie zmienia. Pułapka: 16 wychodzi, gdy patrzy się tylko na wiersze.</details><br>
15. Ruch polega na przemalowaniu każdego pola (białego na czarne, a czarnego na białe) w wybranym wierszu albo w wybranej kolumnie szachownicy. Ile co najmniej ruchów potrzeba, by przemalować całą szachownicę rozmiaru 8×8 na czarno? *(4 pkt)* *(Alfik 2016, zad. 11)*
   - A) 4
   - B) 8
   - C) 12
   - D) 16
   - E) inna liczba
   <details><summary>rozwiązanie</summary>B — 8<br>Przemalowujemy co drugi wiersz (4 ruchy) — wtedy każda kolumna jest jednokolorowa, na przemian biała i czarna. Teraz przemalowujemy 4 białe kolumny — razem 8 ruchów. Mniej się nie da: w każdej kolumnie są pola obu kolorów, więc samymi ruchami kolumnowymi jej nie wyrównamy — trzeba ruszyć wiersze, i to tak, by każda kolumna stała się jednokolorowa (co drugi wiersz: 4 ruchy). Wtedy 4 kolumny są białe i każdą trzeba przemalować osobno. Sprawdzenie komputerem wszystkich możliwości też daje 8.</details><br>
16. Plansza ma wymiary 5 × 5. Ile najmniej pól trzeba pomalować na czerwono, aby w każdym kwadracie 2 × 2 złożonym z czterech pól tej planszy było co najmniej jedno czerwone pole? *(5 pkt)*
   - A) 3
   - B) 4
   - C) 5
   - D) 6
   - E) 9
   <details><summary>rozwiązanie</summary>B — 4<br>Mniej niż 4 się nie da: w czterech rogach planszy leżą cztery kwadraty 2 × 2, które nie mają wspólnych pól, a każdy z nich potrzebuje własnego czerwonego pola. 4 wystarczą: pomaluj pola w 2. i 4. wierszu, które są w 2. i 4. kolumnie. Każdy kwadrat 2 × 2 zawiera jeden z wierszy 2 lub 4 i jedną z kolumn 2 lub 4, więc trafia na czerwone pole.</details><br>
17. Kwadratowa szachownica składa się z 36 pól. Ruch polega na wybraniu jednego rzędu albo jednej kolumny i przemalowaniu wszystkich pól w wybranym rzędzie (albo w wybranej kolumnie): pola białe przemalowujemy na czarno, a czarne – na biało. Ile najmniej ruchów potrzeba wykonać, aby wszystkie 36 pól było koloru czarnego? *(5 pkt)* *(Alfik 2022, zad. 25)*
   - A) 6
   - B) 7
   - C) 8
   - D) 9
   - E) 12
   <details><summary>rozwiązanie</summary>A — 6<br>Szachownica ma 6×6 pól. Przemalowujemy co drugi rząd (3 ruchy) — wtedy każda kolumna staje się jednokolorowa, na przemian biała i czarna. Teraz przemalowujemy 3 białe kolumny — razem 6 ruchów. Mniej się nie da: dwa sąsiednie pola w rzędzie mają różne kolory, więc z każdej pary kolumn 1–2, 3–4, 5–6 dokładnie jedną trzeba przemalować — to co najmniej 3 ruchy kolumnami. Tak samo co najmniej 3 ruchy rzędami. Razem co najmniej 6.</details><br>
18. Przez ile pól szachownicy o rozmiarze 3×4 będzie przechodził odcinek łączący prawy dolny róg szachownicy z lewym górnym rogiem szachownicy? *(5 pkt)* *(Alfik 2021, zad. 22)*
   - A) 3
   - B) 4
   - C) 5
   - D) 6
   - E) 7
   <details><summary>rozwiązanie</summary>D — 6<br>Idąc wzdłuż odcinka, wchodzimy do nowego pola za każdym razem, gdy przecinamy linię siatki. W poziomie przecinamy 3 linie pionowe, w pionie 2 linie poziome, i nigdy obie naraz (3 i 4 nie mają wspólnego dzielnika większego niż 1, więc odcinek nie trafia w żaden wewnętrzny wierzchołek). Pól jest 1 + 3 + 2 = 6.</details><br>
19. Ile najwięcej pól może mieć prostokątna szachownica, która ma dokładnie 20 pól brzegowych (tzn. leżących w pierwszym wierszu, w pierwszej kolumnie, w ostatnim wierszu lub w ostatniej kolumnie)? *(5 pkt)* *(Alfik 2016, zad. 24)*
   - A) 24
   - B) 25
   - C) 32
   - D) 35
   - E) 36
   <details><summary>rozwiązanie</summary>E — 36<br>Szachownica a × b (obie co najmniej 2) ma 2 · (a + b) − 4 pól brzegowych, więc a + b = 12. Możliwe: 2 × 10 (20 pól), 3 × 9 (27), 4 × 8 (32), 5 × 7 (35), 6 × 6 (36). Najwięcej ma kwadrat 6 × 6: 36 pól.</details><br>
20. Trzy kwadratowe czarno-białe szachownice (każda innej wielkości) rozcięto na pojedyncze pola otrzymując łącznie 22 czarne kwadraciki. Ile białych kwadracików otrzymano? *(5 pkt)* *(Alfik 2016, zad. 28)*
   - A) 20
   - B) 21
   - C) 22
   - D) 23
   - E) 24
   <details><summary>rozwiązanie</summary>D — 23<br>Szachownica 2 × 2 ma 2 czarne pola, 4 × 4 — 8 czarnych, a 5 × 5 może mieć 12 czarnych i 13 białych. Razem czarnych 2 + 8 + 12 = 22, białych 2 + 8 + 13 = 23. ⚠ Uwaga: jeśli uznać „szachownicę” 1 × 1 (jedno pole), pasują też inne zestawy: 1 × 1, 3 × 3, 6 × 6 (0 + 4 + 18 czarnych, 24 białe) albo 1 × 1, 4 × 4, 5 × 5 (1 + 8 + 13 czarnych, 20 białych). Odpowiedź 23 zgodna z kluczem wymaga przyjęcia, że szachownica ma co najmniej 2 × 2 pola.</details><br>

## B. Ile kwadratów na kratce

Licz porządnie: najpierw najmniejsze figury, potem coraz większe. Nie zapomnij o całej kratce!

21. Ile jest wszystkich kwadratów (różnej wielkości) na kratce 3 × 3? *(3 pkt)*
   - A) 9
   - B) 10
   - C) 13
   - D) 14
   - E) 16
   <details><summary>rozwiązanie</summary>D — 14<br>Kwadratów 1 × 1 jest 9. Kwadratów 2 × 2 jest 4 (lewy górny róg może być w 2 miejscach w poziomie i 2 w pionie). Kwadrat 3 × 3 jest 1 — cała kratka. Razem 9 + 4 + 1 = 14. Pułapka: 10 — pominięte kwadraty 2 × 2.</details><br>
22. Ile jest wszystkich kwadratów (różnej wielkości) na kratce 4 × 4? *(4 pkt)*
   - A) 16
   - B) 20
   - C) 25
   - D) 26
   - E) 30
   <details><summary>rozwiązanie</summary>E — 30<br>1 × 1: 4 · 4 = 16. 2 × 2: 3 · 3 = 9. 3 × 3: 2 · 2 = 4. 4 × 4: 1. Razem 16 + 9 + 4 + 1 = 30. Pułapka: 26 — zapomniane kwadraty 3 × 3.</details><br>
23. Ile jest wszystkich prostokątów na kratce 3 × 3? Kwadraty też liczymy jako prostokąty. *(5 pkt)*
   - A) 9
   - B) 14
   - C) 30
   - D) 36
   - E) 45
   <details><summary>rozwiązanie</summary>D — 36<br>Liczymy według kształtu. 1 × 1: 9. Paski 1 × 2: 6 poziomych i 6 pionowych, czyli 12. Paski 1 × 3: 3 poziome i 3 pionowe, czyli 6. 2 × 2: 4. Prostokąty 2 × 3: 2 poziome i 2 pionowe, czyli 4. 3 × 3: 1. Razem 9 + 12 + 6 + 4 + 4 + 1 = 36. Pułapka: 14 to tylko kwadraty.</details><br>

## C. Cięcie i układanie

Cięcia wzdłuż linii, układanie kostek domino. Gdy coś „nie chce wyjść”, pomaluj planszę w szachownicę.

24. Prostokątną kartkę o wymiarach 8 cm na 12 cm pocięto na kwadraty o boku 2 cm. Ile kwadratów otrzymano? *(3 pkt)*
   - A) 24
   - B) 40
   - C) 48
   - D) 96
   - E) 192
   <details><summary>rozwiązanie</summary>A — 24<br>Wzdłuż boku 8 cm mieszczą się 8 : 2 = 4 kwadraty, a wzdłuż boku 12 cm — 12 : 2 = 6 kwadratów. Razem 4 · 6 = 24. Pułapka: 48 = 96 : 2 — ale kwadrat 2 × 2 ma pole 4 cm², a nie 2 cm².</details><br>
25. Prostokątne ciasto pocięto prostymi cięciami od brzegu do brzegu: 3 cięcia wzdłuż i 4 cięcia w poprzek. Na ile kawałków podzielono ciasto? *(3 pkt)*
   - A) 7
   - B) 12
   - C) 19
   - D) 20
   - E) 24
   <details><summary>rozwiązanie</summary>D — 20<br>3 cięcia wzdłuż dzielą ciasto na 4 paski. Każde z 4 cięć w poprzek przecina wszystkie paski, więc każdy pasek dzieli się na 5 kawałków. Razem 4 · 5 = 20. Pułapka: 12 = 3 · 4 — liczba cięć to nie liczba kawałków (kawałków jest zawsze o 1 więcej niż cięć).</details><br>
26. Kwadrat o boku długości 4 cm rozcięto na kwadraty o boku długości 1 cm. Ile części otrzymano? *(3 pkt)* *(Alfik 2025, zad. 1)*
   - A) 4
   - B) 8
   - C) 12
   - D) 16
   - E) 64
   <details><summary>rozwiązanie</summary>D — 16<br>W każdym rzędzie mieszczą się 4 kwadraciki, a rzędów jest 4. Razem 4 · 4 = 16. Pułapka: 4 to liczba kwadracików w jednym rzędzie, a 64 to liczba sześcianików, gdyby to był sześcian.</details><br>
27. Narysowano trzy różne średnice pewnego koła. Na ile części podzieliły one to koło? *(3 pkt)* *(Alfik 2024, zad. 4)*
   - A) 3
   - B) 4
   - C) 5
   - D) 6
   - E) 7
   <details><summary>rozwiązanie</summary>D — 6<br>Wszystkie średnice przechodzą przez środek koła. Trzy średnice to 6 „promieni” wychodzących ze środka, a one dzielą koło na 6 kawałków jak tort.</details><br>
28. Dla każdej pary boków kwadratu narysowano odcinek łączący środki tych boków. Rozcinając kwadrat wzdłuż narysowanych odcinków otrzymano pewną liczbę trójkątów. Ile części otrzymano? *(3 pkt)* *(Alfik 2022, zad. 8)*
   - A) 4
   - B) 5
   - C) 6
   - D) 8
   - E) 12
   <details><summary>rozwiązanie</summary>D — 8<br>Kwadrat ma 4 boki, więc par boków jest 6. Cztery odcinki łączą środki sąsiednich boków i tworzą „romb” w środku, odcinając 4 trójkąty w rogach. Dwa odcinki łączą środki przeciwległych boków — tworzą krzyż, który tnie środkowy kwadrat na 4 trójkąty. Razem 4 + 4 = 8.</details><br>
29. Kwadrat o boku długości 12 cm rozcięto na 4 jednakowe kwadraty. Jaka jest długość boku każdego z otrzymanych kwadratów? *(3 pkt)* *(Alfik 2019, zad. 3)*
   - A) 2 cm
   - B) 3 cm
   - C) 4 cm
   - D) 6 cm
   - E) 8 cm
   <details><summary>rozwiązanie</summary>D — 6 cm<br>4 jednakowe kwadraty układają się 2 na 2, więc bok małego kwadratu to połowa boku dużego: 12 : 2 = 6 cm. Pułapka: 12 : 4 = 3 cm byłoby dobre, gdyby kwadraty leżały w jednym rzędzie — ale wtedy nie złożyłyby się w kwadrat.</details><br>
30. Kwadrat o boku długości 5 cm rozcięto na kwadrat o boku długości 4 cm i pewną liczbę kwadracików o boku długości 1 cm. Ile części otrzymano z tego rozcięcia? *(3 pkt)* *(Alfik 2017, zad. 4)*
   - A) 8
   - B) 9
   - C) 10
   - D) 11
   - E) 12
   <details><summary>rozwiązanie</summary>C — 10<br>Duży kwadrat ma pole 25 cm², kwadrat 4 cm ma pole 16 cm². Zostaje 9 cm², czyli 9 kwadracików. Razem z kwadratem 4 cm to 10 części. Pułapka: nie zapomnij policzyć dużego kawałka.</details><br>
31. Prostokąt o szerokości 6 cm rozcięto na trzy kwadraty, wśród których dwa były jednakowe, a trzeci inny. Jaką długość miał ten prostokąt? *(3 pkt)* *(Alfik 2016, zad. 6)*
   - A) 7 cm
   - B) 8 cm
   - C) 9 cm
   - D) 10 cm
   - E) 12 cm
   <details><summary>rozwiązanie</summary>C — 9 cm<br>Duży kwadrat ma bok 6 cm (cała szerokość), a obok, jeden nad drugim, leżą dwa kwadraty o boku 3 cm. Długość: 6 + 3 = 9 cm.</details><br>
32. Kwadrat o boku 24 cm rozcięto na kwadraty o boku 4 cm. Ile kwadratów otrzymano? *(3 pkt)* *(Alfik 2015, zad. 2)*
   - A) 4
   - B) 6
   - C) 12
   - D) 16
   - E) 36
   <details><summary>rozwiązanie</summary>E — 36<br>Wzdłuż jednego boku mieści się 24 : 4 = 6 małych kwadratów, więc jest 6 rzędów po 6 kwadratów: 6 · 6 = 36. Pułapka: odpowiedź 6 to tylko jeden rząd.</details><br>
33. Z planszy 5 × 5 kratek wycinamy wzdłuż linii kratki prostokąty 1 × 2 (kostki domino). Ile najwięcej takich prostokątów można wyciąć? *(4 pkt)*
   - A) 10
   - B) 11
   - C) 12
   - D) 13
   - E) 14
   <details><summary>rozwiązanie</summary>C — 12<br>Plansza ma 25 pól, a każda kostka zabiera 2 pola, więc 13 kostek (26 pól) na pewno się nie zmieści. 12 się da: w każdym z 5 wierszy wycinamy 2 poziome kostki z pierwszych 4 pól (to 10 kostek), a z ostatniej kolumny (5 pól) wycinamy jeszcze 2 pionowe kostki. 10 + 2 = 12, zostaje jedno pole.</details><br>
34. Prostokąt chcemy rozciąć na mniejsze prostokąty prowadząc 7 cięć tak, by każde cięcie było równoległe do dwóch boków tego prostokąta. Ile najwięcej części możemy otrzymać z takiego rozcięcia? *(4 pkt)* *(Alfik 2025, zad. 16)*
   - A) 8
   - B) 10
   - C) 14
   - D) 18
   - E) 20
   <details><summary>rozwiązanie</summary>E — 20<br>Jeśli zrobimy a cięć poziomych i b pionowych (a + b = 7), dostaniemy (a + 1) · (b + 1) części. Najwięcej, gdy cięcia są podzielone możliwie po równo: 3 poziome i 4 pionowe dają 4 · 5 = 20 części. Pułapka: 7 cięć w jedną stronę daje tylko 8 części.</details><br>
35. Jaka jest największa liczba części, na jaką można rozciąć koło trzema odcinkami? *(4 pkt)* *(Alfik 2022, zad. 12)*
   - A) 3
   - B) 4
   - C) 5
   - D) 6
   - E) 7
   <details><summary>rozwiązanie</summary>E — 7<br>Pierwszy odcinek dzieli koło na 2 części. Drugi, przecinając pierwszy, dokłada 2 części (razem 4). Trzeci może przeciąć oba poprzednie w dwóch różnych punktach i wtedy przechodzi przez 3 części, dzieląc każdą — dokłada 3. Razem 4 + 3 = 7.</details><br>
36. Z prostokąta o długości 19 cm i szerokości 12 cm odcięto największy możliwy kwadrat, otrzymując mniejszy prostokąt. Z otrzymanego prostokąta znów odcięto największy możliwy kwadrat, otrzymując jeszcze mniejszy prostokąt. Procedurę tę kontynuowano tak długo, aż otrzymano prostokąt będący kwadratem. Jaka była długość boku tego kwadratu? *(4 pkt)* *(Alfik 2022, zad. 14)*
   - A) 1 cm
   - B) 2 cm
   - C) 3 cm
   - D) 4 cm
   - E) 5 cm
   <details><summary>rozwiązanie</summary>A — 1 cm<br>Śledzimy wymiary: 19×12 → 12×7 → 7×5 → 5×2 → 3×2 → 2×1 → 1×1. Na końcu zostaje kwadrat o boku 1 cm.</details><br>
37. Jeśli prostokąt o wymiarach 6 cm × 8 cm rozetniemy na prostokąty o wymiarach 2 cm × 3 cm, to ile części otrzymamy? *(4 pkt)* *(Alfik 2022, zad. 19)*
   - A) 8
   - B) 9
   - C) 10
   - D) 11
   - E) 12
   <details><summary>rozwiązanie</summary>A — 8<br>Pole dużego prostokąta: 6 · 8 = 48 cm², małego: 2 · 3 = 6 cm². 48 : 6 = 8 części. Takie cięcie jest możliwe: prostokąt 6 cm × 8 cm to dwa paski 3 cm × 8 cm, a każdy pasek tniemy na 4 kawałki 3 cm × 2 cm.</details><br>
38. Na ile najwięcej części można podzielić kwadrat trzema prostymi? *(4 pkt)* *(Alfik 2017, zad. 16)*
   - A) 3
   - B) 4
   - C) 5
   - D) 6
   - E) więcej niż 6
   <details><summary>rozwiązanie</summary>E — więcej niż 6<br>Pierwsza prosta daje 2 części, druga (przecinająca pierwszą wewnątrz kwadratu) dodaje 2 — razem 4. Trzecia, jeśli przetnie obie poprzednie wewnątrz kwadratu w różnych punktach, przechodzi przez 3 części i każdą dzieli na dwie — razem 7.</details><br>
39. Z szachownicy 8 × 8 wycięto dwa przeciwległe narożne pola (lewe górne i prawe dolne). Ile kostek domino 1 × 2 potrzeba, aby dokładnie przykryć pozostałe pola (bez nakładania i bez wystawania poza planszę)? *(5 pkt)*
   - A) 30
   - B) 31
   - C) 32
   - D) 62
   - E) nie da się tak przykryć tej planszy
   <details><summary>rozwiązanie</summary>E — nie da się tak przykryć tej planszy<br>Pomaluj planszę jak szachownicę. Przeciwległe narożniki mają ten sam kolor, np. oba są czarne. Zostaje więc 30 pól czarnych i 32 białe. Każda kostka domino zakrywa jedno pole czarne i jedno białe, więc kostki zawsze zakrywają tyle samo czarnych co białych pól. 30 ≠ 32, więc się nie da. Pułapka: 31 = 62 : 2 — liczba pól się zgadza, ale kolory nie.</details><br>
40. Jeśli prostokąt o wymiarach 12 cm × 17 cm rozetniemy na prostokąty o wymiarach 3 cm × 4 cm, to ile części otrzymamy? *(5 pkt)* *(Alfik 2023, zad. 23)*
   - A) 14
   - B) 15
   - C) 16
   - D) 17
   - E) nie da się przeprowadzić takiego rozcięcia
   <details><summary>rozwiązanie</summary>D — 17<br>Pole: 12 · 17 = 204 cm², jedna część 3 · 4 = 12 cm², 204 : 12 = 17. Cięcie jest możliwe: bok 17 cm dzielimy na 8 + 9. Pasek 12 × 8 tniemy na 4 · 2 = 8 prostokątów (3 cm wzdłuż boku 12, 4 cm wzdłuż boku 8), a pasek 12 × 9 na 3 · 3 = 9 prostokątów (4 cm wzdłuż boku 12, 3 cm wzdłuż boku 9). Razem 8 + 9 = 17.</details><br>

## D. Kostka do gry i siatki sześcianu

Na zwykłej kostce do gry liczby na przeciwległych ścianach sumują się do 7.

41. Zwykła kostka do gry leży na stole. Widać trzy jej ściany: na górnej jest 5, na przedniej 3, a na prawej 1. Jaka jest suma liczb na trzech ścianach, których nie widać? *(3 pkt)*
   - A) 9
   - B) 12
   - C) 13
   - D) 15
   - E) 21
   <details><summary>rozwiązanie</summary>B — 12<br>Wszystkie ściany kostki mają razem 1 + 2 + 3 + 4 + 5 + 6 = 21 oczek. Widać 5 + 3 + 1 = 9, więc niewidocznych jest 21 − 9 = 12. Można też tak: naprzeciw 5 jest 2, naprzeciw 3 jest 4, naprzeciw 1 jest 6, a 2 + 4 + 6 = 12.</details><br>
42. Jeśli od liczby krawędzi sześcianu odejmiemy liczbę jego wierzchołków, to otrzymamy wynik: *(3 pkt)* *(Alfik 2024, zad. 10)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5
   <details><summary>rozwiązanie</summary>D — 4<br>Sześcian ma 12 krawędzi (4 na górze, 4 na dole i 4 pionowe) oraz 8 wierzchołków. 12 − 8 = 4.</details><br>
43. Jedną krawędź sześcianu pomalowano na niebiesko. Pozostałe trzy krawędzie każdej ściany z niebieską krawędzią pomalowano na czerwono. Wszystkie pozostałe krawędzie sześcianu pomalowano na zielono. Ile zielonych krawędzi ma ten sześcian? *(3 pkt)* *(Alfik 2023, zad. 7)*
   - A) 4
   - B) 5
   - C) 6
   - D) 7
   - E) 8
   <details><summary>rozwiązanie</summary>B — 5<br>Sześcian ma 12 krawędzi. Każda krawędź należy do 2 ścian, więc niebieska krawędź leży na 2 ścianach. Na każdej z nich 3 pozostałe krawędzie są czerwone — razem 6 czerwonych. Zielonych: 12 − 1 − 6 = 5.</details><br>
44. Ania w pięciu rzutach sześcienną kostką do gry (której ściany opisane są liczbami od 1 do 6) uzyskała łączny wynik 14. Ile najwięcej szóstek mogła wyrzucić? *(3 pkt)* *(Alfik 2018, zad. 2)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5
   <details><summary>rozwiązanie</summary>A — 1<br>Dwie szóstki to 12, a pozostałe trzy rzuty dają co najmniej 1 + 1 + 1 = 3 — razem co najmniej 15, za dużo. Jedna szóstka wystarczy, np. 6 + 2 + 2 + 2 + 2 = 14.</details><br>
45. Trzy zwykłe kostki do gry ustawiono jedna na drugiej w wieżę na stole. Na samej górze wieży widać 4. Jaka jest suma liczb na wszystkich ścianach, które dotykają innej kostki albo stołu? *(4 pkt)*
   - A) 14
   - B) 15
   - C) 17
   - D) 18
   - E) 21
   <details><summary>rozwiązanie</summary>C — 17<br>Górna kostka ma na górze 4, więc jej dolna ściana to 7 − 4 = 3. Środkowa kostka dotyka górą i dołem — to dwie przeciwległe ściany, razem 7. Dolna kostka dotyka górą środkowej kostki, a dołem stołu — znowu przeciwległe ściany, razem 7. Suma: 3 + 7 + 7 = 17. Pułapka: 14 — pominięta ściana stojąca na stole.</details><br>
46. Na rysunku jest siatka zwykłej kostki do gry. Jaką liczbę trzeba wpisać w pole ze znakiem zapytania?<br><svg width="122" height="92" viewBox="-1 -1 122 92" fill="none" stroke="currentColor"><rect x="0" y="30" width="30" height="30"/><rect x="30" y="30" width="30" height="30"/><rect x="60" y="30" width="30" height="30"/><rect x="90" y="30" width="30" height="30"/><rect x="30" y="0" width="30" height="30"/><rect x="30" y="60" width="30" height="30"/><g fill="currentColor" stroke="none" font-size="16" text-anchor="middle"><text x="15" y="51">3</text><text x="45" y="51">2</text><text x="75" y="51">4</text><text x="105" y="51">5</text><text x="45" y="21">6</text><text x="45" y="81">?</text></g></svg> *(4 pkt)*
   - A) 1
   - B) 2
   - C) 3
   - D) 5
   - E) 6
   <details><summary>rozwiązanie</summary>A — 1<br>Złóż w myślach siatkę: długi pasek czterech ścian (3, 2, 4, 5) owija się wokół kostki, więc co druga ściana jest przeciwległa: 3 naprzeciw 4 i 2 naprzeciw 5 (obie pary dają 7). Ściana nad „2” i ściana pod „2” stają się górą i dołem kostki — są przeciwległe. Naprzeciw 6 musi być 7 − 6 = 1. Zresztą 1 to jedyna liczba, której jeszcze nie ma na siatce.</details><br>
47. Każdą ścianę sześcianu chcemy pomalować na jednolity kolor. Ile co najmniej kolorów potrzebujemy użyć, żeby każde dwie sąsiednie ściany różniły się kolorem? *(4 pkt)* *(Alfik 2024, zad. 20)*
   - A) 2
   - B) 3
   - C) 4
   - D) 5
   - E) 6
   <details><summary>rozwiązanie</summary>B — 3<br>Przeciwległe ściany nie są sąsiednie, więc mogą mieć ten sam kolor: góra i dół — kolor 1, przód i tył — kolor 2, lewa i prawa — kolor 3. Mniej się nie da, bo w jednym rogu sześcianu stykają się trzy ściany, każda z każdą.</details><br>
48. Na każdej ścianie kostki do gry jest od 1 do 6 oczek (na każdej ścianie inna liczba). Na czterech ścianach sąsiadujących ze ścianą z 3 oczkami łącznie jest 14 oczek. Ile oczek jest na ścianie leżącej naprzeciw ściany z 3 oczkami? *(4 pkt)* *(Alfik 2021, zad. 20)*
   - A) 1
   - B) 2
   - C) 4
   - D) 5
   - E) 6
   <details><summary>rozwiązanie</summary>C — 4<br>Na całej kostce jest 1 + 2 + 3 + 4 + 5 + 6 = 21 oczek. Ściana z 3 oczkami, jej 4 sąsiadki i ściana naprzeciwko to wszystkie 6 ścian. Naprzeciwko jest więc 21 − 3 − 14 = 4 oczka. (Zgadza się to z prawdziwą kostką, gdzie przeciwległe ściany dają razem 7.)</details><br>
49. Ściany sześciennej kostki do gry ponumerowane są liczbami od 1 do 6 (każda ściana inną liczbą). Jacek rzucił trzema kostkami i pomnożył trzy otrzymane liczby. Która z poniższych liczb nie mogła być wynikiem tego mnożenia? *(4 pkt)* *(Alfik 2019, zad. 12)*
   - A) 48
   - B) 64
   - C) 72
   - D) 81
   - E) 96
   <details><summary>rozwiązanie</summary>D — 81<br>81 = 3 · 3 · 3 · 3. Na kostce „trójkę w środku” mają tylko 3 i 6, i to tylko jedną, więc trzy kostki dadzą najwyżej trzy trójki w iloczynie — za mało. Pozostałe się da: 48 = 2 · 4 · 6, 64 = 4 · 4 · 4, 72 = 2 · 6 · 6, 96 = 4 · 4 · 6.</details><br>
50. Każdą z sześciu ścian sześciennej kostki do gry pomalowano na niebiesko albo na biało tak, że w każdym wierzchołku kostki schodziły się dwie ściany niebieskie i jedna biała. Ile niebieskich ścian miała ta kostka? *(4 pkt)* *(Alfik 2019, zad. 19)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5
   <details><summary>rozwiązanie</summary>D — 4<br>Kostka ma 8 wierzchołków, a każda ściana ma 4 wierzchołki. Biała ściana „obsługuje” 4 wierzchołki, a każdy wierzchołek ma dokładnie jedną białą ścianę, więc białych ścian jest 8 : 4 = 2. Niebieskich jest 6 − 2 = 4 (np. białe góra i dół, niebieskie boki).</details><br>
51. Zwykła kostka do gry stoi na stole tak, że na górze jest 1, z przodu (od strony Zosi) 2, a po prawej stronie 3. Zosia przetacza kostkę po stole przez krawędź: najpierw do siebie, potem w prawo, potem znowu do siebie i znowu w prawo. Jaka liczba jest teraz na górze? *(5 pkt)*
   - A) 2
   - B) 3
   - C) 4
   - D) 5
   - E) 6
   <details><summary>rozwiązanie</summary>A — 2<br>Najpierw ustal, co jest na niewidocznych ścianach: dół 6, tył 5, lewa 4. Przy przetoczeniu do siebie na górę wchodzi ściana z tyłu; przy przetoczeniu w prawo na górę wchodzi ściana z lewej. Krok 1 (do siebie): góra 5, przód 1, tył 6, lewa 4. Krok 2 (w prawo): góra 4, lewa 2 (dawny dół), dół 3, przód 1, tył 6. Krok 3 (do siebie): góra 6 (dawny tył), lewa 2. Krok 4 (w prawo): na górę wchodzi lewa ściana, czyli 2.</details><br>
52. Chcemy przygotować kostkę do gry, naklejając „oczka” na 6 ścian pustej kostki. Łącznie chcemy nakleić 22 oczka tak, żeby na każdej ścianie była inna liczba oczek i na każdej ścianie było przynajmniej jedno oczko. Ściana z największą liczbą oczek będzie zawierała: *(5 pkt)* *(Alfik 2021, zad. 23)*
   - A) 4 oczka
   - B) 5 oczek
   - C) 6 oczek
   - D) 7 oczek
   - E) 8 oczek
   <details><summary>rozwiązanie</summary>D — 7 oczek<br>Sześć różnych liczb od 1 w górę daje co najmniej 1 + 2 + 3 + 4 + 5 + 6 = 21. Mamy 22, czyli jedno oczko „za dużo”. Dodać je można tylko do największej liczby (inaczej powtórzyłyby się dwie liczby): 1, 2, 3, 4, 5, 7. Największa ściana ma 7 oczek.</details><br>
53. Kasia ma cztery nietypowe sześcienne kostki do gry – każda z nich ma ściany opisane liczbami 1, 2, 4, 8, 16, 32 (każdą ścianę jedną liczbą). Kasia wykonała rzut tymi czterema kostkami i suma czterech liczb, które wypadły wyniosła 48. Która z poniższych liczb na pewno wypadła na jednej z kostek? *(5 pkt)* *(Alfik 2015, zad. 28)*
   - A) 2
   - B) 4
   - C) 8
   - D) 16
   - E) 32
   <details><summary>rozwiązanie</summary>C — 8<br>Bez 16 i 32 cztery kostki dadzą najwyżej 4 · 8 = 32, za mało. Jeśli wypadło 32, pozostałe trzy kostki dają 16: tylko 8 + 4 + 4. Jeśli nie ma 32, to są szesnastki: 16 + 16 + 8 + 8. Są więc tylko dwa rozkłady (32, 8, 4, 4) i (16, 16, 8, 8) — w obu jest 8.</details><br>

---

## Klucz odpowiedzi

1. B — 1
2. B — 5 *(Alfik 2023, zad. 3)*
3. B — 5 *(Alfik 2022, zad. 9)*
4. D — 24 *(Alfik 2019, zad. 10)*
5. D — 24 *(Alfik 2017, zad. 5)*
6. C — 32 *(Alfik 2015, zad. 4)*
7. C — 11
8. B — 3 *(Alfik 2023, zad. 13)*
9. B — 3 *(Alfik 2021, zad. 17)*
10. B — 8 *(Alfik 2019, zad. 13)*
11. E — taka szachownica nie istnieje *(Alfik 2019, zad. 15)*
12. D — 8 *(Alfik 2018, zad. 16)*
13. A — 7 *(Alfik 2018, zad. 17)*
14. A — 8 *(Alfik 2017, zad. 17)*
15. B — 8 *(Alfik 2016, zad. 11)*
16. B — 4
17. A — 6 *(Alfik 2022, zad. 25)*
18. D — 6 *(Alfik 2021, zad. 22)*
19. E — 36 *(Alfik 2016, zad. 24)*
20. D — 23 *(Alfik 2016, zad. 28)*
21. D — 14
22. E — 30
23. D — 36
24. A — 24
25. D — 20
26. D — 16 *(Alfik 2025, zad. 1)*
27. D — 6 *(Alfik 2024, zad. 4)*
28. D — 8 *(Alfik 2022, zad. 8)*
29. D — 6 cm *(Alfik 2019, zad. 3)*
30. C — 10 *(Alfik 2017, zad. 4)*
31. C — 9 cm *(Alfik 2016, zad. 6)*
32. E — 36 *(Alfik 2015, zad. 2)*
33. C — 12
34. E — 20 *(Alfik 2025, zad. 16)*
35. E — 7 *(Alfik 2022, zad. 12)*
36. A — 1 cm *(Alfik 2022, zad. 14)*
37. A — 8 *(Alfik 2022, zad. 19)*
38. E — więcej niż 6 *(Alfik 2017, zad. 16)*
39. E — nie da się tak przykryć tej planszy
40. D — 17 *(Alfik 2023, zad. 23)*
41. B — 12
42. D — 4 *(Alfik 2024, zad. 10)*
43. B — 5 *(Alfik 2023, zad. 7)*
44. A — 1 *(Alfik 2018, zad. 2)*
45. C — 17
46. A — 1
47. B — 3 *(Alfik 2024, zad. 20)*
48. C — 4 *(Alfik 2021, zad. 20)*
49. D — 81 *(Alfik 2019, zad. 12)*
50. D — 4 *(Alfik 2019, zad. 19)*
51. A — 2
52. D — 7 oczek *(Alfik 2021, zad. 23)*
53. C — 8 *(Alfik 2015, zad. 28)*

## Ściąga

| Co | Fakt / sposób |
|---|---|
| Szachownica m × n | gdy m · n parzyste — po równo; gdy nieparzyste — kolor narożnika ma o 1 pole więcej |
| Kwadraty na kratce n × n | 1 · 1 + 2 · 2 + … + n · n (dla 3 × 3: 14, dla 4 × 4: 30, dla 5 × 5: 55, dla 8 × 8: 204) |
| Kwadraty k × k na kratce n × n | (n − k + 1) · (n − k + 1) |
| Cięcia równoległe | k cięć daje k + 1 kawałków; cięcia w dwóch kierunkach: (a + 1) · (b + 1) |
| Domino | zakrywa zawsze 1 pole białe i 1 czarne; nieparzysta liczba pól → zawsze zostaje co najmniej 1 pole |
| Przemalowanie wiersza | czarne → białe, białe → czarne; pole na skrzyżowaniu dwóch przemalowanych linii wraca do koloru wyjściowego |
| Kostka do gry | 1–6, 2–5, 3–4 naprzeciw siebie; suma wszystkich oczek 21 |
| Siatka „krzyż” | w pasku 4 ścian: 1. naprzeciw 3., 2. naprzeciw 4.; dwie ściany doklejone z boków paska są naprzeciw siebie |
