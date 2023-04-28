#Lab 8: The Cow Strikes Back
from heifer_generator import HeiferGenerator
import sys

def list_cows():
    return HeiferGenerator.get_cows()

def find_cow(name):
    cows = list_cows()
    # the [cows] list is made, now for i in [cows], if the instance attribute 'cow.name' == name
    #  where name will be the user entered sys.argv[2], if cow_name == name
    # then cow is returned, ex: cow is 'heifer', so cow.name is the instance attribute of heifer.name which is 'heifer' thanks to get_cows
    # we hope that sys.argv[2] will be 'heifer' so that cow can be returned
    for cow in cows:
        if cow.name == name:
            return cow
    return None

def main(args):
    cows = list_cows()
    # this will initial list of cows that will be taken from the HeiferGenerator
    cow_string = ' '.join([cow.name for cow in cows])
    # since the new heifergenerator.py adds 'dragon_names' to get_cows() in class
    # class HeiferGenerator, cow_string will also list the available dragon and the cow names
    if args[1] ==  '-l':
        print(f'Cows available: {cow_string}')

    # pick a specific cow or dragon
    elif args[1] == '-n':
        # the sys.arg[1] == '-n' means that user should input an element found within the list [cows]
        # [cows] created when main is called and will call the list_cows() function
        # this will then return HeiferGenerator.get_cows() for [cows] from heifer_generator.py
        # since HeiferGenerator class attribute 'cows' is None
        # it will run the if-statement, creating the HeiferGenerator.cows list, which is ['heifer','kitteh','dragon','ice-dragon']

        cow = find_cow(args[2])
        if cow:
            print()
            # adds the user input message to message (from sys.argv index pos 3 to end)
            message = ' '.join(args[3:])
            print(message)
            # print the cow.image
            # say returned cow is dragon, the instance attribute (dragon.image) is pulled from instance dragon
            # which was created in the get_cows() function from the heifer_generator.py file
            print(cow.image)
            # below we add the condition that for the case if cow instance == dragon or ice-dragon
            # the cow instance name must be either 'dragon' 'ice-dragon' AND the can_breathe_fire class attribute is either TRUE or False
            # meeting either set of parameters will deterimine the end printed string
            if cow.name == 'dragon' and cow.can_breathe_fire() == True:
                print('This dragon can breathe fire.')
            elif cow.name == 'ice-dragon' and cow.can_breathe_fire() == False:
                print('This dragon cannot breathe fire.')
        # if invalid name
        else:
            print(f'Could not find {args[2]} cow!')
    # print default cow with message
    else:
        print()
        message = ' '.join(args[1:])
        print(message)
        print(cows[0].image)

if __name__ == '__main__':
    main(sys.argv)


