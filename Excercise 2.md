# ML Excercise 2



**3.7.6**

***Somebody tosses a fair coin and if the result is heads, you get nothing; otherwise, you get \$5. How much would you pay to play this game? What if the win is \$500 instead of \$5?***

I would be willing to pay the same amount (or less) as the expected value of the bet, being $2.5

Same for \$500 - which would be  \$250.  *Although only with repeated trials.*



**3.7.8**

***Generalize the confidence and support formulas for basket analysis to calculate k-dependencies, namely, $P (Y|X_1, . . . , X_k)$.***

It would essentially stay the same, simply adding the joint probability for $X_1..X_k$ to the exsisting formulas.

*Support:* $P(X_1,... X_k, Y)$

*Confidence:* $\frac{P(X_1,... X_k, Y)}{P(X_1,... X_k)}$



**3.7.9**

***Show that as we move an item from the antecedent to the consequent, confidence can never increase: confidence(ABC → D) ≥ confidence(AB → CD).***

By looking at the defination of the *confidence* association rule
$$
\text{confidence}(X \rightarrow Y) = \frac{P(X, Y)}{P(X)}
$$
 we see that the that the numerator, being the joint probability of $X$ and $Y$, will stay the same, while the denomenator $P(X)$ can only increase as $X$ "contains" fewer items and thus is more probable.



















 