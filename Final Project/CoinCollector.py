# Coin Collector class processes the coin deposit option
class CoinCollector:
    # method to parse user input into a deposit, then reject anything that is not listed
    def parseChange(self, change):
        values = {
            "P": 1,
            "N": 5,
            "D": 10,
            "Q": 25,
            "H": 50,
            "W": 100
        }
        deposit = 0
        for coin in change:
            if coin in values:
                coins = values[coin]
                deposit += coins
            else:
                print(f"\n\033[31mInvalid coin: {coin}\033[0m\n")

        return deposit
