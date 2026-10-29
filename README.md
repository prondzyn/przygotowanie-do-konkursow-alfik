# Alfik Matematyczny, klasa 5: trening

Zadania do nauki przed Ogólnopolskim Konkursem Matematycznym **Alfik Matematyczny** dla klasy 5
szkoły podstawowej. Strona zawiera 300 oryginalnych zadań z arkuszy z lat 2015–2025 i 191 nowych
zadań w stylu Alfika. Każda odpowiedź została sprawdzona programem komputerowym.

- **[Zadania według typu](zadania-wg-typu/README.md)** to 9 działów, od kalendarza po szachownice.
  Zadania z prawdziwych arkuszy są wymieszane z nowymi i oznaczone odznaką z rokiem.
  Klikasz odpowiedź: zielona jest dobra i od razu pokazuje się rozwiązanie, czerwona jest zła
  i możesz próbować dalej.
- **[Testy przeszłe](testy-przeszle/README.md)** to 10 oryginalnych arkuszy dla klasy 5
  (2015–2025) do rozwiązania na czas, z punktacją jak na konkursie.
- **[Testy próbne](testy-probne/README.md)** to pełne arkusze: 30 zadań, 75 minut, punktacja
  jak na konkursie, razem z punktami ujemnymi.

Postęp zapisuje się w przeglądarce, osobno dla każdej strony. Przycisk u góry czyści tylko bieżącą stronę.

---

## Jak wygląda konkurs (klasa 5)

| | |
|---|---|
| Czas | **75 minut** |
| Zadania | **30**, jednokrotnego wyboru, odpowiedzi A–E |
| Punkty | zadania 1–10 po **3 pkt**, 11–20 po **4 pkt**, 21–30 po **5 pkt** (razem 120) |
| Brak odpowiedzi | 0 pkt |
| Zła odpowiedź | **minus ¼** punktów zadania (−0,75 / −1 / −1,25) |
| Termin | zwykle druga połowa listopada (2025: 20 listopada). Dokładną datę podaje szkoła i organizator na [jersz.pl](https://jersz.pl) |

### Czy zgadywać?

Policzmy dla zadania za 4 pkt. Jeśli strzelasz na ślepo spośród 5 odpowiedzi, trafiasz średnio
raz na 5 razy: +4 raz, −1 cztery razy, czyli średnio **0 pkt**. Strzelanie w ciemno nic nie daje.

Ale gdy **odrzucisz choć jedną** odpowiedź, strzał już się opłaca. Przy 4 pozostałych:
+4 raz, −1 trzy razy, średnio +¼ pkt. Przy 3 pozostałych: +4 raz, −1 dwa razy, średnio +⅔ pkt.

**Zasada:** nie zgaduj na ślepo. Jeśli umiesz skreślić choć jedną odpowiedź, zaznacz którąś z pozostałych.

### Wskazówki na sam test

1. Najpierw przejdź wszystkie zadania za 3 pkt, potem za 4 i 5. Nie utykaj na jednym zadaniu dłużej niż 4–5 minut.
2. Sprawdzaj odpowiedzi **od tyłu**: wstaw każdą opcję do treści zadania. W Alfiku często to jest najszybsza droga.
3. Rysuj! Kalendarz, kratka, drzewko możliwości, kreski zamiast kulek.
4. Uważaj na słowa „co najmniej”, „najwięcej”, „mieć pewność”, „o ile”, „ile razy”.
5. Opcja E bywa podchwytliwa („5 lub więcej”, „nie da się ustalić”). Czasem to ona jest dobra.

---

## Plan na 3 tygodnie

| Tydzień | Co robić |
|---|---|
| 1 | Działy 01–03 (kalendarz, cyfry, podzielność): po jednym dziale dziennie, potem ściąga z końca działu do zeszytu. |
| 2 | Działy 04–06 (zadania tekstowe, liczenie, logika) i **Test próbny 1** na czas. |
| 3 | Działy 07–09 (geometria, kratki, działania), **Test próbny 2**, a potem **testy przeszłe** od najnowszego: Alfik 2025, 2024, 2023… |

Po każdym teście przejrzyj zadania, w których straciłeś punkty, i wróć do ich działu.

## Oryginalne arkusze

Wszystkie arkusze dla klasy 5 z lat 2015–2025 są w zakładce [Testy przeszłe](testy-przeszle/README.md).
Oryginały w PDF są na stronie organizatora, [jersz.pl](https://jersz.pl/alfik-matematyczny/).
Arkusze i klucze są własnością organizatora konkursu (Łowcy Talentów – JERSZ).

<details><summary>Dla rodzica: jak dodać własne zadanie</summary>

Pliki z zadaniami to zwykłe pliki <code>.md</code> w katalogach <code>zadania-wg-typu</code> i <code>testy-probne</code>.
Zadanie wygląda tak (5 opcji A–E, pod nimi pole z odpowiedzią w jednej linii):

<pre>
7. Treść zadania. *(4 pkt)*
   - A) 10
   - B) 12
   - C) 14
   - D) 16
   - E) 18
   &lt;details&gt;&lt;summary&gt;rozwiązanie&lt;/summary&gt;C — 14&lt;br&gt;Wyjaśnienie.&lt;/details&gt;&lt;br&gt;
</pre>

Jeśli zmieniasz arkusz w <code>testy-przeszle</code>, najpierw uruchom <code>python narzedzia/scal_oryginaly.py</code>.
Skrypt przeniesie zmiany do działów według <code>narzedzia/klasyfikacja.json</code>.
Po zmianach uruchom <code>python zbuduj.py</code>. Skrypt złoży wszystko na nowo w plik <code>index.html</code>.
Na GitHubie nie trzeba tego robić ręcznie, bo po każdym pushu na <code>main</code> akcja „Strona” sama
przebudowuje i publikuje stronę.

</details>

<details><summary>Dla rodzica: jak uruchomić stronę na GitHub Pages</summary>

1. Wrzuć cały katalog do nowego repozytorium na GitHubie (gałąź <code>main</code>).
2. W repozytorium wejdź w <b>Settings → Pages</b> i w <b>Source</b> wybierz <b>GitHub Actions</b>.
3. Po minucie strona będzie pod adresem <code>https://&lt;login&gt;.github.io/&lt;nazwa-repozytorium&gt;/</code>.

Sam plik <code>index.html</code> działa też bez GitHuba, po dwukliku na komputerze (potrzebny internet do czcionek).

</details>
