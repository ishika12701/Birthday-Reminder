import pandas as pd
import datetime
import win10toast # library which is used for displaying windows 10 toast notification

bday = False

if __name__ == "__main__":
    notifier = win10toast.ToastNotifier()
    dates = pd.read_excel("Book1.xlsx")
    # print (dates)
    today = datetime.datetime.now().strftime("%D-%m")
    #print(today)
    #print(dates.iterrows())
    for index, item in dates.iterrows():  # iterating date in excel sheet
        bDate = item['Date'].strftime("%D-%m")
        # print(bDate)

        if (today==bDate):
            name = item['Name']
            notifier.show_toast(f'Wish {name} Happy Birthday!!! ', "  ",duration = 10)
            bday = True

    if bday==False:
        notifier.show_toast('Python', "No Birthday Today", duration = 10)