# Cov-Lang
Repository of Compilation Techniques (Learning) with [Library SLY](https://sly.readthedocs.io/en/latest/sly.html).

## Our Grup:
- Agaphier Redha Bramadya(4611418005)
- Anisa Meidina (4611418015)
- Ivan Permana (4611418033)

# Documentation

## You Must Know

- [x] this language is created using the SLY library which is supported with [PYTHON version 3.*](https://www.python.org/ "Python")
- [x] this language has the extension .cov
- [x] the name of this language was inspired by COVID-19 

## Command in Cov-Lang

| COV-LANG |  MEAN  |
| -------- |  ----  |
| JK       |  IF    |
| CET 	   |  PRINT |
| MAK      |  THEN  |
| LAI      |  ELSE  |
| UNT      |  FOR   |
| FNGS     |  FUN   |
| SAM      |  TO    |
| ->       |  ARROW |


## How To Use 

**Follow this steps**
1. Open CMD or TERMINAL with the directory this folder directory `cd .../Cov-Lang/`
2. And then run file main.py in the Cov-Lang folder

for ex:
Copy paste this text to your cmd or terminal
```
python .main.py .bahasaku.cov
```

**_NOW, YOU CAN DO IT_**

> You can edit file code in the `Bahasaku.cov`

## Examples Cov Lang

### PRINT Hello World!!

**example:**
```
CET "Hello World" 
```

**result**
```
Hello World
```

**or:**
```
a= "Hello World"
CET a 
```

**result**
```
"Hello World"
```

### Addition, Subtraction, Multiplication, Division


**example:**
```
3+2
4-1
3*3
4/2
```

**result**
```
5
3
6
2
```

**or**
```
a=6
b=2
CET a+b
CET a-b
CET a*b
CET a/b
```

**result**
```
8
4
12
3
```

### IF ELSE 

> IF _expr_ THEN _stmt1_ ELSE _stmt2_

**example:**
```
a=6
y="true"
n="false"
JK a==6 MAK CET y ESLE CET n
```

**result**
```
"true"
```

### FOR

> FOR _expr_ TO _stmt1_ THEN _stmt2_

**example:**
```
UNT i=0 SAM 5 MAK CET i
```

**result**
```
0
1
2
3
4
```

### Function

> NUF functionName() -> Your Code Here...

**example:**
```
NUF mantul() -> CET "Mantap Betul!!"

mantul()
```

**result**
```
Mantap Betul!!
```

**or:**
```
NUF loop() -> UNT i=0 SAM 5 MAK CET i

loop()
```

**result**
```
Mantap Betul!!
```

### Use Comment

> You can use `'#'` symbol to make comment in your source code.

**example:**
```
I = "U" #but U not I
JK I == "U" MAK CET "I LOVE U" ESLE CET "I HATE U"
#now you know how this works
```

**result**
```
"I LOVE U"
```

Good luck, Thanks :)

# NOTE
This is a modified source code for the howCode programming language series.

You can watch the video accompanying this series here: [https://www.youtube.com/playlist?list=PLBOh8f9FoHHgPEbiK-FSdSw3FiyP78fbk](https://www.youtube.com/playlist?list=PLBOh8f9FoHHgPEbiK-FSdSw3FiyP78fbk)