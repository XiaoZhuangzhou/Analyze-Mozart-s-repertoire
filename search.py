"""For Models"""
import models
import string
import sys
from PyQt4 import QtCore, QtGui, uic


class Interface(QtGui.QMainWindow):
    """Interface class"""

    def __init__(self):
        super(Interface, self).__init__()
        uic.loadUi("QtUI.ui", self)

        self.data = []
        self.filename = 'save_data.txt'
        self.read_initial_data('list_of_liszt.csv')  # read and save

        self.setup()

    def closeEvent(self, *a, **c):
        print "Saving Data"
        self.save_data()  # saving into 'save_data.txt', once after read from original file 'list_of_liszt.csv', we keep loading from 'save_data.txt' without modifying the original file

    def setup(self):
        self.add_button.clicked.connect(self.add)
        self.search_button.clicked.connect(self.search)

        self.save_button.clicked.connect(self.save)
        self.load_button.clicked.connect(self.load)

        self.sort_button.clicked.connect(self.load)




    def add(self):
        pass
    def save(self):
        pass
    def load(self):
        pass
    def sort(self):
        pass




    def search(self):
        """Searches through our data for a value"""

        name = self.name_input.toPlainText()
        date = self.date_input.toPlainText()
        genre = self.genre_input.toPlainText()
        key = self.key_input.toPlainText()
        orchestration = self.orchestration_input.toPlainText()
        description = self.description_input.toPlainText()

        print name, date, genre, key, orchestration, description

        returns = []

        for item in self.data:
            if string.find(item.get_name(), name) != -1:  # or item.get_date.find(date) != -1 or item.get_genre.find(genre) != -1:   # sub string   Return the lowest index in s where the substring sub is found such that sub. Return -1 on failure
                returns.append(item)

        self.results_table.setRowCount(len(returns))
        self.results_table.setColumnCount(6)

        for i, item in enumerate(returns):  # items matching their indices
            self.results_table.setItem(i, 0, QtGui.QTableWidgetItem(item.name))
            self.results_table.setItem(i, 1, QtGui.QTableWidgetItem(item.date))
            self.results_table.setItem(i, 2, QtGui.QTableWidgetItem(item.genre))
            self.results_table.setItem(i, 3, QtGui.QTableWidgetItem(item.key))
            self.results_table.setItem(i, 4, QtGui.QTableWidgetItem(item.orchestration))
            self.results_table.setItem(i, 5, QtGui.QTableWidgetItem(item.description))








    def read_initial_data(self, filename):
        """Reads in data into the internal data structure"""
        with open(filename, 'r') as files:
            for line in files:
                line = string.lower(line)  # Return a copy of s, but with upper case letters converted to lower case. Convenient for search
                values = line.split(',')
                item = models.Item(values[0], values[1], values[2], values[3], values[4], values[5])
                self.data.append(item)
                # print item

    def save_data(self):
        """Saves all the current data into self.filename"""
        with open(self.filename, 'w') as files:
            for item in self.data:
                files.write(str(item) + '\n')

    def open_data(self):
        """Opens the data from self.filename"""
        """Reads in data into the internal data structure"""
        with open(self.filename, 'r') as files:
            for line in files:
                values = line.split(',')
                item = models.Item(values[0], values[1], values[2], values[3], values[4], values[5])
                self.data.append(item)



def run():
    print 'Starting'
    app = QtGui.QApplication(sys.argv)
    GUI = Interface()
    GUI.show()
    sys.exit(app.exec_())

run()
