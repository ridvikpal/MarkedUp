''' IMPORT MODULES '''
import gui
import connection

''' DEFINE MAIN FUNCTION '''
def main() -> None:
    allStocksDF = update_stocks_list()
    # test = getStockInformation("apple", "United States", allStocksDF)
    # print(test)

    anotherTest = getLivePrice("AAPL")
    print(anotherTest)
    # appleFigure = getStockTimeSeriesGraph("AAPL")
    # gui.show_in_window(appleFigure, "AAPL")
    # test = getStockInformation("apple", "United States", allStocksDF)
    # print(test)
    # tz_string = datetime.now().astimezone().tzname()
    # print(tz_string)



if __name__ == "__main__":
    main()