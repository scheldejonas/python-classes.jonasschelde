class Pirate() :

    # class variables
    _id = 0

    _name = ""

    _next_pirate = 0

    _prev_pirate = 0

    # constructor
    def __init__(self, id, name, gender):

        self._id = id

        self._name = name

        self._gender = gender


    def get_name(self) :

        return self._name


    def get_id(self) :

        return self._id


    def get_qoute(self) :

        return "Good morning"


    def to_string(self) :

        next_pirate = ""

        if ( self._next_pirate == 0 ) :

            next_pirate = "No one"

        else :

            next_pirate = self._next_pirate._name

        if ( self._prev_pirate == 0 ) :

            prev_pirate = "No one"

        else :

            prev_pirate = self._prev_pirate._name

        if ( self._gender == "He" ):

            gender = "him"

        else :

            gender = "her"

        return "Pirate: #" \
               "" + str( self.get_id() ) + " is called " + self._name + "" \
               ", and before "+ gender +" are: "+ prev_pirate + " next to "+ gender +" are: " + next_pirate


class Pirates() :

    # Fields
    _first_pirate = 0

    _current_pirate = 0

    _pirate_counter = 0


    # Contructor
    def  __init__(self):

        self._pirate_counter = 0

        self._current_pirate = 0

        self._first_pirate = 0


    # Methods
    def push_pirate(self, **kwargs) :

        # Prepare - vars given
        name = ""

        gender = ""

        for key, value in kwargs.items():
            # print( "The value of {} is {}".format(key, value) )

            if ( key == "name" ) :

                name = value

            if ( key == "gender" ) :

                gender = value


        # Validate - name
        if ( name == "" ) :

            name = "No name"

        if ( gender == "" ) :

            gender = "Unisex"


        # Prepare - next pirate id
        new_id = self._pirate_counter + 1

        self._pirate_counter = new_id


        # Construct person parent
        pirate = Pirate(
            new_id,
            name,
            gender
        )


        # Push - pirate into the linked list
        if ( self._current_pirate == 0 ) :

            pirate._prev_pirate = pirate

            pirate._next_pirate = pirate


            self._first_pirate = pirate

            self._current_pirate = pirate

        else :

            current = self._current_pirate

            current._next_pirate = pirate


            pirate._prev_pirate = current

            pirate._next_pirate = self._first_pirate

            self._current_pirate = pirate

            self._first_pirate._prev_pirate = pirate


    def start_the_game(self) :

        print()

        print( "! Welcome to the party of who is the best pirate !")

        print()

        print( str(self._pirate_counter) + " pirates joined the party")

        print()

        print( "Pirates joining the game are as follows: ")


    def print_pirates(self) :

        first = self._first_pirate

        current = self._first_pirate

        next = 0

        i = 0

        while i < self._pirate_counter :

            print( current.to_string() )

            next = current._next_pirate

            current = next

            i += 1


    def pull_current_pirate(self) :

        print()

        print( "Oh no ! Someone got planked !")

        print( "Sorry " + self._current_pirate._name + " of you go")

        print("-                                    ")
        print("-__________________                  ")
        print("-                        -            ")
        print("-                         -           ")
        print("-                         --           ")
        print("--                        ---           ")
        print("--                        - "+ self._current_pirate._gender +" -          ")
        print("---                         ---         ")
        print("---                           --       ")
        print("---                             -       ")
        print("---                              -     ")
        print("---                               --      ")
        print("---                              ----       ")
        print("--                              - " + self._current_pirate._name + " -       ")
        print("-                                 ---       ")


        prev = self._current_pirate._prev_pirate

        next = self._current_pirate._next_pirate

        prev._next_pirate = next

        next._prev_pirate = prev

        self._current_pirate = prev

        self._pirate_counter -= 1


    def move_to_next_pirate(self):

        self._current_pirate = self._current_pirate._next_pirate


