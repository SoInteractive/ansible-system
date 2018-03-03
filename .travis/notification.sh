#!/bin/bash
if [ -z "$MM_WEBHOOK" ]
then
  echo "MM_WEBHOOK variable is not set!"
  exit 0
fi

GIT_COMMITER=$(git show -s --pretty=%an)
if [ "$TRAVIS_PULL_REQUEST" != "false" ]
then
  WHAT="[${TRAVIS_REPO_SLUG}:${TRAVIS_PULL_REQUEST_BRANCH}](https://github.com/${TRAVIS_REPO_SLUG}/pull/${TRAVIS_PULL_REQUEST})"
else
  WHAT="[${TRAVIS_REPO_SLUG}:${TRAVIS_BRANCH}](https://github.com/${TRAVIS_REPO_SLUG}/tree/${TRAVIS_BRANCH})"
fi
if [ "$TRAVIS_TEST_RESULT" == "0" ]
then
  COLOR="#00BB00"
  RESULT="passed"
else
  COLOR="#EE0000"
  RESULT="failed"
fi

MESSAGE="Build [#${TRAVIS_BUILD_NUMBER}](travis-ci.org/${TRAVIS_REPO_SLUG}/builds/${TRAVIS_BUILD_ID}) of ${WHAT} by ${GIT_COMMITER} ${RESULT}."

curl -X POST --data-urlencode "payload={\"username\": \"soi\", \"attachments\": [{ \"color\": \"$COLOR\", \"text\": \"$MESSAGE\" }], \"icon_url\": \"https://maxcdn.icons8.com/office/PNG/512/Programming/bot_80-512.png\"}" "${MM_WEBHOOK}"
