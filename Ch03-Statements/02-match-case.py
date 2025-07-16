day = 'Saturday'
match day:
    case 'Monday':
        print('Monday - week starts')
    case 'Tuesday' | 'Wednesday' | 'Thursday':
        print('Tue Wed Thur - Mid of week')
    case 'Friday':
        print('Friday - weekend coming soon')
    case 'Saturday' | 'Sunday':
        print('Sat Sun - Weekend!')
    case _:
        print('Something went wrong')