# Revisiting

Fermat's little theorem states that if p is prime and 0 < a < p, then

a^{p-1} == p mod{p}.
If we want to test whether p is prime, then we can pick random a's in the interval and see whether the equality holds. If the equality does not hold for a value of a, then p is composite. If the equality does hold for many values of a, then we can say that p is probably prime.

It might be in our tests that we do not pick any value for a such that the equality fails. Any a such that

a^{n-1} == pmod{n}
when n is composite is known as a Fermat liar. Vice versa, in this case n is called Fermat pseudoprime to base a.

If we do pick an a such that

a^{n-1} != pmod{n}
then a is known as a Fermat witness for the compositeness of n.

