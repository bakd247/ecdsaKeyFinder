# ecdsaKeyFinder

A Python based ECDSA secp256k1 private key recovery tool
This tool is intended to be used by anyone who has forgotten thier password to their wallet and would in fact have the public key.

This tool cannot be used to find a private key from an address.
It can only be used to recover the private key belonging to a Known Pulbic Key.

If your wallet has signed transacitons to spend coins in the past then the public key is makde public at that point. Address reuse is highly discouraged because of the vulnerability that this tool exploits.

This Tool is to be used for RECOVERY ONLY of Private Keys...

DO NOT GIVE OUT YOUR KEYS TO ANYONE!!!

By Creating A Very Large List of Collisions and searching through this list there is a Much Higher Probability of Recovering a Private Key from a Known Public Key.

These Collisions are Created using Mulitples of a Public Key by 2 and then iterativley dividing the collision found by 2 until the key being searched for is found.
Please See Source code to Understand the inner Workings of this tool.

Any Recovered Keys can be found in a file called 'foundKeys.txt'.

More on the Math Behind ECDSA at my YouTube Channel Located Here:

https://www.youtube.com/@quitethecontrary1846

Note:

The larger the Size of the Collision List you create...the longer each try will take to search through the list. So there is a point around 1 billion or more collisions in the list where the keys per second starts to take a hit due to the search time of the large Collision List. It is recommended to keep your Collision List lower than 4 Billion Keys for the maximum "hash rate"/ "key creation per second rate".

This tool works best with python3

Please Be sure to install the tinyec and hashlib package in pytohn3 before running this benchmark with the folowing command.

pip install tinyec


pip install hashlib


Please check back periodically for updates and optomizations.
