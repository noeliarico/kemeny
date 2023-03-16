kemeny_to_tikz <- function(por) {
  
  v <- votrix(por)
  candidates <- por$candidates
  
  v1 <- colSums(v)
  
  out <- paste0("

\\resizebox{\\textwidth}{!}{%
  \\begin{tikzpicture}
    %\\draw[step=1.0,black,thin,xshift=0.5cm,yshift=0.5cm] (0,0) grid (10, 12);
  
    \\pgfmathtruncatemacro{\\xdist}{2}
    \\pgfmathtruncatemacro{\\xdistt}{3}
    
    \\node (1) at (0, 10.75)    {$",candidates[1],"$ (",v1[1],")};
    \\node (2) at (0, 7.75)     {$",candidates[2],"$ (",v1[2],")};
    \\node (3) at (0, 4.75)     {$",candidates[3],"$ (",v1[3],")};
    \\node (4) at (0, 1.75)     {$",candidates[4],"$ (",v1[4],")};
    
    \\node (43) at (\\xdist, .75+0)     {$",candidates[4]," \\succ ",candidates[3],"$ (", sum(v[-c(4), 3]) + v1[4], ")};
    \\node (42) at (\\xdist, .75+1)     {$",candidates[4]," \\succ ",candidates[2],"$ (", sum(v[-c(4), 2]) + v1[4], ")};
    \\node (41) at (\\xdist, .75+2)     {$",candidates[4]," \\succ ",candidates[1],"$ (", sum(v[-c(4), 1]) + v1[4], ")};
    \\node (34) at (\\xdist, .75+3)     {$",candidates[3]," \\succ ",candidates[4],"$ (", sum(v[-c(3), 4]) + v1[3], ")};
    \\node (32) at (\\xdist, .75+4)     {$",candidates[3]," \\succ ",candidates[2],"$ (", sum(v[-c(3), 2]) + v1[3], ")};
    \\node (31) at (\\xdist, .75+5)     {$",candidates[3]," \\succ ",candidates[1],"$ (", sum(v[-c(3), 1]) + v1[3], ")};
    \\node (24) at (\\xdist, .75+6)     {$",candidates[2]," \\succ ",candidates[4],"$ (", sum(v[-c(2), 4]) + v1[2], ")};
    \\node (23) at (\\xdist, .75+7)     {$",candidates[2]," \\succ ",candidates[3],"$ (", sum(v[-c(2), 3]) + v1[2], ")};
    \\node (21) at (\\xdist, .75+8)     {$",candidates[2]," \\succ ",candidates[1],"$ (", sum(v[-c(2), 1]) + v1[2], ")};
    \\node (14) at (\\xdist, .75+9)     {$",candidates[1]," \\succ ",candidates[4],"$ (", sum(v[-c(1), 4]) + v1[1], ")};
    \\node (13) at (\\xdist, .75+10)    {$",candidates[1]," \\succ ",candidates[3],"$ (", sum(v[-c(1), 3]) + v1[1], ")};
    \\node (12) at (\\xdist, .75+11)    {$",candidates[1]," \\succ ",candidates[2],"$ (", sum(v[-c(1), 2]) + v1[1], ")};
    
    \\node (432) at (\\xdist+\\xdistt, .5+.5*0)         {$",candidates[4]," \\succ ",candidates[3]," \\succ ",candidates[2],"$ (", sum(v[-c(4, 3), 2]) + sum(v[-c(4), 3]) + v1[4], ") };
    \\node (431) at (\\xdist+\\xdistt, .5+.5*1)         {$",candidates[4]," \\succ ",candidates[3]," \\succ ",candidates[1],"$ (", sum(v[-c(4, 3), 1]) + sum(v[-c(4), 3]) + v1[4], ") };
    \\node (423) at (\\xdist+\\xdistt, .5+.5*2)         {$",candidates[4]," \\succ ",candidates[2]," \\succ ",candidates[3],"$ (", sum(v[-c(4, 2), 3]) + sum(v[-c(4), 2]) + v1[4], ") };
    \\node (421) at (\\xdist+\\xdistt, .5+.5*3)         {$",candidates[4]," \\succ ",candidates[2]," \\succ ",candidates[1],"$ (", sum(v[-c(4, 2), 1]) + sum(v[-c(4), 2]) + v1[4], ") };
    \\node (413) at (\\xdist+\\xdistt, .5+.5*4)         {$",candidates[4]," \\succ ",candidates[1]," \\succ ",candidates[3],"$ (", sum(v[-c(4, 1), 3]) + sum(v[-c(4), 1]) + v1[4], ") };
    \\node (412) at (\\xdist+\\xdistt, .5+.5*5)         {$",candidates[4]," \\succ ",candidates[1]," \\succ ",candidates[2],"$ (", sum(v[-c(4, 1), 2]) + sum(v[-c(4), 1]) + v1[4], ") };
    \\node (342) at (\\xdist+\\xdistt, .5+.5*6)         {$",candidates[3]," \\succ ",candidates[4]," \\succ ",candidates[2],"$ (", sum(v[-c(3, 4), 2]) + sum(v[-c(3), 4]) + v1[3], ") };
    \\node (341) at (\\xdist+\\xdistt, .5+.5*7)         {$",candidates[3]," \\succ ",candidates[4]," \\succ ",candidates[1],"$ (", sum(v[-c(3, 4), 1]) + sum(v[-c(3), 4]) + v1[3], ") };
    \\node (324) at (\\xdist+\\xdistt, .5+.5*8)         {$",candidates[3]," \\succ ",candidates[2]," \\succ ",candidates[4],"$ (", sum(v[-c(3, 2), 4]) + sum(v[-c(3), 2]) + v1[3], ") };
    \\node (321) at (\\xdist+\\xdistt, .5+.5*9)         {$",candidates[3]," \\succ ",candidates[2]," \\succ ",candidates[1],"$ (", sum(v[-c(3, 2), 1]) + sum(v[-c(3), 2]) + v1[3], ") };
    \\node (314) at (\\xdist+\\xdistt, .5+.5*10)        {$",candidates[3]," \\succ ",candidates[1]," \\succ ",candidates[4],"$ (", sum(v[-c(3, 1), 4]) + sum(v[-c(3), 1]) + v1[3], ") };
    \\node (312) at (\\xdist+\\xdistt, .5+.5*11)        {$",candidates[3]," \\succ ",candidates[1]," \\succ ",candidates[2],"$ (", sum(v[-c(3, 1), 2]) + sum(v[-c(3), 1]) + v1[3], ") };
    \\node (243) at (\\xdist+\\xdistt, .5+.5*12)        {$",candidates[2]," \\succ ",candidates[4]," \\succ ",candidates[3],"$ (", sum(v[-c(2, 4), 3]) + sum(v[-c(2), 4]) + v1[2], ") };
    \\node (241) at (\\xdist+\\xdistt, .5+.5*13)        {$",candidates[2]," \\succ ",candidates[4]," \\succ ",candidates[1],"$ (", sum(v[-c(2, 4), 1]) + sum(v[-c(2), 4]) + v1[2], ") };
    \\node (234) at (\\xdist+\\xdistt, .5+.5*14)        {$",candidates[2]," \\succ ",candidates[3]," \\succ ",candidates[4],"$ (", sum(v[-c(2, 3), 4]) + sum(v[-c(2), 3]) + v1[2], ") };
    \\node (231) at (\\xdist+\\xdistt, .5+.5*15)        {$",candidates[2]," \\succ ",candidates[3]," \\succ ",candidates[1],"$ (", sum(v[-c(2, 3), 1]) + sum(v[-c(2), 3]) + v1[2], ") };
    \\node (214) at (\\xdist+\\xdistt, .5+.5*16)        {$",candidates[2]," \\succ ",candidates[1]," \\succ ",candidates[4],"$ (", sum(v[-c(2, 1), 4]) + sum(v[-c(2), 1]) + v1[2], ") };
    \\node (213) at (\\xdist+\\xdistt, .5+.5*17)        {$",candidates[2]," \\succ ",candidates[1]," \\succ ",candidates[3],"$ (", sum(v[-c(2, 1), 3]) + sum(v[-c(2), 1]) + v1[2], ") };
    \\node (143) at (\\xdist+\\xdistt, .5+.5*18)        {$",candidates[1]," \\succ ",candidates[4]," \\succ ",candidates[3],"$ (", sum(v[-c(1, 4), 3]) + sum(v[-c(1), 4]) + v1[1], ") };
    \\node (142) at (\\xdist+\\xdistt, .5+.5*19)        {$",candidates[1]," \\succ ",candidates[4]," \\succ ",candidates[2],"$ (", sum(v[-c(1, 4), 2]) + sum(v[-c(1), 4]) + v1[1], ") };
    \\node (134) at (\\xdist+\\xdistt, .5+.5*20)        {$",candidates[1]," \\succ ",candidates[3]," \\succ ",candidates[4],"$ (", sum(v[-c(1, 3), 4]) + sum(v[-c(1), 3]) + v1[1], ") };
    \\node (132) at (\\xdist+\\xdistt, .5+.5*21)        {$",candidates[1]," \\succ ",candidates[3]," \\succ ",candidates[2],"$ (", sum(v[-c(1, 3), 2]) + sum(v[-c(1), 3]) + v1[1], ") };
    \\node (124) at (\\xdist+\\xdistt, .5+.5*22)        {$",candidates[1]," \\succ ",candidates[2]," \\succ ",candidates[4],"$ (", sum(v[-c(1, 2), 4]) + sum(v[-c(1), 2]) + v1[1], ") };
    \\node (123) at (\\xdist+\\xdistt, .5+.5*23)        {$",candidates[1]," \\succ ",candidates[2]," \\succ ",candidates[3],"$ (", sum(v[-c(1, 2), 3]) + sum(v[-c(1), 2]) + v1[1], ") };
    
    \\node (432b) at (\\xdist+1+3*\\xdist, .5+.5*0)         {$",candidates[4]," \\succ ",candidates[3]," \\succ ",candidates[2]," \\succ ",candidates[1],"$};
    \\node (431b) at (\\xdist+1+3*\\xdist, .5+.5*1)         {$",candidates[4]," \\succ ",candidates[3]," \\succ ",candidates[1]," \\succ ",candidates[2],"$};
    \\node (423b) at (\\xdist+1+3*\\xdist, .5+.5*2)         {$",candidates[4]," \\succ ",candidates[2]," \\succ ",candidates[3]," \\succ ",candidates[1],"$};
    \\node (421b) at (\\xdist+1+3*\\xdist, .5+.5*3)         {$",candidates[4]," \\succ ",candidates[2]," \\succ ",candidates[1]," \\succ ",candidates[3],"$};
    \\node (413b) at (\\xdist+1+3*\\xdist, .5+.5*4)         {$",candidates[4]," \\succ ",candidates[1]," \\succ ",candidates[3]," \\succ ",candidates[2],"$};
    \\node (412b) at (\\xdist+1+3*\\xdist, .5+.5*5)         {$",candidates[4]," \\succ ",candidates[1]," \\succ ",candidates[2]," \\succ ",candidates[3],"$};
    \\node (342b) at (\\xdist+1+3*\\xdist, .5+.5*6)         {$",candidates[3]," \\succ ",candidates[4]," \\succ ",candidates[2]," \\succ ",candidates[1],"$};
    \\node (341b) at (\\xdist+1+3*\\xdist, .5+.5*7)         {$",candidates[3]," \\succ ",candidates[4]," \\succ ",candidates[1]," \\succ ",candidates[2],"$};
    \\node (324b) at (\\xdist+1+3*\\xdist, .5+.5*8)         {$",candidates[3]," \\succ ",candidates[2]," \\succ ",candidates[4]," \\succ ",candidates[1],"$};
    \\node (321b) at (\\xdist+1+3*\\xdist, .5+.5*9)         {$",candidates[3]," \\succ ",candidates[2]," \\succ ",candidates[1]," \\succ ",candidates[4],"$};
    \\node (314b) at (\\xdist+1+3*\\xdist, .5+.5*10)        {$",candidates[3]," \\succ ",candidates[1]," \\succ ",candidates[4]," \\succ ",candidates[2],"$};
    \\node (312b) at (\\xdist+1+3*\\xdist, .5+.5*11)        {$",candidates[3]," \\succ ",candidates[1]," \\succ ",candidates[2]," \\succ ",candidates[4],"$};
    \\node (243b) at (\\xdist+1+3*\\xdist, .5+.5*12)        {$",candidates[2]," \\succ ",candidates[4]," \\succ ",candidates[3]," \\succ ",candidates[1],"$};
    \\node (241b) at (\\xdist+1+3*\\xdist, .5+.5*13)        {$",candidates[2]," \\succ ",candidates[4]," \\succ ",candidates[1]," \\succ ",candidates[3],"$};
    \\node (234b) at (\\xdist+1+3*\\xdist, .5+.5*14)        {$",candidates[2]," \\succ ",candidates[3]," \\succ ",candidates[4]," \\succ ",candidates[1],"$};
    \\node (231b) at (\\xdist+1+3*\\xdist, .5+.5*15)        {$",candidates[2]," \\succ ",candidates[3]," \\succ ",candidates[1]," \\succ ",candidates[4],"$};
    \\node (214b) at (\\xdist+1+3*\\xdist, .5+.5*16)        {$",candidates[2]," \\succ ",candidates[1]," \\succ ",candidates[4]," \\succ ",candidates[3],"$};
    \\node (213b) at (\\xdist+1+3*\\xdist, .5+.5*17)        {$",candidates[2]," \\succ ",candidates[1]," \\succ ",candidates[3]," \\succ ",candidates[4],"$};
    \\node (143b) at (\\xdist+1+3*\\xdist, .5+.5*18)        {$",candidates[1]," \\succ ",candidates[4]," \\succ ",candidates[3]," \\succ ",candidates[2],"$};
    \\node (142b) at (\\xdist+1+3*\\xdist, .5+.5*19)        {$",candidates[1]," \\succ ",candidates[4]," \\succ ",candidates[2]," \\succ ",candidates[3],"$};
    \\node (134b) at (\\xdist+1+3*\\xdist, .5+.5*20)        {$",candidates[1]," \\succ ",candidates[3]," \\succ ",candidates[4]," \\succ ",candidates[2],"$};
    \\node (132b) at (\\xdist+1+3*\\xdist, .5+.5*21)        {$",candidates[1]," \\succ ",candidates[3]," \\succ ",candidates[2]," \\succ ",candidates[4],"$};
    \\node (124b) at (\\xdist+1+3*\\xdist, .5+.5*22)        {$",candidates[1]," \\succ ",candidates[2]," \\succ ",candidates[4]," \\succ ",candidates[3],"$};
    \\node (123b) at (\\xdist+1+3*\\xdist, .5+.5*23)        {$",candidates[1]," \\succ ",candidates[2]," \\succ ",candidates[3]," \\succ ",candidates[4],"$};

    % first level
    \\draw [->] (1) edge (12.west);
    \\draw [->] (1) edge (13.west);
    \\draw [->] (1) edge (14.west);
    \\draw [->] (2) edge (21.west);
    \\draw [->] (2) edge (23.west);
    \\draw [->] (2) edge (24.west);
    \\draw [->] (3) edge (31.west);
    \\draw [->] (3) edge (32.west);
    \\draw [->] (3) edge (34.west);
    \\draw [->] (4) edge (41.west);
    \\draw [->] (4) edge (42.west);
    \\draw [->] (4) edge (43.west);
    
    % second level
    \\draw [->] (12) edge (123);
    \\draw [->] (12) edge (124);
    \\draw [->] (13) edge (132);
    \\draw [->] (13) edge (134);
    \\draw [->] (14) edge (142);
    \\draw [->] (14) edge (143);
    \\draw [->] (21) edge (213);
    \\draw [->] (21) edge (214);
    \\draw [->] (23) edge (231);
    \\draw [->] (23) edge (234);
    \\draw [->] (24) edge (241);
    \\draw [->] (24) edge (243);
    \\draw [->] (31) edge (312);
    \\draw [->] (31) edge (314);
    \\draw [->] (32) edge (321);
    \\draw [->] (32) edge (324);
    \\draw [->] (34) edge (341);
    \\draw [->] (34) edge (342);
    \\draw [->] (41) edge (412);
    \\draw [->] (41) edge (413);
    \\draw [->] (42) edge (421);
    \\draw [->] (42) edge (423);
    \\draw [->] (43) edge (431);
    \\draw [->] (43) edge (432);
    
     % third level
    \\draw [->] (432) edge (432b);
    \\draw [->] (431) edge (431b);
    \\draw [->] (423) edge (423b);
    \\draw [->] (421) edge (421b);
    \\draw [->] (413) edge (413b);
    \\draw [->] (412) edge (412b);
    \\draw [->] (342) edge (342b);
    \\draw [->] (341) edge (341b);
    \\draw [->] (324) edge (324b);
    \\draw [->] (321) edge (321b);
    \\draw [->] (314) edge (314b);
    \\draw [->] (312) edge (312b);
    \\draw [->] (243) edge (243b);
    \\draw [->] (241) edge (241b);
    \\draw [->] (234) edge (234b);
    \\draw [->] (231) edge (231b);
    \\draw [->] (214) edge (214b);
    \\draw [->] (213) edge (213b);
    \\draw [->] (143) edge (143b);
    \\draw [->] (142) edge (142b);
    \\draw [->] (134) edge (134b);
    \\draw [->] (132) edge (132b);
    \\draw [->] (124) edge (124b);
    \\draw [->] (123) edge (123b);

\\end{tikzpicture}
}%
         
  ")
  out
}


kemeny_to_tikz_5 <- function(por) {
  
  v <- votrix(por)
  candidates <- por$candidates
  
  v1 <- colSums(v)
  
  out <- paste0("

\\resizebox{\\textwidth}{!}{%
  \\begin{tikzpicture}
    %\\draw[step=1.0,black,thin,xshift=0.5cm,yshift=0.5cm] (0,0) grid (10, 12);
  
    \\pgfmathtruncatemacro{\\xdist}{2}
    \\pgfmathtruncatemacro{\\xdistt}{3}
    
    \\node (1) at (0, 10.75)    {$",candidates[1],"$ (",v1[1],")};
    \\node (2) at (0, 7.75)     {$",candidates[2],"$ (",v1[2],")};
    \\node (3) at (0, 4.75)     {$",candidates[3],"$ (",v1[3],")};
    \\node (4) at (0, 1.75)     {$",candidates[4],"$ (",v1[4],")};
    
    \\node (43) at (\\xdist, .75+0)     {$",candidates[4]," \\succ ",candidates[3],"$ (", sum(v[-c(4), 3]) + v1[4], ")};
    \\node (42) at (\\xdist, .75+1)     {$",candidates[4]," \\succ ",candidates[2],"$ (", sum(v[-c(4), 2]) + v1[4], ")};
    \\node (41) at (\\xdist, .75+2)     {$",candidates[4]," \\succ ",candidates[1],"$ (", sum(v[-c(4), 1]) + v1[4], ")};
    \\node (34) at (\\xdist, .75+3)     {$",candidates[3]," \\succ ",candidates[4],"$ (", sum(v[-c(3), 4]) + v1[3], ")};
    \\node (32) at (\\xdist, .75+4)     {$",candidates[3]," \\succ ",candidates[2],"$ (", sum(v[-c(3), 2]) + v1[3], ")};
    \\node (31) at (\\xdist, .75+5)     {$",candidates[3]," \\succ ",candidates[1],"$ (", sum(v[-c(3), 1]) + v1[3], ")};
    \\node (24) at (\\xdist, .75+6)     {$",candidates[2]," \\succ ",candidates[4],"$ (", sum(v[-c(2), 4]) + v1[2], ")};
    \\node (23) at (\\xdist, .75+7)     {$",candidates[2]," \\succ ",candidates[3],"$ (", sum(v[-c(2), 3]) + v1[2], ")};
    \\node (21) at (\\xdist, .75+8)     {$",candidates[2]," \\succ ",candidates[1],"$ (", sum(v[-c(2), 1]) + v1[2], ")};
    \\node (14) at (\\xdist, .75+9)     {$",candidates[1]," \\succ ",candidates[4],"$ (", sum(v[-c(1), 4]) + v1[1], ")};
    \\node (13) at (\\xdist, .75+10)    {$",candidates[1]," \\succ ",candidates[3],"$ (", sum(v[-c(1), 3]) + v1[1], ")};
    \\node (12) at (\\xdist, .75+11)    {$",candidates[1]," \\succ ",candidates[2],"$ (", sum(v[-c(1), 2]) + v1[1], ")};
    
    \\node (432) at (\\xdist+\\xdistt, .5+.5*0)         {$",candidates[4]," \\succ ",candidates[3]," \\succ ",candidates[2],"$ (", sum(v[-c(4, 3), 2]) + sum(v[-c(4), 3]) + v1[4], ") };
    \\node (431) at (\\xdist+\\xdistt, .5+.5*1)         {$",candidates[4]," \\succ ",candidates[3]," \\succ ",candidates[1],"$ (", sum(v[-c(4, 3), 1]) + sum(v[-c(4), 3]) + v1[4], ") };
    \\node (423) at (\\xdist+\\xdistt, .5+.5*2)         {$",candidates[4]," \\succ ",candidates[2]," \\succ ",candidates[3],"$ (", sum(v[-c(4, 2), 3]) + sum(v[-c(4), 2]) + v1[4], ") };
    \\node (421) at (\\xdist+\\xdistt, .5+.5*3)         {$",candidates[4]," \\succ ",candidates[2]," \\succ ",candidates[1],"$ (", sum(v[-c(4, 2), 1]) + sum(v[-c(4), 2]) + v1[4], ") };
    \\node (413) at (\\xdist+\\xdistt, .5+.5*4)         {$",candidates[4]," \\succ ",candidates[1]," \\succ ",candidates[3],"$ (", sum(v[-c(4, 1), 3]) + sum(v[-c(4), 1]) + v1[4], ") };
    \\node (412) at (\\xdist+\\xdistt, .5+.5*5)         {$",candidates[4]," \\succ ",candidates[1]," \\succ ",candidates[2],"$ (", sum(v[-c(4, 1), 2]) + sum(v[-c(4), 1]) + v1[4], ") };
    \\node (342) at (\\xdist+\\xdistt, .5+.5*6)         {$",candidates[3]," \\succ ",candidates[4]," \\succ ",candidates[2],"$ (", sum(v[-c(3, 4), 2]) + sum(v[-c(3), 4]) + v1[3], ") };
    \\node (341) at (\\xdist+\\xdistt, .5+.5*7)         {$",candidates[3]," \\succ ",candidates[4]," \\succ ",candidates[1],"$ (", sum(v[-c(3, 4), 1]) + sum(v[-c(3), 4]) + v1[3], ") };
    \\node (324) at (\\xdist+\\xdistt, .5+.5*8)         {$",candidates[3]," \\succ ",candidates[2]," \\succ ",candidates[4],"$ (", sum(v[-c(3, 2), 4]) + sum(v[-c(3), 2]) + v1[3], ") };
    \\node (321) at (\\xdist+\\xdistt, .5+.5*9)         {$",candidates[3]," \\succ ",candidates[2]," \\succ ",candidates[1],"$ (", sum(v[-c(3, 2), 1]) + sum(v[-c(3), 2]) + v1[3], ") };
    \\node (314) at (\\xdist+\\xdistt, .5+.5*10)        {$",candidates[3]," \\succ ",candidates[1]," \\succ ",candidates[4],"$ (", sum(v[-c(3, 1), 4]) + sum(v[-c(3), 1]) + v1[3], ") };
    \\node (312) at (\\xdist+\\xdistt, .5+.5*11)        {$",candidates[3]," \\succ ",candidates[1]," \\succ ",candidates[2],"$ (", sum(v[-c(3, 1), 2]) + sum(v[-c(3), 1]) + v1[3], ") };
    \\node (243) at (\\xdist+\\xdistt, .5+.5*12)        {$",candidates[2]," \\succ ",candidates[4]," \\succ ",candidates[3],"$ (", sum(v[-c(2, 4), 3]) + sum(v[-c(2), 4]) + v1[2], ") };
    \\node (241) at (\\xdist+\\xdistt, .5+.5*13)        {$",candidates[2]," \\succ ",candidates[4]," \\succ ",candidates[1],"$ (", sum(v[-c(2, 4), 1]) + sum(v[-c(2), 4]) + v1[2], ") };
    \\node (234) at (\\xdist+\\xdistt, .5+.5*14)        {$",candidates[2]," \\succ ",candidates[3]," \\succ ",candidates[4],"$ (", sum(v[-c(2, 3), 4]) + sum(v[-c(2), 3]) + v1[2], ") };
    \\node (231) at (\\xdist+\\xdistt, .5+.5*15)        {$",candidates[2]," \\succ ",candidates[3]," \\succ ",candidates[1],"$ (", sum(v[-c(2, 3), 1]) + sum(v[-c(2), 3]) + v1[2], ") };
    \\node (214) at (\\xdist+\\xdistt, .5+.5*16)        {$",candidates[2]," \\succ ",candidates[1]," \\succ ",candidates[4],"$ (", sum(v[-c(2, 1), 4]) + sum(v[-c(2), 1]) + v1[2], ") };
    \\node (213) at (\\xdist+\\xdistt, .5+.5*17)        {$",candidates[2]," \\succ ",candidates[1]," \\succ ",candidates[3],"$ (", sum(v[-c(2, 1), 3]) + sum(v[-c(2), 1]) + v1[2], ") };
    \\node (143) at (\\xdist+\\xdistt, .5+.5*18)        {$",candidates[1]," \\succ ",candidates[4]," \\succ ",candidates[3],"$ (", sum(v[-c(1, 4), 3]) + sum(v[-c(1), 4]) + v1[1], ") };
    \\node (142) at (\\xdist+\\xdistt, .5+.5*19)        {$",candidates[1]," \\succ ",candidates[4]," \\succ ",candidates[2],"$ (", sum(v[-c(1, 4), 2]) + sum(v[-c(1), 4]) + v1[1], ") };
    \\node (134) at (\\xdist+\\xdistt, .5+.5*20)        {$",candidates[1]," \\succ ",candidates[3]," \\succ ",candidates[4],"$ (", sum(v[-c(1, 3), 4]) + sum(v[-c(1), 3]) + v1[1], ") };
    \\node (132) at (\\xdist+\\xdistt, .5+.5*21)        {$",candidates[1]," \\succ ",candidates[3]," \\succ ",candidates[2],"$ (", sum(v[-c(1, 3), 2]) + sum(v[-c(1), 3]) + v1[1], ") };
    \\node (124) at (\\xdist+\\xdistt, .5+.5*22)        {$",candidates[1]," \\succ ",candidates[2]," \\succ ",candidates[4],"$ (", sum(v[-c(1, 2), 4]) + sum(v[-c(1), 2]) + v1[1], ") };
    \\node (123) at (\\xdist+\\xdistt, .5+.5*23)        {$",candidates[1]," \\succ ",candidates[2]," \\succ ",candidates[3],"$ (", sum(v[-c(1, 2), 3]) + sum(v[-c(1), 2]) + v1[1], ") };
    
    \\node (432b) at (\\xdist+1+3*\\xdist, .5+.5*0)         {$",candidates[4]," \\succ ",candidates[3]," \\succ ",candidates[2]," \\succ ",candidates[1],"$};
    \\node (431b) at (\\xdist+1+3*\\xdist, .5+.5*1)         {$",candidates[4]," \\succ ",candidates[3]," \\succ ",candidates[1]," \\succ ",candidates[2],"$};
    \\node (423b) at (\\xdist+1+3*\\xdist, .5+.5*2)         {$",candidates[4]," \\succ ",candidates[2]," \\succ ",candidates[3]," \\succ ",candidates[1],"$};
    \\node (421b) at (\\xdist+1+3*\\xdist, .5+.5*3)         {$",candidates[4]," \\succ ",candidates[2]," \\succ ",candidates[1]," \\succ ",candidates[3],"$};
    \\node (413b) at (\\xdist+1+3*\\xdist, .5+.5*4)         {$",candidates[4]," \\succ ",candidates[1]," \\succ ",candidates[3]," \\succ ",candidates[2],"$};
    \\node (412b) at (\\xdist+1+3*\\xdist, .5+.5*5)         {$",candidates[4]," \\succ ",candidates[1]," \\succ ",candidates[2]," \\succ ",candidates[3],"$};
    \\node (342b) at (\\xdist+1+3*\\xdist, .5+.5*6)         {$",candidates[3]," \\succ ",candidates[4]," \\succ ",candidates[2]," \\succ ",candidates[1],"$};
    \\node (341b) at (\\xdist+1+3*\\xdist, .5+.5*7)         {$",candidates[3]," \\succ ",candidates[4]," \\succ ",candidates[1]," \\succ ",candidates[2],"$};
    \\node (324b) at (\\xdist+1+3*\\xdist, .5+.5*8)         {$",candidates[3]," \\succ ",candidates[2]," \\succ ",candidates[4]," \\succ ",candidates[1],"$};
    \\node (321b) at (\\xdist+1+3*\\xdist, .5+.5*9)         {$",candidates[3]," \\succ ",candidates[2]," \\succ ",candidates[1]," \\succ ",candidates[4],"$};
    \\node (314b) at (\\xdist+1+3*\\xdist, .5+.5*10)        {$",candidates[3]," \\succ ",candidates[1]," \\succ ",candidates[4]," \\succ ",candidates[2],"$};
    \\node (312b) at (\\xdist+1+3*\\xdist, .5+.5*11)        {$",candidates[3]," \\succ ",candidates[1]," \\succ ",candidates[2]," \\succ ",candidates[4],"$};
    \\node (243b) at (\\xdist+1+3*\\xdist, .5+.5*12)        {$",candidates[2]," \\succ ",candidates[4]," \\succ ",candidates[3]," \\succ ",candidates[1],"$};
    \\node (241b) at (\\xdist+1+3*\\xdist, .5+.5*13)        {$",candidates[2]," \\succ ",candidates[4]," \\succ ",candidates[1]," \\succ ",candidates[3],"$};
    \\node (234b) at (\\xdist+1+3*\\xdist, .5+.5*14)        {$",candidates[2]," \\succ ",candidates[3]," \\succ ",candidates[4]," \\succ ",candidates[1],"$};
    \\node (231b) at (\\xdist+1+3*\\xdist, .5+.5*15)        {$",candidates[2]," \\succ ",candidates[3]," \\succ ",candidates[1]," \\succ ",candidates[4],"$};
    \\node (214b) at (\\xdist+1+3*\\xdist, .5+.5*16)        {$",candidates[2]," \\succ ",candidates[1]," \\succ ",candidates[4]," \\succ ",candidates[3],"$};
    \\node (213b) at (\\xdist+1+3*\\xdist, .5+.5*17)        {$",candidates[2]," \\succ ",candidates[1]," \\succ ",candidates[3]," \\succ ",candidates[4],"$};
    \\node (143b) at (\\xdist+1+3*\\xdist, .5+.5*18)        {$",candidates[1]," \\succ ",candidates[4]," \\succ ",candidates[3]," \\succ ",candidates[2],"$};
    \\node (142b) at (\\xdist+1+3*\\xdist, .5+.5*19)        {$",candidates[1]," \\succ ",candidates[4]," \\succ ",candidates[2]," \\succ ",candidates[3],"$};
    \\node (134b) at (\\xdist+1+3*\\xdist, .5+.5*20)        {$",candidates[1]," \\succ ",candidates[3]," \\succ ",candidates[4]," \\succ ",candidates[2],"$};
    \\node (132b) at (\\xdist+1+3*\\xdist, .5+.5*21)        {$",candidates[1]," \\succ ",candidates[3]," \\succ ",candidates[2]," \\succ ",candidates[4],"$};
    \\node (124b) at (\\xdist+1+3*\\xdist, .5+.5*22)        {$",candidates[1]," \\succ ",candidates[2]," \\succ ",candidates[4]," \\succ ",candidates[3],"$};
    \\node (123b) at (\\xdist+1+3*\\xdist, .5+.5*23)        {$",candidates[1]," \\succ ",candidates[2]," \\succ ",candidates[3]," \\succ ",candidates[4],"$};

    % first level
    \\draw [->] (1) edge (12.west);
    \\draw [->] (1) edge (13.west);
    \\draw [->] (1) edge (14.west);
    \\draw [->] (2) edge (21.west);
    \\draw [->] (2) edge (23.west);
    \\draw [->] (2) edge (24.west);
    \\draw [->] (3) edge (31.west);
    \\draw [->] (3) edge (32.west);
    \\draw [->] (3) edge (34.west);
    \\draw [->] (4) edge (41.west);
    \\draw [->] (4) edge (42.west);
    \\draw [->] (4) edge (43.west);
    
    % second level
    \\draw [->] (12) edge (123);
    \\draw [->] (12) edge (124);
    \\draw [->] (13) edge (132);
    \\draw [->] (13) edge (134);
    \\draw [->] (14) edge (142);
    \\draw [->] (14) edge (143);
    \\draw [->] (21) edge (213);
    \\draw [->] (21) edge (214);
    \\draw [->] (23) edge (231);
    \\draw [->] (23) edge (234);
    \\draw [->] (24) edge (241);
    \\draw [->] (24) edge (243);
    \\draw [->] (31) edge (312);
    \\draw [->] (31) edge (314);
    \\draw [->] (32) edge (321);
    \\draw [->] (32) edge (324);
    \\draw [->] (34) edge (341);
    \\draw [->] (34) edge (342);
    \\draw [->] (41) edge (412);
    \\draw [->] (41) edge (413);
    \\draw [->] (42) edge (421);
    \\draw [->] (42) edge (423);
    \\draw [->] (43) edge (431);
    \\draw [->] (43) edge (432);
    
     % third level
    \\draw [->] (432) edge (432b);
    \\draw [->] (431) edge (431b);
    \\draw [->] (423) edge (423b);
    \\draw [->] (421) edge (421b);
    \\draw [->] (413) edge (413b);
    \\draw [->] (412) edge (412b);
    \\draw [->] (342) edge (342b);
    \\draw [->] (341) edge (341b);
    \\draw [->] (324) edge (324b);
    \\draw [->] (321) edge (321b);
    \\draw [->] (314) edge (314b);
    \\draw [->] (312) edge (312b);
    \\draw [->] (243) edge (243b);
    \\draw [->] (241) edge (241b);
    \\draw [->] (234) edge (234b);
    \\draw [->] (231) edge (231b);
    \\draw [->] (214) edge (214b);
    \\draw [->] (213) edge (213b);
    \\draw [->] (143) edge (143b);
    \\draw [->] (142) edge (142b);
    \\draw [->] (134) edge (134b);
    \\draw [->] (132) edge (132b);
    \\draw [->] (124) edge (124b);
    \\draw [->] (123) edge (123b);

\\end{tikzpicture}
}%
         
  ")
  out
}

