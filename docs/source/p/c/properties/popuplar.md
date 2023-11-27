# 🎊 popular

C is a popular language, there's no doubt about that. Almost all operating
systems kernels such as Linux are written in the C language. C is also widely used
in embedded systems where microcontrollers are used. Even though C is 50 years
old, C is still one of the most preferred languages for software that needs to
be run close to the hardware, has performance requirements, and takes up little
space. C and C++ are also preferred in applications such as system programming
that run on the operating system but have high performance requirements. When
you write code in C, you can more easily understand exactly what the code you
wrote does on the hardware.

Of course, C is not a language that solves all problems in the most optimal way.
If there was such a programming language, it would be used for all solutions and
there would not be so many languages. But as I mentioned, there are areas where
C shines and there is not much of an alternative. If you work close to these
areas, you can feel how popular C is. Still, people rightfully feel the need to
represent such subjective feelings numerically. **So how can we measure how
popular a language is?**

One of the measures that numerically shows the popularity of a programming
language is the [TIOBE Index.](https://www.tiobe.com/tiobe-index/) There are
various debates regarding the method and accuracy of this measurement, which I
will address in later sections. Let's continue with this measurement for now.

## TIOBE Index

[The TIOBE Index](https://www.tiobe.com/tiobe-index/) is calculated monthly and
measures how popular programming languages are around the world. As of November
2023, when I wrote this article, the C programming language is the 2nd most
popular language. Python ranks 1st and the C++ language ranks 3rd. When we look
at the 35-year history, we can see that the C language has always been among the
top 2 most popular languages [according to this
index.](https://www.tiobe.com/tiobe-index/c/)

## TIOBE Index Flaw

TIOBE Index has a controversial measurement method. They
[states](https://www.tiobe.com/tiobe-index/) that:

> Popular search engines such as Google, Bing, Yahoo!, Wikipedia, Amazon,
> YouTube and Baidu are used to calculate the ratings. It is important to note
> that the TIOBE index is not about the best programming language or the
> language in which most lines of code have been written.

They basically measure the number of results indexed by various search engines
for a programming language [^1f].

Some discussions on the Internet about TIOBE's methodology:

> So how does TIOBE calculate this index? You might not believe this, but they
> count the number of search engine results for each programming language. Not the
> number of people querying, not the number of queries they're making, not
> sentiment. It relies entirely on that useless number that search engines report.

*Source: [Please stop citing TIOBE](https://blog.nindalf.com/posts/stop-citing-tiobe/)*

> This means that (for an example, in theory) you can have a language that
> everyone is talking about that has a lot of hits and gets a high rating even
> though nobody uses it, and you can have a language that lots of people are using
> but there aren't many web pages/hits so it gets a low rating. It doesn't even
> take into account what the web pages contain (for example, imagine a million web
> pages saying a certain language is aweful, that all increase the language's
> TIOBE index).

*Source: [How accurate are the language ratings published in the TIOBE Index?](https://qr.ae/pKNreM)*

> Tiobe's rankings are nothing more than a calculation of web spam on Google. Bad
> languages with lots of articles are ranked just as high as loved languages.
> Languages such as C, get ranked artificially high, most likely due to a flaw in
> the way they are determining Google search results for the single letter C. So
> no, C is not the most widely used, loved or anything language.  It's simply a
> bad algorithm.

*Source: [Why the Tiobe Index Can't Be Trusted](https://www.codehawke.com/blogs/why_the_tiobe_index_can_t_be_trusted.html)*

> But it is so much fun to cite TIOBE!
> People always become happy when you say how Python beats Java now. :)

*Source: [Please stop citing TIOBE (Reddit)](https://www.reddit.com/r/programming/comments/we8kxc/please_stop_citing_tiobe/)*

> Here is the thing: people want some authoritative source backed by science and
> statistics. The TIOBE index checks all these boxes: it is by a reputable (I
> guess) company, it uses a reproducible method, and it publishes its methodology.
> The fact that the methodology and result are complete garbage is irrelevant.

*Source: [Reddit](https://www.reddit.com/r/programming/comments/we8kxc/comment/iip4tv6/)*

As you can see, the topic is quite controversial and there are many opinions
about the meaninglessness of this measurement method.
So are there any other alternative methods?

## TIOBE Index Alternatives

With help of ChatGPT, here some alternatives:

- [Github Octoverse](https://octoverse.github.com/)
- [Stackoverflow Survey
  2023](https://survey.stackoverflow.co/2023/#technology-most-popular-technologies)
  According to that survey, **C language ranks 10th.** This survey says the most
  popular languages are related to web technologies.
- [The RedMonk Programming Language Rankings: January 2023](https://redmonk.com/sogrady/2023/05/16/language-rankings-1-23/)
  Again, C language ranks 10th.
- [PYPL PopularitY of Programming Language](https://pypl.github.io/PYPL.html)
  C/C++ (together) ranks 4th.

Each measurement has its own unique method. I looked at it roughly, but you can
look at the details if you wish.

## So what?

At the end of the day, is C a popular language or not? So is this important to
us? When we look at such measurements, we can see that languages such as Verilog
and VHDL used in the field of FPGA and ASIC design are not popular and
widespread at all, so we certainly shouldn't waste time learning these things,
right? NO! Those languages are mandatory for people working in these fields to
learn. Whether a language is popular or not, we should learn that language if we
need it. As I mentioned at the beginning, **C is a superstar in some areas.** If
you are going to work in these fields or if you are curious, you should learn C.
Other than that, I would say don't worry too much about the popularity numbers.

## Further Read

- [A Hacker News discussion on TIOBE Index](https://news.ycombinator.com/item?id=19767725)

[^1f]: <https://www.tiobe.com/tiobe-index/programminglanguages_definition/>

```{disqus}
:disqus_identifier: 8ad0d052-e480-4569-85ee-ae0af186957b
```
