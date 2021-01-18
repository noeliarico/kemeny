# Algorithms

Algorithms for computing Kemeny winning ranking
 
**DFS branch and bound algorithms pruning the branches using a distance bound**

- `kemenyDFS0()` explores all the search space
- `kemenyDFS1()` extended version of the kemeny1 algorithm that receives the distance
  - Check worst, Borda Count (EUSFLAT)
  - Check Tideman (does it guarantee always the min distance?)

**Complementary rankings**

- `kemenyCR1()` introducing the concept of complementary rankings to reduce the search space explored

**A* **

- `kemenyA1()` sorting the candidates according to the value of their prefix
Ponderation using the number of candidates that have been already added to the prefix?

**Azzini**

- `kemenyAzzini1()` implementation described in the paper
- `kemenyAzzini2()` adds check of Condorcet ranking at the beginning and consideration of matrix 2x2 when both elements are equal
- `kemenyAzzini3()` extends kemenyAzzini2 including Condorcet winner
- `kemenyAzzini4()` extends kemenyAzzini3 including Condorcet ranking in the recursive call
- `kemenyAzzini5()` extends kemenyAzzini4 adding distance bound



# Papers

# Revistas

| Journal | operations research & management science | CS |
|---------|-----|----|
| EUROPEAN JOURNAL OF OPERATIONAL RESEARCH      | 0   | 0  |
| 0       | 0   | 0  |
| 0       | 0   | 0  |

Parallel computing - Elsevier - Q3 Computing Science, theory & methods
International journal of parallel programming - Elsevier - Q3 Computing Science, theory & methods
JOURNAL OF PARALLEL AND DISTRIBUTED COMPUTING - Q2 Computer Science, theory & methods

EUROPEAN JOURNAL OF OPERATIONAL RESEARCH - Q1 operations research & management science



