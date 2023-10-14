# ecdsaKeyFinder

NOTE:
VERY IMPORTANT!!!
You must have all files shown above in the same directory for this tool to work properly!!!!

If you Do NOT know how to run a python file from a terminal or command line...please learn how to use python before attempting to use this tool!!!

A Python based ECDSA secp256k1 private key recovery tool

This Tool is intended to only recover SECURE KEYS ONLY that are NOT easy to guess or "fast to count to"....please see:
https://allprivatekeys.com/check-bitcoin-address-in-leaked-bitcoin-private-keys-database
first to see if your key is a "SECURE KEY"

This tool is intended to be used by anyone who has forgotten thier password to their wallet and would in fact have the public key.

This tool cannot be used to find a private key from an address.
It can only be used to recover the private key belonging to a Known Pulbic Key.

If your wallet has signed transacitons to spend coins in the past then the public key is makde public at that point. Address reuse is highly discouraged because of the vulnerability that this tool exploits.

This Tool is to be used for RECOVERY ONLY of Private Keys...

DO NOT GIVE OUT YOUR KEYS TO ANYONE!!!

DO NOT USE THIS TOOL FOR THEFT!!! Blockchain data is highly transparent...and easily trackable/tracable!!!

How This Tool Works:

By Creating A Very Large List of Collisions and searching through this list there is a Much Higher Probability of Recovering a Private Key from a Known Public Key.

These Collisions are Created using Mulitples of a Public Key by 2 and then iterativley dividing the collision found by 2 until the key being searched for is found.
Please See Source code to Understand the inner Workings of this tool.(privateKeyFinder.py file)

Any Recovered Keys can be found in a file called 'foundKeys.txt'.

Note:

The larger the Size of the Collision List you create...the longer each try will take to search through the list. So there is a point around 100 Thousand or more collisions in the lists where the keys per second starts to take a hit due to the search time of the large Collision List. It is recommended to keep your Collision List lower than 1 Million Total Keys for the maximum "hash rate"/ "key creation per second rate".

THERE IS NO GUARANTEE THAT A KEY WILL EVER BE FOUND!!!

The method developed as shown on github page is only better than brute force...

so technically it breaks the algorithm but it will STILL take A LOT of time and/or computing power to ever have a chance at finding a key...

The Point is that the chances of recovering a key using this method are 100% greater than using both brute force as well as just plain NOT attempting at all...
Use of this tool Guarantees NOTHING....

This tool works best with python3

Please Be sure to install the tinyec and hashlib package in pytohn3 before running this benchmark with the folowing command.

pip install tinyec

Python Version 3.9 or Later is required


Please check back periodically for updates and optomizations.

More on the Math Behind ECDSA at my YouTube Channel Located Here:

https://www.youtube.com/@quitethecontrary1846
