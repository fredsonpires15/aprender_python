pessoa = {'nome': 'Fredson',
          'sobrenome': 'Vila Nova'}
# pessoa.setdefault('idade', 22)
""" print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))
 """

d1 = {'c1': 1,
      'c1': 3,
      'l1': [1,3,4]
      }

""" d2 = d1.copy()

d2['c1'] = 100
print(d1)
print(d2) """
""" novasoma = sum(i*i for  i  in  range ( 10 )) 
somar = 0
for  i  in  range ( 10 ):
    somar += i*i
if somar == novasoma:
    print('Nova apredizagem') """

""" import  __future__ 

all_feature_names = [
    "nested_scopes",
    "generators",
    "division",
    "absolute_import",
    "with_statement",
    "print_function",
    "unicode_literals",
    "barry_as_FLUFL",
    "generator_stop",
    "annotations",
]

__all__ = ["all_feature_names"] + all_feature_names

# The CO_xxx symbols are defined here under the same names defined in
# code.h and used by compile.h, so that an editor search will find them here.
# However, they're not exported in __all__, because they don't really belong to
# this module.
CO_NESTED = 0x0010                      # nested_scopes
CO_GENERATOR_ALLOWED = 0                # generators (obsolete, was 0x1000)
CO_FUTURE_DIVISION = 0x20000            # division
CO_FUTURE_ABSOLUTE_IMPORT = 0x40000     # perform absolute imports by default
CO_FUTURE_WITH_STATEMENT = 0x80000      # with statement
CO_FUTURE_PRINT_FUNCTION = 0x100000     # print function
CO_FUTURE_UNICODE_LITERALS = 0x200000   # unicode string literals
CO_FUTURE_BARRY_AS_BDFL = 0x400000
CO_FUTURE_GENERATOR_STOP = 0x800000     # StopIteration becomes RuntimeError in generators
CO_FUTURE_ANNOTATIONS = 0x1000000       # annotations become strings at runtime


class _Feature:

    def __init__(self, optionalRelease, mandatoryRelease, compiler_flag):
        self.optional = optionalRelease
        self.mandatory = mandatoryRelease
        self.compiler_flag = compiler_flag

    def getOptionalRelease(self):
        '''Return first release in which this feature was recognized.
        This is a 5-tuple, of the same form as sys.version_info.
        '''
        return self.optional

    def getMandatoryRelease(self):
        Return release in which this feature will become mandatory.
        This is a 5-tuple, of the same form as sys.version_info, or, if
        the feature was dropped, or the release date is undetermined, is None.
        '''
        return self.mandatory

    def __repr__(self):
        return "_Feature" + repr((self.optional,
                                  self.mandatory,
                                  self.compiler_flag))


nested_scopes = _Feature((2, 1, 0, "beta",  1),
                         (2, 2, 0, "alpha", 0),
                         CO_NESTED)

generators = _Feature((2, 2, 0, "alpha", 1),
                      (2, 3, 0, "final", 0),
                      CO_GENERATOR_ALLOWED)

division = _Feature((2, 2, 0, "alpha", 2),
                    (3, 0, 0, "alpha", 0),
                    CO_FUTURE_DIVISION)

absolute_import = _Feature((2, 5, 0, "alpha", 1),
                           (3, 0, 0, "alpha", 0),
                           CO_FUTURE_ABSOLUTE_IMPORT)

with_statement = _Feature((2, 5, 0, "alpha", 1),
                          (2, 6, 0, "alpha", 0),
                          CO_FUTURE_WITH_STATEMENT)

print_function = _Feature((2, 6, 0, "alpha", 2),
                          (3, 0, 0, "alpha", 0),
                          CO_FUTURE_PRINT_FUNCTION)

unicode_literals = _Feature((2, 6, 0, "alpha", 2),
                            (3, 0, 0, "alpha", 0),
                            CO_FUTURE_UNICODE_LITERALS)

barry_as_FLUFL = _Feature((3, 1, 0, "alpha", 2),
                          (4, 0, 0, "alpha", 0),
                          CO_FUTURE_BARRY_AS_BDFL)

generator_stop = _Feature((3, 5, 0, "beta", 1),
                          (3, 7, 0, "alpha", 0),
                          CO_FUTURE_GENERATOR_STOP)

annotations = _Feature((3, 7, 0, "beta", 1),
                       None,
                       CO_FUTURE_ANNOTATIONS) """

from functools import singledispatch
@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)

""" @fun.register
def _(arg: int | float, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg) """

from typing import Union
@fun.register
def _(arg: Union[list, set], verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)
s1 = set('Fredson')
fun(1==2)
_([1,2,3,4], s1)