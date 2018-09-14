#!/usr/bin/env python3

import platform, re, nltk


from nltk.chat.util import Chat, reflections

system = platform.system()
processor = platform.processor()
architecture = platform.architecture()[0]
node = platform.node()
dist = platform.dist() if system == 'Linux' else None
distFull = f"{dist[0]} {dist[2]}" if dist else None

print(f"I'm {{name}} calling from the {system} help desk. We have detected \
errors in your {processor} {architecture} processor's microcode. We need to \
update your {node} {distFull} machine to the latest microcode to ...")


def main():
    nltk.chat.eliza.demo()


if __name__ == '__main__':
    main()
