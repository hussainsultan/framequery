from __future__ import print_function, division, absolute_import

from ..util._misc import Record


class DefineTables(Record):
    """Add tables to the scope, before evaluating the subdag"""
    __fields__ = ['node', 'tables']


class Literal(Record):
    """Marker node to tag literal values"""
    __fields__ = ['value']


class GetTable(Record):
    """Retrieve a table from the scope"""
    __fields__ = ['table', 'alias']


class Join(Record):
    """Join two tables"""
    __fields__ = ['left', 'right', 'how', 'on']


class CrossJoin(Record):
    """Compute the cartesian product between two tables"""
    __fields__ = ['left', 'right']


class Transform(Record):
    """Generate a new dataframe by transforming the input columns"""
    __fields__ = ['table', 'columns']


class Aggregate(Record):
    """Aggregate the dataframe"""
    __fields__ = ['table', 'columns', 'group_by']


class Filter(Record):
    """Filter a dataframe to the matching rows"""
    __fields__ = ['table', 'filter']


class Sort(Record):
    """Sort the table by the given value expression"""
    __fields__ = ['table', 'values']


class Limit(Record):
    """Limit the dataframe to the given rows"""
    __fields__ = ['table', 'offset', 'limit']


class DropDuplicates(Record):
    """Remove any duplicates from the table"""
    __fields__ = ['table']