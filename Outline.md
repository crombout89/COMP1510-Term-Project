# Critter Rescue Kitty

* Two levels, the ground and treetops. Each will have randomly generated critters to help.
    * There are tree trunks on the ground, you have the option of either going around them or climbing them
    * In the treetop level, the center square is the tree trunk and allows you to climb back down
        * You will start at the center trunk block after climbing up a tree
        * When you climb down a tree, you will return to the same block you were while on the ground, it doesn't make sense to appear in the same block as the tree trunk at ground level 
    * Trees grow berries which can be picked up while exploring the canopy
        * No distinction between tree species, any tree can produce any colour berry
        * You don't have to manually pick them up, moving across a block that contains a berry will automatically add it to your inventory

* Collect different coloured berries on the ground and in trees. 
    * Here's what I have in terms of what colours treat what ailments: 
        * Red: Injury
        * Green: Poisoning
        * Blue: Dehydration
        * Yellow: Burns
        * Purple: Sadness (it's basically an antidepressant lol)
        * Any berry can treat starvation.
    * You start the game with 2 of each berry in your inventory
        
* Find animals both on the ground and in a tree
    * The game will tell you what's wrong with the animal
        * Colour code this text with the colour of the correct berry
    * You can either give them the right berry to help them or walk past (for example, if you don't have the right berry)

* Animals you help will give you extra berries and other items in return.
    * They will give you 2-5 randomly chosen items
    * The more animals you help, the more items they give you and the more likely they are to give you power ups
    * (Important: Have logic that prevents them from giving you the same berry that you used to treat them, since that wouldn't make sense and they could have just eaten that berry themselves)

* Have a tummy mechanic which is kind of a stand-in for a stamina meter. 
    * Start at 100
    * The more you move around and climb, the hungrier you get. 
        * -1 for moving one block
        * -5 for climbing up or down a tree
    * Give warnings at tummy level 10, 5, and 1
    * Eat any berry to refill your tummy by 10
    * Some spots on trees will allow you to take a cat nap, which will also refill your tummy by 10
    * If it reaches zero the game is over and you have to restart.
    
* Find catnip in the forest or as gifts from animals you help.
    * Eating catnip gives you extra energy for 25 moves, your tummy level won't go down during this duration
    
* Silver vine is another plant that cats really like (also contains nepetalactone, the same "cat drug" chemical as catnip)
    * Similar to catnip but is much rarer
    * Gives you extra energy for 50 moves and also fills your tummy to 100
    
* Entity generation and board layout
    * Starting board is 25x25
    * Trees locations are randomly generated when you load the game
    * Tree canopies can are different sizes but are always square
        * 3x3 5x5, 7x7, or 9x9
        * Always has odd number side lengths so it has a center block that is the tree trunk
    * All other entities are generated dynamically similar to the lab.
        * The game calls the generate function when you move to a given block
        * Only one thing is generated per block
        * Can generate nothing, an animal, a berry (if in a tree), catnip, or silver vine
        * Animal and berry both have 20% probability, but animal generation takes priority
            * (if the RNG generates both an animal and a berry, only an animal will be generated)
        * Catnip probability is 5%, takes priority over animals and berries
        * Silver vine probability is 1%, takes priority over everything else
        
* Plot
    * Kitty's owner is a environmental science professor studying the forest
    * They live in a cabin at the edge of the woods
    * Kitty asks the Professor to go out and play in the forest
    * Professor tells her no, that she'll eat all the critters he's trying to research and protect
    * Kitty promises to not only not eat any of the critters, she will play an active role in helping them
    * Base goal: Help 25 animals
    * Once the goal is reached, she has proven herself to the Professor and he lets her stay out as long as she likes
    * Enters high score mode where the player tries to help as many critters as possible
    


