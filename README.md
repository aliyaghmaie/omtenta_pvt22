Instruktioner
--------------

Provet pågår 13:00-17:00 onsdagen den 8e februari 2023.


1. Gör en fork av repot
2. Bjud in mig (bjornkj) som collaborator
3. Klona repot till din dator genom att använda "get from version control" i pycharm.
4. Lämna in genom att pusha de ändringar eller nya filer du gjort.
5. Det är oftast en bra ide att göra commit och push ofta, så fort du fixat någon deluppgift och programmet fungerar 
   kan du göra en commit.
6. Den sista commit/push som gjorts vid provets slut gäller, den kommer rättas och betygsättas.
7. Det är naturligtvis inte tillåtet att samarbeta med klasskamrater eller andra under provtiden.


Betyg
-----
Betyget bestäms av antalet poäng enligt följande:

| Poäng   | Betyg       |
|---------|-------------|
| 62 - 91 | Godkänt     |
| 92 -115 | Väl godkänt |
| 00 - 61 | Ej godkänt  |


Poäng (totalt 115p)
------------------
10p **Alla** funktioner, inklusive funktioner i den kod som är given har mindre än 20 rader kod.
    Kommentarer och tomma rader räknas inte.

 5p Alla funktioner har en doc-sträng alternativt en kommentar som beskriver vad funktionen gör.

10p Alla argument och returvärden till funktioner och metoder samt attribut i eventuella klasser 
    har typ angett enligt pythons type hints som vi använt oss av i kursen. ex foo(bar: int) -> str:

 5p Alla variabler följer Pythons namnkonventioner och är meningsfulla. Tänk på att se över de variabler som redan
    finns i programmet. Man skall av namnet på en variabel förstå vad den används till.
 
 5p Alla funktioner/klasser/metoder följer pythons namnkonventioner och är meningsfulla. 
    Man skall av namnet kunna förstå vad funktionen gör.

 5p Pycharm ger som mest två varningar (gula utropstecken)

10p Koden är uppdelad i 2 eller flera moduler på ett logiskt och meningsfullt sätt med vettiga namn. (Filer med enhetstester
räknas inte)

5-20p per TODO item som ni löst i koden (totalt 65 poäng)

En TODO item anses löst om:
1. Implementationen ger förväntat resultat vid körning med giltig indata.
2. Programmet inte kraschar vid testkörning.


Tips
----
1. Använd alla resurser ni kan (förutom klasskamrater eller andra personer) google, stack overflow, hjälpsidor etc.
   Detta är saker utvecklare använder hela tiden så det får ni göra på tentan också.
2. Testkör ofta. Jag testkör efter minsta kodändring jag gör. Det gör att felsökning går mycket snabbare. 
   Kraschar programmet så var det med stor sannolikhet ändringen du just gjorde som orsakade det.
3. Gör commit så fort du har löst en del av tentan. Det gör att du snabbt kan gå tillbaks till ett fungerande
   tillstånd och du förlorar inga poäng.
4. Titta igenom uppgiften innan du börjar. Se till att lösa alla uppgifter du är säker på först så att du inte missar
   lätta poäng på grund av tidsbrist.
5. Försök att bryta ner uppgifterna i mindre bitar och lös dom en i taget. Exempelvis sista uppgiften, summering av ett år
   * Ändra programmet så att det förstår kommandot summering <år>
   * Hämta alla priser det året
   * Räkna antal mottagare
   * Summera priserna
   * Skriv ut resultatet
6. Använd debugläget eller utskrifter för att förstå vad programmet gör.