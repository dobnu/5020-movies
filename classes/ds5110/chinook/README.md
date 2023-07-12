# Homework 1
## Question 1
###Results
```
   InvoiceId  MAX(Total)
0        404       25.86
```
```
    TrackId  UnitPrice
0      2814       0.99
1      2823       1.99
2      2832       1.99
3      2841       1.99
4      2850       1.99
5      2859       1.99
6      2868       1.99
7      2877       1.99
8      2886       1.99
9      2895       1.99
10     2904       1.99
11     2913       1.99
12     2922       1.99
13     2931       0.99
```
```
                                       Name
0                                Insensível
1                             Collaborators
2                            The Woman King
3                            One Giant Leap
4                                   The Fix
5   Man of Science, Man of Faith (Premiere)
6                                 Walkabout
7                                  The Moth
8                Stranger In a Strange Land
9                                 Par Avion
10                                  Outlaws
11                          Deus Ex Machina
12          Live Together, Die Alone, Pt. 1
13                                 So Cruel
```
### Analysis
## Question 2
![](img/fig2.png)
### Analysis
I am convinced this question is worded wrong/impossible and is the main reason this homework is being turned in so late there is not artist country and all tracks have only 1 or 2 invoices so there is no difference in popularity.
## Question 3
```
                                       Name
0                                Insensível
1                             Collaborators
2                            The Woman King
3                            One Giant Leap
4                                   The Fix
5   Man of Science, Man of Faith (Premiere)
6                                 Walkabout
7                                  The Moth
8                Stranger In a Strange Land
9                                 Par Avion
10                                  Outlaws
11                          Deus Ex Machina
12          Live Together, Die Alone, Pt. 1
13                                 So Cruel
```
```
   COUNT( DISTINCT Composer)
0                         27
```
## Histogram
### Analysis
![](img/fig1.png)
In this we see that life expectancy does not fit the normal curve rather looking like a saddle with a high density around 40 and higher densisty around 70. This is kind of to be expected as we have shown the positive realtionship between gdp per capita and expected life expectency and expected gdp is not uniformally distrubuted. So it is expected there will be a higher expected life for those who participate in the global economy and those who don't.
## Reproduce
### Data
data is from https://github.com/jennybc/gapminder/blob/main/inst/extdata/gapminder.tsv and can be imported using the command
```
make data
```
### Figures
you can reproduce the figures by doing a make command followed by fig#. An Example to produce figure 1
```
make fig1
```
This must be done after make data and making the repo clean
### Clean
to clean type
```
make clean

