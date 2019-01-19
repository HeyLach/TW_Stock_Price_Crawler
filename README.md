# TW_Stock_Price_Updater - Source code

[important!!] The updater requires a local database to store the stock price, you can easiest build up a local database via XAMPP application.



The crawler queries the stock prices from "TWSE 臺灣證券交易所, http://www.tse.com.tw" month by month.
Since there is a security mechanism to against flooding connection attacks on TWSE servers, I've add a sleep time between 20s~25s for each crawling.


The default earliest date for every stock crawling is '2007-01-01'.
You can change the earliest date via changing date from the following code:

<pre><code>mycursor.execute('SELECT max(date) FROM `\'%s\'`;'%code)
max_date = mycursor.fetchone()[0]
if max_date == None:
    max_date = datetime.date(datetime.strptime('20070101', "%Y%m%d"))
print('[Status] The Newest Date of The Stock Price is {}'.format(max_date))
in_date = max_date</code></pre>



The Stock_List contains 799 stock code, you may recompose the list or make your own stock list with the stock code that you are interested to.
Please remember to modify the file name from the "Stock_Crawler.ipynb" code which is shown as following:

<pre><code>mycursor = mydb.cursor()
file_name = 'Stock_List.txt'
main(file_name)</code></pre>
