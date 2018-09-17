#!/usr/bin/env python3

# Scambot is a tech support scammer bot.
# Authors: asdiamond, eseymour
# For license information see LICENSE.

import platform, re, nltk

# reflections is a translation table used to convert things you say into things
# the computer says back, e.g. "I am" -> "you are".
from nltk.chat.util import Chat, reflections

# Inspired by the chatbot demos in nltk

# A series of variables used by Scambot's responses
botName = "Botbert"
system = platform.system()
processor = platform.processor()
architecture = platform.architecture()[0]
node = platform.node()
dist = platform.dist() if system == 'Linux' else None
distFull = f"{dist[0]} {dist[2]}" if dist else None # FIXME distFull is None on windows.

# A table of response pairs, where each pair consists of a regular expression,
# and a list of possible responses, with group-macros labelled as %1, %2.
pairs = (
    (r'who.*(((is)?.*this)|((are)?.*you))?',
     (f"I'm {botName} calling from the {system} help desk.",
      f"Hello, I'm {botName} from the {system} help desk. We have"
      f"\ndetected errors in your {processor} {architecture} processor's"
      f"\nmicrocode. We need to update your {node} {distFull} machine "
      f"\nto the latest microcode to ensure your security",
      f"This is the {system} help desk.")),

    (r'where(.*)',
     (f"I'm {botName} calling from the {system} help desk.",
      f"I'm {botName}",
      # f"Jesus, I have already told you I am {name}!!",
      f"Yes yes, the {system} help desk")),

    (r'what(.*is.*wrong)?',
     (f"we need to upgrade your {node} {distFull} machine because of a microcode error.",
      f"there is a serious error in your {node} {distFull} computer's processor",
      f"you need to let us update your computer")),

    (r'(?:my)|(?:this) (?:.*) is not a (?:.*) it is a (.*)',
     ("This is the %1 help desk",
      "Yes sir, we can help with your %1 system")),

    (r"(.*)don'?t know(.*)",
     (f"")),

    (r'(.*)why(.*)',
     (f"Im sorry sir, we need to install a microcode update for your security",
      f"for your security!!")),

    (r'.*',
     (f"I'm sorry. I can't understand what you're saying.",
      f"I can't understand.",
      f"Your computer needs support.",
      f"This is so important for your security.",
      f"Your computer needs an update for security."))
)

# Create our bot
tech_support = Chat(pairs, reflections)


def main():
    print("Welcome to your tech support chat. This conversation is not monitored.",
          'Please speak in plain English. Enter "quit" when done.',
          "======================================================================",
          f"Hello, I'm {botName} from the {system} help desk. We have detected",
          "errors in your computer.",
          sep='\n')
    tech_support.converse()


if __name__ == '__main__':
    main()
