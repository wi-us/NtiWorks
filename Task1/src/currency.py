currenciesArray = []

class Currencies:

    def doDictionary():
        currenciesArray.clear()
        currenciesArray.append(Currencies.Currency("EUR", "Евро", 1.0, "€"))
        currenciesArray.append(Currencies.Currency("USD", "Доллар США", 1.08, "$"))
        currenciesArray.append(Currencies.Currency("RUB", "Рубль", 98.72, "₽"))
        currenciesArray.append(Currencies.Currency("AUD", "Австралийский доллар", 1.66, "$"))
        currenciesArray.append(Currencies.Currency("AZN", "Азербайджанский манат", 1.84, "	₼"))
        currenciesArray.append(Currencies.Currency("AMD", "Армянский драм", 436.66, "֏"))
        currenciesArray.append(Currencies.Currency("BYN", "Белорусский рубль", 3.49, "р"))
        currenciesArray.append(Currencies.Currency("BGN", "Болгарский лев", 1.95, "лв"))
        currenciesArray.append(Currencies.Currency("BRL", "Бразильский реал", 5.39, "R$"))
        currenciesArray.append(Currencies.Currency("HUF", "Форинт", 393.49, "ƒ"))
        currenciesArray.append(Currencies.Currency("VND", "Донг", 25943.76, "₫"))
        currenciesArray.append(Currencies.Currency("HKD", "Гонконгский доллар", 8.45, "HK$"))
        currenciesArray.append(Currencies.Currency("GEL", "Грузинский лари", 2.88, "₾"))
        currenciesArray.append(Currencies.Currency("DKK", "Датская крона", 7.44, "kr"))
        currenciesArray.append(Currencies.Currency("AED", "Дирхам ОАЭ", 3.97, "DH"))
        currenciesArray.append(Currencies.Currency("EGP", "Египетский фунт", 33.39, "LE"))
        currenciesArray.append(Currencies.Currency("INR", "Индийская рупия", 89.59, "₹"))
        currenciesArray.append(Currencies.Currency("IDR", "Индонезийская рупия", 16986.36, "Rp"))
        currenciesArray.append(Currencies.Currency("KZT", "Казахстанский тенге", 487.67, "₸"))
        currenciesArray.append(Currencies.Currency("CAD", "Канадский доллар", 1.47, "C$"))
        currenciesArray.append(Currencies.Currency("NOK", "Норвежская крона", 11.47, "kr"))
        currenciesArray.append(Currencies.Currency("KGS", "Киргизский сом", 96.64, "с"))
        currenciesArray.append(Currencies.Currency("CNY", "Китайский юань", 7.82, "	¥"))
        currenciesArray.append(Currencies.Currency("TRY", "Турецкая лира", 33.71, "₺"))
        currenciesArray.append(Currencies.Currency("UAH", "Украинская гривна", 41.13, "₴"))
        currenciesArray.append(Currencies.Currency("UZS", "Узбекский сум", 13507.79, "сўм"))
        currenciesArray.append(Currencies.Currency("GBP", "Фунт стерлингов", 0.854467, "£"))
        currenciesArray.append(Currencies.Currency("CZK", "Чешская крона", 25.32, "Kč"))
        currenciesArray.append(Currencies.Currency("SEK", "Шведская крона", 11.2, "kr"))
        currenciesArray.append(Currencies.Currency("CHF", "Швейцарский франк", 0.956813, "₣"))
        currenciesArray.append(Currencies.Currency("KRW", "Южнокорейская вона", 1439.22, "₩"))
        currenciesArray.append(Currencies.Currency("JPY", "Иена", 162.57, "¥"))
    
    def findCurrency(intCode):
            for cur in currenciesArray:
                if cur.intName == intCode:
                    return cur

    class Currency():
            def __init__(self, internationalName, russianName, ratio, symbol):
                self.intName = internationalName
                self.rusName = russianName
                self.ratio = ratio
                self.symbol = symbol

            def convertToEuro(self, amount):
                return amount / self.ratio

            def convertEuroToCurrency(self, amount):
                return amount * Currencies.findCurrency(self.intName).ratio
    


