test_that("d1", {
  
  roots <- real.roots(1, 7, 12)
  
  expect_that( roots, is_a("numeric") )
  expect_that( length(roots), equals(2) )
  expect_that( roots[1] < roots[2], is_true() )
})

por <- parse_profile_of_rankings("
3, b > d > a > c,
5, c > a > d > b,
2, a > c > b > d
")

3, C3 ≻ C1 ≻ C2 ≻ C4,
4, C2 ≻ C4 ≻ C3 ≻ C1,
3, C4 ≻ C1 ≻ C2 ≻ C3

