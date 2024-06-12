---
og:description: "Installing DokuWiki on a mail disabled server requires a little modification"
giscus: 34d4f976-82d7-40cb-b3ee-6b88b8218c50
---

# Install DokuWiki without Mail Support

[DokuWiki](https://www.dokuwiki.org/) is great. But it requires `mail()` PHP
function for registration or subscriptions. However, depending on your needs you
don’t have to use mail feature of DokuWiki. For single user or registration
closed typed wikis mailing is not essential. You may want to install DokuWiki on
a server where `mail()` function is not available. Some hosting providers may
disable `mail()` function. When you try to install DokuWiki, it gives you an
error like that:

```text
PHP function mail is not available.
```

`install.php` doesn’t allow you to install DokuWiki. To fix this problem, ( for
**2014-09-29b "Hrun"**):

1. Open `install.php`
2. Locate `check_function` around **line 554**.
3. Find `mail` in `explode(' ', 'addslashes call_user_func … ini_get mail mkdir
   …');`
4. Delete `mail` from that text. (Put a space between `ini_get` and `mkdir`, not
   leave as `ini_getmkdir` !)
5. Save `install.php`
6. Now, install your DokuWiki

Don't forget that DokuWiki still is not able to send mails. This steps just
allow us to skip checking mailing feature on installation.

*Published on: 2014-12-31*
