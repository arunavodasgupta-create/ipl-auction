# IPL Auction Arena: how to publish and add real photos/stats

Folder contents
- index.html       the whole game (do not edit unless you want to change the code)
- stats.js         your real stats go here (starts empty)
- photos/          put player photos here, named exactly as in photos-needed.csv (.jpg)
- logos/           put team logos here: CSK.png, MI.png, RCB.png, KKR.png, DC.png, GT.png, LSG.png, PBKS.png, RR.png, SRH.png
- photos-needed.csv / logos-needed.txt   the exact file names the game looks for
- make_stats.py    converts a CSV of stats into stats.js

Anything missing falls back to the drawn crest / silhouette, so you can add files a few at a time.

Test locally: open a terminal in this folder and run `python -m http.server 8000`, then open http://localhost:8000
(opening index.html by double-click also works, but a local server matches the live site better).

Publish free on GitHub Pages
1. Create a free account at github.com and click New repository (name it e.g. ipl-auction, set it Public).
2. Click "uploading an existing file", drag in everything from this folder (index.html, stats.js, photos, logos), commit.
3. Settings > Pages > Source: "Deploy from a branch", Branch: main, folder: / (root), Save.
4. After about a minute the site is live at https://YOUR-USERNAME.github.io/ipl-auction/
To update later, upload the changed files again to the same repo.
