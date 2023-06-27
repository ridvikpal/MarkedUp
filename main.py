''' IMPORT MODULES '''
import gui
import connection

''' DEFINE MAIN FUNCTION '''
def main() -> None:
    gui.createMainWindow()
    # gui.testFunction()
    # test = connection.getStockQuote("AAPL")
    # fiftyTwoWeek = test['fifty_two_week'][0]
    # print(fiftyTwoWeek)



if __name__ == "__main__":
    main()