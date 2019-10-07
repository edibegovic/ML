# ML Exercise 5



**9.8.4**

***In generating a univariate tree, a discrete attribute with $n$ possible values can be represented by $n$ $0/1$ dummy variables and then treated as $n$ separate numeric attributes. What are the advantages and disadvantages of this approach?***

[+] Discrete attributes with many values are generally favord by the impurity measure if no further "normalization"/penalization is applied. 

[+] Binary decision nodes are simpler for humas to grasp - given that interpretability is one of the main advantages of the descision tree.

[+] Allows for more flixibility. If a certain value doesn't contribute enough as an individual attribute, we can ignore it during the tree construction and also get rid of it during post-pruning.

[-] As the process of constructing the tree is "greedy",...



**10.11.1**

***For each of the following basis function, describe where it is nonzero***



**10.11.2**

***For the two-dimensional case of figure 10.2, show equations 10.4 and 10.5***



**10.11.3**

***Show that the derivative of the softmax, $y_i = \frac{exp(a_i)}{\Sigma_j exp(a_j)}$ is $\frac{\partial y_i}{\partial a_j} = y_i(\delta_{ij} - y_j)$ where $\delta_{ij}$ is $1$ if $i = j$ and $0$ otherwise.***



**10.11.6**

***In using quadratic (or higher-order) discriminants as in eq. 10.34, how can we keep variance under control?***



