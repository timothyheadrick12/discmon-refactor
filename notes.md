# Plan for Project Structure

## Game class

---

- On input receive save frames from slightly before input to slightly after input as gif.

- Should constantly be ticking. No reason not to currently. Possibly implement pausing

- Create eventstack so that events can overflow then execute in order

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
