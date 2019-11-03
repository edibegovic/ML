# ML Exercise 8



**17.13.2**

***In bagging, to generate the L training sets, what would be the effect of using L-fold cross-validation instead of bootstrap?*** 

Here I interpret 'L-fold cross-validation' as training each of the L base-learners on L equally sized splits of the training data. This would result in higher variance for the learners, as they're dependent on fewer samples and thus are more sensitive to small changes. 

If all the base-learners are based off the same algorithm, I guess it would have less of an effect, as in the end, the the result of the ensemble will be averaged in some kind of way. 

\**Looking at the solutions*, 'L-fold cross-validation' is meant as using $L-1$ parts of the data for each learner - essentially the same as sampeling $(N - N/L)$, but withut replacement. The only 'effect' of this (mentioned on the solution) is the porportions of training data shared between the learners. 



**17.13.4**

***In mixture of experts, we can have different experts use different input representations. How can we design the gating network in such a case?*** 

¯\\_(ツ)_/¯  



**18.9.1**

***Given the grid world in figure 16.10, if the reward on reaching on the goal is $100$ and $γ = 0.9$, calculate manually $Q'(s,a)$, $V'(S)$, and the actions of optimal policy.***

![82drawing](/Users/edibegovic/Dropbox/ITU/ML/week8/82drawing.png)































