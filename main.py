''' IMPORT MODULES '''
import gui

''' DEFINE MAIN FUNCTION '''
def main() -> None:

    ### PERFORM NECESSARY CHECKS FOR INITIAL PROGRAM ###

    # check if graphs exist, and remove them first before the actual program starts
    oneMonthGraphFilePath = "1 month.html"
    oneMonthDarkGraphFilePath = "1 month_dark.html"
    threeMonthsGraphFilePath = "3 months.html"
    threeMonthsDarkGraphFilePath = "3 months_dark.html"
    sixMonthsGraphFilePath = "6 months.html"
    sixMonthsDarkGraphFilePath = "6 months_dark.html"
    oneYearGraphFilePath = "1 year.html"
    oneYearDarkGraphFilePath = "1 year_dark.html"
    fiveYearsGraphFilePath = "5 years.html"
    fiveYearsDarkGraphFilePath = "5 years_dark.html"

    if gui.os.path.isfile(oneMonthGraphFilePath):
        gui.os.remove(oneMonthGraphFilePath)
    if gui.os.path.isfile(oneMonthDarkGraphFilePath):
        gui.os.remove(oneMonthDarkGraphFilePath)

    if gui.os.path.isfile(threeMonthsGraphFilePath):
        gui.os.remove(threeMonthsGraphFilePath)
    if gui.os.path.isfile(threeMonthsDarkGraphFilePath):
        gui.os.remove(threeMonthsDarkGraphFilePath)

    if gui.os.path.isfile(sixMonthsGraphFilePath):
        gui.os.remove(sixMonthsGraphFilePath)
    if gui.os.path.isfile(sixMonthsDarkGraphFilePath):
        gui.os.remove(sixMonthsDarkGraphFilePath)

    if gui.os.path.isfile(oneYearGraphFilePath):
        gui.os.remove(oneYearGraphFilePath)
    if gui.os.path.isfile(oneYearDarkGraphFilePath):
        gui.os.remove(oneYearDarkGraphFilePath)

    if gui.os.path.isfile(fiveYearsGraphFilePath):
        gui.os.remove(fiveYearsGraphFilePath)
    if gui.os.path.isfile(fiveYearsDarkGraphFilePath):
        gui.os.remove(fiveYearsDarkGraphFilePath)

    # check if the stocks list file exists, and if it doesn't create it
    stocksListPath = "all_stocks.json"

    if not gui.os.path.isfile(stocksListPath):
        gui.connection.update_stocks_list()

    # favourites file is already checked for by initializeFavourites()

    ### START MAIN PROGRAM ###
    gui.createMainWindow()

if __name__ == "__main__":
    main()