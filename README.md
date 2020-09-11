# Escape from maze

**Escape from maze** is my pet project console game. 

### Project schema

![](schema/project_schema.png)

### Description
Player appears in random generated maze. 
The win condition is collect four keys. But it is not that simple, there are some enemies in maze 
which you should avoid.

![](images/game.gif)

If you lose

![](images/lose.gif)

If you win

![](images/win.gif)


### Maze generation
Before the game start, there is a possibility to choose a size of maze. 
If you change the size, the structure of maze will change too.

![](images/size.gif)

### Enemies
Player moves in the main thread, but enemies moving is in another thread. 
**EnemiesManager** manages moving of every enemy. 
Also there is a possibility to change enemies amount and theirs speed.

![](images/enemies.gif)


### Objects appearance
Object appearance consists of char and color, and both may be changed.

![](images/views.gif)


### Play
The command to start game
```shell script
$ python start.py
```