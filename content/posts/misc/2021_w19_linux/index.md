---
title: Hugo with GH actions
date: 2021-05-09T08:47:04-04:00
tags:
 - linux
 - hugo
author: Sebastien Chiasson
summary: My newbie GH Action setup for updating my website
---

## Basic idea

I have GitHub actions build the Hugo website then I use `scp` to copy it over to my remote server. It's a few extra steps to also deploy the site to GitHub Pages, so I do that too.

It's a little project. Here are the steps.

1. Set up SSH keys to give GitHub access to your server
2. Add "secrets" to GitHub so that your Actions can access hidden variables
3. Add the Action script to your repo (build website > upload to server > build for GH pages)
4. Create a cron job on your server to pick up the files


## SSH keys

The idea here is to generate an SSH key on your computer. You then send the public key to the remote server, and you paste your private key into GitHub. That way GitHub can log into your server and dump the new files there.

If ever something goes wrong with GitHub secrets, you can log into your server and delete the key.

First, generate an ssh key on your computer. Put it in a separate place so that you don't mix it up with other keys.

```bash
ssh-keygen -f ~/temp/id_rsa
```

You can then send the public key to your server. If you want to get rid of the key, delete it from `authorized_keys`.

```bash
cat ~/temp/id_rsa.pub | ssh user@hostname 'cat >> .ssh/authorized_keys'
```

Pasting a secret into GitHub is pretty easy. In your repository, navigate here:

```
Settings -> Secrets -> New repository secret
```

Name the secret `KEY` and paste in the private key contents. You can read more about GitHub secrets here: <https://docs.github.com/en/actions/reference/encrypted-secrets>

If you added a passphrase to your key, add it to a `PASSPHRASE` secret.

## Other secrets

Add these other secrets to GitHub. You have to specify the `USERNAME`, `HOST` AND `PORT` separately.

  * `USERNAME` the user you want to log into for the scp
  * `HOST` probably an IP address
  * `PORT` the port number, probably 22 if kept the default

## GitHub action

Here is my full `.yml` file. The last step `Upload` is when the files are copied.

You can read more about `scp-action` here: <https://github.com/appleboy/scp-action>

I stuck to the basic Hugo action. I tried with the latest version of Hugo, but that didn't work. You can tweak your actions by reading the README: <https://github.com/peaceiris/actions-hugo>

```
name: hugo deploy

on:
  push:
    branches:
      - master

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          submodules: true  # Fetch Hugo themes (true OR recursive)
          fetch-depth: 0    # Fetch all history for .GitInfo and .Lastmod

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: '0.81.0'
          extended: true

      - name: Build
        run: hugo --minify

      - name: Upload
        uses: appleboy/scp-action@master
        with:
          username: ${{ secrets.USERNAME }}
          host: ${{ secrets.HOST }}
          port: ${{ secrets.PORT }}
          passphrase: ${{ secrets.PASSPHRASE }}
          key: ${{ secrets.KEY }}
          source: "./public"
          target: "gh_page"
          rm: true
```

I also want to deploy to GitHub pages, so I add these steps at the end.

The `sed` command edits my Hugo `config.toml` to point to the GH pages address. I can then deploy, and the site will work properly. If you don't do this, the site will be broken.

Pro tip: you can run multiple commands by using `run: |`. You can see this below.

```
      - name: Config
        run: |
          sed -i "s=${{ secrets.DO_DOMAIN }}=${{ secrets.GH_DOMAIN }}=" config.toml
          hugo --minify

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```

## Final step: cron job

On your server, run `sudo crontab -e` to start a regular job as `ROOT`. This will regularly copy your files to the web server.

A file will open in your console, where you can paste

```
0 * * * * rsync -avh /home/username/gh_page/public/ /var/www/example.com/
```
