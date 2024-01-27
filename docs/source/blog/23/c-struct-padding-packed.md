# Do not let the structure padding ruin your day

*Be careful with the memory alignment, a True 🇨 story*

Structures (the `struct` keyword) in C are widely used, especially in the
embedded world. For a couple of months, I have been writing a C program targeted
to a [Microblaze](https://www.xilinx.com/products/design-tools/microblaze.html)
processor, a 32-bit soft processor from AMD (Xilinx). While adding new features
to the existing code this week, I added a 1 char member to an existing
structure. After compiling the code, I noticed that the size of the elf file
(compiled code) decreased by 1.2 KB! The target is limited by 32 KB memory, and
I was close to the limit. 1.2 KB reduction was a huge improvement. So what
happened? I added a new code + 1 char and the size decreased, how? First, I
thought that the code I wrote was wrong and that the compiler was optimizing the
existing code due to a reason, such as dead code elimination. Then I immediately
realized that the change was due to 1 char addition to the existing structure,
not related to the newly added code. But how?

If you are new to C programming, you may think that members of a struct are
placed in memory contiguously, like C arrays. **⚠️ However, this assumption is
incorrect.** A C compiler is free to insert padding bytes after structure
members to generate optimized and faster codes for the target architecture.
However, you can force the compiler not to insert **padding bytes** and to lay
the struct members in the memory contiguously, like an array. For example,
adding the **packed** attribute to a struct, `__attribute__((__packed__))`,
forces GCC to do that. There could be several reasons for doing that, and this
is out of scope for now, but my struct was *packed* too.

My structure is a little bit complex, 6-7 level of `struct`s and `union`s, and I
didn't notice that my 32-bit members were not word-aligned, i.e. on a 4-byte
boundary. Therefore, when I accessed a 32-bit struct member, like `x.y =
0x12345678` , the compiler was generating around 25 instructions to set a
variable! The word size of Microblaze processor is 32-bit, and it can work with
32-bit numbers natively given that they are stored on addresses that are a
multiple of 4: 0, 4, 8, 12, and so on.

```text
  Proper Alignment:

  |   0   |   1   |   2   |   3   |
0 |      32 bit  word  member 1   |
4 |      32 bit  word  member 2   |
```

*Native* access (read/write) generates 1 or 2 instructions, not 25! Since I was
forcing the compiler not to add padding bytes and did the alignment wrong, the
32-bit members were unaligned, on addresses like 3, 7, 11... When this happens,
most of the time the C compiler generates (and has to) very inefficient code:
lots of byte access instead of word access, weird arithmetic and logical
operations and so on... This is true for most architectures. I knew this before,
but this time due to the complexity of the data structure, I made an alignment
mistake, damn! 🤦

```text
  My Case 🤦:

  |   0   |   1   |   2   |   3   |
0 |                       |   32  |
4 |  bit word member 1    |   32  |
8 |  bit word member 2    |  32.. |
```

So what happened when I added 1 char to my struct? You guessed right! I added
the `char` before 32-bit members and due to the new 1-byte member, they were
suddenly *pushed* to 4-byte alignment. The compiler was able to generate more
efficient instructions for the existing code sections that access those 32-bit
members. So even I added new code, optimization of previously unoptimized
sections decreased the final size.

## Moral of the story

👉 In C, you can not assume that struct members are contiguous in memory, like
array members. Depending on the target architecture and the struct, most
probably, there will be padding bytes. If you are hearing this fact for the
first time and your existing code relies on this wrong assumption, please make
sure that you learn the limitations of structures well before padding bytes
gives you a headache.

👉 For some reason, you may not want those padding bytes. In this case, check
your compiler's manual to learn how to do this. This is a compiler-specific
feature, not a part of a C standard.

👉 **Padding byte is not evil!** These bytes are added to help generate more
optimized code by compilers. You may think of them as a waste of memory, but if
you screw up with the alignment, your loss will be many times greater +
unoptimized code runtime penalty. If you are packing the struct, just make sure
that the alignment is still correct. Note that even if you allow padding bytes,
which is the default behavior as I mentioned, you may minimize them by ordering
the struct members carefully. But this is not our scope for now.

👉 If you are targeting a memory-limited platform or writing a
performance-critical code, I find skimming over the generated assembly code by
the compiler time-to-time beneficial.

See you! 🙋‍♂️

```{disqus}
:disqus_identifier: b96a82d4-022a-458e-ae9d-067d3848d409
```
