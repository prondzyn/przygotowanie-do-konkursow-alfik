# 09. Działania, ciągi i wzorki

**Dlaczego warto:** Zadania z działaniami są w Alfiku co roku: wstawianie znaków i nawiasów, sumy kolejnych liczb, „która liczba będzie na 100. miejscu”, ułamki. Liczenie „na piechotę” zajmuje za dużo czasu — trzeba zauważyć sprytny skrót (pary, powtarzający się wzorek, parzystość).

- **W pliku:** 40 zadań: 15 nowych i 25 z prawdziwych arkuszy Alfika (18 za 3 pkt, 10 za 4 pkt, 12 za 5 pkt).

**Wskazówki**
- Mnożenie i dzielenie wykonujemy przed dodawaniem i odejmowaniem — chyba że nawiasy mówią inaczej.
- Zmiana znaku + na − zmienia wynik o liczbę parzystą (o dwa razy tę liczbę). Dlatego parzystość wyniku się nie zmienia!
- Sumę kolejnych liczb licz parami: pierwsza + ostatnia, druga + przedostatnia… Suma kilku kolejnych liczb = liczba środkowa · ile ich jest.
- Gdy wzorek się powtarza co k miejsc, podziel numer miejsca przez k i patrz na resztę (reszta 0 = ostatni element wzorku).
- „Połowa z jednej trzeciej” to mnożenie: ½ · ⅓ = 1/6. Kolejność nie ma znaczenia: połowa z jednej trzeciej = jedna trzecia z połowy.

**Spis treści**

- [A. Łamigłówki z działaniami](#a-łamigłówki-z-działaniami)
- [B. Sumy i sprytne liczenie](#b-sumy-i-sprytne-liczenie)
- [C. Ciągi i wzorki](#c-ciągi-i-wzorki)
- [D. Ułamki: „połowa z jednej trzeciej”](#d-ułamki-połowa-z-jednej-trzeciej)
- [Klucz odpowiedzi](#klucz-odpowiedzi)
- [Ściąga](#ściąga)

---

## A. Łamigłówki z działaniami

Kwadraty magiczne, nawiasy i wstawianie znaków + oraz −.

1. W kwadracie magicznym 3 × 3 suma liczb w każdym wierszu, w każdej kolumnie i na obu przekątnych jest taka sama. Ala wpisała do takiego kwadratu liczby 5, 6, 7, 8, 9, 10, 11, 12 i 13 (każdą raz). Ile wynosi suma liczb w jednym wierszu? *(3 pkt)*
   - A) 27
   - B) 30
   - C) 36
   - D) 45
   - E) 81
   <details><summary>rozwiązanie</summary>A — 27<br>Wszystkie liczby razem: 5 + 6 + … + 13 = 81. Kwadrat ma 3 wiersze o tej samej sumie, a każda liczba leży w dokładnie jednym wierszu. Jeden wiersz ma więc 81 : 3 = 27. Pułapka: 81 to suma całego kwadratu.</details><br>
2. Na każdej ścianie kostki do gry jest od 1 do 6 oczek. Bartek w pięciu rzutach kostką uzyskał łącznie 28 oczek. Ile szóstek wyrzucił, jeśli wiemy, że nie wyrzucił ani jednej piątki? *(3 pkt)* *(Alfik 2025, zad. 2)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5
   <details><summary>rozwiązanie</summary>D — 4<br>Pięć szóstek dałoby 30, czyli o 2 za dużo. Brakujące 2 oczka muszą „zniknąć” z jednego rzutu (zamiana 6 na 4) albo z dwóch (6 na 5 i 6 na 5), ale piątek nie było. Zostaje 6 + 6 + 6 + 6 + 4 = 28, czyli 4 szóstki.</details><br>
3. W działaniu 28 + 37 = 69 chcemy zmienić jedną z cyfr tak, aby otrzymać prawdziwą równość. Którą cyfrę musimy zmienić? *(3 pkt)* *(Alfik 2023, zad. 1)*
   - A) 3
   - B) 6
   - C) 7
   - D) 8
   - E) 9
   <details><summary>rozwiązanie</summary>E — 9<br>Naprawdę 28 + 37 = 65. Wystarczy zmienić 9 na 5: 28 + 37 = 65. Żeby lewa strona dała 69, trzeba by zwiększyć ją o 4, a zmiana jednej cyfry dziesiątek zmienia sumę o pełne dziesiątki; zmiana 8 na 12 lub 7 na 11 jest niemożliwa — więc zmienić trzeba cyfrę 9.</details><br>
4. Spośród trzech dodatnich liczb jednocyfrowych, druga liczba jest dwa razy większa niż pierwsza, a trzecia liczba jest trzy razy większa niż druga. Ile wynosi suma tych trzech liczb? *(3 pkt)* *(Alfik 2015, zad. 7)*
   - A) 6
   - B) 8
   - C) 9
   - D) 10
   - E) 12
   <details><summary>rozwiązanie</summary>C — 9<br>Trzecia liczba jest 2 · 3 = 6 razy większa od pierwszej. Musi być jednocyfrowa, więc pierwsza to 1 (bo 6 · 2 = 12 ma już dwie cyfry). Liczby to 1, 2, 6, a ich suma to 9.</details><br>
5. W wyrażeniu 2 + 4 · 5 − 3 wstawiamy jedną parę nawiasów. Jaki największy wynik możemy otrzymać? *(4 pkt)*
   - A) 19
   - B) 21
   - C) 25
   - D) 27
   - E) 30
   <details><summary>rozwiązanie</summary>D — 27<br>Bez nawiasów: 2 + 20 − 3 = 19. Mnożenie powiększa najbardziej, gdy mnożymy coś dużego — wstawmy nawias wokół dodawania: (2 + 4) · 5 − 3 = 30 − 3 = 27. Inne możliwości dają mniej, np. 2 + 4 · (5 − 3) = 10. Pułapka: 30 — zapomniane odjęcie 3 na końcu.</details><br>
6. W wyrażeniu 9 □ 8 □ 7 □ 6 □ 5 w każde okienko wstawiamy znak + albo −. Który z wyników NIE może wyjść? *(4 pkt)*
   - A) 5
   - B) 10
   - C) 13
   - D) 19
   - E) 25
   <details><summary>rozwiązanie</summary>B — 10<br>Same plusy dają 35 — liczbę nieparzystą. Zamiana + na − przed liczbą odbiera ją dwa razy (raz nie dodajemy, raz odejmujemy), czyli zmienia wynik o liczbę parzystą. Dlatego wynik zawsze jest nieparzysty i 10 nie może wyjść. Pozostałe wychodzą, np. 9 + 8 + 7 − 6 − 5 = 13, 9 − 8 + 7 + 6 + 5 = 19, 9 + 8 + 7 + 6 − 5 = 25, 9 − 8 − 7 + 6 + 5 = 5.</details><br>
7. Pewną liczbę jednocyfrową pomnożyłem przez 4, a od wyniku mnożenia odjąłem 6. W ten sposób otrzymałem liczbę dwucyfrową o sumie cyfr 5. Jaką liczbę otrzymałem? *(4 pkt)* *(Alfik 2021, zad. 11)*
   - A) 14
   - B) 23
   - C) 32
   - D) 41
   - E) 50
   <details><summary>rozwiązanie</summary>A — 14<br>Wynik + 6 musi być wielokrotnością 4 (najwyżej 4 · 9 = 36). Sprawdzamy opcje: 14 + 6 = 20 = 4 · 5 — pasuje. 23 + 6 = 29, 32 + 6 = 38, 41 + 6 = 47 nie dzielą się przez 4, a 50 + 6 = 56 = 4 · 14, ale 14 nie jest jednocyfrowa.</details><br>
8. W miejsce każdej gwiazdki w schemacie 6 * 5 * 4 * 3 * 2 * 1 = 7 chcemy wpisać znak „+” lub „–” tak, aby otrzymać prawdziwe działanie. Ile najwięcej minusów możemy wpisać? *(4 pkt)* *(Alfik 2017, zad. 19)*
   - A) 4
   - B) 3
   - C) 2
   - D) 1
   - E) 0
   <details><summary>rozwiązanie</summary>B — 3<br>Same plusy dają 21. Każda liczba ze znakiem minus zmniejsza wynik o dwa razy swoją wartość, więc liczby z minusem muszą mieć sumę (21 − 7) : 2 = 7. Z liczb 5, 4, 3, 2, 1 najwięcej składników daje 4 + 2 + 1 = 7: 6 + 5 − 4 + 3 − 2 − 1 = 7. Czterech liczb o sumie 7 nie wybierzemy (najmniejsza czwórka to 1 + 2 + 3 + 4 = 10).</details><br>
9. W kwadracie magicznym 3 × 3 sumy w każdym wierszu, w każdej kolumnie i na obu przekątnych są równe. W lewym górnym rogu jest liczba 13, w prawym górnym 11, a w lewym dolnym 9. Jaka liczba jest w prawym dolnym rogu? *(5 pkt)*
   - A) 3
   - B) 5
   - C) 6
   - D) 7
   - E) 8
   <details><summary>rozwiązanie</summary>D — 7<br>Warto znać sztuczkę: w kwadracie magicznym 3 × 3 suma każdej linii jest 3 razy większa od liczby w środku. Przekątna z prawego górnego do lewego dolnego rogu to 11 + środek + 9, a to ma być równe trzem środkom. Zatem 20 = dwa środki, czyli w środku jest 10, a każda suma wynosi 30. Druga przekątna: 13 + 10 + ? = 30, więc ? = 7. Cały kwadrat: 13, 6, 11 / 8, 10, 12 / 9, 14, 7.</details><br>
10. W działaniu: 1 + 2 + 3 + 4 + 5 + 6 + 7 = 8 niektóre znaki „+” chcemy zamienić na znaki „–” tak, by równość była prawdziwa. Jaka jest najmniejsza liczba zamian, która pozwoli to osiągnąć? *(5 pkt)* *(Alfik 2025, zad. 22)*
   - A) 2
   - B) 3
   - C) 4
   - D) 5
   - E) 6
   <details><summary>rozwiązanie</summary>A — 2<br>Teraz lewa strona to 28, a ma być 8 — trzeba „zabrać” 20. Zamiana „+ n” na „− n” zmniejsza wynik o 2 · n, więc liczby ze zmienionym znakiem muszą dawać razem 10. Jedna liczba nie wystarczy (największa to 7), ale dwie tak: 3 + 7 = 10. Np. 1 + 2 − 3 + 4 + 5 + 6 − 7 = 8.</details><br>
11. W działaniu: 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 10 należy niektóre ze znaków „+” zastąpić znakami „–” tak, aby otrzymać prawdziwą równość. Ile najmniej znaków trzeba zamienić? *(5 pkt)* *(Alfik 2022, zad. 21)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5
   <details><summary>rozwiązanie</summary>B — 2<br>Suma wszystkich liczb to 44. Zmiana „+” na „–” przed liczbą zmniejsza wynik o dwa razy tę liczbę. Trzeba zmniejszyć o 44 − 10 = 34, czyli liczby ze znakiem „–” mają dać razem 17. Jedna liczba to za mało (największa to 9), ale dwie wystarczą: 8 + 9 = 17. Sprawdzenie: 2 + 3 + 4 + 5 + 6 + 7 − 8 − 9 = 10.</details><br>
12. Ile co najmniej znaków „+” w działaniu: 7 + 6 + 5 + 4 + 3 + 2 + 1 = 12 trzeba zastąpić znakami „–”, aby otrzymać prawdziwe działanie? *(5 pkt)* *(Alfik 2021, zad. 24)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5
   <details><summary>rozwiązanie</summary>B — 2<br>Teraz lewa strona to 28, a ma być 12 — trzeba zmniejszyć o 16. Zamiana „+ a” na „− a” zmniejsza wynik o 2 · a, więc zamienione liczby muszą dawać razem 8. Jedna liczba z 1–6 nie wystarczy, ale dwie tak: 6 + 2 lub 5 + 3. Np. 7 − 6 + 5 + 4 + 3 − 2 + 1 = 12.</details><br>

## B. Sumy i sprytne liczenie

Zamiast dodawać po kolei — łącz w pary albo szukaj liczby środkowej.

13. Ile wynosi suma 1 + 2 + 3 + … + 19 + 20? *(3 pkt)*
   - A) 210
   - B) 220
   - C) 231
   - D) 400
   - E) 420
   <details><summary>rozwiązanie</summary>A — 210<br>Łączymy w pary: 1 + 20 = 21, 2 + 19 = 21, …, 10 + 11 = 21. Par jest 10, więc suma to 10 · 21 = 210. Pułapka: 420 = 20 · 21 — tyle wyjdzie, gdy zapomnimy, że par jest tylko 10, a nie 20.</details><br>
14. Suma siedmiu kolejnych liczb naturalnych wynosi 98. Jaka jest największa z tych liczb? *(3 pkt)*
   - A) 14
   - B) 15
   - C) 16
   - D) 17
   - E) 18
   <details><summary>rozwiązanie</summary>D — 17<br>Liczba środkowa (czwarta z siedmiu) to średnia: 98 : 7 = 14. Liczby to 11, 12, 13, 14, 15, 16, 17 — największa to 17. Sprawdzenie: 11 + 17 = 28, 12 + 16 = 28, 13 + 15 = 28 i jeszcze 14, razem 98. Pułapka: 14 to liczba środkowa, a nie największa.</details><br>
15. Pierwsza godzina parkowania kosztuje 3 zł, a każda kolejna godzina jest o złotówkę droższa od poprzedniej. Ile kosztuje pięciogodzinne parkowanie? *(3 pkt)* *(Alfik 2025, zad. 4)*
   - A) 24 zł
   - B) 25 zł
   - C) 26 zł
   - D) 27 zł
   - E) 28 zł
   <details><summary>rozwiązanie</summary>B — 25 zł<br>Kolejne godziny kosztują 3, 4, 5, 6 i 7 zł. Razem 3 + 4 + 5 + 6 + 7 = 25 zł (środkowa cena 5 zł razy 5 godzin).</details><br>
16. Cennik parkingu pewnej galerii handlowej jest następujący: pierwsza godzina parkowania kosztuje 1 zł, a każda kolejna godzina jest o 2 zł droższa od poprzedniej. Ile kosztuje 4-godzinne parkowanie? *(3 pkt)* *(Alfik 2024, zad. 5)*
   - A) 12 zł
   - B) 13 zł
   - C) 14 zł
   - D) 15 zł
   - E) 16 zł
   <details><summary>rozwiązanie</summary>E — 16 zł<br>Kolejne godziny kosztują 1 zł, 3 zł, 5 zł i 7 zł. Razem 1 + 3 + 5 + 7 = 16 zł. Pułapka: 7 zł to cena tylko czwartej godziny, a nie całego postoju.</details><br>
17. Którą z poniższych liczb można przedstawić w postaci sumy trzech kolejnych liczb jednocyfrowych? *(3 pkt)* *(Alfik 2024, zad. 6)*
   - A) 7
   - B) 8
   - C) 9
   - D) 10
   - E) 11
   <details><summary>rozwiązanie</summary>C — 9<br>Suma trzech kolejnych liczb to trzy razy środkowa liczba, więc musi dzielić się przez 3. Z podanych tylko 9 dzieli się przez 3: 9 = 2 + 3 + 4.</details><br>
18. Jaka liczba leży na osi liczbowej w jednakowej odległości od liczb 3 i 13? *(3 pkt)* *(Alfik 2023, zad. 4)*
   - A) 4
   - B) 5
   - C) 6
   - D) 7
   - E) 8
   <details><summary>rozwiązanie</summary>E — 8<br>Odległość między 3 a 13 to 10, połowa to 5. 3 + 5 = 8 i 13 − 5 = 8. Pułapka: odpowiedź 5 to połowa odległości, a nie punkt.</details><br>
19. Suma trzech kolejnych liczb (naturalnych) wynosi 24. Największą z tych trzech liczb jest: *(3 pkt)* *(Alfik 2021, zad. 4)*
   - A) 6
   - B) 7
   - C) 8
   - D) 9
   - E) 10
   <details><summary>rozwiązanie</summary>D — 9<br>Środkowa z trzech kolejnych liczb to średnia: 24 : 3 = 8. Liczby to 7, 8, 9, więc największa to 9. Pułapka: 8 to środkowa, a nie największa.</details><br>
20. Paczka banknotów to sto sztuk banknotów. W takim razie milion złotych – ile to paczek dziesięciozłotówek? *(3 pkt)* *(Alfik 2019, zad. 1)*
   - A) 1
   - B) 10
   - C) 100
   - D) 1000
   - E) 10 000
   <details><summary>rozwiązanie</summary>D — 1000<br>Jedna paczka dziesięciozłotówek to 100 · 10 zł = 1000 zł. Milion złotych to 1 000 000 : 1000 = 1000 takich paczek.</details><br>
21. W białym pudełku są 2 jednakowe żółte pudełka. W każdym żółtym pudełku są 3 jednakowe brązowe pudełka, a w każdym brązowym pudełku są 4 jednakowe czerwone pudełka. Ile łącznie pudełek (wszystkich kolorów) jest wewnątrz białego pudełka? *(3 pkt)* *(Alfik 2019, zad. 8)*
   - A) 24
   - B) 28
   - C) 30
   - D) 32
   - E) 33
   <details><summary>rozwiązanie</summary>D — 32<br>Żółtych jest 2, brązowych 2 · 3 = 6, czerwonych 6 · 4 = 24. Razem 2 + 6 + 24 = 32. Pułapka: białego pudełka nie liczymy — pytamy o pudełka wewnątrz niego (33 to odpowiedź z białym).</details><br>
22. Paczka banknotów to sto sztuk banknotów. W takim razie milion złotych – ile to paczek stuzłotówek? *(3 pkt)* *(Alfik 2017, zad. 8)*
   - A) 1
   - B) 10
   - C) 100
   - D) 1000
   - E) 10 000
   <details><summary>rozwiązanie</summary>C — 100<br>Jedna paczka stuzłotówek to 100 · 100 zł = 10 000 zł. Milion to 1 000 000 : 10 000 = 100 paczek.</details><br>
23. Ile wynosi 100 − 99 + 98 − 97 + 96 − 95 + … + 4 − 3 + 2 − 1? *(4 pkt)*
   - A) 0
   - B) 1
   - C) 50
   - D) 99
   - E) 100
   <details><summary>rozwiązanie</summary>C — 50<br>Łączymy w pary: (100 − 99) + (98 − 97) + … + (2 − 1). Każda para daje 1. Liczb jest 100, więc par jest 50, a wynik to 50 · 1 = 50.</details><br>
24. Suma pewnych pięciu kolejnych liczb wynosi 40. Jaką liczbą jest najmniejszy z tych pięciu składników? *(4 pkt)* *(Alfik 2022, zad. 11)*
   - A) 5
   - B) 6
   - C) 7
   - D) 8
   - E) 9
   <details><summary>rozwiązanie</summary>B — 6<br>Środkowa z pięciu kolejnych liczb to średnia: 40 : 5 = 8. Liczby to 6, 7, 8, 9, 10, więc najmniejsza to 6. Pułapka: 8 to liczba środkowa, nie najmniejsza.</details><br>
25. Każde zielone pudełko zawiera dwa pudełka czerwone, każde czerwone pudełko zawiera trzy pudełka żółte, każde żółte pudełko zawiera cztery pudełka niebieskie, zaś wszystkie niebieskie pudełka są puste. Ile pudełek różnych kolorów znajduje się wewnątrz jednego pudełka zielonego? *(4 pkt)* *(Alfik 2017, zad. 20)*
   - A) 16
   - B) 18
   - C) 24
   - D) 32
   - E) 36
   <details><summary>rozwiązanie</summary>D — 32<br>W zielonym są 2 czerwone, w nich 2 · 3 = 6 żółtych, a w nich 6 · 4 = 24 niebieskie. Razem 2 + 6 + 24 = 32.</details><br>
26. Uczniowie pewnej klasy wybierali trójkę klasową. Każdy uczeń napisał na karteczce nazwiska trzech osób, na które oddaje głos. Wybory wygrali: Maciek (15 głosów), Karolina (14 głosów) i Kasia (11 głosów). Pozostali uzyskali wyniki: Bartek (5 głosów) i Jacek (3 głosy). Ilu uczniów liczy ta klasa? *(4 pkt)* *(Alfik 2016, zad. 19)*
   - A) 16
   - B) 24
   - C) 32
   - D) 36
   - E) 48
   <details><summary>rozwiązanie</summary>A — 16<br>Wszystkich głosów jest 15 + 14 + 11 + 5 + 3 = 48. Każdy uczeń oddał 3 głosy, więc uczniów jest 48 : 3 = 16.</details><br>
27. Kuba wypisał po kolei wszystkie liczby od 1 do 120. Ile cyfr napisał? *(5 pkt)*
   - A) 120
   - B) 240
   - C) 249
   - D) 250
   - E) 252
   <details><summary>rozwiązanie</summary>E — 252<br>Liczby jednocyfrowe 1–9: 9 cyfr. Liczby dwucyfrowe 10–99: jest ich 90, każda ma 2 cyfry, czyli 180 cyfr. Liczby trzycyfrowe 100–120: jest ich 120 − 100 + 1 = 21, czyli 63 cyfry. Razem 9 + 180 + 63 = 252. Pułapka: 249 — gdy policzymy liczby od 100 do 120 jako 20 zamiast 21.</details><br>
28. Każdy uczeń klasy Maćka uczy się przynajmniej dwóch języków spośród: angielskiego, francuskiego i niemieckiego. Angielskiego uczy się 12 uczniów, niemieckiego – 10 uczniów, zaś francuskiego – 6 uczniów. Ilu uczniów jest w klasie Maćka, jeśli wiemy, że tylko dwóch z nich uczy się wszystkich trzech języków? *(5 pkt)* *(Alfik 2016, zad. 29)*
   - A) 13
   - B) 14
   - C) 15
   - D) 16
   - E) 17
   <details><summary>rozwiązanie</summary>A — 13<br>Wszystkich „miejsc na lekcjach” jest 12 + 10 + 6 = 28. Dwóch uczniów zajmuje po 3 miejsca (razem 6), zostaje 22 miejsc dla uczniów z dwoma językami — to 22 : 2 = 11 uczniów. Razem 11 + 2 = 13.</details><br>
29. Na podłodze stoją trzy wiadra z wodą. W pierwszym i drugim jest łącznie 12 litrów wody, w drugim i trzecim jest łącznie 10 litrów, a w trzecim i pierwszym jest łącznie 16 litrów. Ile wody jest łącznie we wszystkich trzech wiadrach? *(5 pkt)* *(Alfik 2015, zad. 29)*
   - A) 18 litrów
   - B) 19 litrów
   - C) 24 litry
   - D) 28 litrów
   - E) 38 litrów
   <details><summary>rozwiązanie</summary>B — 19 litrów<br>Dodając wszystkie trzy pary, każde wiadro liczymy dwa razy: 12 + 10 + 16 = 38 litrów to podwójna ilość wody. Wody jest więc 38 : 2 = 19 litrów. Pułapka: odpowiedź 38.</details><br>

## C. Ciągi i wzorki

Szukaj tego, co się powtarza albo o ile rośnie kolejny wyraz.

30. Ola zapisuje litery według wzoru ALFIKALFIKALFIK… Jaka litera będzie na 100. miejscu? *(3 pkt)*
   - A) A
   - B) L
   - C) F
   - D) I
   - E) K
   <details><summary>rozwiązanie</summary>E — K<br>Wzorek ALFIK ma 5 liter i się powtarza. 100 : 5 = 20 bez reszty, czyli na 100. miejscu kończy się dwudziesty raz cały wyraz ALFIK. Ostatnia litera wzorku to K. Pułapka: A — gdy myślimy, że „równo” oznacza początek wzorku.</details><br>
31. W ubiegłym tygodniu temperatura każdego dnia spadała o 2 stopnie. Jeśli w poniedziałek było 15°C, to w niedzielę było: *(3 pkt)* *(Alfik 2015, zad. 10)*
   - A) 1°C
   - B) 2°C
   - C) 3°C
   - D) 4°C
   - E) poniżej 0°C
   <details><summary>rozwiązanie</summary>C — 3°C<br>Od poniedziałku do niedzieli jest 6 „przejść” na kolejny dzień: 6 · 2 = 12 stopni spadku. 15 − 12 = 3°C. Pułapka: liczenie 7 spadków zamiast 6.</details><br>
32. Z zapałek układamy rząd kwadratów, przy czym sąsiednie kwadraty mają wspólny bok. Jeden kwadrat to 4 zapałki, dwa kwadraty to 7 zapałek, trzy kwadraty to 10 zapałek. Ile zapałek potrzeba na rząd 25 kwadratów? *(4 pkt)*
   - A) 75
   - B) 76
   - C) 79
   - D) 100
   - E) 101
   <details><summary>rozwiązanie</summary>B — 76<br>Pierwszy kwadrat to 4 zapałki, a każdy następny dokłada 3 (bo jeden bok jest wspólny z poprzednim). Dla 25 kwadratów: 4 + 24 · 3 = 4 + 72 = 76. Pułapka: 100 = 25 · 4 — liczenie wspólnych boków dwa razy.</details><br>
33. Zosia zapisuje liczby 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, … (wciąż powtarzając 1, 2, 3, 4). Ile wynosi suma pierwszych 50 zapisanych liczb? *(5 pkt)*
   - A) 120
   - B) 123
   - C) 124
   - D) 125
   - E) 130
   <details><summary>rozwiązanie</summary>B — 123<br>Jedna „paczka” 1, 2, 3, 4 ma 4 liczby i sumę 10. 50 : 4 = 12 reszty 2, więc mamy 12 pełnych paczek (suma 120) i jeszcze 2 liczby z nowej paczki: 1 i 2. Razem 120 + 1 + 2 = 123. Pułapka: 120 — zapomniane dwie ostatnie liczby; 125 = 50 · 2,5 — tak byłoby tylko dla pełnych paczek.</details><br>
34. Janek zapisał obok siebie kolejne liczby naturalne, zaczynając od 1: 123456789101112131415… Jaka cyfra stoi na 100. miejscu? *(5 pkt)*
   - A) 0
   - B) 4
   - C) 5
   - D) 6
   - E) 9
   <details><summary>rozwiązanie</summary>C — 5<br>Liczby 1–9 zajmują 9 miejsc. Zostaje 100 − 9 = 91 miejsc na liczby dwucyfrowe. 45 liczb dwucyfrowych (od 10 do 54) zajmuje 90 miejsc, czyli kończymy na 99. miejscu ostatnią cyfrą liczby 54. 100. miejsce to pierwsza cyfra kolejnej liczby, 55 — czyli 5. Pułapka: 4 — ostatnia cyfra liczby 54, czyli o jedno miejsce za wcześnie.</details><br>
35. W pudełku jest 30 jajek. W każdym ruchu wyjmujemy z pudełka połowę jajek (jeśli liczba jajek jest parzysta) lub połowę jajek i pół jajka (jeśli liczba jajek jest nieparzysta). W ilu ruchach opróżnimy pudełko? *(5 pkt)* *(Alfik 2025, zad. 26)*
   - A) 4
   - B) 5
   - C) 6
   - D) 7
   - E) 8
   <details><summary>rozwiązanie</summary>B — 5<br>Liczymy po kolei, ile jajek zostaje: 30 → 15 (wyjęto 15), 15 → 7 (wyjęto 7,5 + 0,5 = 8), 7 → 3 (wyjęto 4), 3 → 1 (wyjęto 2), 1 → 0 (wyjęto 1). To 5 ruchów.</details><br>
36. Na stole leży jeden kawałek papieru. W każdym ruchu albo rozcinamy na dwie części każdy leżący na stole kawałek papieru albo zabieramy ze stołu jeden kawałek papieru. Jaka jest najmniejsza liczba ruchów, którymi doprowadzimy do sytuacji, gdy na stole będzie dokładnie 30 kawałków papieru? *(5 pkt)* *(Alfik 2018, zad. 27)*
   - A) 6
   - B) 7
   - C) 8
   - D) 9
   - E) 10 lub więcej
   <details><summary>rozwiązanie</summary>A — 6<br>Rozcinanie wszystkiego podwaja liczbę kawałków. Najlepiej myśleć od końca: 30 to podwojone 15, 15 to 16 − 1, a 16 to 1 podwojone 4 razy. Czyli: 1 → 2 → 4 → 8 → 16 → 15 → 30 — 6 ruchów. W 5 ruchach liczby 30 nie da się otrzymać (można to sprawdzić, wypisując wszystkie możliwości), więc 6 to najmniej.</details><br>

## D. Ułamki: „połowa z jednej trzeciej”

„Część z części” to mnożenie ułamków. Najprościej liczyć na konkretnej liczbie albo na rysunku czekolady.

37. Ile to jest połowa z jednej trzeciej z 60? *(3 pkt)*
   - A) 10
   - B) 15
   - C) 20
   - D) 30
   - E) 40
   <details><summary>rozwiązanie</summary>A — 10<br>Jedna trzecia z 60 to 60 : 3 = 20. Połowa z 20 to 10. Pułapka: 20 — zatrzymanie się w połowie rachunku; 30 — wzięcie tylko połowy z 60.</details><br>
38. Ile jest takich nieskracalnych ułamków, które są mniejsze od 1 i których licznik i mianownik to jednocyfrowe liczby o sumie 10? *(3 pkt)* *(Alfik 2023, zad. 9)*
   - A) 1
   - B) 2
   - C) 3
   - D) 4
   - E) 5
   <details><summary>rozwiązanie</summary>B — 2<br>Ułamek mniejszy od 1 ma licznik mniejszy od mianownika: 1/9, 2/8, 3/7, 4/6. Ułamki 2/8 i 4/6 można skrócić przez 2. Zostają 1/9 i 3/7 — dwa ułamki.</details><br>
39. Ola zjadła 1/3 czekolady. Ania zjadła połowę tego, co zostało. Jaka część czekolady jeszcze została? *(4 pkt)*
   - A) 1/6
   - B) 1/4
   - C) 1/3
   - D) 1/2
   - E) 2/3
   <details><summary>rozwiązanie</summary>C — 1/3<br>Podziel czekoladę na 6 kostek. Ola zjada 1/3, czyli 2 kostki — zostają 4. Ania zjada połowę z 4, czyli 2 kostki. Zostają 2 kostki z 6, czyli 2/6 = 1/3. Pułapka: 1/6 — liczenie połowy z 1/3 zamiast połowy z tego, co zostało.</details><br>
40. Jedna trzecia z połowy pewnej liczby wynosi 8. Ile wynoszą trzy czwarte tej liczby? *(5 pkt)*
   - A) 6
   - B) 12
   - C) 24
   - D) 32
   - E) 36
   <details><summary>rozwiązanie</summary>E — 36<br>Jedna trzecia z połowy to jedna szósta całości. Skoro 1/6 liczby to 8, cała liczba to 6 · 8 = 48. Jedna czwarta z 48 to 12, a trzy czwarte to 3 · 12 = 36. Pułapka: 24 — wzięcie połowy zamiast trzech czwartych; 6 = trzy czwarte z 8.</details><br>

---

## Klucz odpowiedzi

1. A — 27
2. D — 4 *(Alfik 2025, zad. 2)*
3. E — 9 *(Alfik 2023, zad. 1)*
4. C — 9 *(Alfik 2015, zad. 7)*
5. D — 27
6. B — 10
7. A — 14 *(Alfik 2021, zad. 11)*
8. B — 3 *(Alfik 2017, zad. 19)*
9. D — 7
10. A — 2 *(Alfik 2025, zad. 22)*
11. B — 2 *(Alfik 2022, zad. 21)*
12. B — 2 *(Alfik 2021, zad. 24)*
13. A — 210
14. D — 17
15. B — 25 zł *(Alfik 2025, zad. 4)*
16. E — 16 zł *(Alfik 2024, zad. 5)*
17. C — 9 *(Alfik 2024, zad. 6)*
18. E — 8 *(Alfik 2023, zad. 4)*
19. D — 9 *(Alfik 2021, zad. 4)*
20. D — 1000 *(Alfik 2019, zad. 1)*
21. D — 32 *(Alfik 2019, zad. 8)*
22. C — 100 *(Alfik 2017, zad. 8)*
23. C — 50
24. B — 6 *(Alfik 2022, zad. 11)*
25. D — 32 *(Alfik 2017, zad. 20)*
26. A — 16 *(Alfik 2016, zad. 19)*
27. E — 252
28. A — 13 *(Alfik 2016, zad. 29)*
29. B — 19 litrów *(Alfik 2015, zad. 29)*
30. E — K
31. C — 3°C *(Alfik 2015, zad. 10)*
32. B — 76
33. B — 123
34. C — 5
35. B — 5 *(Alfik 2025, zad. 26)*
36. A — 6 *(Alfik 2018, zad. 27)*
37. A — 10
38. B — 2 *(Alfik 2023, zad. 9)*
39. C — 1/3
40. E — 36

## Ściąga

| Co | Sposób |
|---|---|
| Kolejność działań | nawiasy → mnożenie i dzielenie → dodawanie i odejmowanie |
| Znaki + i − | zmiana znaku nie zmienia parzystości wyniku |
| 1 + 2 + … + n | (n · (n + 1)) : 2, np. do 10: 55, do 20: 210, do 100: 5050 |
| Kilka kolejnych liczb o sumie S | środkowa = S : (ile liczb); np. 7 liczb o sumie 98 → środkowa 14 |
| Na przemian − i + | łącz w pary, każda para daje tyle samo |
| Wzorek długości k | numer miejsca : k, patrz na resztę (reszta 0 → ostatni element) |
| Ciąg „co 3” od 4 | n-ty wyraz = 4 + (n − 1) · 3 |
| Cyfry w liczbach 1–100 | 9 + 180 + 3 = 192 |
| Kwadrat magiczny 3 × 3 | suma linii = suma wszystkich liczb : 3 = 3 · (liczba w środku) |
| Część z części | ½ z ⅓ = 1/6, ⅓ z ¼ = 1/12; kolejność nie ma znaczenia |
