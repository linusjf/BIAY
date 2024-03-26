#!/usr/bin/env bash

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : internet
# @created     : Tuesday Mar 26, 2024 11:57:10 IST
#
# @description :
######################################################################
checkinternet() {
  hash cat || exit
  cat </dev/null >/dev/tcp/8.8.8.8/53
  return $?
}
