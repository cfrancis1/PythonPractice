allValues=[''] * 3
size = 10

theNames=[''] * size
theZips=[''] * size
theResults=[''] * size

def main():
    count = 0
    menu_selection = 0  # Initialize to start loop

    # Main menu loop
    while menu_selection !='':
        menu_selection = display_menu()
        if menu_selection =='1':
             enterRecords(theNames, theZips, theResults, count)
             count+=1
        elif menu_selection =='2':
            updateRecords(allValues)
        elif menu_selection == '3':
            runReports(allValues)


#establish menu module
def display_menu():

    # Display  the menu.
    print()
    print('1 - Enter Records')
    print('2 - Update Test Results')
    print('3 - Run Records')

     # Prompt the user for a selection
    selection = input('Please select an option (press Enter to exit): ')

    # Validate the menu selection
    while selection != '1' and selection != '2' and selection != '3' and selection !='':
        selection = input('That is an invalid selection. Enter 1, 2, 3, or Space to exit the program ')

    return selection

def enterRecords(names, zips, results, count):
    user_name = input('Name: ')
    user_zip = input('Zip: ')
    user_result = input('Result: ')

    if user_name == '':
        print('user is empty')
    elif len(user_zip) != 5:
        print('zipcode not correct')
    elif user_result != 'P' and user_result != 'N' and user_result != '':
        print('result not P or N')
    else:
        theNames[count] = user_name
        theZips[count] = user_zip
        theResults[count] = user_result

    allValues[0] = theNames
    allValues[1] = theZips
    allValues[2] = theResults
    #print(allValues)
    

def updateRecords(values):
    updated = 0
    update_name = '_'

    while update_name != '':
        update_name = input("Enter a Name to search (press Enter to exit): ")
        updated = 0
        if update_name != '':
            for counter in range(0, 10):
                if updated == 0:
                    if values[0][counter] == update_name:
                        print("Current Test Result: ", values[2][counter])
                        update_result = input("Enter a new test result (P for positive, N for Negative, or leave empty): ")
                        values[2][counter] = update_result
                        updated = 1
            if updated == 0:
                print("That name isn't in the database.")


def runReports(values):
    temp_P = 0
    temp_N = 0
    user_choice = '_'
    currZip = ''
    testZip = ''

    for i in range (0, len(values[1]) - 1):
        for j in range (0, len(values[1]) - 1 - i):
            if values[1][j] > values[1][j+1]:
                values[0][j], values[0][j+1] = values[0][j+1], values[0][j]
                values[1][j], values[1][j+1] = values[1][j+1], values[1][j]
                values[2][j], values[2][j+1] = values[2][j+1], values[2][j]

    while user_choice != '':
        
        print('1 - Display test results by Zip Code')
        print('2 - Display total test results')
        user_choice = input("Please select an option (press Enter to exit): ")

        if user_choice == '1':
            print(format('Zip', '15s'), format('Positive', '15s'), format('Negative','15s'), format('Percent Positive','15s'))
            currZip = values[1][0]

            if(values[2][0] == 'N'):
                temp_N += 1
            if(values[2][0] == 'P'):
                temp_P += 1


            for counter in range(1, 10):
                testZip = values[1][counter]
                if(currZip == testZip):
                    if(values[2][counter] == 'N'):
                        temp_N += 1
                    if(values[2][counter] == 'P'):
                        temp_P += 1


                else:
                    if(currZip == ''):
                        pass
                    else:
                        if temp_P == 0:
                            percent_positive = 0
                        else:
                            percent_positive = (temp_P / float(temp_P + temp_N)) * 100
                        print(currZip, temp_P, temp_N, percent_positive)
                    
                    currZip = testZip
                    if(values[2][counter] == 'N'):
                        temp_N = 1
                    else:
                        temp_N = 0
                    if(values[2][counter] == 'P'):
                        temp_P = 1
                    else:
                        temp_P = 0

                if counter == 9:
                    if temp_P == 0:
                       percent_positive = 0
                    else:
                        percent_positive = (temp_P / float(temp_P + temp_N)) * 100
                    print(currZip, temp_P, temp_N, percent_positive)



        if user_choice == '2':
            temp_N = 0
            temp_P = 0
            for counter in range(0, 10):
                if(values[2][counter] == 'N'):
                    temp_N += 1
                if(values[2][counter] == 'P'):
                    temp_P += 1
            if temp_P == 0:
                percent_positive = 0
            else:
                percent_positive = (temp_P / float(temp_P + temp_N)) * 100
            print(format('Positive', '15s'), format('Negative','15s'), format('Percent Positive','15s'))
            print(temp_P, temp_N, percent_positive)



main()