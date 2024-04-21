---
og:description: "How to work with VS Code behind proxy with self signed SSL certificates"
giscus: 3a8ff637-6397-4a0d-a4ce-087660d906df
---

# Using VS Code with self signed SSL certificates behind proxy

Similar to the case I mentioned in [my previous
post](using-pip-and-pipenv-with-self-signed-certificates.md), you may want to
use VS Code behind a proxy which also signs SSL traffic with a self signed
certificate. In that case, Internet related features of the VS Code like
Extensions Marketplace won't work.

## Solution

### SSL certificate

If we know that the proxy checks the certificates correctly and signs the packets
with a self signed certificate, we can safely ignore certificate errors by
trusting the proxy.

Just start the VS Code with the `--ignore-certificate-errors` flag like

```shell
$ code --ignore-certificate-errors
```

```{warning}
This approach is suitable if you **know** that you are behind a proxy or a
similar equipment that signs the traffic with self-signed certificates.
Since `--ignore-certificate-errors` flag disables SSL checking, this will
cause a potential security risk if you are not in such network, like working
at home.
```

### Proxy

You can set proxy for system wide or just for VS Code.

#### Using environment variables

On Linux (and probably somehow on Windows), you can use environment variables
to pass proxy information to VS Code. Environment variables are processed in an
order [^1f]. According to this, setting `https_proxy` should be sufficient.
Generally, I set both `http_proxy` and `https_proxy` on my systems. I did a
small test to check effects of setting variables on VS Code.

| https_proxy | http_proxy | Works? |
|-------------|------------|--------|
| Correct     | Correct    | Yes    |
| Correct     | Incorrect  | Yes    |
| Incorrect   | Correct    | No     |
| Incorrect   | Incorrect  | No     |

As you can see, setting `https_proxy` is sufficient but I recommend to set
both `https_proxy` and `http_proxy` on your system because other software
may use both of them.

For example, you can set an environment variable on Linux with `~/.bashrc`. You
may add the following commands at the end of the file

```bash
export http_proxy="http://<ip.addr>:<port>"
export https_proxy=$http_proxy
```

#### Only for VS Code

You can also set proxy information just for VS Code. To set proxy URL just for
VS Code, go to `File` → `Preferences` → `Settings` and search for `Proxy` then
enter the proxy URL in `Http: Proxy`. You can leave other settings at default
values. (You don't need to disable `Http: Proxy Strict SSL`.)

Without using GUI, in `settings.json` set
`"http.proxy":"http://<ip.addr>:<port>"`

*Published on: 2020-11-26*


[^1f]: <https://github.com/microsoft/vscode/issues/84845#issuecomment-558952807>
