import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sql_replacer_ui

class SQLReplacer(QDialog, sql_replacer_ui.Ui_frmMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # attach events
        self.btnBrowse.clicked.connect(self.browse_files)
        self.btnConvert.clicked.connect(self.convert_sql)


    def convert_sql(self):
        # get base tables from text file
        tables = []
        with (open(self.lneBaseTables.text(), 'r')) as f:
            for line in f:
                tables.append(line.rstrip('\n'))

        # get sql query
        sql_query = self.txtSQLToChange.toPlainText()

        # set up before and after table names
        char_to_replace = self.lneCharToReplace.text()
        char_replace_with = self.lneCharReplaceWith.text()
        tables_to_replace = [table + char_to_replace for table in tables]
        tables_replace_with = [table + char_replace_with for table in tables]

        # replace query
        sql_query = self.sql_query_find_n_replace(sql_query, \
                                                  tables_to_replace, \
                                                  tables_replace_with)

        # update textbox
        self.txtResultingQuery.insertPlainText(sql_query)


    def browse_files(self):
        open_file = QFileDialog.getOpenFileName(self,
                                                caption='Open Base Table File',
                                                directory='.',
                                                filter='Text Files (*.txt)')
        self.lneBaseTables.setText(QDir.toNativeSeparators(open_file))


    def sql_query_find_n_replace(self, sql_query, old_tables, new_tables):
        for old_table, new_table in zip(old_tables, new_tables):
            sql_query = sql_query.replace(old_table, new_table)

        return sql_query


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sql_replacer = SQLReplacer()
    sql_replacer.show()
    app.exec_()
