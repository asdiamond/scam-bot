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
      f"\nmicrocode. We need to update your {node} {distFull} machine "  # FIXME distFull is None on windows.
      f"\nto the latest microcode to ensure your security",
      f"\nThis is the {system} help desk.")),

    (r'Where (.*)',
     (f"I'm {name} calling from the {system} help desk.",
      f"I'm {name}",
      # f"Jesus, I have already told you I am {name}!!",
      f"Yes yes, the {system} help desk")),

    (r'what is wrong',
     (f"we need to upgrade your {node} {distFull} machine because of a microcode error.",
      f"there is a serious error in your {node} {distFull} computer's processor",
      f"you need to let us update your computer")),

    (r'My (.*) is not a (.*) it is a (.*)',
     ("This is the %3 help desk",
      "Yes sir, we can help with your %3 system")),

    (r"(.*) dont know (.*)",
        (f"")),

    (r'(.*) why (.*)',
     (f"Im sorry sir, we need to install a microcode update for your security",
      f"for your security!!"))
)

tech_support = Chat(pairs, reflections)


def main():
    print(f"\nHello, I'm {name} from the {system} help desk. We have"
          f"\ndetected errors in your {processor} {architecture} processor's"
          f"\nmicrocode. We need to update your {node} {distFull} machine "  # FIXME distFull is None on windows.
          f"\nto the latest microcode to ensure your security")
    print("Tech support\n--------------------------------------------")
    tech_support.converse()


if __name__ == '__main__':
    main()
