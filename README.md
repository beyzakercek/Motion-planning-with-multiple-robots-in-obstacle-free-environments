# Motion-planning-with-multiple-robots-in-obstacle-free-environments
1. 2 Turtles will move in a single ROS TurtleSim window. 
2. All turtles should start moving simultaneously (ignore slight drifts). 
3. The motion of the first turtle proceeds in rounds; round-1, round-2, and round-3. The turtle stops moving after it executes 3 rounds. Consider that the starting directions of the turtle in these rounds are as follows: Right, Right, and Left. After the turtle completes its movement in a direction, it moves 0.2 units down, and returns back to its initial location. If the previous direction of the turtle is the same as its current direction, the turtle increases the distance it travels by one unit in the next round; otherwise, it doubles its distance in the next round. For example: For the “Right, Right, and Left” directions of the turtle; the turtle moves 1 unit right in round=1, 2 units right in round=2, and 4 units left in round=3. 
4. The motion of the second turtle also proceeds in rounds; round-1, round-2, …., round-5. The turtle stops moving after it executes 5 rounds. In each round, the turtle draws a half circle. The radius of each half circle up to round-5 is as follows: 1.0, 1.6, 2.2 , 2.8, and 3.4. You can change the values as long as you maintain the concentric half circles motion pattern that the turtle follows. 
5. Each turtle should always face the direction it moves. 
6. You should create one python node to control turtle1 and a separate python node to control turtle2. 
7. Create a launch file that will start the ROS Turtlesim also the motion of two turtles simultaneously.

![image](https://user-images.githubusercontent.com/79270344/173448864-ac136826-f8bb-46f7-a001-13ee0188d192.png)
