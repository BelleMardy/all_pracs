"""
dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
… 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join'…]
"""
print("Typing in dir() in the console, produces a list of the useful string methods")
print("""
'__add__'
__add__(self, value, /)
 |      Return self+value.

'__class__'

'__contains__'
__contains__(self, key, /)
 |      Return key in self.

'__delattr__'
'__dir__'
'__doc__'

'__eq__'
__eq__(self, value, /)
 |      Return self==value.


'__format__'
 __format__(...)
 |      S.__format__(format_spec) -> str
 
        Return a formatted version of S as described by format_spec.


'__ge__'
__ge__(self, value, /)
 |      Return self>=value.


'__getattribute__'
 __getattribute__(self, name, /)
 |      Return getattr(self, name).

'__getitem__'
__getitem__(self, key, /)
 |      Return self[key].


'__getnewargs__'
__getnewargs__(...)

'__gt__'
__gt__(self, value, /)
 |      Return self>value.

'__hash__'
 __hash__(self, /)
 |      Return hash(self).

'__init__'
'__init_subclass__'
'__iter__'
__iter__(self, /)
 |      Implement iter(self).

'__le__'__le__(self, value, /)
 |      Return self<=value.
 |  

'__len__'__len__(self, /)
 |      Return len(self).

'__lt__'
 __lt__(self, value, /)
 |      Return self<value.

'__mod__'
__mod__(self, value, /)
 |      Return self%value.


'__mul__'
__mul__(self, value, /)
 |      Return self*value.n

'__ne__'
__ne__(self, value, /)
 |      Return self!=value

'__new__'__new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

'__reduce__'
'__reduce_ex__'
'__repr__'
 __repr__(self, /)
 |      Return repr(self).

'__rmod__'
__rmod__(self, value, /)
 |      Return value%self.

'__rmul__'__rmul__(self, value, /)
 |      Return self*value.

'__setattr__'
'__sizeof__'
 __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  

'__str__'
 __str__(self, /)
 |      Return str(self).

'__subclasshook__'
'capitalize'
capitalize(...)
 |      S.capitalize() -> str
 |      
 |      Return a capitalized version of S, i.e. make the first character
 |      have upper case and the rest lower case.
 | 

'casefold'
 casefold(...)
 |      S.casefold() -> str
 |      
 |      Return a version of S suitable for caseless comparisons.

'center'center(...)
 |      S.center(width[, fillchar]) -> str
 |      
 |      Return S centered in a string of length width. Padding is
 |      done using the specified fill character (default is a space)

'count'
count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number_int of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.

encode'encode(...)
 |      S.encode(encoding='utf-8', errors='strict') -> bytes
 |      
 |      Encode S using the codec registered for encoding. Default encoding
 |      is 'utf-8'. errors may be given to set a different error
 |      handling scheme. Default is 'strict' meaning that encoding errors raise
 |      a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
 |      'xmlcharrefreplace' as well as any other name registered with
 |      codecs.register_error that can handle UnicodeEncodeErrors.
 |  

'endswith'endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.

'expandtabs'expandtabs(...)
 |      S.expandtabs(tabsize=8) -> str
 |      
 |      Return a copy of S where all tab characters are expanded using spaces.
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  

'find'find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.

'format'format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  

'format_map'format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  


'index'index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Like S.find() but raise ValueError when the substring is not found.
 |  

'isalnum' isalnum(...)
 |      S.isalnum() -> bool
 |      
 |      Return True if all characters in S are alphanumeric
 |      and there is at least one character in S, False otherwise.
 |  

'isalpha'
isalpha(...)
 |      S.isalpha() -> bool
 |      
 |      Return True if all characters in S are alphabetic
 |      and there is at least one character in S, False otherwise.
 |  

'isdecimal'isdecimal(...)
 |      S.isdecimal() -> bool
 |      
 |      Return True if there are only decimal characters in S,
 |      False otherwise.


'isdigit'isdigit(...)
 |      S.isdigit() -> bool
 |      
 |      Return True if all characters in S are digits
 |      and there is at least one character in S, False otherwise

'isidentifier'isidentifier(...)
 |      S.isidentifier() -> bool
 |      
 |      Return True if S is a valid identifier according
 |      to the language definition.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers
 |      such as "def" and "class".


'islower' islower(...)
 |      S.islower() -> bool
 |      
 |      Return True if all cased characters in S are lowercase and there is
 |      at least one cased character in S, False otherwise.
 |  

'isnumeric'
isnumeric(...)
 |      S.isnumeric() -> bool
 |      
 |      Return True if there are only numeric characters in S,
 |      False otherwise.
 |  

'isprintable' isprintable(...)
 |      S.isprintable() -> bool
 |      
 |      Return True if all characters in S are considered
 |      printable in repr() or S is empty, False otherwise.

'isspace'
 S.isspace() -> bool
 |      
 |      Return True if all characters in S are whitespace
 |      and there is at least one character in S, False otherwise.
 |  

'istitle'
S.istitle() -> bool
 |      
 |      Return True if S is a titlecased string and there is at least one
 |      character in S, i.e. upper- and titlecase characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |      Return False otherwise.
 |  

'isupper'
S.isupper() -> bool
 |      
 |      Return True if all cased characters in S are uppercase and there is
 |      at least one cased character in S, False otherwise.
 |  

'join'
 S.join(iterable) -> str
 |      
 |      Return a string which is the concatenation of the strings in the
 |      iterable.  The separator between elements is S.

'ljust'
ljust(...)
 |      S.ljust(width[, fillchar]) -> str
 |      
 |      Return S left-justified in a Unicode string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |  

'lower'
 S.lower() -> str
 |      
 |      Return a copy of the string S converted to lowercase.
 |  

'lstrip'
S.lstrip([chars]) -> str
 |      
 |      Return a copy of the string S with leading whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |  

'maketrans'
 Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the


'partition'
S.partition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.

'replace'
S.replace(old, new[, count]) -> str
 |      
 |      Return a copy of S with all occurrences of substring
 |      old replaced by new.  If the optional argument count is
 |      given, only the first count occurrences are replaced.

'rfind'
S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.

'rindex'
S.rindex(sub[, start[, end]]) -> int
 |      
 |      Like S.rfind() but raise ValueError when the substring is not found.
 |  

'rjust'
S.rjust(width[, fillchar]) -> str
 |      
 |      Return S right-justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space).

'rpartition'S.rpartition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, starting at the end of S, and return
 |      the part before it, the separator itself, and the part after it.  If the
 |      separator is not found, return two empty strings and S.

'rsplit' S.rsplit(sep=None, maxsplit=-1) -> list of strings
 |      
 |      Return a list of the words in S, using sep as the
 |      delimiter string, starting at the end of the string and
 |      working to the front.  If maxsplit is given, at most maxsplit
 |      splits are done. If sep is not specified, any whitespace string
 |      is a separator.
 |  

'rstrip'
S.rstrip([chars]) -> str
 |      
 |      Return a copy of the string S with trailing whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |  

'split'
 S.split(sep=None, maxsplit=-1) -> list of strings
 |      
 |      Return a list of the words in S, using sep as the
 |      delimiter string.  If maxsplit is given, at most maxsplit
 |      splits are done. If sep is not specified or is None, any
 |      whitespace string is a separator and empty strings are
 |      removed from the result.

'splitlines'
S.splitlines([keepends]) -> list of strings
 |      
 |      Return a list of the lines in S, breaking at line boundaries.
 |      Line breaks are not included in the resulting list unless keepends
 |      is given and true.
 |  

'startswith'S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  

'strip'
S.strip([chars]) -> str
 |      
 |      Return a copy of the string S with leading and trailing
 |      whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |  

'swapcase'
S.swapcase() -> str
 |      
 |      Return a copy of S with uppercase characters converted to lowercase
 |      and vice versa.
 |  

'title'
S.title() -> str
 |      
 |      Return a titlecased version of S, i.e. words start with title case
 |      characters, all remaining cased characters have lower case.
 |  
 |

'translate'
S.translate(table) -> str
 |      
 |      Return a copy of the string S in which each character has been mapped
 |      through the given translation table. The table must implement
 |      lookup/indexing via __getitem__, for instance a dictionary or list,
 |      mapping Unicode ordinals to Unicode ordinals, strings, or None. If
 |      this operation raises LookupError, the character is left untouched.
 |      Characters mapped to None are deleted.

'upper'
S.upper() -> str
 |      
 |      Return a copy of S converted to uppercase.
 |  

'zfill' S.zfill(width) -> str
 |      
 |      Pad a numeric string S with zeros on the left, to fill a field
 |      of the specified width. The string S is never truncated.
 |  

""")