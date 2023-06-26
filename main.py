''' IMPORT MODULES '''
import ui_user_interface_design
import connection

''' DEFINE MAIN FUNCTION '''
def main() -> None:
    # allStocksDF = connection.update_stocks_list()
    # # test = getStockInformation("apple", "United States", allStocksDF)
    # # print(test)

    # # anotherTest = connection.getLivePrice("AAPL")
    # anotherTest = connection.getStockQuote("AAPL")
    # anotherTest.to_csv('test.csv', index=False)
    # print(anotherTest)
    # appleFigure = getStockTimeSeriesGraph("AAPL")
    # gui.show_in_window(appleFigure, "AAPL")
    # test = getStockInformation("apple", "United States", allStocksDF)
    # print(test)
    ui_user_interface_design.createMainWindow()



if __name__ == "__main__":
    main()