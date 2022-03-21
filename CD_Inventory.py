#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Artem Lamnin, 2022-03-19, added functionality
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.dat'
lstOfCDObjects = []
import pickle
class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """

    # TODone Added Code to the CD class
    def __init__(self, cd_id,cd_title,cd_artist):
        print('Adding new CD...')
        try:
            self.__cd_id=int(cd_id)
        except: 
            print('Warning: CD ID must be an integer!')
        self.__cd_title=cd_title
        self.__cd_artist=cd_artist
    @property 
    def cd_id(self):
        try:
            return self.__cd_id
        except:
            print('Invalid CD ID value!')
    @property
    def cd_title(self):
        return self.__cd_title
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    def __str__(self):
        return self.rowinfo()
    def rowinfo(self):
        return str([self.cd_id,self.cd_title,self.cd_artist])

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """  
    # TODOne Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, lst_inventory):
        """Args: file_name(string): name of file to which program will write inventory 
             lst_inventory(list): list that will be saved to file
        Returns: None"""
        objFile = open(file_name, 'wb')
        pickle.dump(lst_inventory,objFile)
        objFile.close()
    # TODone Add code to process data from a file     
    @staticmethod
    def load_inventory(file_name):
        """args: file_name(string): name of file from which program will load inventory
        returns: list of cd objects"""
        cd_obj_list=[]
        objFile = open(file_name, 'rb')
        cd_obj_list=pickle.load(objFile)
        objFile.close()
        return cd_obj_list

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODone added docstring
    '''Processes user input and output functions
       Methods: print_menu(): -> None
                menu_choice(): -> user choice string
                show_inventory(table): -> None
                collect_cd_info(): -->cd info strings
                '''
            
    # TODone added code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
    # TODone added code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s, or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    # TODone add code to display the current data on screen
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        index=0
        print('======= The Current Inventory: =======')
        print('ID\tCD Title \t(by: Artist)\n')
        for row in table:
            print(table[index].cd_id,'\t',table[index].cd_title,'\t',table[index].cd_artist)
            index+=1
        print('======================================')
        

    # TODone add code to get CD data from user
    @staticmethod
    def collect_cd_info():  #added function to collect CD data from user
        """Collects CD info

        Args: None

        Returns:
            strID(string): CD ID string
            strTitle(string): CD Title string
            stArtist(string): Artist name string
        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, stArtist

# -- Main Body of Script -- #
# TODOne Added Code to the main body
# Load data from file into a list of CD objects on script start    
try: 
    lstOfCDObjects=FileIO.load_inventory(strFileName)
except:
    print('cdInventory.dat not found.')    

while True:
# Display menu to user
    IO.print_menu()
    str_choice=IO.menu_choice()

    # show user current inventory
    if str_choice=='i':
        IO.show_inventory(lstOfCDObjects)
    # let user add data to the inventory
    elif str_choice=='a':
        [string_ID,string_title,string_artist]=IO.collect_cd_info()
        
        CD_obj=CD(string_ID,string_title,string_artist)
        lstOfCDObjects.append(CD_obj)
    # let user save inventory to file
    elif str_choice=='s':
            FileIO.save_inventory(strFileName,lstOfCDObjects)
    # let user load inventory from file
    elif str_choice=='l':
        try: 
            lstOfCDObjects=FileIO.load_inventory(strFileName)
        except:
            print('cdInventory.dat not found')
    # let user exit program
    elif str_choice=='x':
        break

