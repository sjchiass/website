---
title: Review of VSI Computer Science
date: 2020-11-01T17:25:00
tags:
- books
- vsi
author: Sebastien Chiasson
summary: What I learned from the book
---

`ISBN 978-0-19-873346-1`

### General impression

I think the book was alright. I thought that the author was very good at explaining most abstract concepts, but I found his explanations of more concrete things unsatisfying. I liked his explanations of algorithms and computer engineering, but I didn't enjoy his talk of "liminal artefacts" and "symbol processing systems". I'm still not sure what these are.

It seems a bit like the book was better with things I already knew of, but new concepts were harder for me to understand. That said the good parts were enjoyable to read and maybe re-read.

### Lesson 1: computational thinking

The last chapter and the epilogue bring up the idea that computer science is a basic science that accesses something basic about the universe. Computers are complex systems that you can't really understand by studying, say, the physical properties of silicon. To understand the computers, you have to start at computer science.

In other words, what do you need to understand the universe? A good knowledge of mathematics and physics maybe? How would you explain computer systems without computer science? There's something about computer science that feels fundamental and a bit necessary, especially when you have a complex computer on your desk.

I think the author did a good job of setting up this argument. In the rest of the book you're given examples of our human intellect needing tricks to deal with computers. We can't really design computer hardware all on our own, for example, because it's too complex. So computer science is the entrance to the world of computers.

#### Computers affecting people

Computers might then be teaching us fundamental skills we would not otherwise have. If you spend all day programming algorithms or designing hardware, your mental abilities change. You can start designing non-computer algorithms better, and you can better design non-computer systems. You might then have ideas that you would not have otherwise, such as approaching biology as *bioinformatics*.

The author brings up a good comparison with the theory of evolution. Evolution has given us a lot of other ideas.

### Lesson 2: algorithms

I thought that the author explained these well. Algorithms are *fully* defined procedures for getting an output out of an input. Heuristics are not fully defined and are more like reusable strategies (ex: divide and conquer). As I understood it, algorithms are more easily fed to computers; however, not all heuristics can be programmed into computers, and heuristics can be used by humans to make computers.

The author defines algorithms as fully-defined procedures that are self-contained and can be broken down into primitive steps. He gives the example of doing multiplication with pen and paper: if the inputs are always whole numbers, you always know what you have to do to get the output products.

#### Algorithm design

One interesting thing that he mentions is algorithm design. I enjoy reading about things like this. When you think of a similar problem, you use analogical reasoning. By using a familiar strategy, you use heuristic reasoning. By using a formal theory in the problem domain, you use theoretical reasoning. The authors offers us a glimpse of the algorithm designers by showing us the tools of the trade.

#### Procedural knowledge

Another interesting idea is that algorithms are procedural knowledge. This can be understood in two levels. The first is that "I can learn more about something by reading its algorithm", so that algorithms are a source of information. The second is that "the definition of a thing is its algorithm", so that the algorithm is how you see the thing itself. How do you define multiplication? Well, here's how you multiply two numbers with pen and paper.

### Lesson 3: heuristics

Heuristics are explained in the later chapters. Unlike algorithms, we do not know heuristics as fully-defined procedures. Rather, we know heuristics as general solutions or strategies. While algorithms are single solutions to single problems, heuristics are malleable solutions to varied problems.

The author helps us understand heuristics by making us think of their use outside of computers. For example, I know that I use heuristics for putting the dishes away. I start with the items that can be removed without making others fall. I also tend to favour larger and heavier items first. At some arbitrary point I decide to put away the utensils.

An example of a well-known heuristic is divide-and-conquer.

Heuristics are very general but can still be used with computers. The heuristic may be better than an algorithm when the algorithms are too costly, the algorithms don't exist, or we don't sufficiently understand the problem we're trying to solve. In these cases, heuristics can provide the solution.

#### Satisficing

*Satisficing* is how the author describes imperfect solutions still end up being satisfactory. Rather than coming up with a perfect algorithmic solution, you can come up with a satisfactory heuristic solution instead. For example, how would you design a chess-playing computer program? Rather than solving the game of chess completely, the author says, you can give the human player a moderate challenge by using *satisficing* solution.

### Tidbits

Computer programs are *liminal* artefacts that are algorithms written in computer languages.

Computer architecture refers both to the "inner" physical architecture of the circuitry and the "outer" architecture of the instruction set.

### Final thoughts

I wonder how much of this book I'll remember. I'll probably think of it when I hear about algorithms and heuristics. When I hear about computer science I might now recall "computational thinking".
