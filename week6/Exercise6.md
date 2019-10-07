# ML Exercise 6



**6.2.a**

***Show that in the 2D case we have that $\frac{1}{\sqrt{(2 \pi)^{D}|\mathbf{\Sigma}|}}=\frac{1}{2 \pi \sigma_{1} \sigma_{2} \sqrt{1-\rho^{2}}}$***


$$
\begin{align*}
|\mathbf{\Sigma}|
&=
|\left[\begin{array}{cc}{\sigma_{1}^{2}} & {\rho \sigma_{1} \sigma_{2}} \\ {\rho \sigma_{1} \sigma_{2}} & {\sigma_{2}^{2}}\end{array}\right]| \\[1.2em]
&=
\sigma_1^2 ~ \sigma_2^2 - \rho^2 ~ \sigma_1^2 ~ \sigma_2^2 \\[1.2em]
&= 
\sigma_1^2 ~ \sigma_2^2 ~(1-\rho^2)
\end{align*}
$$
Adding the new term back to the eq.:
$$
\frac{1}{\sqrt{(2\pi)^2 ~ \sigma_1^2 ~ \sigma_2^2 ~(1-\rho^2)}} 
=
\frac{1}{\sqrt{(2\pi)^2} ~ \sqrt{\sigma_1^2} ~ \sqrt{\sigma_2^2} ~ \sqrt{1-\rho^2}}
=
\frac{1}{2\pi ~ \sigma_1^2 ~ \sigma_2^2 ~ \sqrt{1-\rho^2}}
$$


**6.3.a**

Intter term represents the "outputs" of the previous layer.
$$
\begin{align*}
y(\mathbf{x}, \mathbf{w})
&=
\sum_{j=1}^{2} w_{j}^{(2)} h\left(\sum_{i=1}^{2} w_{j i}^{(1)} x_{i}+w_{j 0}^{(1)}\right)+w_{0}^{(2)}
\\[1.3em]&=
w_1^{(2)} ~ h\left(w_{11}^{(1)}x_1 + w_{12}^{(1)}x_2 + w_{10}^{(1)} \right) +
w_2^{(2)} ~ h\left(w_{21}^{(1)}x_1 + w_{22}^{(1)}x_2 + w_{20}^{(1)} \right) + 
w_0^{(2)}
\\[1.3em]&=
1 ~ h\left(1x_1 + 1x_2 + 0 \right) +
(-2) ~ h\left(1x_1 + 1x_2 - 1 \right) + 
0
\\[1.3em]&=
h\left(x_1 + x_2 \right) -
2 ~ h\left(x_1 + x_2 - 1 \right)
\end{align*}
$$


$y((0,0), \mathbf{w}) = h\left(0 + 0 \right) -
2 ~ h\left(0 + 0 - 1 \right) = 0$ 

$y((1,0), \mathbf{w}) = h\left(1 + 0 \right) -
2 ~ h\left(1 + 0 - 1 \right) = 1-0 = 1$

$y((0,1), \mathbf{w}) = h\left(0 + 1 \right) -
2 ~ h\left(0 + 1 - 1 \right) = 1-0 = 1$

$y((1,1), \mathbf{w}) = h\left(1 + 1 \right) -
2 ~ h\left(1 + 1 - 1 \right) = 2-2 = 0$



**6.3.b**

![IMG_6207](/Users/edibegovic/Desktop/IMG_6207.JPG)