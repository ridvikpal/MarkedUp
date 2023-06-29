''' IMPORT MODULES '''
import gui

''' DEFINE MAIN FUNCTION '''
def main() -> None:

    # check if graphs exist, and remove them first before the actual program starts
    oneMonthGraphFilePath = "1 month.html"
    threeMonthsGraphFilePath = "3 months.html"
    sixMonthsGraphFilePath = "6 months.html"
    oneYearGraphFilePath = "1 year.html"
    fiveYearsGraphFilePath = "5 years.html"

    if gui.os.path.isfile(oneMonthGraphFilePath):
        gui.os.remove(oneMonthGraphFilePath)
    if gui.os.path.isfile(threeMonthsGraphFilePath):
        gui.os.remove(threeMonthsGraphFilePath)
    if gui.os.path.isfile(sixMonthsGraphFilePath):
        gui.os.remove(sixMonthsGraphFilePath)
    if gui.os.path.isfile(oneYearGraphFilePath):
        gui.os.remove(oneYearGraphFilePath)
    if gui.os.path.isfile(fiveYearsGraphFilePath):
        gui.os.remove(fiveYearsGraphFilePath)

    gui.createMainWindow()
    # gui.testFunction()
    # gui.initFavourites()

if __name__ == "__main__":
    main()