class State_Machine:
    """
    Mapping for commands
    Position-> move to position state-> state_position
    Repeat  ->move to Repeat state-> state_repeat
    Left,right,up,down,forward,backwards-> move in given direction-> move_left(),move_right(),move_up(),move_down(),move_forward(),move_backwards() respectively
    stop-> stop all motion-> stop()
    set-> set the position-> stop()-> set_position();
    reset-> leave position state without setting position -> state_base()
    """
    _state = None
    
    def __init__(self, State = "Base") -> None:
            self._state = State
    
    
    #The following functions set the states, get_state() returns the current state    
    def state_base  (self):
            self._state = "Base"
            #move back to base position
            print("State is now Base")
    
    def state_position  (self):
        if (self.get_state() != "Base"):
            print ("ERROR not in base state, Current state is:")
            print(self._state)
        else:
            self._state = "Position"
            print("State is now Position")
    
    def state_repeat(self):
        """This takes the object and sets the state to "repeat" if possible (only possible in base state), should only be called in repeat function
        """
        if (self.get_state() != "Base"):
            print ("ERROR not in base state, Current state is:")
            print(self._state)
        else:
            self._state = "Set"
            print("State is now Set")
    
    def get_state(self):
        """This returns the current state of the object
        Returns:
            [string]: [This is the current state]
        """
        return self._state
    
        
    def stop (self):
        print ("Filler function replace please")
        #stop motion in all motors
    
    #This set of functions will hold logic to move in each direction ----------------------------------------------------------
    def move_left (self):
        if (self.get_state() != "Position"):
            print("ERROR INCORRECT STATE")
            return
        self.stop()
        #actuate motor left
        
    def move_right (self):
        if (self.get_state() != "Position"):
            print("ERROR INCORRECT STATE")
            return
        self.stop()
        #actuate motor right
        
    def move_forward (self):
        if (self.get_state() != "Position"):
            print("ERROR INCORRECT STATE")
            return
        self.stop()
        #actuate motor forward
        
    def move_backwards (self):
        if (self.get_state() != "Position"):
            print("ERROR INCORRECT STATE")
            return
        self.stop() 
        #actuate motor backwards
        
    def move_up (self):
        if (self.get_state() != "Position"):
            print("ERROR INCORRECT STATE")
            return
        self.stop()    
        #actuate motor up
        
    def move_down (self):
        if (self.get_state() != "Position"):
            print("ERROR INCORRECT STATE")
            return
        #stop motion in all motors
        #actuate motor down
     #set_position() sets the position and does the calculation, repeat() goes through given trajectory ----------------------------------------------------------  
    
    def set_position(self):
        #give the position here? or does this just need to send a signal that its time for calculation? idk
        #probably some matlab stuff
        self.state_base();
        
    def repeat(self):
        self.state_repeat()
        #do the motions of repeating? just send activation signal?
        #probably do things in matlab
        self.state_base()
        
#Test Code   
instance = State_Machine()
print(instance.get_state())
instance.state_position()
print(instance.get_state())
instance.state_repeat()
instance.stop()
print(instance.get_state())
        