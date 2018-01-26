# Regular Expression and Automata

### Update 2018-01-26

**Function**
- Regular Expression

  `Regex(string, alphabet='01')` returns a Regex object based on string.

  `regex.match(string)` returns whether this regex and this string match.

- Automata

  `Automata(begin, alphabet='01')` returns an Automata object.

  `automata.parse(string)` returns whether this automata accepts this string.

**Feature**
- Regular Expression
  - `~` is used as symbol of epsilon and `#` is used as ending symbol, so do not include them in the alphabet.
- Automata
  - Now using NFA(including epsilon-transformation and multi-transformation).

### Update 2018-01-25

**Input**

- simple re
  - \*
  - \+
  - []
  - concatenate
- input string

**Output**

- automata
- match (or not)
- matcher
