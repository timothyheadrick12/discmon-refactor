# Plan for Project Structure

## Game class

---

- On input receive save frames from slightly before input to slightly after input as gif.

- Should constantly be ticking. No reason not to currently. Possibly implement pausing

- Create eventstack so that events can overflow then execute in order

- Need events that interrupt the main control flow no matter what is happening (In case of Pokemon for battles, people talking to you, etc)

  - interruptEvents should all have a condition in them that checks if they are happening. This condition will contain all the event's code.

    - "All the code for the event" means the event completely takes over the mainLoop and must manually tick the emulator and handle logic.

  - All interrupt events needed should be initialized by the child class (i.e. PokemonEmulator) in an init that pushes them into the interruptEvents list.

  - The Game class will loop over all possible interruptEvents each tick no matter what is happening.

---

## PokemonEmu class

---

- Put all Pokemon specific events within this class.

- Some events in the Pokemon class might require a lot of padding for gif recording. i.e pressing A when reading text.

- Will need to check tiles of the tilemap occasionally in order to see if battles have started or something similar.

---

## DiscordClient class

---

- TODO

---
