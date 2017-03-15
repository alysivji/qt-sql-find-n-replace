# SQL Query Find and Replace

At work we have a few of our tables set up as follows:

* TableForX0 (current year table), TableForX1 (previous year table), TableForX2 (table from 2 years ago), ...
* ABCTable0, ABCTable1, ABCTable2, ...

When creating trended queries across multiple years, I write a query for a single year and then manually change table names to get queries for all other years. I wrote up a program with a Qt front-end to automate this task.

Releasing my code as part of the [Qt Open Source LGPL license](http://doc.qt.io/qt-5/opensourcelicense.html)
