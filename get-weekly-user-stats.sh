#!/bin/sh

until python weekly-user-activity.py org.fedoraproject.prod.irc.karma; do sleep 5; done
until python weekly-user-activity.py org.fedoraproject.prod.git.receive; do sleep 5; done
until python weekly-user-activity.py org.fedoraproject.prod.bodhi.update.comment; do sleep 5; done
until python weekly-user-activity.py org.fedoraproject.prod.wiki.article.edit; do sleep 5; done
until python weekly-user-activity.py org.fedoraproject.prod.infragit.receive; do sleep 5; done
until python weekly-user-activity.py org.fedoraproject.prod.fedoratagger.rating.update; do sleep 5; done
until python weekly-user-activity.py io.pagure.prod.pagure.git.receive; do sleep 5; done
until python weekly-user-activity.py io.pagure.prod.pagure.issue.new; do sleep 5; done
until python weekly-user-activity.py org.fedoraproject.prod.fedbadges.badge.award; do sleep 5; done
