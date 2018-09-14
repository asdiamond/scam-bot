#!/usr/bin/env python3

# A tech support scammer bot
# Authors: asdiamond, eseymour
# for liscence information see LICENSE
# a translation table used to convert
# things you say into things the computer
# says back, e.g. "I am" -> "you are"
#
# Inspired by the chatbot demos in nltk

import platform, re, nltk

from nltk.chat.util import Chat, reflections

system = platform.system()
processor = platform.processor()
architecture = platform.architecture()[0]
node = platform.node()
dist = platform.dist() if system == 'Linux' else None
distFull = f"{dist[0]} {dist[2]}" if dist else None

# a table of response pairs, where each pair consists of a
# regular expression, and a list of possible responses,
# with group-macros labelled as %1, %2.

name = "bobert"

pairs = (

    (r'Who is this',
     (f"I'm {name} calling from the {system} help desk.",
      f"\nHello, I'm {name} from the {system} help desk. We have"
      f"\ndetected errors in your {processor} {architecture} processor's"
      f"\nmicrocode. We need to update your {node} {distFull} machine " # FIXME distFull is None on windows.
      f"\nto the latest microcode to ensure your security",
      f"\nThis is the {system} help desk.")
     ),
    (r'My (.*) is not a (.*) it is a (.*)',
     ("This is the %3 help desk",
      "Yes sir, we can help with your %3 system")
     )

)


tech_support = Chat(pairs, reflections)


def main():
    print("Tech support\n-----------")
    print("Enter quit when done.")
    tech_support.converse()


if __name__ == '__main__':
    main()
