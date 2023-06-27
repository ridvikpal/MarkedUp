''' IMPORT MODULES '''
import ui_user_interface_design
import connection

''' DEFINE MAIN FUNCTION '''
def main() -> None:
    ui_user_interface_design.createMainWindow()
    # test = connection.getStockQuote("AAPL")
    # name = test['name'][0]
    # print(name)



if __name__ == "__main__":
    main()