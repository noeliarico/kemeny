kemeny_to_tikz <- function(v) {
  n <- ncol(v)
  h <- ((v[1,2]+v[2,1])*(n-1))%/%2
  alt <- colnames(v)
  
  nodesrows <- paste0("(",0,",",n:1,")")
  nodesrows <- paste(paste0("\\node at ",nodesrows,"    {\\Large $",alt,"$};"), 
                collapse = "\n")
  nodescols <- paste0("(",1:n,",",n+1,")")
  nodescols <- paste(paste0("\\node at ",nodescols,"    {\\Large $",alt,"$};"), 
                  collapse = "\n")
  
  arrows <- paste(paste0("\\draw [arrow] (",n+1,",",n:1,") -- (",n+2,",",n:1,");"),
                collapse = "\n")
    
  sym <- ifelse(rowSums(v) < h, "\\xmark", "\\cmark")
  nodeadmit <- paste(paste0("\\node at (",n+3,", ",n:1,")    {\\Large $",rowSums(v),"$ ",sym,"};"),
                  collapse = "\n")
  
  e <- expand.grid(1:n, 1:n)
  pairs <- paste0("(", e$Var2, ",", n-e$Var1+1, ")")
  print(pairs)
  values <- paste(paste0("\\node at ",pairs,"    {\\Large $",as.numeric(v),"$};"),
                collapse = "\n")
  
  out <- paste0("
\\begin{scope}
  
  \\node at (0, ",n+2,".5)    {\\large \\textbf{Step xX:}};
  
  \\draw[step=1.0,black,thin,xshift=0.5cm,yshift=0.5cm] (0,0) grid (",n,", ",n,");
  \\draw[step=1.0,black,thin,xshift=0.5cm,yshift=0.5cm] (0,",n,") grid (",n,", ",n+1,");
  \\draw[step=1.0,black,thin,xshift=0.5cm,yshift=0.5cm] (-1,0) grid (0, ",n,");
  % rows \n",
  nodesrows,
  "\n\n% columns \n",
  nodescols,
  "\n\n% values \n",
  values,
  "\n\n% arrows \n",
  arrows,
  "\n\n% sum and whether it is ok \n",
  nodeadmit,
  "\n\n% Current ranking
  \\node[anchor=west,align=left] at (-1,0) {\\large Recursive call with ranking: $xX \\succ \\dots $};
  
  \\end{scope}")
  out
}

