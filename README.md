This is a hacky collection of scripts to create visualizations and hopefully
insight from contributor-triggered activity on Fedora's messaging bus, via
the ["datagrepper" service](https://apps.fedoraproject.org/datagrepper/).

Results are currently run on a personal system belonging to Matthew Miller,
and published weekly there: https://mattdm.org/fedora/fedora-contributor-trends/

There's also a text report: https://mattdm.org/fedora/fedora-contributor-trends/report.txt

You may also want to watch talk at DevConf 2016 where these metrics were
first presented: https://mattdm.org/fedora/2016devconf/

----

### Get started
To get started you must have `python3` installed, after that, clone this repo and follow the instructions below:

* Create one virtual environment and activate it

Linux/MacOS
```
  python3 -m venv .venv
  source .venv/bin/activate
```
Windows
```
  python3 -m venv .venv
  .venv/bin/activate.bat
```

* Install the requirements of the project in the environment

```
  pip install -r requirements.txt
```

* Run the project
```
  ./run.sh
```

Note that this will try to gather data going back to the beginning of the
message bus, which is a long time and a lot of data, and it hits the service
pretty hard in doing so. The weekly data is therefore cached, so on later
runs only the last week is re-loaded. **The first run may time out a lot and
even take several days to finish.** This isn't ideal, of course, but it got
me up and running. See [this
issue](https://pagure.io/fedora-contributor-trends/issue/16) for ideas on
how this bootstrap might be made better.

Anyway, you'll see that theme a lot here -- this started as a sysadmin-hack
kind of project, not an elegant software-engineer one.

But that's not the end! I'd love for this to be better. In fact, there are
six main areas looking for improvement:

1. The Fedora Message bus is in the midst of transitioning to new technology, which may make the way the current script gets data obsolete. See [this mailing list post](https://lists.fedoraproject.org/archives/list/infrastructure@lists.fedoraproject.org/message/6NRUH7EP6ERTBUEVTTXYLA25QUSHTKBE/) for possible plans. The upside is that some of the new options could be much better; the current code hits the server very hard.
2. The code really is hacky and ugly. It could use refactoring and beautification.
3. There are some data sources we're not using and could be: there are messages from pagure and will be ones from discourse that would be excellent candidates.
4. The visualizations I created for my presentation in 2016 are nice, but there are many other ways to look at the data. Come up with new ways to look at it which may show more insights.
5. Find an official place for this to run rather than on mattdm's personal server.
6. Simply put, the graphs and reports could be prettier.

Any or all of these things would be a huge improvement.


----

I originally designed this to answer these questions:

* How many people are active in Fedora over time?
* How many of those contributors are highly or constantly active?
* Are we gaining new contributors?
* Are we retaining the new folks who show up?
* Are we retaining older contributors?
    -  I would actually like to see more on this, like the average length of contribution over time, and perhaps even patterns in the "shape" of contribution level (like, small activity at first and then growth; abrupt stops vs slowly ramping down, etc.)
* What percentage of work is done by a few people, vs. percentage where a lot of people contribute each a small amount
* What percentage of contributors work for Red Hat (or other companies that are paying people to work on Fedora)?
    - this required some manual analysis, because there is no "I work for Red Hat" metadata

Some things that aren't well-explored but could be:

* What areas are new users most active in?
* Does activity in one area (like QA or Ask Fedora) flow to activity in other areas? 
* Are the most active people the most vocal? (
    - We need https://pagure.io/fedora-infrastructure/issue/9576 for this; also, it's hard because Fedora Accounts don't map to mailing list IDs easily so I just avoided that.

One thing that's an explicit non-goal: anything that is easily tied to a specific individual in the results, except maybe for very high level totals.

----

### Contributions
Before you push any changes or improvements remember in order to follow the rules PEP8 you must run the style code tools

* Running `flake8`

all project
```
  flake8 .
```
or a single file

```
  flake8 my_python_file.py
```
**NOTE** you must resolve any errors that show `flake8`


* Running `black`

all project
```
  black .
```
or a single file

```
  black my_python_file.py
```

More? See https://pagure.io/fedora-contributor-trends/issues!