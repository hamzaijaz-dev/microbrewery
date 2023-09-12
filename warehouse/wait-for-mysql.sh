#!/bin/bash
# wait-for-mysql.sh

set -e

host="$1"
port="$2"
shift 2
cmd="$@"

until timeout 1 bash -c "cat < /dev/null > /dev/tcp/$host/$port"; do
  >&2 echo "MySQL is unavailable."
  sleep 1
done

>&2 echo "MySQL is up - executing command"
exec $cmd
