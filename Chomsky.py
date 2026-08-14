#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Chomsky.py

An aid to writing linguistic papers in the style of Noam Chomsky.
It is based on selected phrases taken from actual books and articles
written by the great master.  Upon request, it assembles the phrases
in the elegant stylistic patterns that marxist N. Chomsky was noted for.

You are encouraged to add more patterns.

To generate n sentences of linguistic wisdom, type ...
chomsky(n)
chomsky(5) generates about half a screen of linguistic truth

tested with LinuxMint and VSCodium IDE  vegaseat  14aug2026
"""

import textwrap
import random
from itertools import chain, islice

def chomsky(n=1, line_length=72):
    """
    put it all together Noam Chomsky style, n = number of sentences
    """
    parts = []
    for part in (leadins, subjects, verbs, objects):
        phrase_list = [x.strip() for x in part.splitlines()]
        random.shuffle(phrase_list)
        parts.append(phrase_list)
    output = chain(*islice(zip(*parts), 0, n))
    return textwrap.fill(' '.join(output), line_length)

# 'lead ins' to buy some time ...
leadins = """\
To characterize a linguistic level L,
On the other hand,
This suggests that
It appears that
Furthermore,
We will bring evidence in favor of the following thesis:
To provide a constituent structure for T(Z,K),
From C1, it follows that
Analogously,
Clearly,
Note that
Of course,
Suppose, for instance, that
Thus
With this clarification,
Conversely,
We have already seen that
By combining adjunctions and certain deformations,
I suggested that these results would follow from the assumption that
However, this assumption is not correct, since
In the discussion of resumptive pronouns following (81),
So far,
Nevertheless,
For one thing,
Summarizing, then, we assume that
A consequence of the approach just outlined is that
Presumably,
On our assumptions,
It may be, then, that
It must be emphasized, once again, that
Let us continue to suppose that
Notice, incidentally, that """

# subjects chosen for maximum professorial macho ...
subjects = """\
the notion of level of grammaticalness
a case of semigrammaticalness of a different sort
most of the methodological work in modern linguistics
a subset of English sentences interesting on independent grounds
the natural general principle that will subsume this case
an important property of these three types of EKC
any associated supporting element
the speaker-listener's linguistic intuition
the descriptive power of the base component
the earlier discussion of deviance
this analysis of a formative as a pair of sets of features
this selectionally introduced contextual feature
a descriptively adequate grammar
the fundamental error of regarding functional notions as categorial
relational information
the systematic use of complex symbols
the theory of syntactic features developed earlier"""

# verbs chosen for autorecursive obfuscation ...
verbs = """\
can be defined in such a way as to impose
delimits
suffices to account for
cannot be arbitrary in
is not subject to
does not readily tolerate
raises serious doubts about
is not quite equivalent to
does not affect the structure of
may remedy and, at the same time, eliminate
is not to be considered in determining
is to be regarded as
is unspecified with respect to
is, apparently, determined by
is necessary to impose an interpretation on
appears to correlate rather closely with
is rather different from"""

# objects selected for profound sententiousness ...
objects = """\
problems of phonemic and morphological analysis.
the traditional practice of grammarians.
a stipulation to place the constructions into these categories.
a descriptive fact.
a parasitic gap construction.
the extended c-command discussed in connection with (34).
the system of base rules exclusive of the lexicon.
irrelevant intervening contexts in selectional rules.
nondistinctness in the sense of distinctive feature theory.
a general convention regarding the forms of the grammar.
an abstract underlying order.
an important distinction in language use.
the strong generative capacity of the theory."""

# test it ...
print(( chomsky(1) ))

print(( '='*72 ))

print(( chomsky(5) ))

''' possible result...

With this clarification, the earlier discussion of deviance is to be
regarded as the system of base rules exclusive of the lexicon.
========================================================================
Conversely, this selectionally introduced contextual feature may remedy
and, at the same time, eliminate a descriptive fact. We will bring
evidence in favor of the following thesis: a descriptively adequate
grammar is not subject to an important distinction in language use. We
have already seen that relational information appears to correlate
rather closely with irrelevant intervening contexts in selectional
rules. Of course, the speaker-listener's linguistic intuition is,
apparently, determined by nondistinctness in the sense of distinctive
feature theory. A consequence of the approach just outlined is that this
analysis of a formative as a pair of sets of features is rather
different from a parasitic gap construction.

'''

