import re


def problem1(searchstring):
    """
    Match phone numbers.

    :param searchstring: string
    :return: True or False
    """
    phoneMatch = re.search(r'^((\([0-9]{3}\)\s|[0-9]{3}\-)*[0-9]{3}\-[0-9]{4})$', searchstring)

    return True if phoneMatch else False

def problem2(searchstring):
    """
    Extract street name from address.

    :param searchstring: string
    :return: string
    """
    streetAddr = re.search(r'((.*)(?P<street_num>[0-9]+\s)(?P<street_name>[\w\s]+)(?P<road>('
                           r'Rd.|Dr.|Ave.|St.))([\w\s]*))', searchstring)

    streetName = streetAddr['street_name']

    return streetName.strip()

def problem3(searchstring):
    """
    Garble Street name.

    :param searchstring: string
    :return: string
    """
    streetAddr = re.search(r'((.*)(?P<street_num>[0-9]+\s)(?P<street_name>[\w\s]+)(?P<road>('
                           r'Rd.|Dr.|Ave.|St.))([\w\s]*))', searchstring)

    streetName = streetAddr['street_name'].strip()
    reverseStreet = streetName[::-1]

    #replaceStreet = re.sub(r'(?P<street_num>[0-9]+\s)'+streetName+r'([\w\s]*)', r'\1'+reverseStreet+r'\2',streetAddr.groups()[0])
    replaceStreet = re.sub(r'([0-9]+\s)'+streetName, r'\1'+reverseStreet, streetAddr.groups()[0])

    return replaceStreet


if __name__ == '__main__':
    print(problem1('765-494-4600'))  # True
    print(problem1(' 765-494-4600 '))  # False
    print(problem1('(765) 494 4600'))  # False
    print(problem1('(765) 494-4600'))  # True
    print(problem1('494-4600'))  # True
    print(problem1('(abc) 765-1111'))
    print(problem1('(765 123-4367'))
    print(problem1('7651-312'))
    print(problem1('302-761-3124'))
    print()

    print(problem2('The EE building is at 465 Northwestern Ave.'))  # Northwestern
    print(problem2('Meet me at 201 South First New York St. at noon'))  # South First
    print(problem2('123 st. 465 Northwestern Ave.'))
    print(problem2('44 West Rd.'))
    print(problem2('Professor Brinton lives on 123 Have No Clue Ave.'))
    print(problem2('123 st. 465 Northwestern Ave.') == 'Northwestern')
    print(problem2('44 West Rd.') == 'West')
    print()

    print(problem3('The EE building is at 465 Northwestern Ave.'))
    print(problem3('Meet me at 201 South First St. at noon'))
    print(problem3('The EE building is at 465 Northwestern Ave.')=='The EE building is at 465 nretsewhtroN Ave.')
    print(problem3('Meet me at 201 South First St. at noon')=='Meet me at 201 tsriF htuoS St. at noon')
    print(problem3('123 st. 465 Northwestern Ave.')=='123 st. 465 nretsewhtroN Ave.')
    print(problem3('44 West Rd.')=='44 tseW Rd.')
    print(problem3('1 South First St.')=='1 tsriF htuoS St.')
    print(problem3('I live on the East side of 123 East St.'))
    print(problem3('I live on the East side of 123 East St.')=='I live on the East side of 123 tsaE St.')
