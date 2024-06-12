---
og:description: "VS Code allows us to recommend extensions to developers along with code."
og:image: assets/social/blog/22/vscode-recommend.jpg
giscus: 12a9459d-22ba-41b6-af06-bec07545f2d6
---

# Recommend Visual Studio Code extensions along with your code

```{figure} /extra/assets/social/blog/22/vscode-recommend.jpg
:align: center
:figclass: thmbnl
```

---

[Visual Studio Code](https://code.visualstudio.com/), VS Code in short, is a
very popular editor (my main editor for several years) among many developers
[^1f]. Its power is at least doubled by [variety of
extensions](https://marketplace.visualstudio.com/vscode). **In this post, I will
show you a way of recommending VS Code extensions to developers along with
code.** [The
steps](https://code.visualstudio.com/docs/editor/extension-marketplace) are
already explained by Microsoft but here I will add my tips.

## Basics

If you open a project in VS Code and the root of the project has a directory
named `.vscode` then the editor searches some specific files in that directory.
One of them is `extensions.json`. This file enables us to recommend extensions
with our code. As an example, let's look at source code of my blog. Source code
of my blog is open and [hosted on Github](https://github.com/alperyazar/home).

```{figure} assets/vscode-recommend-1.png
:align: center

My blog as an example
```

If you clone or download source of [my
blog](https://github.com/alperyazar/home), you will see
`.vscode/extensions.json`. Notice that lines started with `//` are shown in red
by Github, I will come to this issue later. For now, 8 extensions are
recommended in this file. If you open the project (via `File` → `Open Folder`)
with VS Code and if recommended extensions are not installed (or partially
installed) on your system, you will see a box at bottom right of the editor
asking for installing recommended extensions.

```{figure} assets/vscode-recommend-2.jpeg
:align: center

Asking for installing recommended extensions
```

`Install` will install all recommended extensions as the name suggests. Click
`Show Recommendations` to see recommended extensions. They are listed under
`WORKSPACE RECOMMENDATIONS`

```{figure} assets/vscode-recommend-3.png
:align: center

2 of 8 extensions are not installed on my machine
```

From there, you can install extensions one by one.

```{hint}
If you want to list recommended extensions for a project in any time,
open the project, go to `Extensions` (`Ctrl-Shift-X` by default) and search for
`@recommended`. Here you will see both Workspace Recommendations given by
`extensions.json` and Other Recommendations offered by VS Code itself.
```

Now you see the basics of the mechanism. With your code, create a file named
`extensions.json` under `.vscode` and write names of extensions that could be
useful for other developers working on your project and you're done!

## Working with git

I assume that the project you created `extensions.json` for it is a git
repository. It is not recommended to commit whole `.vscode` directory with your
code since this directory may include some user specific configurations
irrelevant to codebase[^2f]. We should add some rules to `.gitignore`. I
recommend to use [template suggested by Github
team](https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore)
for this purpose. The template looks like this:

```text
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
!.vscode/*.code-snippets

# Local History for Visual Studio Code
.history/

# Built Visual Studio Code Extensions
*.vsix
```

The first line excludes all files under `.vscode`. The following lines define
some exceptions. As you can see, `extensions.json` will be in your commits.
Don't forget to add these line to your `.gitignore` file. You can put these line
to anywhere (most probably) in `.gitignore` but don't change their order.
Personally, I don't like tracking `settings.json` with project but you can leave
like this, it won't affect extension recommendation system. [.gitignore of my
blog](https://github.com/alperyazar/home/blob/master/.gitignore) can be taken as
an example.

## extensions.json

This JSON file has a very simple structure:

```json
{
  "recommendations": [
      // Similar (same) markdownlint used in CI
      "DavidAnson.vscode-markdownlint",
      // Easy indentation
      "oderwat.indent-rainbow",
      // .editorconfig
      "EditorConfig.EditorConfig"
  ]
}
```

You list names of recommended extensions one by one.

### Wait! This is an invalid JSON file!

**Yes!** You can not comment in JSON with `//` or `/**/` or with any
character[^3f]. JSON doesn't support comments. So, if you try to validate the
example with a [validator/linter](https://jsonlint.com/), you will get errors.
Do you remember the first image where lines starting with `//` are in red? This
is because parser of Github thinks that there is a syntax error and yes, there
is. BUT, VS Code allows comments in its configuration files (like
`extensions.json`) with **JSON with Comments (jsonc).**[^4f] Therefore, it is
valid to have C-like comments in `extensions.json`. **I highly recommend
commenting** for each extensions like writing purpose of the extension or human
readable name of it since some extension names could be little cryptic. If your
project CI pipeline runs some JSON linter on all project files ending with
`.json`, this may cause your CI pipeline to fail. Don't forget to exclude
`extensions.json` (if you are adding comments) from JSON linting process if you
have any.

## Finding names of extensions

The last step is adding extensions names to `extensions.json` file. How can we
find the names? If the extension is installed on your VS Code, go to
`Extensions` and click little gear symbol (⚙) next to extension name and click
`Copy Extension ID` and then paste into `extensions.json`. The second method is
searching the extension on
[Marketplace](https://marketplace.visualstudio.com/vscode). After finding the
extension, open the extension page and look for `Unique Identifier`.

## Why?

We saw how we can utilize `extensions.json` to recommend VS Code extensions with
code to developers. But why do we want to do this? The purpose is making life of
developers/contributors easier. For example, I use
[indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow)
to make indents more readable. Let's say that you are using
[markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli) with your
CI setup then you may consider adding
[markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
to `extensions.json`. This extension runs same rules with `markdownlint-cli` and
immediately detects linting errors while you typing. This allows contributors to
detect linting errors before pushing anything and waiting CI pipeline (linting)
to fail. This shortens the loop significantly. So if you (as a
repository/codebase maintainer) think that a particular VS Code extension helps
contributors then add it. But don't recommend anything satisfying your personal
choices like color theme, icon set, etc. They won't help other developers much.

## Do not trust developers!

No, please trust them. What do I mean that don't assume that all developers are
using VS Code and they will install all recommended extensions. This is
impossible for open source projects. A contributor may use any editor or even
web IDEs of Github or Gitlab. One may choose to use VS Code without installing
the recommended extensions. So if you are linting markdown files with CI
pipelines, you should consider suggesting some extension to developers to make
merge/pull request loops shorter. But you should have always linting tests
running before merging and you should assume that all recommended extensions are
disabled by developers.

Happy (VS)coding!

*Published on: 2022-09-03*

[^1f]: <https://survey.stackoverflow.co/2022/#most-loved-dreaded-and-wanted-new-collab-tools-love-dread>
[^2f]: <https://stackoverflow.com/questions/32964920/should-i-commit-the-vscode-folder-to-source-control>
[^3f]: <https://stackoverflow.com/questions/244777/can-comments-be-used-in-json>
[^4f]: <https://code.visualstudio.com/docs/languages/json#_json-with-comments>
