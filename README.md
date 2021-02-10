- :file_folder: `agreement` to store the files that contain functions to measure the agreement among the voters
  - :page_facing_up: `margin.R` has the function `agreement_margin(om, normalize = TRUE)`
- :file_folder: `creation`
- :file_folder: `kemeny`
- :file_folder: `languages` has code to export from R to Latex and Python
  - :page_facing_up: `kemeny_to_tikz.R`
  - :page_facing_up: `to_python.R` has the functions:
    - `to_python_ranking(ranking, name = "r")` gives the python code to create
    the `ranking` using numpy. `name` is the name of the variable using on python.
    - `to_python_om(matix, name = "om")` gives the python code to create
    the outranking matrix `matrix` using numpy. `name` is the name of the variable using to store the outranking matrix on python.



# Algorithms

Algorithms for computing Kemeny winning ranking
 
**DFS branch and bound algorithms pruning the branches using a distance bound**

- `kemenyDFS0()` explores all the search space
- `kemenyDFS1()` extended version of the kemeny1 algorithm that receives the distance
  - Check worst, Borda Count (EUSFLAT)
  - Check Tideman (does it guarantee always the min distance?)
  
  Example for the paper
  
```r
p <- parse_profile_of_rankings(
"3, a_4 > a_2 > a_1 > a_3,
 4, a_3 > a_4 > a_2 > a_1,
 2, a_4 > a_1 > a_2 > a_3,
 1, a_1 > a_2 > a_3 > a_4"
)
```


**Complementary rankings**

- `kemenyCR1()` introducing the concept of complementary rankings to reduce the search space explored

**A* **

- `kemenyA1()` sorting the candidates according to the value of their prefix
Ponderation using the number of candidates that have been already added to the prefix?

**Azzini**

- `kemenyAzzini1()` implementation described in the paper
- `kemenyAzzini2()` adds check of Condorcet ranking at the beginning and consideration of matrix 2x2 when both elements are equal
- `kemenyAzzini3()` extends `kemenyAzzini2()` including Condorcet winner
- `kemenyAzzini4()` extends `kemenyAzzini3()` including Condorcet ranking in the recursive call
- `kemenyAzzini5()` extends `kemenyAzzini4()` adding distance bound

# Python package:

- azzinimunda
- benchmark
- dfs
- scf

# Further research:

## DFS

### Linear extension

For the vast majority of the profile of rankings when the Kemeny method yields to more than one winning ranking, at least one of those rankings is a linear extension of the 

This does not happen always, for example:

```
p1 <- parse_profile_of_rankings("2, F>G>D>A>B>C>E,
                                 2, F>G>E>A>B>C>D,
                                 1, F>G>C>D>E>A>B,
                                 2, G>F>D>A>B>C>E,
                                 2, G>F>E>A>B>C>D,
                                 1, G>F>C>D>E>A>B")
tideman(p1)
kemeny(p1)
```

### Ranked pairs (Tideman)

Does the tideman method always give the minimum Kemeny distance that can be obtained. It is necessary to study the majority relationship of the margin.

For all of the profiles of rankings that I have checked this is the case but probably it is not for some exceptions.

Even if it is not the case this can be a good heuristic for a directed search.

## Agreement among the voters

Relationship among the number of alterntives which rowsum >= colsum and the agreement among the voters.


