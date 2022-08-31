  *    .  *       .             *
                         *
 *   .        *       .       .       *
   .     *
           .     .  *        *
       .                .        .
.  *           *                     *
                             .
         *          .   *
''')
print("Welcome to my spooky treasure hunt!")
print("Your mission is to find the treasure.") 

print("You start your journey and reach a fork in the road.")
print("Would you like to go left or right?")
first = input("Select left or right: ").lower()
if first != "right":
  print("You were abducted by aliens. You lose.")
  print('''
                _____
             ,-"     "-.
            / o       o \.
           /   \     /   \.
          /     )-"-(     \.
         /     ( 6 6 )     \.
        /       \ " /       \.
       /         )=(         \.
      /   o   .--"-"--.   o   \.
     /    I  /  -   -  \  I    \.
 .--(    (_}y/\       /\y{_)    )--.
(    ".___l\/__\_____/__\/l___,"    )
 \                                 /
  "-._      o O o O o O o      _,-"
      `--Y--.___________.--Y--'
         |==.___________.==| 
         `==.___________.==' 
        ''')
else:
  print("You come to a lake.")
  print("Do you want to swim across or walk around?")
  second = input("Select swim or walk: ").lower()
  if second != "walk":
    print("The Loch Ness Monster took you away. You lose.")
    print('''
                          _   _       _a_a
              _   _     _{.`=`.}_    {/ ''\_
        _    {.`'`.}   {.'  _  '.}  {|  ._oo)
       { \  {/ .-. \} {/  .' '.  \} {/  |
     ~`~^~`~^~`~^~`~^~^~`^~^~`^~^~^~^~^~^~`^~~`
          ''')
  else:
    print("You get to the other side of the lake and find a building.")
    print("Do you go inside or keep looking around?")
    third = input("Select inside or look: ").lower()
    if third != "inside":
      print("A vampire came and sucked your blood. You lose.")
      print('''
                 _..__.          .__.._
               .^"-.._ '-(\__/)-' _..-"^.
                      '-.' oo '.-'
                         `-..-'  
            ''')
    else:
      print("Yay! You found the treasure! It's a room full of cats!")
      print('''
                   /)
                  ((
                   ))
              ,   //,
             /,\="=/,\.
            /` d   b `\.
           =\:.  Y  .:/=
            /'***o***'\.
           ( (       ) )
           (,,)'-=-'(,,)
            ''')
