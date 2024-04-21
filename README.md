# ayazar.dev

[My](https://ayazar.dev) personal web page + notes

## Checking Broken Links

```shell
docker run --init --rm -it -v ${PWD}:/input lycheeverse/lychee -c /input/lychee.toml --exclude-path /input/vendor "/input/**/*.md"
```

## Linting Markdown Files

On Linux:

```shell
sudo docker run -v $PWD:/workdir ghcr.io/igorshubovych/markdownlint-cli:latest "**/*.md"
```

On Windows (?):

```shell
docker run -v ${PWD}:/workdir ghcr.io/igorshubovych/markdownlint-cli:latest "**/*.md"
```
