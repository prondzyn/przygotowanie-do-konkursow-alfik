# Alfik: trening

Zadania do nauki przed konkursami **Alfik** (Łowcy Talentów – JERSZ). Wybierz konkurs i klasę.
Każda odpowiedź w zadaniach matematycznych została sprawdzona programem komputerowym.

<div class="menu">

## Alfik Matematyczny

- [Klasa 5](matematyczny/klasa-5/README.md) 431 zadań w 9 działach, 10 arkuszy z lat 2015–2025, 2 testy próbne

## Alfik Humanistyczny

- [Klasa 5](humanistyczny/klasa-5/README.md) wkrótce

</div>

Postęp zapisuje się w przeglądarce, osobno dla każdej strony. Przycisk u góry czyści tylko bieżącą stronę.

<details><summary>Dla rodzica: jak zbudowane są katalogi</summary>

Każda klasa ma swój katalog <code>&lt;konkurs&gt;/klasa-&lt;N&gt;/</code>, np. <code>matematyczny/klasa-5/</code>.
W środku jest <code>README.md</code> (strona startowa klasy) i dowolne z trzech podkatalogów:

<pre>
matematyczny/klasa-5/
  README.md
  zadania-wg-typu/   README.md, 01-….md, 02-….md, …
  testy-przeszle/    README.md, alfik-2015.md, alfik-2016.md, …
  testy-probne/      README.md, test-1.md, test-2.md, …
  klasyfikacja.json  (który oryginał trafia do którego działu)
</pre>

Skrypt <code>zbuduj.py</code> sam znajduje wszystkie takie katalogi. Nowa klasa albo nowy konkurs:
utwórz katalog, np. <code>humanistyczny/klasa-6/</code>, z plikiem <code>README.md</code> i dopisz link
w menu na tej stronie (w pliku <code>README.md</code> w głównym katalogu). Nowy rok: dodaj plik
<code>testy-przeszle/alfik-RRRR.md</code> i wiersz w tabeli w <code>testy-przeszle/README.md</code>.

</details>

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

Jeśli zmieniasz arkusz w <code>testy-przeszle</code>, najpierw uruchom
<code>python narzedzia/scal_oryginaly.py matematyczny/klasa-5</code>.
Skrypt przeniesie zmiany do działów według <code>klasyfikacja.json</code> z katalogu klasy.
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
