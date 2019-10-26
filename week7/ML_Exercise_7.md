# ML Exercise 7



**7.2.a**

![xor](/Users/edibegovic/Dropbox/ITU/ML/week7/xor.png)

Grabbed from the previoues chapter

**7.2.b**

$\mathbf{z}_1 = [1, \sqrt{2}, \sqrt{2}, \sqrt{2}, 1, 1]^T$

$\mathbf{z}_2 = [1, -\sqrt{2}, -\sqrt{2}, \sqrt{2}, 1, 1]^T$

$\mathbf{z}_3 = [1, -\sqrt{2}, \sqrt{2}, -\sqrt{2}, 1, 1]^T$

$\mathbf{z}_4 = [1, \sqrt{2}, -\sqrt{2}, -\sqrt{2}, 1, 1]^T$



**7.2.c** + **7.2.d** + **7.2.e**

![calculations72](/Users/edibegovic/Dropbox/ITU/ML/week7/calculations72.png)



**7.2.f**

As all $\mathbf{\alpha}$ are greater than $0$, all four training points are thus support vectors. 



**7.2.g**
$$
\mathbf{w} = \sum_{i = 1}^4 \alpha_ir_i\mathbf{\phi}(\mathbf{x}_i) 
=
\begin{bmatrix}
0 \\
0 \\
0 \\
\frac{\sqrt{2}}{2} \\
0 \\
0 \\
\end{bmatrix}
$$


**7.2.h**

Assuming we should use the polynomial kernel (of degree 2) instead of explicitly computing the feature vectors in $\mathbb{R}^6$ - that is, using the *kernel trick*: 
$$
g(\mathbf{x})
=
\mathbf{w}^T~\mathbf{\phi}(\mathbf{x})
=
\sum_{i = 1}^4 \alpha_ir_i\mathbf{\phi}(\mathbf{x}_i)^T \mathbf{\phi}(\mathbf{x})
=
\sum_{i = 1}^4 \alpha_ir_i \mathbf{K}(\mathbf{x}_i, \mathbf{x})
=
\sum_{i = 1}^4 \alpha_ir_i (\mathbf{x}_i^T \mathbf{x}+1)^2
$$


If it's simply implied that the discriminant function "takes" the original attributes and we do the transformations as part of the function, we get: 
$$
g(\mathbf{x})
=
\mathbf{w}^T~\mathbf{\phi}(\mathbf{x})
=
\frac{\sqrt{2}}{2}\cdot \sqrt{2}x_1x_2
=
x_1x_2
$$
**7.2.i**

$g(\mathbf{x}_1) = 1 \cdot 1 = 1$

$g(\mathbf{x}_2) = -1 \cdot -1 = 1$

$g(\mathbf{x}_3) = -1 \cdot 1 = -1$

$g(\mathbf{x}_4) = 1 \cdot -1 = -1$ 



**13.16.10**

***Let us say we have two representations for the same object and associated with each, we have a different kernel. How can we use both to implement a joint dimensionality reduction using kernel PCA?***

An apporach would be to combine the conceepts of multiple kernel learning to generate a (more general) kernel and afterwards applying PCA on the kernel matrix, as the kernel values give us an idea about the similarity of the inputs. 

 Further, as mentioned in the book, having projected the inputs from our high dimensional kernel space onto the principal components, we can use this new representation both for a linear SVM or for visual representation (exploratory). As we can also multiply the kernels with some constant, one could also experiment with various wheigts when adding together the various kernels (and thus the impact of the different data sources/representations).









































