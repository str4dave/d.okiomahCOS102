{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your state of origin is:  Akwa Ibom \n",
      "The first character is:  A\n",
      "The characters starting from 3rd to 5th are:  wa \n",
      "The string starting from 3rd character is:  wa Ibom \n",
      "State of origin 2 times Akwa Ibom Akwa Ibom \n"
     ]
    }
   ],
   "source": [
    "str = input(\"Enter your state of origin: \")\n",
    "\n",
    "print(\"Your state of origin is: \", str)\n",
    "print(\"The first character is: \", str[0])\n",
    "print(\"The characters starting from 3rd to 5th are: \", str[2:5])\n",
    "print(\"The string starting from 3rd character is: \", str[2:])\n",
    "print(\"State of origin 2 times\", str*2)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}