# dynatrace

Hello, this is my Backend oriented task (Python)

Running server via Docker:

sudo dockebuild --network=host -t currency .py

sudo docker run -it -e date=2023-04-20 -e currency=EUR -e quotations=30 currency python3 app.py

Also, you need to switch from sys.argv to os.environ.get. To do that you have to uncomment line 10, 11 and 12 and comment lines from 14 to 22 so it will look like this:

date = os.environ.get('date')
currency = os.environ.get('currency')
quotations = int(os.environ.get('quotations'))

Running server via comand line:

 python3 app.py "2023-04-20" "USD" "10"
 
 And same thing as above with variables:

date = sys.argv[1]
currency = sys.argv[2]
quotations = int(sys.argv[3])

When the server starts, there are there buttons which will redirect you to first, second and third endpoint. Every endpoint returns data in json.

There also are three tests added and they all pass.

