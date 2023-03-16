- :file_folder: `agreement` to store the files that contain functions to measure the agreement among the voters
  - :page_facing_up: `margin.R` has the function `agreement_margin(om, normalize = TRUE)`
- :file_folder: `creation`
  - permute_om has a function of the same name that given an outranking matrix and two candidates permutes their position in the matrix
- :file_folder: `experiments`
- :file_folder: `kemeny`
- :file_folder: `languages` has code to export from R to Latex and Python
  - :page_facing_up: `kemeny_to_tikz.R`
  - :page_facing_up: `to_python.R` has the functions:
    - `to_python_ranking(ranking, name = "r")` gives the python code to create
    the `ranking` using numpy. `name` is the name of the variable using on python.
    - `to_python_om(matix, name = "om")` gives the python code to create
    the outranking matrix `matrix` using numpy. `name` is the name of the variable using to store the outranking matrix on python.
    
    
# Carpeta `ejor`

- `0.setup`
- `1.function_create_profiles`
- `2.function_create_scripts`
- `3.create_profiles_of_scripts`
- `4.load_profiles`
- `5.add_scripts`


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

- `kemenyAzzini1()` implementation described in the paper adding the consideration of 
- `kemenyAzzini2()` adds check of Condorcet winner at the beginning
- `kemenyAzzini3()` adds check of Condorcer winner recursively

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

## Uncertanty: Measuring the agreement among the voters

### u1: lower bound to the optimal cost



### u2: upper bound to the optimal 

### u3: uniformity

### u4: intransitivity

### u5: average rank entropy

### u6: average rank variance

### u7: borda score

### u8: sum of the absolute majorities


### u9: ponderated beta


